---
title: "Windows Server Installations Display \"Entitlement Consumption Rule or Software Assurance Requirement Not Met\" Despite Valid Entitlements"
aliases:
  - KB2700689
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2700689
kb_number: KB2700689
last_modified: 2026-05-01
---

## Issue

## Symptoms

-   Windows Server software installations appear as unlicensed in Software Asset Management
-   Installations display the unlicensed reason: "Entitlement Consumption Rule or Software Assurance Requirement Not Met"
-   Valid entitlements exist with Software Assurance (SA) and downgrade rights that should cover the installations
-   No custom Consumption Rules have been configured that would restrict entitlement allocation
-   Downgrade rights appear to be correctly configured but installations remain unlicensed

## Resolution

## Resolution

### Step 1: Verify the Current License Metric

1.  Navigate to Software Asset Management > Entitlements > Software Entitlements.
2.  Locate the entitlement record for Microsoft Windows Server.
3.  Review the License Metric field and note the current value.

### Step 2: Identify the Correct License Metric

For Microsoft Windows Server products, the correct license metric is Per Core (with CAL).

Refer to the following guidance:

| Product Type | Correct License Metric |
| --- | --- |
| Microsoft Windows Server | Per Core (with CAL) |
| Microsoft Windows Server Standard | Per Core (with CAL) |
| Microsoft Windows Server Datacenter | Per Core (with CAL) |
| Microsoft System Center | Per Core (with CAL) |
| Core Infrastructure Server Suite | Per Core (with CAL) |
| Microsoft SQL Server | Per Core |
| Microsoft BizTalk Server | Per Core |

### Step 3: Update the License Metric

1.  Open the affected software entitlement record.
2.  Change the License Metric field from Per Core to Per Core (with CAL).
3.  Save the record.
4.  Repeat for any other Windows Server entitlements using the incorrect metric.

### Step 4: Run Reconciliation

1.  Navigate to Software Asset Management > Reconciliation > Reconcile.
2.  Run the reconciliation process for the affected software models.
3.  Alternatively, wait for the next scheduled reconciliation job to execute.

### Step 5: Verify Results

1.  After reconciliation completes, navigate to the previously unlicensed installations.
2.  Verify the installations now show as Licensed.
3.  Confirm the unlicensed reason has been cleared.

* * *

## Additional Context: Downgrade Rights

If you are also working with downgrade rights for Windows Server:

-   Downgrade rights allow you to use entitlements for a newer software version to license earlier versions of the same software
-   The `samp_dmap_downgrade_model_list` table can be used to identify parent-child relationships for Definitive Media Application Profile (DMAP) records
-   Even with correctly configured downgrade rights, installations will remain unlicensed if the license metric is incorrect

* * *

## Key Points Summary

| Issue | Resolution |
| --- | --- |
| Windows Server shows unlicensed | Verify license metric is "Per Core (with CAL)" |
| Entitlement has SA but not reconciling | Check license metric configuration |
| Downgrade rights not applying | Confirm both license metric AND downgrade configuration |

* * *

## Reference Documentation

-   Microsoft Software License Metrics Overview
-   Microsoft Per Core (with CAL) Licensing Model
-   Understanding Downgrade Rights in Software Asset Management
-   Software Entitlement Configuration Guide

* * *

## Related Articles

-   Configuring Software Entitlements for Microsoft Products
-   Understanding Software Asset Management Reconciliation
-   Troubleshooting Unlicensed Software Installations
-   Microsoft License Metric Best Practices

* * *

## Additional Information

-   Always verify license metrics against your Microsoft licensing agreement
-   Consider reviewing all Microsoft server product entitlements to ensure consistent metric configuration
-   Contact your Microsoft licensing representative if unsure which metric applies to your specific agreement
