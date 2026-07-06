---
title: "Password is blocked after only one unsuccessful attempt"
aliases:
  - KB0752484
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752484
kb_number: KB0752484
last_modified: 2024-04-07
---

## Password is blocked after only one unsuccessful attempt

  

### Issue

# Symptoms

Users are getting locked out of their accounts after only one unsuccessful password entry.

# Release

all releases.

# Cause

password\_reset.request.max\_attempt is set to 1.

# Resolution

Set the property password\_reset.request.max\_attempt to 2 or more. Can also be located in Password Reset > Properties module.
