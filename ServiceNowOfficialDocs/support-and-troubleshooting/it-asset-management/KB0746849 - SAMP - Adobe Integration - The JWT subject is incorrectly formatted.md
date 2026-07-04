---
title: "SAMP - Adobe Integration - The JWT subject is incorrectly formatted"
aliases:
  - KB0746849
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746849
kb_number: KB0746849
last_modified: 2024-04-07
---

## SAMP - Adobe Integration - The JWT subject is incorrectly formatted

  

### Issue

# Description

* * *

The scheduled job "SAM - Import User Subscriptions" needs to retrieve a JWT token from Adobe for authentication in order to continue with the necessary calls to retrieve data.

If the job fails, check the syslog. You may see an error similar to:

Adobe - Unhandled exception: Error: {"error\_description":"The JWT subject is incorrectly formatted: missing @","error":"invalid\_token"}

# Solution

* * *

The "The JWT subject is incorrectly formatted: missing @" error is caused by bad formatting in the subject payload.

This payload is compiled from the Adobe "samp\_sw\_subscription\_profile" record, specifically the technical\_account\_id field.

This field must be an email address. If it's just a username you'll see the "missing @" error.

# Applicable Versions

* * *

All
