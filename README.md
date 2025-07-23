# 🛡️ CloudSentinel: Automated AWS Infrastructure Compliance

CloudSentinel is a lightweight AWS-native framework that ensures cloud infrastructure remains in strict compliance with organizational policies. It actively monitors EBS volume provisioning and automatically remediates misconfigured `gp2` volumes by converting them to `gp3` via Lambda-triggered workflows.

This solution provides a scalable foundation for broader policy enforcement across EC2, S3, RDS, EKS, and more.

---

## 📌 Problem Statement

Misconfigured EC2 instances using `gp2` volumes violate internal cloud governance rules, leading to:
- Increased storage costs 📈
- Broken compliance posture ❌
- Complicated automation and monitoring workflows 🐛

CloudSentinel ensures all volumes conform to the required `gp3` standard automatically — no manual intervention needed.

---

## 🧭 Project Scope

While originally focused on EBS `gp3` enforcement, the solution is designed to scale across:
- **EC2**: Restrict oversized or unauthorized instances
- **S3**: Enforce encryption and access controls
- **RDS**: Validate instance classes and backups
- **EKS**: Monitor role bindings and cluster usage
- **IAM & Networking**: Enforce least privilege and block unsafe configurations

---

## 🛠️ Solution

This project uses:
- **AWS EventBridge (CloudWatch Events)** to detect volume creation events
- **AWS Lambda (Python)** to extract volume IDs and convert non-compliant volumes to `gp3`
- **IAM Policies** to grant secure and limited permissions for volume remediation

The workflow triggers automatically whenever an EC2 instance attaches a new volume.

---

## 🚀 Setup

You'll find detailed steps in the [USER GUIDE](https://docs.google.com/document/d/1O73aYG3dEW-SVD-vY3Hh7_JyM-RvC3qv38r4D9mEFDo/edit?usp=sharing) . In summary:

1. Create a Python-based Lambda function
2. Configure EventBridge rule:
   - Service: EC2
   - Event Type: `createVolume`
   - Target: the Lambda function
3. Attach IAM policies to permit `DescribeVolume` and `ModifyVolume`
4. Test by provisioning a `gp2` volume and observing its automated conversion to `gp3`

---

## 🔍 Monitoring

Log outputs are stored in **CloudWatch Logs** under the Lambda execution group. Use this to verify events and troubleshoot configuration.

---

## 📄 License

This project is open for internal use and customization. Licensing may be added based on deployment context.
