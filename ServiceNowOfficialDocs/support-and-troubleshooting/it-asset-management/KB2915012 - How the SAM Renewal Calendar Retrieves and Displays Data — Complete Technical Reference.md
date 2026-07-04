---
title: "How the SAM Renewal Calendar Retrieves and Displays Data — Complete Technical Reference"
aliases:
  - KB2915012
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2915012
kb_number: KB2915012
last_modified: 2026-03-25
---

## How the SAM Renewal Calendar Retrieves and Displays Data — Complete Technical Reference

  

### Summary

**1\. Overview**

The SAM Renewal Calendar in the Software Asset Workspace provides a visual timeline of upcoming and (optionally) past-due software renewals. It does not query contracts or entitlements the way a standard list view does. Instead, it relies on the server-side script include `RenewalsCalendarUtils`, which executes two independent data retrieval paths and merges the results into a single calendar view.

Understanding these two paths — and every condition within them — is essential for troubleshooting why records may or may not appear on the calendar.

The two paths are:

Path A — Contract-based renewals: Retrieves contracts via the Assets Covered M2M table (`clm_m2m_contract_asset`), not from the Contracts table (`ast_contract`) directly.

Path B — Standalone entitlement renewals: Retrieves software entitlements (`alm_license`) that are approaching expiration and are not already covered by a contract.

Both paths feed into a shared response array that the calendar renders. A record must fully satisfy every condition in its respective path to appear. Failing even one condition results in silent exclusion — no error is shown, the record simply does not appear.

* * *

**2\. The Renewal Type Selector**

The SAM Renewal Calendar UI provides a "Renewal type" dropdown with options such as "All contracts and all entitlements," contracts only, or entitlements only. This selection controls which of the two paths execute. If the selection includes contracts, Path A runs. If the selection includes entitlements, Path B runs. If "All contracts and all entitlements" is selected, both paths run and results are merged.

If a user has selected a renewal type that excludes one path, records from that path will never appear regardless of how correctly they are configured. This is the first thing to verify during troubleshooting.

* * *

**3\. Path A — Contract-Based Renewals (Detailed Conditions)**

This is the most commonly misunderstood path. The query targets the Assets Covered related list (`clm_m2m_contract_asset`), not the Contracts table itself. Every condition below must be true simultaneously for a contract to appear on the SAM Renewal Calendar.

3.1 — Assets Covered records must exist

The SAM Renewal Calendar queries the Assets Covered M2M table. If a contract has zero records in its "Assets Covered" related list, the query returns nothing for that contract. The contract is completely invisible to the calendar.

This is the single most common reason contracts do not appear. A contract can be perfectly configured — correct state, correct model, valid dates — and still not show up if the Assets Covered related list is empty.

3.2 — The linked asset must be a software entitlement

The query explicitly filters on the asset's class being `alm_license`. This means the linked asset must be a software entitlement record specifically. Hardware assets, consumables, or other CI types linked under Assets Covered are ignored by the SAM Renewal Calendar.

3.3 — Contract state and substate conditions

The SAM Renewal Calendar applies a compound query on the contract's state and substate. The contract qualifies if either of these two condition groups is met.

Group 1 requires that the State is Active or Expired, AND the Substate is empty (no value set).

Group 2 requires that the Substate is Renewal Rejected or Awaiting Review, AND the Process field is set to Renewal.

There are important nuances here. A contract in Active state but with a non-empty Substate (e.g., "In Renewal") will fail Group 1. It would then need to satisfy Group 2 to qualify. A contract in Draft, Cancelled, or any state other than Active or Expired will fail Group 1. Group 2 does not explicitly check state, so theoretically a contract in any state could qualify via Group 2 if the substate and process values match

3.4 — Contract must be Active

In addition to the state/substate check above, there is a separate explicit filter requiring the contract's boolean Active flag to be true. This is distinct from the State field having a value of "Active."

