# 🛡️Cloud-Threat-Detection
This project shows how to build an automatic security system on Amazon Web Services (AWS) that constantly watches for cyber threats, takes action to stop them, and immediately alerts your security team. The system uses smart detection tools to spot unusual activity, like someone trying to steal data or hack into a server, and then automatically responds—for example, by isolating the affected server and creating a backup for investigation. This all happens in minutes or even seconds, which means your team can find and fix security problems much faster than if they had to do everything manually.

## 📋 Table of Contents
- <a href="#key-features">Key Features</a>
- <a href="#architecture-diagram">Architecture Diagram</a>
- <a href="#tech-stack">Tech Stack</a>

<h2><a class="anchor" id="key-features"></a> 🎯 Key Features</h2>

- 🔍 **Real-time Threat Detection**: Utilizes Amazon GuardDuty and CloudWatch Alarms to monitor for malicious activities.

- ⚡ **Automated Response**: AWS Lambda functions execute pre-defined response playbooks (EC2 isolation, forensic snapshot creation).

- 📨 **Instant Notifications**: Amazon SNS sends real-time alerts to security teams.

- 🔄 **End-to-End Testing**: Kali Linux penetration testing validates the entire pipeline.

<h2><a class="anchor" id="architecture-diagram"></a> 🏗️ Architecture Diagram</h2>

![image alt](https://github.com/Akanksha-cloudsec/Cloud-Threat-Detection/blob/a9810dda0c0974a6039bc5c90ad7e85dad4c42ea/Architecture%20Diagram/Blank%20diagram.png)


