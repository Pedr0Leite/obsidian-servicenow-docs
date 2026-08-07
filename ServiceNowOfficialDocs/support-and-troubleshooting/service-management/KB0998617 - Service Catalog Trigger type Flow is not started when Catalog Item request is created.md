---
title: "\"Service Catalog\" Trigger type Flow is not started when Catalog Item request is created"
aliases:
  - KB0998617
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998617
kb_number: KB0998617
last_modified: 2026-01-13
---

## "Service Catalog" Trigger type Flow is not started when Catalog Item request is created

  

### Issue

In some customer instances, after defining a Service Catalog–type trigger flow in Flow Designer, the flow does not start when a catalog request is submitted.

The same flow works correctly in their PDI or development instance.

### Release

All

### Cause

This occurs because the customer may not have the request set to be approved first.

The OOB workflow below is used to automatically approve requests.

This workflow is included in demo data; therefore, some production instances may not have it installed.

![Service catalog request workflow](sys_attachment.do?sys_id=6a4aada7939aba90def533527cba1020)

Details of the Request management structure can be referred to below:

[Request Management architecture](https://www.servicenow.com/docs/bundle/zurich-it-service-management/page/product/planning-and-policy/concept/request-management-architecture.html)  

### Resolution

The Service Catalog flow will start once the Request record has been approved.

This can be done manually or by creating a workflow or flow to perform the same action.

You can also refer to the KB below to install the OOB workflow:

[KB0687119 - Service Catalog Item Request and Service Catalog Request OOB workflows/ flows are missing](https://hi.service-now.com/kb_view.do?sysparm_article=KB0687119 "KB0687119")
