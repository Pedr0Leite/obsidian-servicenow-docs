---
title: "Publisher missing from the Run Reconciliation publisher list in Software Asset Management"
aliases:
  - KB3079387
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3079387
kb_number: KB3079387
last_modified: 2026-06-22
---

## Issue

Troubleshoot why a software publisher does not appear in the publisher selection list when you run reconciliation in Software Asset Management (SAM Pro). For example, Microsoft does not appear in the Run Reconciliation publisher list even though you have an active Microsoft 365 subscription entitlement.

## Resolution

To identify why the publisher is excluded, validate the entitlement and its related records in the following order. These steps require the SAM administrator role.

1\. Confirm the software model publisher.  
   - Open the entitlement in the Software Entitlements \[alm\_license\] table and open its related software model.  
   - Verify that the Manufacturer field is the normalized publisher company, not a duplicate such as Microsoft Corp or MSFT.  
2\. Confirm the product type.  
   - On the software model, open the related product.  
   - Verify that the product type is Licensable. If it is not, correct the product type, then run reconciliation again.  
3\. Check the entitlement metric.  
   - On the entitlement, review the Metric and metric group.  
   - If the entitlement uses a custom metric, either change it to a standard metric or set the system property com.snc.samp.recon.enablecustommetrics to true in the System Property \[sys\_properties\] table.  
4\. Validate SaaS consumption, if Microsoft 365 is managed as SaaS.  
   - Confirm that the SaaS License Management plugin (sn\_sam\_saas) is active.  
   - Confirm that the SaaS Consumption Summary \[sam\_saas\_consumption\_summary\] table contains rows for the Microsoft software model. These rows depend on a successful run of the SAM - Import M365 User Subscriptions scheduled job and a successful Validate Connection result on the Microsoft 365 integration profile.  
5\. Run reconciliation for all publishers once, then reopen the Run Reconciliation dialog and confirm whether the publisher now appears.

If the publisher is still missing after all of the preceding checks pass, gather the following details for further investigation:

\- The affected entitlement record.  
\- The related software model and product records, including the product type value.  
\- The entitlement metric and metric group.  
\- Confirmation of whether SaaS License Management is active and whether SaaS consumption rows exist.

## Additional Information

\- Run software reconciliation in Software Asset Management: [https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/t\_RunReconciliation.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/t_RunReconciliation.html)  
\- Run software reconciliation in the workspace: [https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/run-recon-workspace.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/run-recon-workspace.html)  
\- Review software reconciliation results: [https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/software-reconciliation-results.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/software-reconciliation-results.html)  
\- Understand software discovery and normalization: [https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/c\_SAMDiscovery.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/c_SAMDiscovery.html)
