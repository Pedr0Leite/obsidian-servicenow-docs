---
title: "SAMP | How To Troubleshoot Unlicensed Software Installation Records"
aliases:
  - KB2758314
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2758314
kb_number: KB2758314
last_modified: 2026-05-12
---

## SAMP | How To Troubleshoot Unlicensed Software Installation Records

  

**Issue**

Software installation records appear as unlicensed in ServiceNow Software Asset Management (SAM), even when valid licenses may exist in the system.

## **Symptoms**

-   Software installation records display with an unlicensed status
-   Installation records are not automatically associated with available license entitlements
-   License compliance reports show discrepancies between installations and licenses
-   Software models appear in unlicensed installation reports despite having purchased licenses

## Facts

-   ServiceNow SAM uses normalization and reconciliation processes to match software installations with licenses
-   The system relies on publisher and product name matching between discovery data and license records
-   Software model normalization maps discovered software to standardized product definitions
-   License entitlements must be properly configured with the correct software model relationships
-   Installation records require accurate publisher and product information for proper license matching

## Cause

Unlicensed software installation records typically occur due to:

-   Normalization failures: Discovery data does not match existing software models in the product catalog
-   Missing software model associations: License entitlements are not linked to the correct software models
-   Inaccurate discovery data: Publisher or product names from discovery contain variations or inconsistencies
-   Incomplete license records: License entitlements lack proper software model relationships
-   Manual installation records: Manually created installations missing required normalization fields

## Solution

### Verify Software Model Normalization

1.  Navigate to Software Asset Management > Software Models
2.  Search for the software product in question
3.  Verify the software model exists and contains accurate publisher and product name information
4.  Check the Normalized Publisher and Normalized Product fields

### Review Installation Records

1.  Open Software Asset Management > Installations > All Installations
2.  Filter for unlicensed installations of the specific software
3.  Review the Publisher and Product fields on the installation record
4.  Compare these values with the corresponding software model

### Check License Entitlements

1.  Navigate to Software Asset Management > Entitlements > Software Entitlements
2.  Locate the license entitlement for the software product
3.  Verify the Software Model field is populated with the correct model
4.  Confirm the entitlement has available rights (not fully consumed)

### Run Reconciliation

1.  Go to Software Asset Management > Reconciliation > Reconcile Licenses
2.  Select the specific software model or run a full reconciliation
3.  Execute the reconciliation job
4.  Monitor the job progress in System Logs > Scheduled Jobs

### Update Normalization Rules

If installations consistently fail to normalize:

1.  Navigate to Software Asset Management > Normalization > Normalization Rules
2.  Create or modify normalization rules to handle product name variations
3.  Add publisher and product name patterns that match your discovery data
4.  Test the rule against sample installation records

### Manually Associate Installations (Temporary Workaround)

For immediate resolution while fixing root causes:

1.  Open the unlicensed installation record
2.  Locate the Licensed by related list
3.  Click Edit and select the appropriate license entitlement
4.  Save the record

### Verify Discovery Source Configuration

1.  Review your discovery sources (Discovery > Discovery Schedules)
2.  Ensure discovery is capturing complete software information
3.  Verify software identification patterns are up to date
4.  Run a targeted discovery on affected devices if needed

### Monitor Reconciliation Results

1.  Access Software Asset Management > Compliance > License Compliance
2.  Review compliance status after reconciliation
3.  Check for remaining unlicensed installations
4.  Investigate any persistent issues using the above steps

* * *

**Additional Resources:**

-   [ServiceNow Software Asset Management Documentation](https://www.servicenow.com/docs/r/zurich/it-asset-management/now-assist-for-software-asset-management-sam/c_SoftwareAssetMgmt.html)
-   [Software Normalization Overview](https://docs.servicenow.com/bundle/xanadu-it-asset-management/page/product/software-asset-management2/concept/software-normalization.html)
-   [License Reconciliation Guide](https://docs.servicenow.com/bundle/xanadu-it-asset-management/page/product/software-asset-management2/task/reconcile-software-licenses.html)
-   [ServiceNow Community - Software Asset Management](https://www.servicenow.com/community/software-asset-management-articles/tkb-p/software-asset-management-articles)
-   [Contact ServiceNow Support](/)
