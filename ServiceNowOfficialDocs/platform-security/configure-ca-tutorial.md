---
title: Tutorial: Configure Continuous Authentication for a Data Class
description: Procedure that describes end to end configuration of continuous authentication policy for a data class and the impacts to the users due to the configuration changes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/configure-ca-tutorial.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configuring CA, Continuous Authentication \(CA\), Zero Trust Access, Access Management]
tags:
  - platform-security
  - type-task
---

# Tutorial: Configure Continuous Authentication for a Data Class

Procedure that describes end to end [[sc-configuration|configuration]] of continuous [[c_Authentication|authentication]] policy for a data class and the impacts to the [[users|users]] due to the configuration changes.

## Before you begin

-   Role required: ca\_admin

    **Note:** You must elevate your role to **ca\_admin**.

-   You must install the **Zero Trust - Continuous Authentication** \(`com.snc.zero_trust_continuous_authentication`\) for opting CA which requires a license.
-   Enable the Continuous Authentication \(**glide.zta.continuous\_authentication.enabled**\) system property. For more information, see [[ca-system-properties|System properties]].
-   Activate the Integration - Multiple Provider Single Sign-On Installer \(**com.snc.integration.sso.multi.installer**\) plugin.
-   Understand the pre-work that is required before configuring CA for the instance. For more information, see [[pre-work-ca|Pre-work for Continuous Authentication]].

## Procedure

1.  Navigate to **All** &gt; **Continuous Authentication**.

2.  Select **[[ca-policies|Policies]]** tab.

3.  Select **New**.

4.  On the form, fill the fields:

<table id="table_cvy_xnw_ycc"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Policy Name

</td><td>

Name of the policy

</td></tr><tr><td>

Description

</td><td>

Generic description to the policy

</td></tr><tr><td>

Select the resources

</td><td>

Select the **Data Class**. You can create data class and use it for CA policy configuration.**Note:** To know more about how to create data class, see [Data Classification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-classification/data-classification.md).

</td></tr></tbody>
</table>    \[Omitted image "ca-policy-dataclass.png"\] Alt text: CA Policy for a Data Class

    **Note:** You can use either of the login methods for the CA policy:

    -   **SSO based login**: Specify the fields in the **Continuous Authentication** tab within the [[identity-landing|Identity]] Provider record and the set the Identity Provider record as **Active**. \[Omitted image "ca-tab.png"\] Alt text: Continuous Authentication - tab information

        To know more about Identity Providers configuration, see [OIDC](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/create-OIDC-configuration-SSO.md) and [SAML](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/t_CreateASAML2Upd1SSOConfigMultiSSO.md).

    -   **Non-SSO based login**: By default, if there are no Identity Provider with Continuous Authentication configuration, [[mfa-landing|Multi-factor Authentication]] \(MFA\) is used as a login method. Make sure the MFA properties are Active and configured based on your requirement. To know more about MFA properties, see [Multi-factor Authentication system properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/mfa-properties.md).
5.  Select **Save &amp; Activate**.


## Result

Based on the details provided for the configuration, CA policy is created with [[sc-access-control|Access Control]] List \(ACLs\) for the selected table or data class. You can view the details of the ACLs that are created by selecting the **View ACLs** on the policy page.

\[Omitted image "ca-acl-details-dataclass.png"\] Alt text: ACL Details for Data Class CA policy

The CA policy created, prompts the user for authentication to data class \(in this case data class set for the table **Account Recovery**\) that you've protected using the policy. The users can select **Authenticate** option.

\[Omitted image "ca-policy-data-class.png"\] Alt text: CA Policy enforced for data class

Perform the authentication based on the following:

-   User who had performed local login to log in to the instance, is displayed with platform MFA for step-up authentication.

    \[Omitted image "mobile-screen-mfa.png"\] Alt text: MFA-SMS

-   User who had performed SSO login \(OIDC or [[c_SAML2.0WebBrowserSSOProfile|SAML]]\) to log in to the instance is displayed with the SSO for re-authentication.

    \[Omitted image "ca-sso-screen.png"\] Alt text: SSO - Screen


After successful authentication the table with the data class is displayed.

\[Omitted image "ca-acr-table-after-login.png"\] Alt text: ACR table after successful login

An high assurance session is now established for the user. High assurance session is limited to the High Assurance session length \(**glide.zta.high\_assurance.session.timeout**\) system property. If the high assurance session time exceeds the property length, the user is prompted for re-authentication or step up authentication.

**Related topics**  


[[configure-ca|Configuring Continuous Authentication]]

[[high-assurance-ca|High Assurance session with Continuous Authentication]]

[[explore-continuous-auth|Exploring Continuous Authentication]]

## Related

- [[ca-system-properties|System properties]]
- [[pre-work-ca|Pre-work for Continuous Authentication]]
- [[configure-ca|Configuring Continuous Authentication]]
- [[high-assurance-ca|High Assurance session with Continuous Authentication]]
- [[explore-continuous-auth|Exploring Continuous Authentication]]
- [[sc-configuration|Configuration]]
- [[c_Authentication|Authentication]]
- [[users|Users]]
- [[ca-policies|Policies]]
- [[identity-landing|Identity]]
- [[mfa-landing|Multi-factor authentication]]
- [[sc-access-control|Access control]]
- [[c_SAML2.0WebBrowserSSOProfile|SAML]]
