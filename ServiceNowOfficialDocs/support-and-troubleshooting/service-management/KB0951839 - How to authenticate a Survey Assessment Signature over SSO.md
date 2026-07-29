---
title: "How to authenticate a Survey Assessment Signature over SSO"
aliases:
  - KB0951839
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951839
kb_number: KB0951839
last_modified: 2025-01-02
---

## How to authenticate a Survey Assessment Signature over SSO

  

### Summary

When using Signature for Survey Assessments, users are requested to provide their credentials when submitting a survey.

Signature configured on Survey Assessment is authenticating against User table.

How to authenticate using SSO instead?

### Instructions

The code was designed to only allow the signature to work with a local login.  
  
The current functionality uses the 'GlideUser().authenticate(user\_name, password)' to validate the user authentication.

This get the data from the 'sys\_user' table which contains user's local user name and password.  

Unfortunately, Survey/Assessment signature is designed for local logins only.
