---
title: "Determining if the SAML issue is the result of the user having a duplicate record"
aliases:
  - KB0538780
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538780
kb_number: KB0538780
last_modified: 2025-10-21
---

## Issue

Troubleshooting: Determining if the SAML issue is the result of the user having a duplicate record

The user cannot log in to the system or log in as the correct user.

## Resolution

  To solve the issue:

1.  Check the SAML logs to find out which user ID is being used. 
2.  Look up the **sys\_user** table, and check if there are duplicate user records with the same user ID.
3.  If so, delete the duplicate record.
4.  Ask the user to try to log in again.
