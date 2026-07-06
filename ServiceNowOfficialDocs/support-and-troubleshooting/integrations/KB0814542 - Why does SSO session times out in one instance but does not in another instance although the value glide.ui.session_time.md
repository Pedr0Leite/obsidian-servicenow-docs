---
title: "Why does SSO session times out in one instance but does not in another instance although  the value glide.ui.session_timeout' is the same ?"
aliases:
  - KB0814542
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814542
kb_number: KB0814542
last_modified: 2025-02-13
---

## Why does SSO session times out in one instance but does not in another instance although the value glide.ui.session\_timeout' is the same ?

  

### Issue

This issue can happen in a scenario where 2 instances have  the same value for 'glide.ui.session\_timeout', for example, 60 minutes, but the session is persisted by the Identity Provider (IDP).

In this context, the session settings on the IDP provider can be something like 7 hours, however, in one instance the session persists for as long as the 7 hours and in the other instance the session times out after the 60 minutes.

### Release

Any

### Cause

This is related to the IDP option 'Force authentication request'

### Resolution

Whilst Azure is configured with "tenant independent endpoint" , it is correct for the same URL to be used with 2 instances, however there is another option that can trigger this inconsistent behaviour of the session duration.

The IDP record in the Platform has the option 'Force authentication request' set to enabled. When 'Force authentication request' is enabled, this means that when the default 60 minutes set in 'glide.ui.session\_timeout' expire, the authentication is requested rather than automatically granted.
