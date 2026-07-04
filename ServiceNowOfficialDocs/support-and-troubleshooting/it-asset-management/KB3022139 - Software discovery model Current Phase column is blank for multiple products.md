---
title: "Software discovery model \"Current Phase\" column is blank for multiple products"
aliases:
  - KB3022139
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3022139
kb_number: KB3022139
last_modified: 2026-05-15
---

## Software discovery model "Current Phase" column is blank for multiple products

  

### Issue

In the Software Discovery Models list (`cmdb_sam_sw_discovery_model`), the Current Phase column is blank for a large number of software products.

### Symptoms

-   In the Software Discovery Models list (`cmdb_sam_sw_discovery_model`), the Current Phase column is blank for a large number of software products.
-   Products affected include both licensable and non-licensable software types.
-   The issue impacts EOS (End of Support) and EOL (End of Life) tracking and reporting.
-   The `SAM - Generate Software Lifecycle Report` The scheduled job has run successfully, but the phase data is still missing for certain products.

### Release

ALL

### Cause

The Current Phase field on the Software Discovery Model is populated by dot-walking from `sam_sw_product_lifecycle_report` (Software Lifecycle Report). That table is populated by the `SAM - Generate Software Lifecycle Report` job, which reads lifecycle dates from the content table `sam_sw_product_lifecycle`. The phase is blank under any of the following three conditions:

**Condition 1 — Missing lifecycle dates in the content table:** 

The vendor has published EOS/EOL dates, but that data has not yet been loaded into `sam_sw_product_lifecycle`. The product will appear in the lifecycle report only once the content is shipped or a content request is fulfilled.

**Condition 2 — Only the GA phase exists:** 

OS-level packages, libraries, and RPM components (e.g., `libacl`, `abrt-gui-libs`) often only have a General Availability date — no EOS/EOL/EOES dates are published by the vendor. The lifecycle report only populates records where a phase start date is older than 18 months and one of EOS/EOL/EOES is defined. These products will never have a Current Phase value.

**Condition 3 — No normalised product reference**: 

Discovery models without a linked normalised product (`norm_product` is empty) cannot be mapped to a lifecycle record. The phase cannot be populated without a product reference.

### Resolution

**For Condition 1** — Verify whether vendor lifecycle dates exist publicly. If they do, submit a content request via the ITAM portal: `Now Platform → ITAM → Content Requests → New`. Attach vendor documentation showing the lifecycle dates. ServiceNow's content team will review and add the data in an upcoming content release.

**For Condition 2** — No action is required. OS-level packages and libraries will not have a Current Phase populated. This is by design, and the behaviour cannot be changed without a platform enhancement.

**For Condition 3** — Review discovery models with no `norm_product` reference. Ensure software normalisation is running correctly and that the normalised product catalogue is up to date. Manually link products where feasible.

After the content is updated or the products are linked, re-run the `SAM - Generate Software Lifecycle Report` scheduled job and verify the Current Phase column is now populated.
