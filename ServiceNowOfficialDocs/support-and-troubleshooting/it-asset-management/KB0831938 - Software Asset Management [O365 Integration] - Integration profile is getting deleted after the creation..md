---
title: "Software Asset Management [O365 Integration] - Integration profile is getting deleted after the creation."
aliases:
  - KB0831938
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831938
kb_number: KB0831938
last_modified: 2024-04-08
---

## Issue

This document was followed to integrate O365 and ServiceNow as a SAAS license in Software Asset Management.

[https://docs.servicenow.com/csh?topicname=set-up-microsoft-office-365.html&version=latest](https://docs.servicenow.com/csh?topicname=set-up-microsoft-office-365.html&version=latest)

After following the steps, the Integration profile is getting deleted after the creation.

Only the "oauth\_entity" and the "sys\_rest\_message" will get created.

## Resolution

1\. Removed the following:

a. oauth\_entity

b. sys\_rest\_message

2\. Try to follow the procedures again to create the Integration Profile.

3\. Check the Integration Profile and should be created.
