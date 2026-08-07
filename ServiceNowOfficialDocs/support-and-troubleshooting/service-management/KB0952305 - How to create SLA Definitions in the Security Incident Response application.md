---
title: "How to create SLA Definitions in the Security Incident Response application"
aliases:
  - KB0952305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0952305
kb_number: KB0952305
last_modified: 2025-01-02
---

## How to create SLA Definitions in the Security Incident Response application

  

### Summary

The below steps can be followed, when a user has correct roles, to create SLA Definitions from within the Security Incident Response scoped application.

### Instructions

_Roles required: **sn\_si.admin** and **admin**  
_

1\. Log in to the desired instance

2\. In the left navigator, type "Security Incident", and navigate to **Security Incident** ➛ **Setup** ➛ **SLAs**

3\. From this table, select the "New" UI Action  

4\. Create your new SLA Definition, setting all desired field values, and select the "Submit" button in the top right of the form when ready  
  

Note: Attempting to create SLA Definitions through the traditional means, even when the user has **sn\_si.admin** and **admin** roles (i.e. through going to contract\_sla table) will cause the SLA form to display incorrectly due to failing ACLs. Please use the correct, above method to create SLA Definitions specifically for the Security Incident Response application.
