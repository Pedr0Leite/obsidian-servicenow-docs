---
title: "Why my software installs are not getting normalized?"
aliases:
  - KB3004328
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3004328
kb_number: KB3004328
last_modified: 2026-05-18
---

## Why my software installs are not getting normalized?

  

### Issue

In Software Asset Management, users may observe that a Software Discovery Model is normalized, but the related Software Install records do not show normalized publisher, product, or normalized display name values.

### Symptoms

You may observe one or more of the following:

-   The Software Discovery Model shows Normalization status = Normalized.
-   The Software Discovery Model has a normalized Publisher, Product, and Version.
-   The related Software Install records still show the discovered/raw publisher or product values.
-   Two discovery models may both be normalized, but their related install records appear different.
-   Software Install records are not populated with:
    -   `norm_product`
    -   `norm_publisher`
    -   `normalized_display_name`

### Release

NA

### Cause

The out-of-the-box Business Rule “Update install with product information” runs on the Software Discovery Model table.

This Business Rule updates related records in the Software Install table only when specific conditions are met.

The key logic is:

```
if (current.getValue('norm_type') === 'licensable' && !current.getElement('norm_product.ignore_installs')) {
    var display = SAMPremiumUtils.calculateNormDisplayName(current);
    installGr.setValue('norm_product', current.getValue('norm_product'));
    installGr.setValue('norm_publisher', current.getValue('norm_publisher'));
    installGr.setValue('normalized_display_name', display);
}
```

This means the install records are updated with normalized product information only when:

-   The Software Discovery Model has `norm_type = licensable`
-   The normalized product is not marked to ignore installs
-   The related install records are linked to the same discovery model

If the Software Discovery Model is Not Licensable, this normalization update block is skipped.

### Resolution

## When does the Business Rule run?

The Business Rule runs after update on the Software Discovery Model table.

It is triggered when one of the following conditions is true:

```
current.norm_product.changes() 
|| current.norm_type.changes() 
|| (!current.norm_product.nil() && 
   (current.norm_version.changes() || current.norm_edition.changes()))
```

In simple terms, the Business Rule runs when:

-   The normalized product changes
-   The normalization type changes
-   The normalized version changes, when normalized product is populated
-   The normalized edition changes, when normalized product is populated

The Business Rule does not run simply because install records exist. It runs when the relevant fields on the Software Discovery Model are updated.  
  

## Required conditions for Software Install normalization

For related Software Install records to be updated with normalized product data, the following conditions must be satisfied:

| Condition | Requirement |
| --- | --- |
| Discovery Model update | The Software Discovery Model must be updated |
| Trigger condition | `norm_product`, `norm_type`, `norm_version`, or `norm_edition` must change as per the Business Rule condition |
| Normalization Type | `norm_type` must be `licensable` |
| Normalized Product | `norm_product` must be populated |
| Ignore installs | `norm_product.ignore_installs` must not be true |
| Related installs | Software Install records must reference the same discovery model |
| Business Rule active | The Business Rule must be active |

## Important distinction

There are two different concepts:

### 1\. Discovery Model normalization

This means the Software Discovery Model has been matched to normalized content such as publisher, product, version, edition, or product type.

### 2\. Software Install normalization

This means the related Software Install records have been updated with normalized fields such as:

-   `norm_product`
-   `norm_publisher`
-   `normalized_display_name`

A Discovery Model can be normalized while the related Software Install records are not updated with normalized SAM fields if the product is not licensable.

## Additional behavior for SN File Discovery :

The Business Rule also contains separate logic for discovery models where:

```
current.getValue('discovery_source') === 'SN File Discovery'
```

In that scenario, it updates install fields such as:

```
installGr.setValue('publisher', current.getDisplayValue('norm_publisher'));
installGr.setValue('display_name', current.getDisplayValue('norm_product'));
installGr.setValue('version', current.getDisplayValue('norm_version'));
```

This is separate from the licensable-product normalization block.

Therefore, behavior can vary depending on the discovery source and whether the install fields being reviewed are regular install fields or normalized SAM fields.

## Why non-licensable installs may not retain normalized fields?

Out-of-the-box SAM utility logic also includes cleanup behavior for non-licensable installs. The utility method `clearNormFieldsForNonLicensableInstalls()` covers non-licensable and inactive installs and clears normalized/reconciliation fields from applicable software install records.

This supports the expected behavior that non-licensable software installs are not treated the same way as licensable installs for SAM normalization and reconciliation.

## How to validate?

To confirm why a Software Install is not getting normalized, validate the following:

1.  Open the related Software Discovery Model.
2.  Confirm the Normalization status.
3.  Check the backend value of Product Type / Normalization Type.
4.  Confirm whether the value is Licensable or Not Licensable.
5.  Confirm that Product is populated.
6.  Confirm that the normalized product is not configured to Ignore installs.
7.  Open the related Software Install records.
8.  Confirm whether the install is linked to the same discovery model.
9.  Review whether you are checking raw install fields or normalized fields.

## Expected behavior:

If the Software Discovery Model is Licensable, the related install records should be updated with normalized product information when the Business Rule conditions are met.

If the Software Discovery Model is Not Licensable, the Discovery Model may still show as normalized, but the related install records may continue to show discovered/raw values. This is expected out-of-the-box behavior.
