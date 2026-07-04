---
title: "SAM Pro - Adobe SaaS Subscriptions Showing as Unlicensed Despite Sufficient Entitlement Rights"
aliases:
  - KB2991887
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2991887
kb_number: KB2991887
last_modified: 2026-04-30
---

## SAM Pro - Adobe SaaS Subscriptions Showing as Unlicensed Despite Sufficient Entitlement Rights

  

### Issue

After running reconciliation in SAM Pro with an Adobe SaaS integration configured, Adobe subscription records continue to show as unlicensed despite the entitlement having sufficient rights to cover all active subscriptions.

### Symptoms

-   Unlicensed subscriptions count is greater than 0 in License Usage workspace for an Adobe product
-   License Metric Results shows licenses owned exceeds licenses required with $0 true-up cost
-   Remediation options show Affects Compliance = false
-   Create Allocations remediation action does not resolve the unlicensed count
-   Subscription records have number\_of\_installs = 0
-   Subscription data is sourced from the Adobe SaaS integration
-   Entitlement license metric is set to Per User

### Facts

-   Adobe Creative Cloud SaaS integration is configured and pulling subscription data
-   Software model mapping and entitlement chain are correctly configured
-   Entitlement license type is Subscription

### Release

All Applicable Releases

### Cause

In this case, the entitlement license metric was set to Per User. However the default value for SaaS entitlements is User Subscription. 

Reference:

See License Metric:

[https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/software-entitlement-fields.html](https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/software-entitlement-fields.html)

### Resolution

-   Open the affected Adobe entitlement record (Software Asset Management > Software Entitlements)
-   Change the License metric from Per User to User Subscription
-   Save the record
-   Run Reconciliation
-   Confirm the unlicensed subscriptions count resolves to 0

### Related Links

[https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/c\_SAMLicenseMetrics.html](https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/c_SAMLicenseMetrics.html)

[https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/software-entitlement-fields.html](https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/software-entitlement-fields.html)

[https://www.servicenow.com/community/sam-forum/reconciling-entitlements-with-unlicensed-subscriptions/m-p/2653763/page/2](https://www.servicenow.com/community/sam-forum/reconciling-entitlements-with-unlicensed-subscriptions/m-p/2653763/page/2)
