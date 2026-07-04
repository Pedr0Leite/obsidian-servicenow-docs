---
title: "SAP Entitlement have 'License type\" field hidden with Model with SAP named user product"
aliases:
  - KB2975302
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2975302
kb_number: KB2975302
last_modified: 2026-04-27
---

## SAP Entitlement have 'License type" field hidden with Model with SAP named user product

  

### Issue

While creating entitlements for SAP S/4HANA Cloud products in ServiceNow SAM Pro, the License type field disappears and start/end dates cannot be added when no Publisher Part Number is provided.

The entitlement is saved as 'Perpetual' instead of 'Subscription', and changing the metric group to 'Common' and license metric to 'Resource Consumption' triggers a blocking error about SAP Engine Measurement applicability. Similar behavior is observed for other products.

### Release

All

### Cause

-   The License type field is hidden by design for SAP products using Named User or Engine Measurement licensing due to a client script ('Manage fields for SAP named user product').   
      
    The field License Type is getting removed from UI when user selects Software model value related to SAP  
    Client Script "Manage fields for SAP named user product" = /nav\_to.do?uri=sys\_script\_client.do?sys\_id=76c225c50bb31300815805c137673ad9

```
// SAP Named User product or SAP Engine product
if ((swModelRef.product === '5e73bc41dbab570024cd68461b9619f5')
|| (sapEngineProduct)) {
g_form.setDisplay('product_type', false);
```

-   SAP Private Cloud integration is not currently supported, causing mismatches when attempting to use Engine Measurement for S/4HANA Cloud versions.

### Resolution

1.  Inactivate the client script 'Manage fields for SAP named user product' to display the License type field.
2.  Submit an enhancement request to evaluate making the License type field available for SAP Private Cloud offerings by following the link provided in the case details.
3.  Check for existing enhancement requests related to this issue and upvote them, or create a new enhancement idea if none exist.  
      
    

### Related Links

Refer doc for creating SAP, it does not show License Type is available field on form  
[https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/create-entitlement-sap.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/create-entitlement-sap.html)
