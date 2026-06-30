---
title: Activate Customer Success Management
description: The Customer Success Management \(com.sn\_acct\_lc\) plugin is available as a separate subscription. Activating this plugin also activates the related plugins required to use the application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/acct-lifecycle-events/account-lifecycle-activate.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Getting started, Configure, Customer Success Management]
---

# Activate Customer Success Management

The [[account-lifecycle-events-landing|Customer Success Management]] \(com.sn\_acct\_lc\) plugin is available as a separate subscription. Activating this plugin also activates the related plugins required to use the application.

## Before you begin

Role required: sn\_customerservice.customer\_admin

## About this task

If the related plugins aren’t already active, the [[account-lifecycle-events-customer-success-about|Customer Success]] Management plugin activates them. For more information, see [[account-lifecycle-required-plugins|Plugins activated with Customer Success Management]].

## Procedure

1.  Navigate to **All** &gt; **Application Manager**.

2.  Find the plugin using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you can’t find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install**, and then in the Activate Plugin dialog box, select **Activate**.

    **Note:** When domain separation and delegated admin are enabled in an instance, you must be in the **global** domain. Otherwise, the following error message appears:

    ```
    Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>
    ```

    .


## What to do next

After activating the application, complete the following steps:

-   To enable [[account-lifecycle-playbook-overview|account onboarding]], configure the [[account-lifecycle-onboard-playbook|onboarding playbook]]. See [[account-lifecycle-configure|Configure the account onboarding playbook]].
-   To enable [[account-lifecycle-use-cust-success|customer success]], create the choice and definition records. See [[account-lifecycle-basic-config|Getting started with Customer Success]].

**Parent Topic:**[[account-lifecycle-get-started|Getting started with Customer Success Management]]

## Related

- [[account-lifecycle-required-plugins|Plugins activated with Customer Success Management]]
- [[account-lifecycle-configure|Configure the account onboarding playbook]]
- [[account-lifecycle-basic-config|Getting started with Customer Success]]
- [[account-lifecycle-get-started|Getting started with Customer Success Management]]
- [[account-lifecycle-events-landing|Customer Success Management]]
- [[account-lifecycle-onboard-playbook|Onboarding playbook]]
- [[account-lifecycle-playbook-overview|Account onboarding]]
- [[account-lifecycle-events-customer-success-about|Customer success]]
- [[account-lifecycle-use-cust-success|Customer success]]
