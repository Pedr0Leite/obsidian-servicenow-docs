---
title: "[SuccessFactor] - Last Activity is empty in the Software Subscription record"
aliases:
  - KB0996544
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996544
kb_number: KB0996544
last_modified: 2024-08-23
---

## Issue

SAP Connection is successfully connected.

Integration Profile has the Excel File attached.

SAM - Refresh Success Factor Integration Activity job is completed but the "Last Activity" field in the "Software Subscriptions" record for "Success Factor Integration" is empty.

## Resolution

1\. The size must be not greater than 5 MB.

\- Remove the unnecessary information from the Excel File.

2\. Update the Excel file and make sure it only has the required columns/fields which are as follows and in the right order:

1st column: Last Login

2nd column: User Sys ID

Optional: User Name

E.g.

![](sys_attachment.do?sys_id=7b9b2d0ddbb6b450770be6be1396193c)

3\. Save the file and attach it to the Integration Profile.

4\. Run the "SAM - Refresh Success Factor Integration Activity" job.

5\. Verify the "Last activity" information from the Software Subscription records.
