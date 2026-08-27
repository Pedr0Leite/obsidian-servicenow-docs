---
title: "About error cross scope access privilege denied error"
aliases:
  - KB2291532
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2291532
kb_number: KB2291532
last_modified: 2026-03-24
---

## About error cross scope access privilege denied error

  

### Summary

When operate HR or legal relevant records, access portals, some time error below happens.

XXX operation on table 'AAA' from scope 'BBB' was denied. The application 'CCC' must declare a cross scope access privilege. Please contact the application admin to update their access requests.

![](/sys_attachment.do?sys_id=f0ec6d2347ae2654c2488d01426d4300 "2025-07-11_17-13-47.png")

### Release

All Releases.

### Instructions

This is an expected behavior.

When the operation needs access the restricted scope, there is a record generated at  Restricted Caller Access Privileges table(**sys\_restricted\_caller\_access**), with Status=Requested.

This makes the error happened.

The error is also an expected behavior, which means, the admin has to review the operation and confirm if the access is allowed or not, regarding the business needs.

If the operation is allowed, detect the record generated at sys\_restricted\_caller\_access, and change the status from **Requested** to **Allowed**.

Else admin needs to deny the request by setting status from **Requested** to **Denied**.

Basically, all status = Requested records in table **sys\_restricted\_caller\_access** should be checked and confirmed. 

In other words, status=Requested should not exist.

For more details, refer to the official document '[Define cross-scope access to an application resource](https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest)' by clicking [here](https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest).
