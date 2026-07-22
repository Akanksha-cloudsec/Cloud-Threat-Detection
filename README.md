# 🛡️Cloud-Threat-Detection
This project shows how to build an automatic security system on Amazon Web Services (AWS) that constantly watches for cyber threats, takes action to stop them, and immediately alerts your security team. The system uses smart detection tools to spot unusual activity, like someone trying to steal data or hack into a server, and then automatically responds—for example, by isolating the affected server and creating a backup for investigation. This all happens in minutes or even seconds, which means your team can find and fix security problems much faster than if they had to do everything manually.

## 📋 Table of Contents
- <a href="#key-features">Key Features</a>
- <a href="#architecture-diagram">Architecture Diagram</a>
- <a href="#tech-stack">Tech Stack</a>
- <a href="#project-phase">Project Phase</a>
- <a href="#result">Result</a>
- <a href="#security-best-practices">Security Best Practices</a>
- <a href="#resources">Resources</a>

<h2><a class="anchor" id="key-features"></a> 🎯 Key Features</h2>

- 🔍 **Real-time Threat Detection**: Utilizes Amazon GuardDuty and CloudWatch Alarms to monitor for malicious activities.

- ⚡ **Automated Response**: AWS Lambda functions execute pre-defined response playbooks (EC2 isolation, forensic snapshot creation).

- 📨 **Instant Notifications**: Amazon SNS sends real-time alerts to security teams.

- 🔄 **End-to-End Testing**: Kali Linux penetration testing validates the entire pipeline.

<h2><a class="anchor" id="architecture-diagram"></a> 🏗️ Architecture Diagram</h2>

![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/a9810dda0c0974a6039bc5c90ad7e85dad4c42ea/Architecture%20Diagram/Blank%20diagram.png)

<h2><a class="anchor" id="tech-stack"></a> 🚀 Tech Stack</h2>

### 🔍 Detection Layer
| **Service** | **Purpose** |
| :--- | :--- |
| Amazon GuardDuty | Intelligent threat detection (port scans, anomalous API calls) |
| Amazon CloudWatch | Custom metrics and alarms (S3 data exfiltration) |
| AWS CloudTrail | Detailed API logging for S3 object-level events |

### ⚡ Orchestration & Response Layer
| **Service** | **Purpose** |
| :--- | :--- |
| Amazon EventBridge | Event routing and triggering Lambda functions |
| AWS Lambda | Executes automated response playbooks |
| AWS Step Functions | Coordinates multi-step remediation workflows |

### 📨 Notification 
| **Service** | **Purpose** |
| :--- | :--- |
| Amazon SNS | Real-time alerts (email/SMS) |

### 🧪 Testing Layer
| **Service** | **Purpose** |
| :--- | :--- |
| Kali Linux / Pacu | Penetration testing and attack simulation |

### 🏗️ Infrastructure Layer
| **Service** | **Purpose** |
| :--- | :--- |
| Amazon VPC | Isolated network environment |
| Amazon EC2 | Target instances for attack simulation |
| Amazon S3 | Sensitive data storage for exfiltration testing |
| Amazon RDS | High-value target for lateral movement testing |

<h2><a class="anchor" id="project-phase"></a> 📝 Project-Phase</h2>

- ### Phase 1 : Lab Environment Setup

  Create isolated VPC with public and private subnets.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/c7de7b398136c5e824610c54c3d340f912b7c547/IMAGES/image%201.png)

  Deploy "Compromised" EC2 instance with IAM role(S3ReadOnly).

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/c7de7b398136c5e824610c54c3d340f912b7c547/IMAGES/image%202.png)

  Create sensitive S3 bucket with dummy data.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/c7de7b398136c5e824610c54c3d340f912b7c547/IMAGES/image%203.png)

  Deploy RDS database in private subnet.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/c7de7b398136c5e824610c54c3d340f912b7c547/IMAGES/image%204.png)

  Enable the SNS.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/5e7d3812f48b1551e4101000c3bfc631696457a0/IMAGES/image%205.png)

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/5e7d3812f48b1551e4101000c3bfc631696457a0/IMAGES/image%206.jpeg)

- ### Phase 2 : Detection Services Configuration

  Enable Amazon **GuardDuty**.

  Configure AWS CloudTrail, first create a trail for S3 object-level logging and enable the **CloudWatch logs option**.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/5e7d3812f48b1551e4101000c3bfc631696457a0/IMAGES/image%207.png)

  Create CloudWatch Metric Filter, first create log group then create metric filter in it for **GetObject** events.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/5e7d3812f48b1551e4101000c3bfc631696457a0/IMAGES/image%208.png)

  Create Alarm for S3 exfiltration, In alram select the custom metric filter with threshold > 2.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/5e7d3812f48b1551e4101000c3bfc631696457a0/IMAGES/image%209.png)

- ### Phase 3 : Automated Response Implementation

  Develop AWS Lambda function for automated response.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2010.png)

  Create EventBridge rule for high-severity GuardDuty findings.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2011.png)

- ### Phase 4 : Attack Simulation & Validation

  Set up Kali Linux attack machine.

  Configure Pacu for automated AWS pentesting. Execute attacks: S3 exfiltration, port scanning, lateral movement.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2012.png)

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2013.png)

  <h2><a class="anchor" id="result"></a> 📄 Result</h2>

  Amazon **SNS** Notification for S3 exfiltration.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2014.jpeg)

  Check **CloudWatch**.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/Image%2016.png)

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2015.png)

  Check **GuardDuty** findings.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/Image%2017.png)

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2018.png)

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2019.png)

  Check **GuardDuty** Summary.

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2020.png)

  ![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/997e0e3681964fcf538eb8e7a3abc989c12947a7/IMAGES/image%2021.png)

<h2><a class="anchor" id="security-best-practices"></a> ✅ Security Best Practices</h2>

 - Principle of Least Privilege for IAM roles

 - Isolated lab environment for testing

 - MFA enforcement on all users

 - Regular security reviews

 - Encryption at rest and in transit

 - Secure storage of sensitive data

 - Regular penetration testing

<h2><a class="anchor" id="resources"></a> 📚 Resources</h2>

  [Amazon VPC](https://aws.amazon.com/vpc/)
  
  [Amazon EC2](https://aws.amazon.com/ec2/)
  
  [Amazon S3](https://aws.amazon.com/s3/)
  
  [Amazon RDS](https://aws.amazon.com/rds/)

  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

  [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
  
  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
  
  [AWS Lambda](https://aws.amazon.com/lambda/)
  
  [Pacu](https://github.com/RhinoSecurityLabs/pacu)
  
 
