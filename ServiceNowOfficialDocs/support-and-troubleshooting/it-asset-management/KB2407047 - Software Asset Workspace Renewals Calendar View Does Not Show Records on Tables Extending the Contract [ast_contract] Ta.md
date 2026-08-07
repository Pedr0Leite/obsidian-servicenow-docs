---
title: "Software Asset Workspace | Renewals Calendar View Does Not Show Records on Tables Extending the Contract [ast_contract] Table"
aliases:
  - KB2407047
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2407047
kb_number: KB2407047
last_modified: 2026-05-12
---

## Software Asset Workspace | Renewals Calendar View Does Not Show Records on Tables Extending the Contract \[ast\_contract\] Table

  

### Issue

The Renewals Calendar view in Software Asset Workspace is not showing expiring contracts as expected.

### Symptoms

The contracts are NOT directly on the Contract \[ast\_contract\] table, they're on a custom table that extends the Contract \[ast\_contract\] table.

The contract meets the below conditions from ServiceNow's Documentation, however it still doesn't show in the Renewals Calendar view.

  
  
[ServiceNow Product Documentation - Renewals Calendar view](https://www.servicenow.com/docs/csh?topicname=renewal-calendar-view.html&version=latest)  

The Renewals Calendar view shows upcoming and expired renewals with the following conditions:

-   The contract must be active.
-   Contracts expiring in 90 days or fewer.
-   The end date of the contract must not be empty.
-   The state of the contract is active or expired.
-   The substate of the contract is either Awaiting review or Renewal rejected.
-   Contracts with contract model types such as Subscription, Software License, and Maintenance.
-   Entitlements with only license types of Perpetual or Subscription.
-   Entitlements without any associated contract.

### Facts

-   Records on tables extending Contract \[ast\_contract\] are not supported on Renewals Calendar.
-   Only records directly on the Contract \[ast\_contract\] table are supported on Renewals Calendar.

### Release

All releases

### Cause

The contracts not showing in the Renewals Calendar view are on tables extending the Contract \[ast\_contract\] table.

Records on tables extending Contract \[ast\_contract\] are not supported on Renewals Calendar.

### Resolution

Contract Records on tables extending Contract \[ast\_contract\] not showing in the Renewals Calendar view in Software Asset Workspace is expected behavior.
