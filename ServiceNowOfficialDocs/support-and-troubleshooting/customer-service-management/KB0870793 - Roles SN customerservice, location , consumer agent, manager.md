---
title: "Roles SN customerservice, location , consumer agent, manager"
aliases:
  - KB0870793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870793
kb_number: KB0870793
last_modified: 2023-12-23
---

## Roles SN customerservice, location , consumer agent, manager

  

### Issue

roles are: sn\_customerservice.svc\_location\_consumer\_agent & sn\_customerservice.svc\_location\_manager which are both documented as existing in Paris

[Paris Field Service Management](https://docs.servicenow.com/bundle/paris-field-service-management/page/product/field-service-management/concept/setup-fsm-agent-workspace.html "Paris Field Service Management")

But the roles don't appear to exist in Paris instances, and this has caused an issue where the ACLs were passed due to the roles not existing. 

### Cause

The plugin industry data models is nbot active

### Resolution

  
The roles sn\_customerservice.svc\_location\_consumer\_agent & sn\_customerservice.svc\_location\_manager are from the plugin Configure industry data models  
  
**Industry data model roles**

[Paris Customer Service Management](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/csm-data-model-roles.html "Paris Customer Service Management DOC")

**Configure industry data models**

  
[Paris Customer Service Management](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/task/configure-industry-data-model.html "Paris Customer Service Management")
