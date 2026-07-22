# 🛡️Cloud-Threat-Detection
This project shows how to build an automatic security system on Amazon Web Services (AWS) that constantly watches for cyber threats, takes action to stop them, and immediately alerts your security team. The system uses smart detection tools to spot unusual activity, like someone trying to steal data or hack into a server, and then automatically responds—for example, by isolating the affected server and creating a backup for investigation. This all happens in minutes or even seconds, which means your team can find and fix security problems much faster than if they had to do everything manually.

## 📋 Table of Contents
- <a href="#key-features">Key Features</a>
- <a href="#architecture-diagram">Architecture Diagram</a>
- <a href="#tech-stack">Tech Stack</a>
- <a href="#project-phase">Project Phase</a>

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
