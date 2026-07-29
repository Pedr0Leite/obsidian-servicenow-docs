---
title: "Adobe User Subscription Licensing"
aliases:
  - KB2769635
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2769635
kb_number: KB2769635
last_modified: 2026-02-09
---

## Adobe User Subscription Licensing

  

## License Metric Overview

The Adobe User Subscription metric allocates one license per user with an active software subscription. When reconciliation runs and a Software Model links to entitlements using this metric, the system consumes one license right for each distinct, active Software Subscription record tied to a user. Software installations associated with that model are also covered under the subscription.

Rights Consumption in Different Scenarios:

Scenario 1: User Allocation with No Subscription Record

-   Rights consumed = 1 per allocated user
-   User allocations serve as the authoritative consumption source
-   The allocation counts against purchased rights in the entitlement
-   However, the allocation displays as "Allocated NOT in use" because no subscription record validates the allocation

Scenario 2: Subscription Record with No User Allocation

-   Rights consumed = 1 per subscription record
-   Subscription data from SaaS portal integration automatically drives consumption
-   Displays as "Not allocated in use," meaning consumption occurs automatically without manual allocation

Scenario 3: Both Allocation and Subscription Exist

-   Rights consumed = 1 (not double-counted)
-   SAM deduplicates by recognizing the same user across both sources
-   Shows as "Allocated in use"—allocation and subscription are matched and validated

Scenario 4: Installation Without Subscription

-   Rights consumed = 0
-   Installations without corresponding subscription records remain unlicensed under User Subscription metrics
-   No license consumption occurs, but non-compliance is flagged

## Software Subscriptions (`samp_sw_subscription`)

Adobe cloud offerings—including Creative Cloud, Illustrator CC, InDesign CC, and similar products—operate on user-based subscription models. The SAM – Import User Subscription scheduled job retrieves subscription data from Adobe and populates the Software Subscription table. This import requires prior configuration of the Adobe Cloud Integration Profile.

Once subscription data arrives from the Adobe portal, the system matches each record to a User (`sys_user`) via the User Principal Name. Successful matches populate the user reference on the subscription record, along with a reference to the appropriate Software Model. Both references are essential for reconciliation—without them, related software installations cannot be properly licensed.

Software Subscription records function as the core data source for User Subscription metrics and contain suite- and reconciliation-related fields similar to those on Software Installation records:

-   `inferred_suite`
-   `inferred_suite_level`
-   `inferred_suite_product`
-   `is_reconciled`
-   `unlicensed_subscription`
-   `product_result`
-   `software_model_result`
-   `license_metric_result`

## Software Installations (`cmdb_sam_sw_install`)

This table filters to display only Adobe Systems products. Adobe cloud applications can be installed locally on devices—such as Photoshop or Illustrator—enabling offline work. These installations receive licensing through User Subscription entitlements only when the device's assigned user possesses a matching Software Subscription record. Without a corresponding subscription, installations remain unlicensed under this metric.

## Reconciliation and License Usage

Reconciliation processes both Adobe Software Subscription and Software Installation records. The resulting compliance position and usage statistics appear in the License Usage module within the SAM Workspace.
