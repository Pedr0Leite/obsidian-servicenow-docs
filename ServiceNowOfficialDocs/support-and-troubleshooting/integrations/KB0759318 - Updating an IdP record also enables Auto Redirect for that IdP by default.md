---
title: "Updating an IdP record also enables Auto Redirect for that IdP by default"
aliases:
  - KB0759318
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759318
kb_number: KB0759318
last_modified: 2023-07-12
---

## Updating an IdP record also enables Auto Redirect for that IdP by default

  

### Issue

Updating an IdP record even with a minor change, set **Auto Redirect IdP** checkbox as true for that IdP. Now that this checkbox is read-only therefore, in order to turn it off, you always need to go to system properties and set the value of system property glide.authenticate.sso.redirect.idp as empty.

  

This article explains how to avoid this default update.

### Cause

This is an OOB behaviour and controlled by Business Rule **MultiSSO - Activated second IDP** whenever you update an IdP record.

  

### Resolution

Deactivate Business Rule **MultiSSO - Activated second IDP,** post which updating the IdP record will not set **Auto Redirect IdP** checkbox as true for that specific IdP. Going forward this feature will be controlled via **Set as Auto Redirect IdP** Related Link(s) only and not when you simply update the IdP record.
