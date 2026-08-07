---
title: "[CMDB/Certification audits] Erros in the Audit Health Report"
aliases:
  - KB0780855
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780855
kb_number: KB0780855
last_modified: 2025-04-08
---

## Issue

-   The Certification filter template which is defined for CI Class e.g. Business Service with specific Filter conditions is not getting applied correctly.
-   Due to which there are lots of errors observed post Health results,

Too many 'Failed for audit Prefix/Recommended Field SUS - Operational'  
  
![](sys_attachment.do?sys_id=44917d391b9af890ccc253da234bcb4b)

## Resolution

#### Troubleshooting:

-   On the instance, there was Certification Audit configured for specific CI Class i.e. Business Service.
-   One such e.g. is to look for CI's with "Prefix/Recommended Fields SUS Supplier Service - Operational" with Filter Condition defined as "Class = Business Service".
-   Each Certification Filters are associated with respective updated Certificate Template and Audit.
-   But post the execution of Audit schedule job it was observed that irrespective of Filter condition defined, all the Certification Filter was applied thus many errors were observed as below.

![](sys_attachment.do?sys_id=d4917d391b9af890ccc253da234bcb4d)

-   It was observed that the user who was running the Audit schedule job does not have any required roles.
-   In order to avoid this Certification Filters applied to all CIs irrespective of the Filter condition defined, the user must have either "**certification\_admin**" or "**admin**" configured.

## Additional Information

Please refer [Audit Scheduling](https://docs.servicenow.com/ "Audit Scheduling") on the pre-requisite for the user role to run the on-demand audits.
