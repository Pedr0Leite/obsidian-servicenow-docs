---
title: "Resolve flow activation issue for Service Catalog items"
aliases:
  - KB0863116
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863116
kb_number: KB0863116
last_modified: 2025-08-28
---

## Resolve flow activation issue for Service Catalog items

  

### Summary

After submitting a request, the flow is not visible in the Service Catalog as shown in the following image.

![Service catalog does not show the flow context after submitting the request](sys_attachment.do?sys_id=15929a4b936fa6145736b25d6cba106c)

### Release

All supported releases

### Instructions

In this scenario, the request approval status was not set to approve by the default workflow when the request was created. 

To resolve this issue:

1.  Verify that the default workflow sets the approval status correctly.
2.  If the default workflow doesn't set the approval status, create a business rule to set it automatically.

Sample code:

var gr = new GlideRecord('sc\_request');  
gr.get('614b59271bc46010411e80f4464bcb95');  
gr.approval='approved';  
gr.update();
