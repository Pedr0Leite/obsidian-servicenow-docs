---
title: Activating Continuous Authentication
description: For activating the Continuous Authentication feature on your instance, install the Zero Trust - Continuous Authentication \(com.snc.zero\_trust\_continuous\_authentication\) plugin.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/activate-continuous-authentication.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Continuous Authentication \(CA\), Zero Trust Access, Access Management]
---

# Activating Continuous Authentication

For activating the Continuous [[c_Authentication|Authentication]] feature on your instance, install the **Zero Trust - Continuous Authentication** \(`com.snc.zero_trust_continuous_authentication`\) plugin.

## Before you begin

Role required: admin

This plugin enables security administrators to define security [[ca-policies|policies]] that require step-up authentication \(MFA\) or re-authentication \(SSO\) within a logged-in session, based on the data the user is accessing and the activities they are performing.

You must install the **Zero Trust - Continuous Authentication** \(`com.snc.zero_trust_continuous_authentication`\) for opting CA which requires a license.

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the **Zero Trust - Continuous Authentication** \(`com.snc.zero_trust_continuous_authentication`\) plugin using the [[adaptive-auth-filter-criteria|filter criteria]] and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to [[c_requestAPI|request]] it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).


**Related topics**  


[[pre-work-ca|Pre-work for Continuous Authentication]]

[[configure-ca|Configuring Continuous Authentication]]

[[high-assurance-ca|High Assurance session with Continuous Authentication]]

## Related

- [[pre-work-ca|Pre-work for Continuous Authentication]]
- [[configure-ca|Configuring Continuous Authentication]]
- [[high-assurance-ca|High Assurance session with Continuous Authentication]]
- [[c_Authentication|Authentication]]
- [[ca-policies|Policies]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[c_requestAPI|request]]
