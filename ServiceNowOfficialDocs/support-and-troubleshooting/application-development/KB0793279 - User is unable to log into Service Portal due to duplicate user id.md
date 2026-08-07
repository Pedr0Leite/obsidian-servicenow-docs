---
title: "User is unable to log into Service Portal due to duplicate user id"
aliases:
  - KB0793279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793279
kb_number: KB0793279
last_modified: 2026-03-03
---

## User is unable to log into Service Portal due to duplicate user id

  

### Issue

What is the result of allowing a duplicate value for the "User ID"(sys\_user.user\_name) column by setting the "Unique" field's value of its sys\_dictionary record to 'false'?

### Release

Any

### Resolution

By default, NO duplicate entries for the "User ID"(sys\_user.user\_name) column are allowed. 

The instance prevents duplicate records from being created by setting the "Unique" value in its sys\_dictionary record to 'true'

/sys\_dictionary.do?sys\_id=73f49b00db1123008102d311ce961928

If the "User ID"(sys\_user.user\_name) column can be duplicated, users can not be correctly authenticated because "User ID" and "Password" generally are used.

Allowing duplicate user entries sharing the same user names is not supported out of the box as it can affect: Authentication, User Imports, and Security.
