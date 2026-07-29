---
title: "Purchase Requisition Remains in \"Pending Submission\" State After Purchase Order Is Created"
aliases:
  - KB3129374
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3129374
kb_number: KB3129374
last_modified: 2026-06-30
---

## Text

## Summary

When ordering goods through ShoppingHub, the Purchase Requisition (PR) created by the order remains in the "Pending Submission" state after a Purchase Order (PO) is created, instead of transitioning to the expected "Closed Complete" state.

This is a known issue currently being tracked under PRB2021802.

* * *

## Symptoms

-   A Purchase Requisition created from a ShoppingHub order does not progress to the expected state after a Purchase Order is generated.
-   The PR remains stuck in the "Pending Submission" state.
-   The PR is not moved to "Closed Complete" even after all related cases, tasks, and approvals are completed.

* * *

## Steps to Reproduce

1.  Open ShoppingHub.
2.  Order a product from the supplier catalog.
3.  Open the Source-to-Pay (S2P) Workspace.
4.  Locate the newly created Purchase Requisition.
5.  Approve the Purchase Requisition.
6.  Close all open cases and tasks associated with the requisition.
7.  Create a Purchase Order from the Purchase Requisition.

Expected Result: The Purchase Requisition moves to the "Closed Complete" state.

Actual Result: The Purchase Requisition remains in the "Pending Submission" state.

* * *

## Cause

When the order is created, records are written to the procurement integration (outbound) tables. A business rule responsible for updating the Purchase Order Line status re-triggers and sets the status back to "Pending Submission", preventing the Purchase Requisition from completing.

* * *

## Workaround

A workaround is available while a permanent fix is being developed under PRB2021802.

### Disable the Outbound Purchase Order Workflow

Disable the workflow responsible for creating, updating, or canceling purchase orders on the outbound integration tables:

1.  Navigate to Workflow > Workflow Editor (or the Workflow administration area).
2.  Locate the workflow named "Create or update or cancel purchase order on outbound tables".
3.  Disable (deactivate) the workflow.
4.  Test the process again by creating a Purchase Order from a Purchase Requisition.
5.  Confirm the Purchase Requisition now transitions to the expected "Closed Complete" state.

> Important: This workaround disables outbound purchase order integration processing. If your organization relies on this integration to send purchase order data to an external system, evaluate the impact before applying. Test the workaround in a sub-production environment first.

* * *

## Related Articles

-   ShoppingHub Ordering Overview
-   Source-to-Pay (S2P) Workspace Guide
-   Managing Purchase Requisitions and Purchase Orders
-   Procurement Integration Configuration

* * *

## Additional Information

-   Always validate workarounds in a non-production environment before applying to production.
-   If you have applied the workaround and rely on outbound purchase order integration, plan to re-enable the workflow once the permanent fix from PRB2021802 is available.
-   For assistance applying the workaround or to report additional impact, contact ServiceNow Support and reference PRB2021802.
