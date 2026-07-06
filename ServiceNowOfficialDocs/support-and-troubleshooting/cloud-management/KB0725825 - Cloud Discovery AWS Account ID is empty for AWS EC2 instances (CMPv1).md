---
title: "Cloud Discovery : AWS Account ID is empty for AWS EC2 instances (CMPv1)"
aliases:
  - KB0725825
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725825
kb_number: KB0725825
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Discovery on AWS accounts will create EC2 instances in the cmdb\_ci\_ec2\_instance table with empty Account ID.

# Release

* * *

Any, when We are using CMPv1

# Cause

* * *

1\. Account ID is retrieved from the respective AWS account record in the aws\_account table.

2\. When we input the AWS account in the ServiceNow instance, the account gets inserted into the aws\_account\_admin table.

3\. There is a business rule "**Populate AWS account**" which populates the respective **aws\_account\_admin** record in the **aws\_account** table

4\. For some reason, if we have either deleted the record or the record did not get inserted into the aws\_account table, we will observe that the Account ID would be empty for resources related to this account.

# Resolution

* * *

1\. The business rule "**Populate AWS account**" is on the AWS credential table. 

2\. Modify the Business rule to trigger an update.

3\. Update the Credential record, for example: Change the name of the credential

4\. This will make sure the business rule gets triggered and the related AWS account will be populated in the aws\_account table.

5\. Re-run discovery on the AWS account and the Account ID should now be populated
