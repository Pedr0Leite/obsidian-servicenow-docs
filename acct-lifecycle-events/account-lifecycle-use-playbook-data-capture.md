---
title: Data capture and validation
description: This phase is meant to gather the necessary information about the account such as support contacts, locations, sold products, entitlements.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/acct-lifecycle-events/account-lifecycle-use-playbook-data-capture.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Account onboarding playbook, Manage account onboarding cases, Account onboarding, Use, Customer Success Management]
---

# Data capture and validation

This phase is meant to gather the necessary information about the account such as support contacts, locations, sold products, entitlements.

<table id="table_ghf_3n4_1yb"><thead><tr><th>

Stage

</th><th>

Activity

</th></tr></thead><tbody><tr><td>

**Data Capture &amp; Validation**

</td><td>

Select the **Data capture** activity to import relevant data into the system and validate it before moving to the next stage.

 The following default tables are available with the base system:

-   Customer contacts
-   Location
-   Service entitlement
-   Install base item
-   Account address relationship
-   Contract
-   Sold products
-   Install base M2M sold products

 Custom conditions have been defined and field values in these tables like source table, target table, and data source are auto-populated in each of these tables. You can use these flows by directly importing data into these tables and publish them when they’re ready. For details on importing data into these tables, see [[account-lifecycle-import-data|Import data into the account onboarding playbook]].

 These tables have been configured with specific conditions and field values have been auto-populated. You can modify these tables, add new tables, and activities depending on your requirements using the Process Automation Designer. See [[account-lifecycle-data-valid-assist|Configure data validation]] for details.

</td></tr></tbody>
</table>Review the data in the Summary activity and select **Mark Complete** to move to the next stage.

-   **[Import data into the account onboarding playbook](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/acct-lifecycle-events/account-lifecycle-import-data.md)**  
As part of the [[account-lifecycle-events-landing|Customer Success Management]] process, you can import, configure, and publish data.

**Parent Topic:**[[account-lifecycle-account-onboard-playbook|Account onboarding playbook]]

## Related

- [[account-lifecycle-import-data|Import data into the account onboarding playbook]]
- [[account-lifecycle-data-valid-assist|Configure data validation]]
- [[account-lifecycle-account-onboard-playbook|Account onboarding playbook]]
- [[account-lifecycle-events-landing|Customer Success Management]]
