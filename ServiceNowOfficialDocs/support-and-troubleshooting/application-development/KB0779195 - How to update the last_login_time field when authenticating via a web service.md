---
title: "How to update the last_login_time field when authenticating via a web service"
aliases:
  - KB0779195
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779195
kb_number: KB0779195
last_modified: 2026-04-14
---

## How to update the last\_login\_time field when authenticating via a web service

  

### Issue

Resolve the `last_login_time` field on the User `[sys_user]` table not updating when a user authenticates via a web service.

When a user logs in through the UI, the User `[sys_user]` record is updated to reflect the most recent login time, login device, and other login details. However, when a user authenticates via a web service, this update does not occur by default and the `last_login_time` field retains its previous value.

### Release

All supported releases

### Cause

By default, the system does not update the `sys_user.last_login_time` field when a user authenticates via a web service (REST, SOAP, and similar protocols). This is by design — web service authentication does not trigger the same login event processing as UI authentication.

### Resolution

To enable the `last_login_time` field to update during web service authentication, set the `glide.basicauth.update_last_login_time` system property to `true`.

1.  Go to the System Properties `[sys_properties]` table.
2.  Search for the property `glide.basicauth.update_last_login_time`.
    -   If the property exists, open the record and set the Value field to `true`.
    -   If the property does not exist, create a new record with the Name `glide.basicauth.update_last_login_time` and the Value `true`.
3.  Save the record.

The `sys_user.last_login_time` field now updates when a user authenticates via a web service.
