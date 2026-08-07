---
title: "Unable to create a Standard Change Template - why?"
aliases:
  - KB0748181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748181
kb_number: KB0748181
last_modified: 2024-04-07
---

## Unable to create a Standard Change Template - why?

  

### Issue

# Symptoms

-   When the user is trying to create a simple Standard Change Template, the system is not allowing them. The template will not process to completion. 

# Release

-   Kingston Patch 12

# Cause

In this case, the user was trying to utilize a custom group to populate Approvers, but the Platform's "Standard Change Catalog" workflow is hard-coded to point to the Out of Box (OOB) "Change Management" group which was not present in the user's instance.  
  
Read on for more details.

# Resolution

It was also discovered that in order to use a custom group to populate Approvers (a necessary step to create a Standard Change Template), the below details must be true:

-   The group must have at least one member, and
-   The group itself must possess the "change\_manager" role to be able to have its users populate as approvers for a Standard Change Template, and
-   The associated workflow's "Approval - Group" activity must be updated to reflect the new custom group \[versus the OOB "Change Management" group which is hard-coded into that activity\]

There was also an additional DOC request created to address the incomplete nature of the current documentation on how to create a Standard Change Template: DOC67866.
