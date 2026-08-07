---
title: "SAM Pro: PVU License Reconciliation Fails for Non-IBM Publishers (HCL Products)"
aliases:
  - KB2951012
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2951012
kb_number: KB2951012
last_modified: 2026-05-07
---

## SAM Pro: PVU License Reconciliation Fails for Non-IBM Publishers (HCL Products)

  

### Issue

For any formerly IBM Products such as HCL Digital Experience Manager which uses the Processor Value Unit (PVU) license metric, which is recognized in the ServiceNow Content Library. However, SAM Pro's PVU reconciliation engine is designed exclusively for IBM products and relies on the samp\_ilmt\_sw\_install table, which is restricted to IBM publishers. As a result, PVU-based licenses assigned to HCL as the publisher are not processed during reconciliation, leaving the software out of compliance tracking.

### Symptoms

-   Reconciliation runs complete without errors but skip HCL-published products.
-   No usage records are generated for HCL Digital Experience Manager despite valid license assignments with the PVU metric.

### Facts

-   HCL acquired several IBM products (including IBM WebSphere Portal and IBM Digital Experience) as part of a portfolio deal. These products retained PVU as their licensing metric.
-   SAM Pro's PVU reconciliation engine only processes IBM publisher records, so even manually importing PVU data into ILMT tables does not enable correct reconciliation for HCL/non-IBM products due to publisher restrictions in SAM Pro.
-   ILMT V2 uses the ilmt\_v2\_product\_usage table, and its license calculators (PVU, RVU, VPC) do not hard-code IBM as publisher making it the recommended integration path if ILMT is managing the non-IBM products.

### Release

Not release specific

### Cause

The SAM Pro PVU reconciliation engine was built exclusively for IBM products and uses the SAM publisher pack's integration with IBM's ILMT APIs. The reconciliation logic filters records by IBM publisher, so any product even one with a valid PVU license metric will be excluded from compliance calculations if its publisher is set to HCL or any non-IBM value. This is a platform-level constraint in the reconciliation engine.

### Resolution

Step 1: Confirm ILMT tool visibility

Verify whether HCL Digital Experience Manager is visible in your ILMT tool (either ILMT or BigFix Inventory). Obtain an audit snapshot or REST API output confirming whether PVU consumption is being reported for this product.

Step 2: Use ILMT V2 integration

If ILMT is managing the HCL product, ensure the ILMT V2 integration is active and that records are populating the `ilmt_v2_product_usage` table. The ILMT V2 calculators are not restricted by publisher and should process PVU consumption for HCL products correctly.

Step 3: Check system property

Verify that the property `com.snc.samp.ibm.use_samp_ibm_licensing` is not set to true unless you are enrolled in IBM's IASP program. Enabling this property incorrectly stops the ILMT V2 integration from pulling data.

Step 4: Use Resource Value metric as a fallback

If ILMT is not managing the HCL product and PVU consumption data must be entered manually, use the Resource Value license metric instead. Manual imports into ILMT tables do not trigger PVU reconciliation for non-IBM publishers.
