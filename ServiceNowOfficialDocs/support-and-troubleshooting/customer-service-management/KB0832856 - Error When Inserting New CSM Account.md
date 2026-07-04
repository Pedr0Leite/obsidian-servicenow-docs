---
title: "Error When Inserting New CSM Account"
aliases:
  - KB0832856
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832856
kb_number: KB0832856
last_modified: 2025-09-23
---

## Issue

Error When Inserting New CSM Account "java.sql.BatchUpdateException: (conn=36647) Duplicate entry '0z6muD1vew9s1ycsttMqFw==' for key 'mzddhpej\_canonical\_hash\_inde'"

## Resolution

This is working as expected. If you already have the record in the **'core\_company'** table with the same name then it will cause this issue

  
This is because of below business rules:

-   Make Canonical Company
-   Set Canonical Hash

This is an out-of-the-box business rule whose logic is written in the Java layer. It should not be disabled. Instead, you should not create an account with the same name as the company. Also, the customer\_account table extends the core\_company table.
