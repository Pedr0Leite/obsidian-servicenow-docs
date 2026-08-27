---
title: "Patch method in Change Management API is not updating State fields"
aliases:
  - KB0816149
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816149
kb_number: KB0816149
last_modified: 2025-05-22
---

## Patch method in Change Management API is not updating State fields

  

### Issue

API : Change Management

NameSpace: sn\_chg\_rest

Normal (Patch) method to update the "state" is throwing error as below

Normal Change Request cannot move to state: scheduled

### Resolution

You need to pass the \`Label\` value in Change Management API, but in table API it should be the value

Namespace= sn\_chg\_rest

API Name= Change Management

API version= latest

PATCH https://<instance-name>.service-now.com/api/sn\_chg\_rest/change/standard/{sys\_id}

### Related Links

Refer more in detail: [https://developer.servicenow.com/app.do#!/rest\_api\_doc?v=madrid&id=c\_change-management-api](https://developer.servicenow.com/app.do#!/rest_api_doc?v=madrid&id=c_change-management-api)
