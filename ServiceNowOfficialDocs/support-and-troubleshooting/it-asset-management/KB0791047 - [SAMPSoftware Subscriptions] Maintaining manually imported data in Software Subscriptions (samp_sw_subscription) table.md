---
title: "[SAMP/Software Subscriptions] Maintaining manually imported data in Software Subscriptions (samp_sw_subscription) table"
aliases:
  - KB0791047
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791047
kb_number: KB0791047
last_modified: 2024-04-07
---

## \[SAMP/Software Subscriptions\] Maintaining manually imported data in Software Subscriptions (samp\_sw\_subscription) table

  

### Issue

-   The manually imported data in Software Subscriptions (samp\_sw\_subscription) table gets cleaned/deleted post the "SAM - Import User Subscriptions" scheduled job run, whereas the Software Subscriptions created from the Integration Profile (Office 365) remains undeleted.

https://<<instance\_name>>.service-now.com/samp\_sw\_subscription\_list.do

![](/sys_attachment.do?sys_id=1fdc17bcdb0078d066e0a345ca96193a)

### Release

-   Instance with Software Asset Management Professional plugin enabled.

### Cause

-   When the value of the field "Source from integration" (sourced\_from\_integration) column is "null", then the record gets cleaned during the "SAM - Import User Subscriptions" import job run.

![](/sys_attachment.do?sys_id=97dc17bcdb0078d066e0a345ca96193c)

### Resolution

-   In general, when the "**SAM - Import User Subscriptions**" scheduled job runs, it will clean out all records in the Software Subscriptions (samp\_sw\_subscription) table where the value of the field "Sourced from integration" (sourced\_from\_integration) column is "null".
-   "Null" also happens to be the default value of the column, so when importing into the subscription table, the value of "sourced\_from\_integration" needs to be explicitly set to 'No' to ensure that the records are retained post the scheduled job run.
-   This can be done by either setting this value with either a script in the transform map or including the value for the column in the source import file and mapping the value.
