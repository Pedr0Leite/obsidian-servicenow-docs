---
title: Activate the MFA with SMS plugin
description: For MFA with SMS, install the Multi-factor authentication with SMS \(com.snc.authentication.sms\_mfa\) plugin.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/active-mfa-sms-plugin.html
release: australia
product: Authentication
classification: authentication
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [SMS as an MFA factor, MFA factor policies, MFA verification methods, Configuring MFA, Multi-factor authentication, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-task
---

# Activate the MFA with SMS plugin

For MFA with SMS, install the [[mfa-landing|Multi-factor authentication]] with SMS \(`com.snc.[[c_Authentication|authentication]].sms_mfa`\) plugin.

## Before you begin

Role required: admin

## About this task

The following items are installed with Multi-factor authentication with SMS:

-   [[adaptive-authentication|Adaptive Authentication]] \(`com.snc.adaptive_authentication`
-   Notify - Twilio Direct Driver \(`com.snc.notify.twilio_direct`\)

Dependent Plugin: Integration - Multifactor Authentication \(`com.snc.integration.multifactor.authentication`\)

**Note:** You can load the demo data when installing the plugin if you are configuring a custom provider for generating the SMS.

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Multi-factor authentication with SMS plugin \(`com.snc.authentication.sms_mfa`\) using the [[adaptive-auth-filter-criteria|filter criteria]] and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to [[c_requestAPI|request]] it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Related

- [[mfa-landing|Multi-factor authentication]]
- [[c_Authentication|Authentication]]
- [[adaptive-authentication|Adaptive authentication]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[c_requestAPI|request]]