A contract can have State = Active but the boolean Active flag = false (e.g., if it was manually deactivated). Such a contract would fail this condition. Conversely, in some configurations, an Expired-state contract could still have the boolean Active flag = true. Both the state/substate condition and the boolean active flag must pass for the contract to qualify.

3.5 — Contract Model must be one of three accepted types

The SAM Renewal Calendar only accepts contracts whose Contract Model matches one of three hardcoded sys\_ids corresponding to Subscription, Software License, and Maintenance.

Any other contract model — including Service Contract, Leasing Contract, Warranty, or custom contract models — is excluded.

Critical consideration for non-production or cloned instances: These sys\_ids are OOB values. If the instance was built from scratch, or if contract model records were deleted and recreated, or if they were imported from another instance, the sys\_ids may differ. In that case, even a contract correctly showing "Software License" in the UI would fail this filter because the underlying sys\_id does not match. This can be verified by navigating directly to the contract model record and checking its sys\_id against the OOB values.

3.6 — End Date must be populated

The query includes a not-null check on the contract's End Date field (`ends`). If the End Date is empty, the contract is excluded. This is logical — a contract with no end date has no renewal date to plot on the calendar.

3.7 — End Date must fall within the selected date window

The "Days past / until renewal" selector on the SAM Renewal Calendar UI (60, 90, 120, or 150 days) defines a date window. The behavior depends on whether the calendar is configured to show upcoming-only or both past and upcoming.

In the combined past and upcoming mode, the End Date must fall between (today minus X days) and (today plus X days), where X is the selected day count. This means a contract that expired up to X days ago and a contract expiring within the next X days will both appear.

In the upcoming-only mode, the End Date must fall between today and (today plus X days). Past-due contracts are excluded entirely.

For example, with "60 days" selected in combined mode and today being March 25, 2026, the window spans from January 24, 2026 through May 24, 2026. A contract ending April 30, 2026 would qualify. A contract ending July 15, 2026 would not. If the user selects "60 days" but the contract ends in 90 days, it will not appear — switching to "90 days" or higher would bring it into scope.

3.8 — Domain filtering

If domain separation is active and a domain ID is provided, the query filters Assets Covered records to those belonging to the specified domain or the Global domain. Records in other domains are excluded from the SAM Renewal Calendar.

* * *

**4\. How Contracts Are Grouped and Displayed on the Calendar**

The query on the Assets Covered table is ordered by contract. As the script iterates through the results, it groups all Assets Covered records belonging to the same contract together. For each contract group, it collects the publisher names (manufacturer) from each linked entitlement's software model, deduplicates them, and sorts them alphabetically. It then creates a single calendar entry per contract, with the publisher names concatenated as the display name (for example, "Adobe, Microsoft, Oracle").

The End Date displayed is the contract's end date. The Renewal Start Date is calculated as End Date minus the selected day window — so if a contract ends April 30 and the window is 60 days, the renewal start date is March 1. The bar on the calendar spans from the renewal start date to the end date.

The cost displayed is the contract's `total_cost` field, and the cost center comes from the contract record. When a user clicks a contract entry on the calendar, it opens the `ast_contract` record.

* * *

**5\. Path B — Standalone Entitlement Renewals (Detailed Conditions)**

Path B retrieves software entitlements (`alm_license`) that are nearing expiration on their own — independent of any contract. This path runs in two sub-queries based on product type.

5.1 — Sub-query 1: Perpetual-type entitlements

This sub-query targets entitlements where the Product Type is Full, Perpetual Maintenance, or Perpetual Software Assurance. For these product types, the relevant date field is Maintenance Expiration Date (`maintenance_expiration_date`). The entitlement must have a Maintenance Expiration Date that falls between today and (today plus X days), where X is the selected day window.

Unlike the contract path, this sub-query only looks forward — it does not include past-due entitlements. The Maintenance Expiration Date must be greater than or equal to today AND less than or equal to the future cutoff date.

5.2 — Sub-query 2: Subscription-type entitlements

