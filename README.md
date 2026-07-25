
GIT Repository: 

# AWS Lambda & Boto3 Automation — Assignment Submission

Automation of common AWS operational tasks using Python, Boto3, and Lambda — triggered via EventBridge (scheduled or event-driven) and monitored through CloudWatch Logs.

## Region
`us-east-1`

## Status
| # | Assignment | Status |
|---|---|---|
| 1 | [S3 Bucket Cleanup](#1-automated-s3-bucket-cleanup) | ✅ Complete |
| 2 | [EBS Snapshot Creation & Cleanup](#2-automated-ebs-snapshot-creation-and-cleanup) | ✅ Complete |
| 3 | [EC2 Auto-Tagging on Launch](#3-auto-tagging-ec2-instances-on-launch) | ✅ Complete |
| 4 | [Daily Cost Alert via Cost Explorer + SNS](#4-daily-aws-cost-alert) | ✅ Complete |
| 5 | [Restore EC2 from Latest Snapshot](#5-restore-an-ec2-instance-from-the-latest-snapshot) | 🔲 In Progress |
| 6 | [Audit S3 Buckets for Public Access](#6-audit-s3-buckets-for-public-access-and-notify) | 🔲 In Progress |

---

## Repository Structure
```
aws-lambda-boto3-assignment/
├── README.md
├── assignment-1-s3-cleanup/
│   ├── lambda_function.py
│   ├── iam_policy.json
│   └── screenshots/
├── assignment-2-ebs-snapshot/
│   ├── lambda_function.py
│   ├── iam_policy.json
│   └── screenshots/
├── assignment-3-ec2-autotag/
│   ├── lambda_function.py
│   ├── iam_policy.json
│   └── screenshots/
├── assignment-4-cost-alert/
│   ├── lambda_function.py
│   ├── iam_policy.json
│   └── screenshots/
├── assignment-5-ec2-restore/
│   ├── lambda_function.py
│   └── iam_policy.json
└── assignment-6-s3-public-audit/
    ├── lambda_function.py
    └── iam_policy.json
```

---

## 1. Automated S3 Bucket Cleanup
**Objective:** Automatically delete objects older than 30 days from an S3 bucket.
**Bucket:** `herovirs3asign1`
**Trigger:** Manual / on-demand invocation

**Code:** [`lambda_function.py`](./assignment-1-s3-cleanup/lambda_function.py)
**IAM Policy:** [`iam_policy.json`](./assignment-1-s3-cleanup/iam_policy.json)

**Screenshots:**
1. [Setting budget](./assignment-1-s3-cleanup/screenshots/0.%20Setting%20budget.png)
2. [Accessing directory](./assignment-1-s3-cleanup/screenshots/1.%20Accessing%20directory.png)
3. [S3 created and files uploaded](./assignment-1-s3-cleanup/screenshots/2.%20S3%20created%20and%20files%20uploaded.png)
4. [Creating IAM Role for Lambda](./assignment-1-s3-cleanup/screenshots/3.%20Creating%20IAm%20Role%20for%20Lambda.png)
5. [IAM Role created for Lambda](./assignment-1-s3-cleanup/screenshots/3.1%20IAM%20Role%20created%20for%20Lambda.png)
6. [Lambda function created](./assignment-1-s3-cleanup/screenshots/4.%20lambda%20function%20created.png)
7. [Lambda code](./assignment-1-s3-cleanup/screenshots/4.1%20Lambda%20code.png)
8. [Two new files uploaded on S3](./assignment-1-s3-cleanup/screenshots/5.%20two%20new%20files%20uploaded%20on%20S3.png)
9. [Deployed with 10-minute threshold to test](./assignment-1-s3-cleanup/screenshots/6.%20deployed%20with%2010%20minutes%20to%20test.png)
10. [Testing Lambda](./assignment-1-s3-cleanup/screenshots/7.%20Testing%20lambda.png)
11. [Test output](./assignment-1-s3-cleanup/screenshots/8.%20test%20output.png)
12. [Test — threshold changed to 1 minute for test purposes](./assignment-1-s3-cleanup/screenshots/9.%20test-%20code%20changed%20to%201%20minute%20for%20test%20purpose.png)
13. [Files deleted — CloudWatch Logs](./assignment-1-s3-cleanup/screenshots/9.1%20files%20deleted-%20cloud%20watch.png)
14. [Test completed — nothing left in S3 (Final Result)](./assignment-1-s3-cleanup/screenshots/9.2%20Test%20completed.%20Nothing%20in%20S3.png)
15. [Threshold updated back to 30 days](./assignment-1-s3-cleanup/screenshots/10.%20time%20updated%20to%2030%20days..png)

---

## 2. Automated EBS Snapshot Creation and Cleanup
**Objective:** Create a snapshot of an EBS volume and delete snapshots older than the retention period.
**Volume ID:** `vol-0a5f8145eca191784`
**Trigger:** EventBridge — weekly schedule

**Code:** [`lambda_function.py`](./assignment-2-ebs-snapshot/lambda_function.py)
**IAM Policy:** [`iam_policy.json`](./assignment-2-ebs-snapshot/iam_policy.json)

**Screenshots:**
1. [Creating Elastic Block Store volume](./assignment-2-ebs-snapshot/screenshots/1.%20creating%20Elastic%20Block%20store.png)
2. [EBS created](./assignment-2-ebs-snapshot/screenshots/2.%20EBS%20created.png)
3. [IAM role created](./assignment-2-ebs-snapshot/screenshots/3.%20Iam%20role%20created.png)
4. [Lambda function created](./assignment-2-ebs-snapshot/screenshots/4.%20lambda%20function%20created.png)
5. [Lambda deployed](./assignment-2-ebs-snapshot/screenshots/5.%20Lambda%20Deployed.png)
6. [Test case created](./assignment-2-ebs-snapshot/screenshots/6.%20Creat%20case%20created.png)
7. [Test results — snapshot ID created](./assignment-2-ebs-snapshot/screenshots/7.%20test%20results-%20Snap%20ID%20created.png)
8. [EBS snapshots (Final Result)](./assignment-2-ebs-snapshot/screenshots/8.%20EBS-%20snaps.png)
9. [Scheduling it with EventBridge](./assignment-2-ebs-snapshot/screenshots/9.%20Scheduling%20it%20with%20EventBridge.png)
10. [Schedule configuration](./assignment-2-ebs-snapshot/screenshots/10.%20Schedule.png)
11. [Schedule mapped to Lambda function](./assignment-2-ebs-snapshot/screenshots/11.%20schedule%20mapping%20with%20lambda%20fun.png)
12. [Weekly EBS job scheduled](./assignment-2-ebs-snapshot/screenshots/12.%20weekly%20ebs%20job%20scheduled..png)
13. [Code pushed to Git](./assignment-2-ebs-snapshot/screenshots/13.%20Code%20pusded%20to%20Git.png)
14. [Git add and commit](./assignment-2-ebs-snapshot/screenshots/13.%20Git%20add%20and%20commit.png)

---

## 3. Auto-Tagging EC2 Instances on Launch
**Objective:** Automatically tag newly launched EC2 instances for tracking and cost allocation.
**Trigger:** EventBridge event pattern — `aws.ec2` / `EC2 Instance State-change Notification` / state `running`

**Code:** [`lambda_function.py`](./assignment-3-ec2-autotag/lambda_function.py)
**IAM Policy:** [`iam_policy.json`](./assignment-3-ec2-autotag/iam_policy.json)

**Screenshots:**
1. [IAM role for Auto-Tagging EC2 Instances on Launch](./assignment-3-ec2-autotag/screenshots/1.%20Iam%20role%20for%20Auto-Tagging%20EC2%20Instances%20on%20Launch.png)
2. [Permissions added](./assignment-3-ec2-autotag/screenshots/2.%20Permissions%20added.png)
3. [IAM role created](./assignment-3-ec2-autotag/screenshots/3.%20IAM%20role%20created.png)
4. [IAM policy](./assignment-3-ec2-autotag/screenshots/4.%20IAM%20policy.png)
5. [Auto-tag policy attached](./assignment-3-ec2-autotag/screenshots/4.%20Auto%20tag%20policy%20attached.png)
6. [Creating new Lambda function](./assignment-3-ec2-autotag/screenshots/4.%20creating%20new%20lambda%20functions%20for%20Auto-Tagging%20EC2%20Instances%20on%20Launch.png)
7. [Lambda function created — ready to deploy](./assignment-3-ec2-autotag/screenshots/5.%20Lambda%20function%20created%20-%20ready%20to%20deploy.png)
8. [Lambda function code](./assignment-3-ec2-autotag/screenshots/5.1%20LAMBDA%20function%20.png)
9. [Creating EventBridge pattern](./assignment-3-ec2-autotag/screenshots/6.%20creating%20eventbridge%20pattern.png)
10. [Launching real EC2 instance for testing](./assignment-3-ec2-autotag/screenshots/7.%20launching%20real%20EC2%20instance%20for%20testing.png)
11. [Launched EC2 for testing](./assignment-3-ec2-autotag/screenshots/8.%20launched%20ec2%20for%20testing.png)
12. [Testing completed — showing LaunchDate and Owner tags (Final Result)](./assignment-3-ec2-autotag/screenshots/9.%20tsting%20completed-%20showing%20tag-date%20and%20owner.png)
13. [CloudWatch Logs](./assignment-3-ec2-autotag/screenshots/10.%20Cloudwatch%20logs.png)
14. [Git add and status](./assignment-3-ec2-autotag/screenshots/11.%20Git%20add%20and%20staus.png)
15. [Git commit and push done](./assignment-3-ec2-autotag/screenshots/12.%20Git%20cmmit%20and%20push%20done.png)

**Bonus (discussed, not implemented):** The launching IAM user's ARN can be extracted from a CloudTrail `RunInstances` event via `cloudtrail.lookup_events` and applied as the `Owner` tag instead of a hardcoded value.

---

## 4. Daily AWS Cost Alert
**Objective:** Alert via SNS when month-to-date AWS spend exceeds a threshold.
**Trigger:** EventBridge — daily schedule

**Code:** [`lambda_function.py`](./assignment-4-cost-alert/lambda_function.py)
**IAM Policy:** [`iam_policy.json`](./assignment-4-cost-alert/iam_policy.json)

> ⚠️ Note: the committed `lambda_function.py` still has `THRESHOLD_USD` set to the test value (`0.01`) and a real AWS account ID embedded in the SNS ARN — worth reviewing before final submission.

**Screenshots:**
1. [SNS topic created](./assignment-4-cost-alert/screenshots/1.%20SNS%20created.png)
2. [Creating subscription](./assignment-4-cost-alert/screenshots/2.%20Creating%20subscripson.png)
3. [Subscription confirmed](./assignment-4-cost-alert/screenshots/3.%20subscription%20confirmed.png)
4. [Creating IAM role for Cost Alert Lambda](./assignment-4-cost-alert/screenshots/4.%20Creating%20IAM%20role%20for%20cost%20allert%20Lambda.png)
5. [IAM role created](./assignment-4-cost-alert/screenshots/5.%20IAM%20role%20craeted.png)
6. [Inline policy created for IAM role](./assignment-4-cost-alert/screenshots/6.%20inline%20policy%20created%20for%20IAM%20role.png)
7. [Creating Lambda function](./assignment-4-cost-alert/screenshots/7.%20creating%20Lambda%20function.png)
8. [Lambda function created — ready to deploy](./assignment-4-cost-alert/screenshots/8.%20lambda%20function%20created%20-ready%20to%20deploy.png)
9. [Setting timeout to 10 sec](./assignment-4-cost-alert/screenshots/8.1%20setting%20timeout%20to%2010%20sec%20in%20lambda%20function.png)
10. [Lambda test created](./assignment-4-cost-alert/screenshots/8.2%20Lambda%20test%20created.png)
11. [Lambda test result](./assignment-4-cost-alert/screenshots/8.3%20lambda%20test%20result.png)
12. [AWS Cost Alert email (Final Result)](./assignment-4-cost-alert/screenshots/8.4%20AWS%20cost%20allert.png)
13. [CloudWatch Logs](./assignment-4-cost-alert/screenshots/9.%20AWS%20cloud%20watch%20results.png)
14. [Creating EventBridge schedule](./assignment-4-cost-alert/screenshots/10.%20Creating%20event%20bridge%20to%20schedule%20run.png)
15. [EventBridge rule created](./assignment-4-cost-alert/screenshots/10.1%20Eventbridge%20rule%20created.png)
16. [Code pushed to Git](./assignment-4-cost-alert/screenshots/11%20code%20pushed%20to%20git.png)
17. [Additional screenshot](./assignment-4-cost-alert/screenshots/Screenshot%202026-07-25%20205237.png)

---

## 5. Restore an EC2 Instance from the Latest Snapshot
**Status:** 🔲 In Progress — code and screenshots not yet added.
**Objective:** Rebuild an EC2 instance from the most recent EBS snapshot (disaster recovery).
**Depends on:** Assignment 2's snapshot output.

**Code:** [`lambda_function.py`](./assignment-5-ec2-restore/lambda_function.py) *(pending)*
**IAM Policy:** [`iam_policy.json`](./assignment-5-ec2-restore/iam_policy.json) *(pending)*

---

## 6. Audit S3 Buckets for Public Access and Notify
**Status:** 🔲 In Progress — code and screenshots not yet added.
**Objective:** Detect publicly accessible S3 buckets (via Block Public Access config, bucket policy, and ACLs) and alert via SNS.

**Code:** [`lambda_function.py`](./assignment-6-s3-public-audit/lambda_function.py) *(pending)*
**IAM Policy:** [`iam_policy.json`](./assignment-6-s3-public-audit/iam_policy.json) *(pending)*

---

## Cleanup Notes
Test/throwaway resources (EC2 test instance, extra snapshots) were removed after screenshots were captured, to avoid ongoing charges.
