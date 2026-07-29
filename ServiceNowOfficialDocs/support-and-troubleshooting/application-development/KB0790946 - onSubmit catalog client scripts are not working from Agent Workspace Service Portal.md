---
title: "onSubmit catalog client scripts are not working from Agent Workspace Service Portal"
aliases:
  - KB0790946
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790946
kb_number: KB0790946
last_modified: 2024-04-08
---

## onSubmit catalog client scripts are not working from Agent Workspace Service Portal

  

### Issue

The client script is acting properly in service portal and not in agent workspace.

Please check if customer is using " GlobalCAtalogItemFUnctions API function" in the UI script.

It has angular in it.This angular is not supported in agent workspace but this is supported in service portal.

### Cause

Error message shown:

"Please attach Cost Transfer form before submitting the request"

This error message has been found on customer instance.

Error message will not be exact like the above in different cases.

.

### Resolution

In order to work this client script in agent workspace customer has  to change this angular in UI script.
