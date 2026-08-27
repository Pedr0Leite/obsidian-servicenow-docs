---
title: "Why do multiple Publisher Part Numbers with different license metrics map to the same Software Model in SAM Pro?"
aliases:
  - KB3014528
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3014528
kb_number: KB3014528
last_modified: 2026-05-29
---

## Why do multiple Publisher Part Numbers with different license metrics map to the same Software Model in SAM Pro?

  

### Issue

Why do multiple Publisher Part Numbers with different license metrics map to the same Software Model in SAM Pro?

### Symptoms

In Software Asset Management Professional, also known as SAM Pro, it is expected behavior for multiple Publisher Part Numbers, also called PPNs, with different license metrics to map to the same Software Model.

This is because the Software Model represents the installed software product, while the license metric represents how the software was purchased or licensed through an entitlement.

For example, Microsoft SQL Server Enterprise may have different PPNs for Per Core, Per Server, or Server + CAL licensing. These PPNs may still map to the same Software Model because the discovered installed product is the same.

### Release

NA

### Cause

NA

### Resolution

In SAM Pro, Software Models and Entitlements serve different purposes.

The Software Model represents the discovered or normalized installed software product. It identifies what software is installed in the environment.

The Software Entitlement represents the licensing rights that were purchased. It stores commercial and licensing details such as:

-   Publisher Part Number
-   License metric
-   Purchased rights
-   Cost

Because of this design, the license metric is not treated as a property of the Software Model. Instead, it is stored and managed at the entitlement level.

## Example

A user may have the following PPNs:  
  

| Publisher Part Number | License Metric | Software Model |
| --- | --- | --- |
| 7JQ-00663 | Per Core | Microsoft SQL Server Enterprise |
| 810-04760 | Per Server | Microsoft SQL Server Enterprise |

  
  

Both PPNs can point to the same Software Model because the installed software is still Microsoft SQL Server Enterprise.

The difference is not in the software installation itself. The difference is in how the customer purchased the rights to use that software.

## Why this is expected behavior ?

Discovery identifies installed software based on installation evidence, signatures, normalization, and product recognition logic.

Discovery does not determine which purchase, contract, entitlement, PPN, or license metric should be associated with a specific installation.

Therefore:

-   The Software Model acts as the proof of installation.
-   The Software Entitlement acts as the proof of purchase.
-   The license metric is derived from the entitlement, not from the Software Model.

This allows a single discovered software installation to be covered by different licensing models, depending on the customer’s entitlement strategy.

For example, a SQL Server Enterprise installation may be covered by either:

-   a Per Core entitlement, or
-   a Server + CAL entitlement,

depending on how the customer purchased and allocated the license.

## Recommended approach

To report cost by PPN or license metric, create a custom report using entitlement and allocation data rather than relying only on the Software Model.

If additional chargeback-specific attributes are required, customers may also consider creating a custom table or extending their reporting model to maintain business-specific chargeback details.

## Frequently asked questions

### Why does the same Software Model appear for different PPNs?

Because the Software Model represents the installed product, not the purchase model. Different PPNs can represent different ways of licensing the same installed software.

### Why is the license metric not stored directly on the Software Model?

The license metric is related to the entitlement or purchase agreement. The same software product may be licensed using different metrics depending on the customer’s contract.

### Can Discovery identify whether an install should be Per Core or Per Server?

No. Discovery identifies what software is installed. It does not know which entitlement or purchase should cover that installation.

### Where should chargeback be calculated from?

Chargeback should be calculated from entitlement and allocation data, as these records contain the PPN, license metric, and cost details.

### Is this a product defect?

No. This behavior is expected and is working by design.

## Conclusion

Multiple PPNs with different license metrics can map to the same Software Model because SAM Pro separates the installed software identity from the licensing and purchase context.

\-The Software Model identifies what is installed.  
\-The Entitlement identifies how it was purchased and licensed.

### Related Links
