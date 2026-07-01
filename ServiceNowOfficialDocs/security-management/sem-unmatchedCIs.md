---
title: Managing unmatched configuration items \(CIs\)
description: When assets are imported, they are automatically matched against existing CIs in your Configuration Management Database \(CMDB\). Assets that do not find a match are listed as 'Unmatched CIs' under Discovered Items.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sem-unmatchedCIs.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Associating finding with a configuration item using lookup rules, Automating prioritization and triaging, Security Exposure Management workflow, Explore, Unified Security Exposure Management, Security Operations]
tags:
  - security-management
  - type-concept
---

# Managing unmatched configuration items \(CIs\)

When assets are imported, they are automatically matched against existing CIs in your Configuration Management Database \(CMDB\). Assets that do not find a match are listed as 'Unmatched CIs' under [[cj-discovered-items|Discovered Items]].

## Locating unmatched CIs

You can view these unmatched configuration items in the **[[security-operations-landing-page|Security Operations]]** &gt; **CMDB** &gt; **Discovered Items** module. By default, this list is filtered to show only "unmatched" items. To see all discovered items from an import, simply remove this filter.

## Taking action on Unmatched CIs

-   **Review Lookup rules:** If you believe an unmatched CI should belong to an existing class within the CMDB, it's recommended to review your lookup rules. This can help ensure proper matching in the future. See [[sem-configure-lookup-rules|Create lookup rule]] for more information.
-   **Consider reclassification:** If a CI doesn't fit an existing class, you may need to reclassify it to ensure accurate CMDB data. See [reclassifying the configuration item](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/view-discovered-items.md) for more information.

**Note:** If the Identification and Reconciliation Engine \(IRE\) is active, the reclassify option for discovered items is not supported.

**Parent Topic:**[[sem-associate-finding-configuration-item-using-lookup-rules|Associating finding with a configuration item using lookup rules]]

**Related topics**  


[View and reclassify unmatched configuration items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/view-discovered-items.md)

[Reconcile unmatched discovered items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/reapply-reconcile-unmatched-discovered-items.md)

[Steps to help prevent duplicate or orphaned records after running Vulnerability Response CI lookup rules](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/ci-identifier-rules-impl-test.md)

[De-duplicating existing configuration items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/reapply-deduplication.md)

## Related

- [[sem-configure-lookup-rules|Configuring lookup rules]]
- [[sem-associate-finding-configuration-item-using-lookup-rules|Associating finding with a configuration item using lookup rules]]
- [[cj-discovered-items|Discovered Items]]
- [[security-operations-landing-page|Security Operations]]
