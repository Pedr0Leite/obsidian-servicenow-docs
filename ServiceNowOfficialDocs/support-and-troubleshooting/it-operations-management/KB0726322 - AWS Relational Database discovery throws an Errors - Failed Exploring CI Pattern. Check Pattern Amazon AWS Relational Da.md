---
title: "AWS Relational Database discovery throws an Errors - Failed Exploring CI Pattern. Check Pattern Amazon AWS Relational Database Service"
aliases:
  - KB0726322
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726322
kb_number: KB0726322
last_modified: 2024-04-07
---

## AWS Relational Database discovery throws an Errors - Failed Exploring CI Pattern. Check Pattern Amazon AWS Relational Database Service

  

### Issue

# Symptoms

* * *

Amazon AWS Relational Database Service pattern failures when there are no RDS instances in the LDC with an error - **Failed Exploring CI Pattern. Check Pattern Amazon AWS Relational Database Service**

# Release

* * *

Jakarta release. Same is fixed in Kingston.

# Cause

* * *

When there are no RDS instances available in data center, Step 3 of Identification section of "Amazon AWS Relational Database Service" pattern fails with error.

# Resolution

* * *

1.  Open "Amazon AWS Relational Database Service" pattern
2.  Open "Identification of Amazon AWS RDS" of Identification Section
3.  Open step 3 and change this step as below.
    -   Change Termination Type to "Expected"
    -   Update Information Message to "No RDS is found in the LDC (region)".
    -   Save and Publish.
    -   Attached screenshot have the updated step.
4.  Restart the MID Server to Sync the pattern changes
5.  Further discoveries should show this Information message in the patterns logs.

![](sys_attachment.do?sys_id=69fca822db82b450e515c22305961983)
