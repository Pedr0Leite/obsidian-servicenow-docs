---
title: Provisioning user using OAuth
description: Configure the provider for SCIM automatically provisions and de-provisioning of users and groups to ServiceNow by using the providers provisioning service with OAuth.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/identity/provisioning-user-oauth.html
release: australia
product: Identity
classification: identity
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Tutorial: Configure SCIM for user provisioning with a Provider, SCIM Provider, System for Cross-domain Identity Management \(SCIM\), Identity]
tags:
  - platform-security
  - identity
  - idp
  - federation
  - sso
  - type-task
---

# Provisioning user using OAuth

Configure the provider for SCIM automatically provisions and de-provisioning of [[users|users]] and groups to ServiceNow by using the providers provisioning service with [[oauth-inbound-and-outbound|OAuth]].

## Before you begin

Role required: scim\_admin

**Warning:** Grant this role carefully. The scim\_admin role is equivalent to giving the user the admin role, where the scmin\_admin can add or update Personally Identifiable Information \(PII\).

You must activate the SCIM plugin.

## Procedure

1.  Navigate to **All** &gt; **System OAuth** &gt; **Application Registry**.

2.  In the Application Registries page, click the **SCIM API** record.

3.  Verify the **SCIM API** record details.

    These details should be provided while configuring the ServiceNow application on Azure AD.

4.  Navigate to **All** &gt; **System Web Services** &gt; **[[inbound-authentication-profile|REST API Access Policies]]** to check the details on the REST API Access Policies.

5.  In the [[api-access-policy|API Access Policy]] page, click the **SCIM API Policy** record.

6.  Verify the **SCIMAPIOAuthOnly** record is available in the [[c_Authentication|Authentication]] Profiles sections.

7.  Check if the **OAuth Entity** field is specified with **SCIM API** record that was earlier configured or verified as application registry.

8.  Create the required configurations at the provider's end.

9.  Test the connection to ensure that the provider can connect to ServiceNow.

    **Note:** If the connection fails, ensure that your ServiceNow account has admin permissions and try again.

## Related

- [[users|Users]]
- [[oauth-inbound-and-outbound|OAuth]]
- [[inbound-authentication-profile|REST API access policies]]
- [[api-access-policy|API access policy]]
- [[c_Authentication|Authentication]]
