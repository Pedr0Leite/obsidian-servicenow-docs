---
title: Add the OAuth Application User
description: Add the OAuth Application User field on the OAuth Entity form to use the Client Credentials grant type for OAuth inbound integrations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/add-oauth-application-user.html
release: australia
product: Authentication
classification: authentication
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Client Credentials, Old Inbound integrations experience, OAuth Inbound, OAuth authentication, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-task
---

# Add the OAuth Application User

Add the OAuth Application User field on the [[oauth-inbound-and-outbound|OAuth]] Entity form to use the [[client-credential-grant|Client Credentials grant]] type for [[oauth-inbound|OAuth inbound]] integrations.

## Before you begin

Role required: oauth\_admin

Plugin required: [[c_OAuthApplications|OAuth 2.0]].

You must create an OAuth client. For more information, see [Create an endpoint for clients to access the instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/t_CreateEndpointforExternalClients.md).

## Procedure

1.  Open the OAuth client record that was created.

2.  Select more options icon on the page header.

3.  Select **Configure** &gt; **Form Design**.

4.  On the Form Design page, add **OAuth Application User** from the list of fields.

5.  Save or Update the form.

6.  Select the user for the **OAuth Application User**.

    For example, System Administrator.\[Omitted image "add-oauth-application-user.png"\] Alt text: OAuth Application User

    **Note:** You must use the [[rest-api-auth-scope|REST API Auth Scope]] with client credentials grant type to control the access provided to the 3rd party client.

7.  Save or Update the form.

    Any authorization [[c_requestAPI|request]] with the **Grant Type** as **[[client-credentials|Client Credentials]]**, **Client ID**, and **Secret** is passed for the associated OAuth Application User in ServiceNow®.

    **Note:** If the OAuth Application User isn’t selected on the OAuth client record or the Client Credentials property is set to `false`, then the authorization request isn’t passed.

## Related

- [[oauth-inbound-and-outbound|OAuth]]
- [[client-credential-grant|Client credentials grant]]
- [[oauth-inbound|OAuth Inbound]]
- [[c_OAuthApplications|OAuth 2.0]]
- [[rest-api-auth-scope|REST API Auth Scope]]
- [[c_requestAPI|request]]
- [[client-credentials|Client Credentials]]
