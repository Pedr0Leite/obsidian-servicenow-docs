---
title: "Setting a multi-row variable mandatory"
aliases:
  - KB0778516
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778516
kb_number: KB0778516
last_modified: 2025-05-30
---

## Setting a multi-row variable mandatory

  

### Issue

The user wants to know how to set a multi-row variable to mandatory. They are able to set the variables in the variable set mandatory, but that does not prevent the end-user from submitting the request with no data.

### Cause

**Note:** Catalog UI Policies **do not enforce mandatory behavior** on Multi-Row Variable Sets (MRVS) in the **non-portal (Platform UI)** view. This behavior is only supported in the **Service Portal**. If MRVS fields must be mandatory in non-portal views, consider using a Catalog Client Script or other workarounds.

### Resolution

Unfortunately, it is true that until or unless the user makes the multi-row variable set (MRVS) itself mandatory, an end-user can simply bypass the variable set even when the variables inside the MRVS are set to mandatory.

What is needed in this case is a way to force the end-user to open up the MRVS per the "Add" UI Action (prevent them from submitting the Request until they do this) - then, things will progress naturally (as at this point the user has already set the variables inside the MRVS to mandatory).  
  
To do this, on the affected Catalog Item, create a Catalog UI Policy.  
  
Within the Catalog UI Policy, create a Catalog UI Policy Action which sets the MRVS itself to mandatory. This change will now wholly prevent the user from ordering the Catalog Item until they interact with the MRVS. Then, when they open the MRVS per the "Add" button, the user has their mandatory variables and the end-user must provide values to proceed with submitting the Request.
