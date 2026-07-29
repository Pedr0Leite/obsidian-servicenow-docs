---
title: "User gets permissions error when trying to create a response template "
aliases:
  - KB1707094
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1707094
kb_number: KB1707094
last_modified: 2025-09-08
---

## Issue

Upon submitting the creation of a response template, that includes the "Open for" field, the user gets the below error despite having "sn\_templated\_snip.template\_snippet\_writer" role.

"Following variables are not accessible based on your permissions: ${opened\_for}"  
  
![](/sys_attachment.do?sys_id=a4ebdc6847391e50c2488d01426d435b "ResponseTemplate.png")  

![](/sys_attachment.do?sys_id=759a9c2447391e50c2488d01426d4333)

## Resolution

The resolution is to create an explicit ACL for those fields that will be used in the response template, making sure read access is being provided to  the user creating the template.  
  
Note: If the table used for the template is scoped, the ACL would need to be scoped as well.
