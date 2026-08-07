---
title: "Hardware assets incorrectly display the Eligible for Refresh label on the portal"
aliases:
  - KB3036353
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3036353
kb_number: KB3036353
last_modified: 2026-07-01
---

## Hardware assets incorrectly display the Eligible for Refresh label on the portal

  

### Issue

Hardware assets displayed in the My Assets widget on the portal show the Eligible for Refresh label for assets that do not yet qualify for refresh under the organisation's refresh policy.

![](/sys_attachment.do?sys_id=534c14af97cdc3940ed83bbe2153af78)

### Facts

-   Navigate to the ServiceNow portal (for example, `https://<instance>.service-now.com/support`).
-   As an administrator, impersonate an end user who has hardware assets assigned.
-   Scroll to the My Assets widget.
-   Observe the Eligible for Refresh label appearing on an asset that should not yet qualify.

### Release

All supported releases.

### Resolution

Refresh eligibility is not determined solely by the `eligible_for_refresh` field on the `alm_hardware` record. The eligibility is evaluated dynamically by the SAM - Calculate Asset Refresh Eligibility scheduled job, which considers the following two factors:

Factor 1 — Hardware Model Useful Life (in months). The Hardware Model record associated with the asset includes a Useful Life field, configured in months. This value defines the expected lifespan of that asset model.

Factor 2 — Asset Install Date: The scheduled job compares the asset's install date against the current date. If the number of months elapsed since the install date equals or exceeds the configured Useful Life value, the asset is flagged as Eligible for Refresh.

To resolve this issue, update the Useful Life field on the affected Hardware Model record to reflect the correct refresh period in months.

Steps

1.  Navigate to Hardware Asset Management > Product Catalog > Hardware Models, or go directly to `cmdb_hardware_product_model_list.do`.
2.  Search for the Hardware Model associated with the affected asset using the Model Number or Model Name.
3.  Open the Hardware Model record.
4.  Locate the Useful Life (Months) field.
5.  Update the value to match your organisation's refresh policy (for example, change 60 months to 84 months for a 7-year lifecycle).
6.  Select Save.

> Note: If the Useful Life field is already set correctly and assets are still flagged, verify that the asset's Install Date field is populated accurately. The eligibility calculation uses the Install Date, not the record creation date.
