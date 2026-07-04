---
title: "SAM Workspace: Renewals Calendar Displays No Data"
aliases:
  - KB3051605
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3051605
kb_number: KB3051605
last_modified: 2026-05-29
---

## SAM Workspace: Renewals Calendar Displays No Data

  

### Issue

The Renewals Calendar in the Software Asset Workspace displays no data, even when contracts and entitlements exist that should meet the visibility criteria.

### Symptoms

Navigating to the Software Asset Workspace (`/now/softwareasset/home`) and selecting Renewals Calendar (`/now/softwareasset/renewal-calendar`) shows an empty calendar ("No items to display") with no contract or entitlement records displayed.

### Facts

-   Feature: SAM Workspace Renewals Calendar
-   Script Include involved: `RenewalsCalendarUtils` (`sys_script_include.do?sys_id=b32f39ac43e1111084202a421cb8f257`)
-   Table involved: `cmdb_contract_product_model`
-   The script include hardcodes the sys\_ids of the three accepted contract product models: Subscription (`84941ac0ef60300035c61ab995c0fbc4`), Software License (`d781e836c3102000b959fd251eba8f89`), and Maintenance (`a581e836c3102000b959fd251eba8fba`).

### Release

All

### Cause

The `RenewalsCalendarUtils` script include hardcodes the sys\_ids of the three out-of-box contract product model records (Subscription, Software License, and Maintenance) in the `acceptedContractModels` array. If any of these `cmdb_contract_product_model` records have been customized, resulting in a sys\_id that differs from the out-of-box values, the query filtering on `contract.contract_model IN [acceptedContractModels]` will return no matches, and the calendar will display no data.

### Resolution

-   Navigate to Contract Product Models (`cmdb_contract_product_model.list`) and identify any records for Subscription, Software License, or Maintenance that have been modified or cloned (sys\_ids differing from the out-of-box values noted above).
-   Revert the customized contract product model records to their out-of-box state and ensure their sys\_ids match the values hardcoded in `RenewalsCalendarUtils`.
-   Once the out-of-box product model records are restored, create or update a contract that references one of these out-of-box contract product models and confirm it meets all of the following conditions required for display on the Renewal Calendar:
    -   Contract state is Active or Expired
    -   Contract substate is either Awaiting review or Renewal rejected (with process set to Renewal), or substate is empty and state is Active/Expired
    -   Contract model type is Subscription, Software License, or Maintenance
    -   Contract is active (`contract.active = true`)
    -   Contract end date is not empty
    -   Contract end date falls within the configured expiration window (default: 90 days or fewer from today)
-   For standalone Entitlements (without an associated contract) to appear on the calendar, confirm:
    -   License type is Full/Perpetual (using `maintenance_expiration_date`) or Subscription (using `end_date`)
    -   The entitlement is not linked to any contract via `clm_m2m_contract_asset`
    -   The expiration date falls within the configured window and is not in the past
-   Reload the Renewals Calendar and confirm records now appear.

### Related Links

Renewals calendar view:

[https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/renewal-calendar-view.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/renewal-calendar-view.html)
