---
title: "Import API is not giving a response "
aliases:
  - KB0813223
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813223
kb_number: KB0813223
last_modified: 2025-01-03
---

## Import API is not giving a response

  

### Summary

A user without admin roles, but with  required roles for REST API Explorer (web\_service\_admin, rest\_api\_explorer) is not getting RESPONSE 

User is trying to POST a record to import set via Import set API

[https://<instance>.service-now.com/api/now/import/<staging table>](https://fastenaltst.service-now.com/api/now/import/u_create_incident)

He is getting Response code as 201 but no response

![](/sys_attachment.do?sys_id=7ac32b3cdbcc38d022e0fb2439961982)

### Related Links

Apart from checking Table and field ACL's for that table, you may need to add any of the below roles to the user.

| Role | Description |
| --- | --- |
| import\_set\_loader | Allows users to load import sets. |
| import\_scheduler | Allows users to scheduled imports. |
| import\_transformer | Allows users to manage import set transform maps and run transforms. |
| import\_admin | Allows users to manage all aspects of import sets and imports. |
