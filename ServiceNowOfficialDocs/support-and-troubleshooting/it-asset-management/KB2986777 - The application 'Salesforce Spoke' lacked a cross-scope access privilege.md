---
title: "The application 'Salesforce Spoke' lacked a cross-scope access privilege "
aliases:
  - KB2986777
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2986777
kb_number: KB2986777
last_modified: 2026-05-19
---

## The application 'Salesforce Spoke' lacked a cross-scope access privilege

  

### Issue

**Problem**  
The Salesforce CRM direct SaaS integration scheduled jobs do not seem to trigger. No job result record is created when they're executed, despite the published status of the integration profile and successful retrieval of the OAuth token

### Release

SaaS License management - Any version

### Cause

**Root Cause**  
The application 'Salesforce Spoke' lacked a cross-scope access privilege to execute the Script Include 'SAMSaasIntegrationUtils' from the Global scope, resulting in security-restricted execution and failure to create job result records.  
  

### Resolution

**Steps to Resolve**  
1\. Identify the target Script Include and scope: Target: SAMSaasIntegrationUtils, Caller: Salesforce Spoke  
2\. Create a Cross-Scope Privilege:  
\- Navigate to: System Definition → Cross-Scope Access → Application Cross-Scope Privileges  
\- Add a record:  
\- Source Scope: Salesforce Spoke  
\- Target Scope: Global  
\- Operation: execute API  
\- Target Type: Script Include  
\- Target Name: SAMSaasIntegrationUtils  
\- Set Status to Allowed.  
3\. Re-run the job again after completing the above steps.  
  

### Related Links

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2291532](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2291532) - About error cross scope access privilege denied error

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1702731](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1702731) - Cross Scope Access Privilege Error in Subscription Management
