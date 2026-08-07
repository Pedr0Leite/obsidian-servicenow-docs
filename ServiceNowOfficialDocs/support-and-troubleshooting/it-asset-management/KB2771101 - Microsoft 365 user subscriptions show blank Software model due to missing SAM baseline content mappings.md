---
title: "Microsoft 365 user subscriptions show blank Software model due to missing SAM baseline content mappings"
aliases:
  - KB2771101
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2771101
kb_number: KB2771101
last_modified: 2026-02-10
---

## Issue

● Microsoft 365 subscription imports complete, but Software model is not populated because subscription identifiers cannot be resolved to SAM baseline content mappings

## Resolution

● Force a full baseline content load by clearing the delta checkpoint on the relevant Data Services schedules, then execute the content jobs and re-run the import

\- Step 1: Prepare to run the baseline content sync outside business hours  
● This content sync can be heavy depending on instance size and content volume, so schedule it during off hours as per KB0694718  
[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0694718](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694718)

\- Step 2: Reset the delta checkpoint for the required content schedules  
● Open each of the following Data Services schedules and clear the Last updated on value to reset the checkpoint  
● Download Software Content: Entitlement Definition  
● Download Software Content: Subscription Product Definition  
● Note: Only a maint user can blank or modify the Last updated on field on these schedule records

\- Step 3: Run the content download jobs and apply content  
● Execute the following scheduled jobs  
● Download Software Content: Entitlement Definition  
● Download Software Content: Subscription Product Definition  
● SAM - Apply latest content changes

\- Step 4: Validate and re-run the Microsoft 365 import  
● Confirm Subscription Product Definitions now have Entitlement Definition populated for identifiers  
● Re-run the Microsoft 365 subscriptions import job  
● Confirm Software model is now populated and identifiers no longer appear as unrecognized
