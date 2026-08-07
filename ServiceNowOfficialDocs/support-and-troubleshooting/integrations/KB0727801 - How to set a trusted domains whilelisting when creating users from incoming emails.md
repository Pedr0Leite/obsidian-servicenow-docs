---
title: "How to set a trusted domains whilelisting when creating users from incoming emails "
aliases:
  - KB0727801
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727801
kb_number: KB0727801
last_modified: 2026-01-06
---

## How to set a trusted domains whilelisting when creating users from incoming emails

  

### Issue

Is it possible to restrict the domains for which the users will be created from incoming Emails from outside your company domain?

### Release

All releases

### Cause

Incoming Emails are filtered by a system property: "glide.user.trusted\_domain". The default is a \* (which allows all domains).

This property matches the field "Trusted domains when creating new users from incoming email" in Email properties.

### Resolution

Set 'Trusted domains when creating users from incoming email' to a comma-separated list of trusted domains for which the instance automatically creates a guest user based on incoming emails. Use an asterisk (\*) to trust all domains.

_servicenow.com, yourcompany.com_

 **Note:** The setting "**Automatically create users for incoming emails from trusted domains**" should also be enabled.

If an email is not from a trusted domain, the instance processes the inbound email as a "guest user" however, it does not create a guest user in the instance.

-   **Type**: string
-   **Default value**: asterisk (\*)

 **Warning:** Potentially unlimited number of Emails can be added into a Servicenow instance unless either "glide.user.trusted\_domain" is set, OR, Email filters are used.
