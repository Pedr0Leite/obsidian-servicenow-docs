---
title: "Microsoft 365 SAM integration profile saves without a REST Message; jobs fail with \"No REST message record found\""
aliases:
  - KB3066264
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3066264
kb_number: KB3066264
last_modified: 2026-06-05
---

## Text

**Issue:**

Creating a Microsoft 365 integration profile (SAM Pro / SaaS License Management) saves the profile but leaves the REST message field blank and creates no `sys_rest_message` record. The Microsoft 365 import jobs then fail with the following error in system logs:

```
No REST message record found for the Microsoft 365 integration profile: <profile_sys_id>
SAM:SAM - Import M365 User Subscriptions: Failed to run job.
```

Profiles created with a unique Display Name succeed; recreating one with the same Display Name + Tenant ID fails. The failure is unrelated to the Client ID/Secret values.

**Cause:**

On insert, the business rule **Create Office 365 OAuth app and REST msg** auto-creates an OAuth Application Registry record (`oauth_entity`) named `<DisplayName>_<TenantID>_app`. The `oauth_entity` Name column has a unique index (`oauth_entity_name_key`). If that name already exists (leftover from an earlier attempt or an improperly removed profile), the insert is rejected:

```
duplicate key value violates unique constraint "oauth_entity_name_key"Detail: Key (name)=(<DisplayName>_<TenantID>_app) already exists.
```

With the OAuth app insert failing, the rule never gets the OAuth profile reference and then errors in the Azure AD Spoke credential step, terminating before the REST Message is created:

```
Unable to match value 'undefined' with field 'oauth_entity_profile' in table 'oauth_2_0_credentials'. Expecting type 'reference'
```

The profile still saves — without an OAuth app or REST Message — so the jobs fail. Since the name derives only from Display Name + Tenant ID, a unique display name avoids the collision while a repeated one triggers it.

**Resolution:**

Use either option:

**Option A — Use a unique Display Name (no deletions):**

Recreate the integration profile with a Display Name that differs from any existing one (Tenant ID can stay the same). This produces a new, unique OAuth app name, so the rule creates the OAuth app, profile, REST Message, and HTTP methods cleanly without touching the existing OAuth records.

**Option B — Remove the leftover OAuth records, then recreate:**

1.  In System OAuth → Application Registry, find the `oauth_entity` named `<DisplayName>_<TenantID>_app` and confirm no active profile (`samp_sw_subscription_profile.oauth_app`) still uses it.
2.  If orphaned, delete it and its dependents: `oauth_entity_profile_scope`, `oauth_entity_scope`, the child `sys_alias` connection alias and its `http_connection` / `oauth_2_0_credentials` / `connection_attributes`, the `oauth_entity_profile` records, the `oauth_entity`, and any leftover `sys_rest_message` named `<DisplayName>_<TenantID>_REST_msg`.
3.  Recreate the profile and confirm the REST Message populates and the import job completes.

**Reference Doc:**

[Create a Microsoft 365 integration profile](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/set-up-microsoft-office-365.html)
