---
title: Activate Field Encryption
description: Activate either Field Encryption Starter or Field Encryption Enterprise.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/activate-platform-encryption.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-task
---

# Activate Field Encryption

Activate either [[field-encryption|Field Encryption]] Starter or [[now-platform-encryption|Field Encryption Enterprise]].

## Before you begin

Role required: admin

ServiceNow has replaced [[column-level-encryption-landing|Column Level Encryption]] with Field Encryption beginning in the Yokohama release.

In the Yokohama release, customers that have not previously used Column Level Encryption may start using either Field Encryption Starter or Field Encryption Enterprise under the new entitlement structure.

Customers that were [[using-column-level-encryption-2|using Column Level Encryption]] in previous releases, and who want to begin [[using-column-level-encryption|using Field Encryption]], have the following options:

-   **Field Encryption Starter**

    Column Level Encryption Starter customers can install Field Encryption Starter with no need for re-implementation. Field Encryption Starter takes over the existing [[sc-configuration|configuration]] and adds new features seamlessly.

    **Warning:** There are differences in entitlement between Column Level Encryption Starter and Field Encryption Starter. Before installing Field Encryption Starter, ensure that your configuration complies with the entitlements. For information on entitlements for Field Encryption Starter, see [[exploring-fe|Exploring Field Encryption]].

-   **Field Encryption Enterprise**

    [[now-platform-encryption-2|Column Level Encryption Enterprise]] customers should work with their account teams to ensure they have the correct entitlement for Field Encryption Enterprise. Once that happens, the Field Encryption Enterprise plugin will be available to install in their instances.

    **Important:** Column Level Encryption Enterprise does not automatically grant an entitlement to Field Encryption Enterprise, as it is a different, but replacement, product.


## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Plugins**

2.  Under **Search your licensed applications and plugins**, search for `Field Encryption`.

    The search should reveal the plugin. If you purchase a subscription for Field Encryption Enterprise, you can also see this plugin available.

    **Important:** To activate Field Encryption Enterprise, you must first purchase a subscription. Your account manager can arrange to have the plugin activated on your organization's production and non-production instances, generally within a few days.

3.  Select or Field Encryption Enterprise, then select **Install**.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`


**Parent Topic:**[[configuring-column-level-encryption|Configuring Field Encryption]]

## Related

- [[exploring-fe|Exploring Field Encryption]]
- [[configuring-column-level-encryption|Configuring Field Encryption]]
- [[field-encryption|Field Encryption]]
- [[now-platform-encryption|Field Encryption Enterprise]]
- [[column-level-encryption-landing|Column Level Encryption]]
- [[using-column-level-encryption-2|Using Column Level Encryption]]
- [[using-column-level-encryption|Using Field Encryption]]
- [[sc-configuration|Configuration]]
- [[now-platform-encryption-2|Column Level Encryption Enterprise]]