This sub-query targets entitlements where the Product Type is Subscription. For subscriptions, the relevant date field is End Date (`end_date`), not Maintenance Expiration Date. The same forward-looking date window applies.

5.3 — The contract-association exclusion

This is a critical filter that applies to both sub-queries. After each entitlement passes the date and product type filters, the script checks whether that entitlement has any record in the Assets Covered table — meaning, is it linked to any contract.

If the entitlement is linked to a contract, it is skipped and excluded from Path B results. The reasoning is that if an entitlement is covered by a contract, it should appear via Path A rather than appearing again independently. This prevents duplication on the SAM Renewal Calendar.

5.4 — Domain filtering

Same behavior as Path A — if domain separation is active, entitlements are filtered to the specified domain or Global.

5.5 — How standalone entitlements are displayed

Each qualifying entitlement appears as its own individual entry on the SAM Renewal Calendar. The display name is the entitlement's `display_name` field value. The End Date is the Maintenance Expiration Date for perpetual types or the End Date for subscription types. The cost displayed is the entitlement's `cost` field. When a user clicks an entitlement entry on the calendar, it opens the `alm_license` record.

* * *

**6\. Category Filters**

The SAM Renewal Calendar UI provides a "Filter by" option with a category selector. The available categories are Publisher, Product, Cost Center, and Contract Model.

