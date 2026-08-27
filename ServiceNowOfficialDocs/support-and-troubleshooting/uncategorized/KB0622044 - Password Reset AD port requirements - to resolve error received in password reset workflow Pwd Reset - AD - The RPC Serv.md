---
title: "Password Reset AD port requirements - to resolve error received in password reset workflow Pwd Reset - AD - The RPC Server is unavailable"
aliases:
  - KB0622044
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622044
kb_number: KB0622044
last_modified: 2024-04-07
---

## Issue

TCP port 389 and 445 from MID server host to Active Directory Domain Controller must be enabled for password reset to work.

These are the only two ports required for password reset, WMI ports are not required.
