import json
import boto3
import os
from botocore.exceptions import ClientError

# --- Configuration ---
# The ID of your quarantine security group (no inbound/outbound rules)
ISOLATION_SG_ID = os.environ.get('ISOLATION_SG_ID', 'sg-xxxxxxxxxxxxx')

# Initialize AWS clients
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    """
    Main handler triggered by EventBridge on GuardDuty findings.
    Isolates the affected EC2 instance and creates forensic snapshots.
    """
    print(f"Received event: {json.dumps(event, indent=2)}")

    try:
        # --- Step 1: Parse the GuardDuty finding from the event ---
        # The finding details are nested within the EventBridge event
        detail = event.get('detail', {})
        finding = detail  # In EventBridge, 'detail' *is* the GuardDuty finding

        # Extract instance ID and finding details
        instance_id = finding.get('resource', {}).get('instanceDetails', {}).get('instanceId')
        finding_type = finding.get('type')
        severity = finding.get('severity')
        finding_id = finding.get('id')

        if not instance_id:
            print("No instance ID found in the finding. Skipping.")
            return {
                'statusCode': 200,
                'body': json.dumps('No instance ID found.')
            }

        print(f"Processing GuardDuty finding: {finding_id} for instance {instance_id}")

        # --- Step 2: Isolate the EC2 instance by changing its security group ---
        # This replaces all existing security groups with the quarantine group
        print(f"Applying quarantine security group {ISOLATION_SG_ID} to instance {instance_id}")

        response = ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[ISOLATION_SG_ID]
        )

        print(f"Successfully isolated instance {instance_id}")

        # --- Step 3: Create forensic EBS snapshots ---
        # This creates snapshots of attached volumes for later investigation
        try:
            print(f"Creating forensic snapshots for instance {instance_id}")
            volumes = ec2.describe_volumes(
                Filters=[
                    {'Name': 'attachment.instance-id', 'Values': [instance_id]}
                ]
            )

            for vol in volumes.get('Volumes', []):
                vol_id = vol['VolumeId']
                snapshot = ec2.create_snapshot(
                    VolumeId=vol_id,
                    Description=f'Forensic snapshot for instance {instance_id} from GuardDuty finding {finding_id}'
                )
                print(f"Created snapshot {snapshot['SnapshotId']} for volume {vol_id}")
        except Exception as e:
            print(f"Warning: Could not create forensic snapshots: {str(e)}")
            # Continue even if snapshot creation fails

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Successfully isolated instance {instance_id}',
                'instance_id': instance_id,
                'finding_id': finding_id
            })
        }

    except ClientError as e:
        print(f"AWS Client Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Unexpected Error: {str(e)}')
        }