The Publisher filter restricts results to entitlements whose software model's manufacturer matches the selected values. This applies to both Path A (via the linked entitlement's software model) and Path B (directly on the entitlement's software model).

The Product filter restricts results to entitlements whose software model's product matches the selected values. This also applies to both paths.

The Cost Center filter restricts results based on the cost center field — on the contract in Path A, and on the entitlement in Path B.

The Contract Model filter restricts results to contracts with a matching contract model. This filter only applies to Path A. If the Contract Model filter is selected, Path B returns zero results by design, since standalone entitlements do not have a contract model field. This means selecting a Contract Model filter while the Renewal Type is set to "All contracts and all entitlements" will effectively suppress all entitlement results.

An important behavior to note: if the user selects a category (e.g., Publisher) but then clears all specific values within that category, the script resets the filter entirely rather than applying an impossible "IN empty list" filter. Clearing filter values shows all records, not zero records.

* * *

**7\. The 1000-Record Global Cap**

The script enforces a maximum of 1000 total records across both paths combined. A shared counter tracks how many records have been added to the response.

Once the counter reaches 1000, in Path A the script stops processing further contracts and adjusts the qualified records list to maintain count consistency. In Path B, the script simply stops processing further entitlements.

This is a global cap, not a per-path cap. The order of execution matters — Path A (contracts) runs first, followed by Path B (entitlements). This means contracts take priority over standalone entitlements when the cap is reached. If Path A alone returns 1000 contracts, Path B will return zero even if qualifying entitlements exist.

If a user expects to see a specific record but it does not appear, and all other conditions are met, the 1000-record cap should be considered as a possible explanation — particularly in large environments with many active contracts.

* * *

**8\. Renewal Start Date Calculation**

For every record that qualifies on the SAM Renewal Calendar (whether contract or entitlement), the script calculates a Renewal Start Date which determines the left edge of the bar on the timeline. The calculation is: Renewal Start Date equals the End Date minus the selected day window.

For example, if a contract ends on June 30, 2026 and the selected window is 90 days, the Renewal Start Date is April 1, 2026. The bar spans from April 1 to June 30 on the calendar.

This means changing the day window not only affects which records appear (by expanding or contracting the eligibility range) but also how far back each bar extends on the timeline.

* * *

**9\. Key Behavioral Differences Between the Two Paths**

There are several important behavioral differences between Path A and Path B that affect troubleshooting.

The source table differs — Path A queries the Assets Covered M2M table while Path B queries the entitlement table directly.

Past-due records are handled differently. Path A can show contracts that have already expired (within the selected day window looking backward), while Path B is strictly forward-looking and never shows past-due entitlements.

The date fields used differ by path and by product type. Path A always uses the contract's End Date field. Path B uses Maintenance Expiration Date for perpetual-type entitlements and End Date for subscription entitlements. If the wrong date field is populated on an entitlement, the record will not match.

Display name logic differs. Path A groups all entitlements under a single contract and shows a comma-separated list of publisher names. Path B shows each entitlement individually with its own display name.

The cost field source differs — Path A uses the contract's total cost while Path B uses the entitlement's cost field.

The Contract Model category filter only works for Path A and actively suppresses Path B results when selected.

* * *

**10\. Comprehensive Troubleshooting — Why Records May Not Appear on the SAM Renewal Calendar**

\- Missing Assets Covered records (Path A): The Assets Covered related list on the contract is empty. Since the SAM Renewal Calendar queries the M2M table and not the contract table, no M2M records means no calendar entry. This is the most common root cause.

\- Assets Covered exist but linked asset is not a software entitlement (Path A): The linked asset must be of class `alm_license`. If hardware assets, consumables, or other types are linked, they are ignored.

\- Contract State is not Active or Expired (Path A): Contracts in Draft, Cancelled, or other states fail the primary condition group. Only Active or Expired states qualify under Group 1.

\- Contract State is Active but Substate is not empty (Path A): Group 1 requires Substate to be empty. A contract with Substate "In Renewal" fails Group 1 and would need to match Group 2 (Substate = Renewal Rejected or Awaiting Review with Process = Renewal) to qualify.

\- Contract Model is not one of the three accepted types (Path A): Only Subscription, Software License, and Maintenance contract models are accepted. Service Contract, Leasing Contract, Warranty, and custom models are excluded.

\- Contract Model sys\_id mismatch on non-production instances (Path A): The filter uses hardcoded OOB sys\_ids. If contract model records have different sys\_ids on this instance (due to recreation, import, or clone issues), even correctly named models won't match.

\- Contract's boolean Active flag is false (Path A): This is separate from the State field. A contract can show State = Active in the UI but have the boolean Active flag set to false. Both must pass.

\- Contract End Date is empty (Path A): A not-null check excludes contracts with no end date from the calendar.

\- Contract End Date falls outside the selected day window (Path A): A contract ending in 90 days won't appear if "60 days" is selected. The user needs to select a wider window.

\- Entitlement Product Type is not one of the expected values (Path B): Only Full, Perpetual Maintenance, Perpetual Software Assurance, and Subscription product types are queried. Other product types are invisible to Path B.

\- Wrong date field populated on entitlement (Path B): Perpetual-type entitlements use Maintenance Expiration Date while Subscription entitlements use End Date. If the expected date field is empty but the other one is populated, the record won't match.

\- Entitlement is linked to a contract via Assets Covered (Path B): The contract-association exclusion removes it from Path B. If the parent contract also fails Path A conditions, the entitlement is invisible on both paths — this is the double-miss scenario.

\- The 1000-record global cap has been reached (Both paths): Once 1000 records are collected across both paths, all further records are silently dropped. Contracts take priority since Path A runs first.

\- Domain separation filtering (Both paths): If a domain ID is active, only records in that domain or Global domain are included.

\- Category filter mismatch (Both paths): An active Publisher, Product, Cost Center, or Contract Model filter excludes non-matching records.

\- Contract Model filter suppressing entitlements (Path B): Selecting the Contract Model category filter causes Path B to return zero results by design, since entitlements don't have contract model fields.

\- Renewal type dropdown excludes the record's path (Both paths): If only contracts are selected in the Renewal Type dropdown, Path B doesn't run, and vice versa. Records from the excluded path will never appear.

\- Entitlement expiration date is in the past (Path B): Path B is strictly forward-looking. Unlike Path A, which can display past-due contracts within the backward window, Path B never shows entitlements whose expiration date has already passed.

### Related Links

[Renewals calendar view](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/renewal-calendar-view.html "Renewals calendar view")
