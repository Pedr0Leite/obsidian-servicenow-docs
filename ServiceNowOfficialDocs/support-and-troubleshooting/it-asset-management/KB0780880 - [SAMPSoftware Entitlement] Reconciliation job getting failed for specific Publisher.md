---
title: "[SAMP/Software Entitlement] Reconciliation job getting failed for specific Publisher"
aliases:
  - KB0780880
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780880
kb_number: KB0780880
last_modified: 2024-04-08
---

## Issue

-   Reconciliation jobs are getting failed via. Scheduled jobs and even when tried manually for specific Publisher.

![](sys_attachment.do?sys_id=ef71240ddbc838d0fec4fb24399619fc)

## Resolution

#### Troubleshooting:

-   In order to capture the required information, ran the reconciliation for the affected Publisher. 
-   In System logs below errors were captured,

Error undefined SAM:ReconciliationEngine  
  
Error SAM:ReconciliationEngine: undefined: no thrown error com.glide.ui.ServletErrorListener  
  
Error org.mozilla.javascript.EvaluatorException: GlideRecord.addQuery() - invalid table name: undefined (sys\_script\_include.525cc34e0b1232006586650d37673a47.script; line 16) SAM:ReconciliationEngine  
  
Error SAM:ReconciliationEngine: org.mozilla.javascript.EvaluatorException: GlideRecord.addQuery() - invalid table name: undefined (sys\_script\_include.525cc34e0b1232006586650d37673a47.script; line 16): no thrown error

-   It was determined that recon was failing when processing "Allocated Pass: Processing the User Subscription licenses for Microsoft Power BI Pro".

The error is in:  
org.mozilla.javascript.EvaluatorException: GlideRecord.addQuery() - invalid table name: undefined (sys\_script\_include.525cc34e0b1232006586650d37673a47.script; line 16)

-   This appears that we are creating a GlideAggregate on an undefined variable.
-   In order to debug this issue, few breakpoints were added to recon Script Includes and found that there were few of the entitlements related to affected Publisher are incorrectly set to an invalid "User Subscription" (sys id: XXXXXX) license metric.

![](sys_attachment.do?sys_id=6b71240ddbc838d0fec4fb24399619fb)

-   Possibly, this is a result of bad data import.
-   In order to resolve this reconciliation job failure, the affected entitlements were set to correct "sys\_id" of the "User Subscription License Metric" and then the reconciliation job was successful.
