---
title: Activating Zero Trust Access
description: Activate the Zero Trust - Policy Based Session Access com.snc.zero\_trust\_session\_access plugin to enable security admins to reduce or limit user access in a session based on IP address, location, Identity Provider attributes, and user attributes using adaptive authentication policies.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/activate-session-access.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Zero Trust Access, Access Management]
tags:
  - platform-security
  - type-task
---

# Activating Zero Trust Access

Activate the **Zero Trust - Policy Based Session Access** `com.snc.zero_trust_session_access` plugin to enable security admins to reduce or limit user access in a session based on IP address, location, [[identity-landing|Identity]] Provider attributes, and user attributes using [[adaptive-authentication|adaptive authentication]] [[ca-policies|policies]].

## Before you begin

Role required: admin

Plugin type: Paid and requires license.

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the **Zero Trust - Policy Based Session Access** \(`com.snc.zero_trust_session_access`\) plugin using the [[adaptive-auth-filter-criteria|filter criteria]] and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to [[c_requestAPI|request]] it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Related

- [[identity-landing|Identity]]
- [[adaptive-authentication|Adaptive authentication]]
- [[ca-policies|Policies]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[c_requestAPI|request]]
