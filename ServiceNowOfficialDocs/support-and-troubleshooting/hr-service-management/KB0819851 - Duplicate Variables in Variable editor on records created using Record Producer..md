---
title: "Duplicate Variables in Variable editor on records created using Record Producer."
aliases:
  - KB0819851
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819851
kb_number: KB0819851
last_modified: 2026-02-17
---

## Issue

Some of the records showing variables twice in the variable editor

## Resolution

For the affected eg records try clearing extra values which have been created in question\_answer table.

To prevent this in near future customer can add a business rule which will prevent duplicate records insertion

[https://docs.servicenow.com/csh?topicname=c\_EnforcingUniqueNumbering.html&version=latest](https://docs.servicenow.com/csh?topicname=c_EnforcingUniqueNumbering.html&version=latest)
