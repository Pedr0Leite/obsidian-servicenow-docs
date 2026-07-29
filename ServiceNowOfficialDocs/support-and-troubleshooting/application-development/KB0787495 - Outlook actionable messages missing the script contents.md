---
title: "Outlook actionable messages missing the script contents"
aliases:
  - KB0787495
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787495
kb_number: KB0787495
last_modified: 2024-04-08
---

## Issue

Knowledge Article talks about the <script> content is missing in the Outlook Actionable messages.

Outlook Actionable messages not carrying the <script> contents being encoded in sent approval email which is referred to in the notification by the email script "include\_approval\_actionable".

Document Reference for OAM on Approval Email: [https://docs.servicenow.com/csh?topicname=embed-approval-in-outlook.html&version=latest](https://docs.servicenow.com/csh?topicname=embed-approval-in-outlook.html&version=latest "https://docs.servicenow.com/csh?topicname=embed-approval-in-outlook.html&version=latest")

## Resolution

Please check the Type of the Body field for sys\_email table in sys\_dictionary is "String (Full UTF-8)"
