---
title: "Workday Direct Integration (SAM Pro SaaS LM) – \"Workday Download Subscriptions\" returns 500 with authentication error"
aliases:
  - KB2597914
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2597914
kb_number: KB2597914
last_modified: 2025-10-31
---

## Workday Direct Integration (SAM Pro SaaS LM) – "Workday Download Subscriptions" returns 500 with authentication error

  

### Issue

When publishing the Workday direct integration, Workday Download Subscriptions subflow shows HTTP 500; SOAP fault body says invalid username or password.

### Symptoms

Subflow test run: Step 2 – Look up Workers \[SOAP\] executes with Status = Success in Flow Designer (no ServiceNow runtime error).

Response from Workday: HTTP 500 and SOAP fault:

`faultcode: SOAP-ENV:Client.authenticationError`

`faultstring: invalid username or password`

### Release

Any

### Cause

Not a ServiceNow defect. The outbound SOAP request is built and sent correctly.  
Workday endpoint responds with an authentication fault, indicating credential/username format issue on the Workday side.

### Resolution

Correct the Workday credentials/username and format for the integration user.

Customer confirmed fix: adding the tenant suffix to the username (e.g., `username@<tenant>` ) resolved authentication and cleared the error.

Re-run the subflow to verify success.
