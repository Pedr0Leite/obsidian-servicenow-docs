---
title: "Restricted Change Request values are not working - why?"
aliases:
  - KB0748237
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748237
kb_number: KB0748237
last_modified: 2024-04-07
---

## Restricted Change Request values are not working - why?

  

### Issue

# Symptoms

-   In Standard Change Properties, when a user selects various Change Request fields to be restricted from selection via the Restricted Change Request values selector, _the fields selected to be restricted still display when an ITIL User selects to add a new template field under the Default Change Request values_.

# Release

-   London Patch 4, Hot Fix 2

# Cause

This was a Product Defect (PRB), and the implemented fix prevents the user from requesting approvals via the "Request Approval" UI Action.

# Resolution

Per the above cause, if a restricted field is selected, submission of the Proposed Standard Change Template is blocked and the following error message is thrown:  
  

> The following "Change Request values" are not allowed to be set in a template" 

The error message is followed by however many forbidden selected values there are, with each individual value labeled as "undefined".  
  
For example, if a user selected two restricted values, the error message would read,   
  

> "The following 'Change Request values' are not allowed to be set in a template: undefined, undefined"

Therefore, the behavior experienced is expected per the fix implemented through the PRB.
