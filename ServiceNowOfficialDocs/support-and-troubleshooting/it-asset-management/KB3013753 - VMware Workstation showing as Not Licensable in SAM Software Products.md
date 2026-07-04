---
title: "VMware Workstation showing as \"Not Licensable\" in SAM Software Products"
aliases:
  - KB3013753
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3013753
kb_number: KB3013753
last_modified: 2026-05-14
---

## VMware Workstation showing as "Not Licensable" in SAM Software Products

  

### Issue

VMware Workstation is classified as "Not Licensable" in the SAM Software Products table (samp\_sw\_product). Customers who have purchased VMware Workstation licenses report that the product is excluded from license tracking and reconciliation in SAM, and expect the product type to be "Licensable."  
  

### Symptoms

-   VMware Workstation shows Product Type as "Not Licensable" in samp\_sw\_product
-   Software Discovery Models linked to the Workstation product inherit the "Not Licensable" classification from samp\_sw\_product
-   VMware Workstation is not available for entitlement mapping or license reconciliation in SAM

### Release

Applicable to all ServiceNow instances that have received the June 2025 SAM content library or later. That was is a content library change, not a platform release.

### Cause

Broadcom changed the VMware Workstation Pro licensing model on November 2024, making the product free for all user types with no license key required from version 17.5.2 onwards. The SAM content library was updated accordingly in June 2025. 

The "Not Licensable" classification is the correct reflection of the current Broadcom licensing terms.

However customers still have Licensed installs, which this change breaks.

### Resolution

The "Not Licensable" classification for VMware Workstation in the SAM content library is correct and aligns with the current Broadcom licensing model.

If entitlements were purchased prior to the November 2024 licensing change, they can still be tracked within SAM as Licensed using this workaround:

1.  Create a custom software model (samp\_sw\_model) with the product type set to "Licensable."
2.  Link the relevant Software Discovery Models to the custom model instead of the content library model.

Note: Discovery models mapped to a custom software model will no longer receive automatic updates from the SAM content library for that product. Customers should be made aware of this before proceeding.
