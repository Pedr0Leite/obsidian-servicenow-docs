---
title: "AWS S3 Bucket provisioning fails with the error \"Error executing translator script :Request AWS S3 Bucket.Provision_CloudFormation_Template com.snc.cmp.common.exception.BaseCmpException: One or more tags are not valid\" "
aliases:
  - KB0790059
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790059
kb_number: KB0790059
last_modified: 2025-08-25
---

## Issue

AWS S3 Bucket provisioning fails with the below error

"Error executing translator script :Request AWS S3 Bucket.Provision\_CloudFormation\_Template com.snc.cmp.common.exception.BaseCmpException: One or more tags are not valid"

## Resolution

Make sure the tags passed when provisioning does not contain any special characters other than + - = . \_ : / @.
