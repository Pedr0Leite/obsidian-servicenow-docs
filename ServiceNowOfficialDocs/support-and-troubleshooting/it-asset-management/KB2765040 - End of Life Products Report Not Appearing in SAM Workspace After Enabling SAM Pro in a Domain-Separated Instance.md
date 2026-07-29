---
title: "End of Life Products Report Not Appearing in SAM Workspace After Enabling SAM Pro in a Domain-Separated Instance"
aliases:
  - KB2765040
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2765040
kb_number: KB2765040
last_modified: 2026-05-20
---

## End of Life Products Report Not Appearing in SAM Workspace After Enabling SAM Pro in a Domain-Separated Instance

  

### Issue

  
The End of Life Products report data is not appearing in the SAM Workspace after enabling SAM Pro in a domain-separated instance.  
  

### Symptoms

The scheduled job SAM – Generate Software Lifecycle Report is responsible for creating records in the Software Lifecycle Reports table. Please verify whether the table `sam_sw_product_lifecycle_report` is empty.

### Release

Any Release

### Cause

The Run asset process flag was not enabled for the domain that contains the normalized discovery models. As a result, the scheduled job did not process data for that domain, which led to empty records in the Software Lifecycle Reports table.  
  

### Resolution

1.  Verify the Run asset process setting in the Domain Asset Process Settings table for the relevant domain that contains the normalized discovery models. ( [https://<instance-name>.service-now.com/alm\_domain\_asset\_process\_setting\_list.do](https://\<instance-name\>.service-now.com/alm_domain_asset_process_setting_list.do))
2.  After enabling the setting for the correct domain, rerun the scheduled job SAM – Generate Software Lifecycle Report.
3.  Finally, confirm that the Software Lifecycle Reports table is populated as expected after the job completes.

### Related Links

# Domain separation and Software Asset Management

[https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/domain-separation-software-asset-management.html](https://www.servicenow.com/docs/r/yokohama/it-asset-management/software-asset-management/domain-separation-software-asset-management.html)
