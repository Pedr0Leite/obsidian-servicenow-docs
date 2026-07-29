---
title: "Widget errors on Employee Center after upgrade – isContentPreview not found"
aliases:
  - KB0999110
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999110
kb_number: KB0999110
last_modified: 2026-06-09
---

## Widget errors on Employee Center after upgrade – isContentPreview not found

  

### Issue

After upgrading to Rome or later, multiple failing widget errors appear when navigating to the Employee Service Center. The errors reference widgets such as Employee Center Header, Video Carousel (CD), Upcoming Events (CD), and Content Experience, and include messages such as "Cannot find function isContentPreview". The errors typically result from customized Script Includes that were skipped during upgrade, missing plugin records, or restricted caller access (RCA) records that are not set to Allowed.

### Release

All releases

### Cause

When navigating to the Employee Service Center, multiple failing widget errors appear. The errors are similar to the following:

  
Server JavaScript error Cannot find function isContentPreview in object function () {...}.  
Error Line number 96 (sp\_widget.d0009941eb103010ed7966d6475228c1.script)  
Error Script source code logged to browser console  
Error Failing widget: 'Employee Center Header' (d0009941eb103010ed7966d6475228c1)  
Error Line number 16 (sp\_widget.1b6504a30b0303008cd6e7ae37673ae3.script)  
Error Failing widget: 'Video Carousel (CD)' (1b6504a30b0303008cd6e7ae37673ae3)  
Error Line number 19 (sp\_widget.62974aeb0b5303008cd6e7ae37673a42.script)  
Error Failing widget: 'Upcoming Events (CD)' (62974aeb0b5303008cd6e7ae37673a42)  
Error Line number 11 (sp\_widget.26b2b8cfff02201014c6a36cf43bf1a0.script)  
Error Failing widget: 'Content Experience' (26b2b8cfff02201014c6a36cf43bf1a0)  
  

Three root causes can produce these errors:

**Customizations:** Script Include records referenced in the failing widgets had been customized before the upgrade. Customized records are skipped during upgrade, so the widgets reference outdated code. For example, the baseline **Employee Center Header** widget (sys\_id: \`d0009941eb103010ed7966d6475228c1\`) references several Script Includes stored in the \`sys\_script\_include\` table. If any of those Script Includes were modified from baseline, they will not be updated during upgrade.

**Missing plugin records:** Instances that previously had older Employee Center plugins may be missing files expected by Employee Center Pro. If the errors reference null or undefined values, expected files may not be present on the instance.

**Restricted caller access:** Script Includes in scoped applications may be blocked by restricted caller access (RCA) records in the \`sys\_restricted\_caller\_access\` table that are not set to **Allowed**.

### Resolution

Identify which root cause applies by checking the scripts named in the error messages, then follow the corresponding steps below.

**Fix customizations**

1\. Review the scripts named in the error messages and compare them to their baseline versions to confirm they have been modified.   
2\. Revert the customized Script Includes and widgets to baseline.  
3\. Re-apply any required customizations to the reverted baseline versions.

**Fix missing plugin records**

1\. Confirm that the errors reference null or undefined values, which indicates missing files.  
2\. Repair the Employee Center plugins to restore expected files to the instance. 

**Fix RCA errors**

1\. Navigate to the \`sys\_restricted\_caller\_access\` table.   
2\. Review all records in the table.  
3\. Set the **Status** field to **Allowed** for any records that are not already set to **Allowed**.

### Related Links

[Approve application restricted caller access privileges](https://www.servicenow.com/docs/r/employee-service-management/employee-experience-foundation/ur-mst-approve-rca.html "Approve application restricted caller access privileges")

[RCA Errors in HR scoped application after upgrading](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759087 "RCA Errors in HR scoped application after upgrading")
