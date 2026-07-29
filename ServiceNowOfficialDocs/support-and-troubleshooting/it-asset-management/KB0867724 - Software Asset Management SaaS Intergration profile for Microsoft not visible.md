---
title: "Software Asset Management: SaaS Intergration profile for Microsoft not visible"
aliases:
  - KB0867724
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867724
kb_number: KB0867724
last_modified: 2023-11-11
---

## Software Asset Management: SaaS Intergration profile for Microsoft not visible

  

### Issue

SaaS Integration profile for Microsoft is not visible even though Software Asset Management for Microsoft and SaaS License Management plugins are installed in the instance.

![](sys_attachment.do?sys_id=1bc47b89dbcda410190b1ea668961982)

### Release

Software Asset Management Microsoft and SaaS License Management plugins are installed.

### Resolution

\- Navigate to SaaS License -> Administration -> Create New Profile -> Click on the "Interceptor" on the right side corner.

\- The interceptor page would open and in the answer section check if the "Direct to Office 365 Subscription Profile" is active and if it is not activate it like below.

![](sys_attachment.do?sys_id=f4f5bb05db01e410190b1ea66896198d)
