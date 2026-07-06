---
title: "Page stuck on \"Establishing Session\" after login"
aliases:
  - KB0746907
  - Page stuck on "Establishing Session" after login
tags:
  - servicenow
  - support-kb
  - login
  - session
  - glide-login-home
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746907
kb_number: KB0746907
last_modified: 2024-04-20
---

## Page stuck on "Establishing Session" after login

  

### Issue

# Symptoms

Page stuck on "Establishing Session" after login

![](sys_attachment.do?sys_id=35aa68a6db42b450e515c2230596191f)

# Release

All Supported

# Cause

Caused by a newline character in the value field on the system property "glide.login.home".

![](sys_attachment.do?sys_id=75aa68a6db42b450e515c22305961924)

# Resolution

Remove the extra space from the value on "glide.login.home" property

## Related

- [[KB0745590 - session_timeout page is displayed when navigating to instance URL using side_door]]
- [[KB0746067 - Disable local login on the instance by disabling login.do page]]
