---
title: "Jira Spoke - Webhook Routing Policies"
aliases:
  - KB0852278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852278
kb_number: KB0852278
last_modified: 2025-01-02
---

## Jira Spoke - Webhook Routing Policies

  

### Summary

Custom fields created in Jira are not available while configuring Jira Webhook Routing Policies under conditions, although this is available in the incoming payload from Jira to ServiceNow instance.

  

### Related Links

Jira Webhook Routing Policies i.e., Decision Table (sys\_decision\_question) currently does not support custom fields. Fields present in the condition are hardcoded and these are not configurable.
