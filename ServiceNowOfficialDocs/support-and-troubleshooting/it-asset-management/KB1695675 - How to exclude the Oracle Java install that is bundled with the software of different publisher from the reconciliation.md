---
title: "How to exclude the Oracle Java install that is bundled with the software of different publisher from the reconciliation"
aliases:
  - KB1695675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1695675
kb_number: KB1695675
last_modified: 2024-08-02
---

## Issue

There could be some softwares which running on the top of JRE, hence the Java Platform is delivered along with the software which is from a different publisher other than Oracle.  
  
There is a requirement the Oracle Java which being delivered along with another software should be excluded from the license reconciliation.

## Resolution

The current workaround is to create two Software Models for Oracle Java and set one of them as 'License Under Management' = False.

On the Software Model with 'License Under Management' = False, further add 'Software Install Condition' with all the CIs (installed on) on which bundled software is installed. So Java installs on those CIs will be ignored from reconciliation as 'License Under Management' is set to False. In this case, you need update the the list of the CIs when needed. 

If it's possible to include any info to the Oracle Java installs which could be used to identify the installs are actually coming along with another software installs when populating the Oracle Java installs to the CMDB, then there's no need to manually update the device CI list on software model but configure the 'Software Install Condition' with this specific info.
