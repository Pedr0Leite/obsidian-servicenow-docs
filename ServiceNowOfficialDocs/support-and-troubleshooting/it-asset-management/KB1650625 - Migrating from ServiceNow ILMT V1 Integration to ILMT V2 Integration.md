---
title: "Migrating from ServiceNow ILMT V1 Integration to ILMT V2 Integration"
aliases:
  - KB1650625
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1650625
kb_number: KB1650625
last_modified: 2025-09-09
---

## Text

## Issue

IBM has announced the end-of-life (EOL) for the [IBM License Metric Tool (ILMT) REST API v1](https://www.ibm.com/support/pages/ibm-license-metric-tool-deprecated-rest-api-default-disabled-and-going-be-removed-completely-end-2024), with removal and end-of-support scheduled by the end of 2024.

Once IBM sunsets ILMT REST API v1:

-   The ServiceNow SAM ILMT v1 integration will stop functioning.
-   Organizations relying on ILMT v1 will face disruptions in their software asset management process.

This transition is critical to maintain:

-   Accurate IBM software deployment tracking
-   Ongoing license compliance
-   Seamless integration with ServiceNow SAM

Failure to migrate to ILMT REST API v2 will result in incomplete or failed IBM software asset management.

### Resolution

To address the end-of-life for ILMT REST API v1 and ensure continuity in software asset management processes, use the following steps to transition to ILMT REST API v2:

1) **Review the [ServiceNow ILMT integration documentation](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/integrating-ilmt-bigfix-v2-apis.html)**

-   Refer to the [ServiceNow documentation](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/integrating-ilmt-bigfix-v2-apis.html) to understand prerequisites and configuration requirements for ILMT v2 integration.

2) **Update the ILMT Integration Property**

-   Set the Connect to ILMT using property (`sn_samp_ibm_lic.ilmt_api_version`) to v2 API.
-   Refer to the [ServiceNow documentation](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/integrating-ilmt-bigfix-v2-apis.html) for detailed instructions.

3) **Known Issue – Validate Connection UI Action**

-   **Issue**: The **Validate Connection** UI action does not work when using ILMT v2 in **Washington DC and earlier releases**.
-   **Resolution**: An update set is available under **PRB1732950** to address this issue. If you encounter the problem, raise a support case for further assistance.

By following above steps, you can ensure a smooth transition from the ILMT v1 to ILMT v2 integration in ServiceNow, maintaining the efficiency and accuracy of your software asset management processes.

## Additional Considerations – Reasons for data limitations in ILMT v2 integration v/s ILMT v1 integration

When migrating from ILMT v1 integration to ILMT v2 integration, be aware of the following data limitations you may observe in ILMT V2 integration and reasons for such limitations:

-   **Incomplete Classification** – ILMT v2 does not provide sufficient detail to properly classify computers in CMDB. Consequently, computers are created as generic records rather than being identified by specific types (e.g., Linux server, Windows server).
-   **Configuration Issues** – If ILMT is not configured correctly, TLM\_VM errors occur when importing computer data. These affected computers are skipped, which can lead to gaps when they have associated installs or usage records.
-   **Missing Relationships** – ILMT v2 lacks the necessary information to accurately map relationships between virtual and physical machines, preventing complete dependency modeling.
-   **Stale Data** – After a computer is initially created, attributes such as CPU count and core information are not refreshed, leading to outdated hardware details in CMDB.

## Summary

By proactively migrating from ILMT REST API v1 to v2 and understanding the reasons for its data limitations, organizations can ensure:

-   Continued ServiceNow SAM–ILMT integration support
-   Compliance with IBM licensing requirements
-   Stable and accurate IBM software asset management processes
