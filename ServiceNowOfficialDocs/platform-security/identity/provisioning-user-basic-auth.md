---
title: Provisioning user using Basic Authentication
description: Configuring SCIM automatically provisions and de-provisions users and groups to ServiceNow by using the providers' provisioning service with Basic Authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/identity/provisioning-user-basic-auth.html
release: australia
product: Identity
classification: identity
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Tutorial: Configure SCIM for user provisioning with a Provider, SCIM Provider, System for Cross-domain Identity Management \(SCIM\), Identity]
---

# Provisioning user using Basic Authentication

Configuring SCIM automatically provisions and de-provisions [[users|users]] and groups to ServiceNow by using the providers' provisioning service with [[basic-authentication|Basic Authentication]].

## Before you begin

Role required: scim\_admin

**Warning:** Grant this role carefully. The scim\_admin role is equivalent to giving the user the admin role, where the scmin\_admin can add or update Personally Identifiable Information \(PII\).

You must activate the SCIM plugin.

## Procedure

1.  Navigate to **All** &gt; **System Web Services** &gt; **[[inbound-authentication-profile|REST API Access Policies]]** to check the details on the REST API Access Policies.

2.  In the [[api-access-policy|API Access Policy]] page, click the **SCIM API Policy** record.

3.  Verify the **SCIM API Basic Auth** record is available in the [[c_Authentication|Authentication]] Profiles sections.

4.  Select **Basic Auth** as the Type.

5.  Create the required configurations at the provider's end.

6.  Test the connection to ensure that the provider can connect to ServiceNow.

    **Note:** If the connection fails, ensure that your ServiceNow account has admin permissions and try again.

## Related

- [[users|Users]]
- [[basic-authentication|Basic authentication]]
- [[inbound-authentication-profile|REST API access policies]]
- [[api-access-policy|API access policy]]
- [[c_Authentication|Authentication]]
