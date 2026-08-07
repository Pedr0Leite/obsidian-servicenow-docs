---
title: "HR Onboarding Workflow approvals are not marking the \"Approval\" field on the parent HRC record to \"Rejected\" when approvers reject"
aliases:
  - KB0830995
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830995
kb_number: KB0830995
last_modified: 2024-09-20
---

## HR Onboarding Workflow approvals are not marking the "Approval" field on the parent HRC record to "Rejected" when approvers reject

  

### Issue

The user had a HR Onboarding Workflow where approvals, upon rejection, were not marking the "Approval" field on the parent HRC record to "Rejected" as expected. They wanted to know why.

### Resolution

The issue, in this case, is that the user had a custom approval script within their Approval - User workflow activity.   
  
The rejection should occur if the script entered a certain "if" condition, and through putting in many **gs.info** debugging statements, it was found that the if's condition was not satisfied. Hence, the code to mark the parent HRC record was never run and the "Approval" field was never set to "Rejected".  
  
As the code was custom, and as Support Engineers are experts in OOB behavior, and specialize in resolving OOB break-fix behaviors, it was shared with the user that it is their responsibility to evaluate and fix the incorrect, custom code internally.
