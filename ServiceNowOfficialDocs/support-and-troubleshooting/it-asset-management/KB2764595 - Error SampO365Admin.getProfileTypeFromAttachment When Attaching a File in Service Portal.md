---
title: "Error \"SampO365Admin.getProfileTypeFromAttachment\" When Attaching a File in Service Portal"
aliases:
  - KB2764595
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2764595
kb_number: KB2764595
last_modified: 2026-05-12
---

## Error "SampO365Admin.getProfileTypeFromAttachment" When Attaching a File in Service Portal

  

  

## Issue

An error is thrown when attempting to attach a file in Service Portal referencing the business rule "Validate M365 attachments" and the Script Include "SampO365Admin".

## Symptoms

-   Attaching a file in Service Portal triggers an error in the system logs.
-   The following error message appears:

`Condition 'Condition: SampO365Admin.getProfileTypeFromAttachment(current.table_sys_id) === 'microsoft_office_365' && gs.nil(SampO365Admin.parseCSVFileDateTime(current.file_name)); Filter Condition: table_name=samp_sw_subscription_profile^file_nameSTARTSWITHVisio^ORfile_nameSTARTSWITHCopilot ^ORfile_nameSTARTSWITHProject^EQ' in business rule 'Validate M365 attachments' on sys_attachment: sc_cat_item (sys_idSTARTSWITHebe9027fc3ffae5487f63fbf05013192).xml evaluated to null; skipping business rule`

-   The business rule "Validate M365 attachments" is skipped due to the condition evaluating to null.

## Facts

-   The business rule **Validate M365 attachments** and the Script Include **SampO365Admin** are part of the **SaaS License Management Microsoft Extension** \[`com.sn_sam_saas_int.samp.microsoft`\] plugin.
-   Upgrading the **SaaS License Management** \[`sn_sam_saas_int`\] plugin also upgrades all associated software publisher integration extension plugins, including the Microsoft Extension.
-   The Script Include **SampO365Admin** is an out-of-the-box component delivered with the plugin.

## Cause

The `getProfileTypeFromAttachment` function is missing from the Script Include **SampO365Admin**. This function is called in the advanced condition of the business rule **Validate M365 attachments**, and because it does not exist, the condition evaluates to null and the business rule is skipped.

This most likely occurred because the Script Include **SampO365Admin** was not updated to its latest version from the `com.sn_sam_saas_int.samp.microsoft` plugin when the **SaaS License Management** plugin was last upgraded.

## Solution

Repair or upgrade the **SaaS License Management** \[`sn_sam_saas_int`\] plugin to restore the missing function in the Script Include.

### Option A: Repair the Plugin

1.  Navigate to **Application Manager** on your instance.
2.  Search for **SaaS License Management** \[`sn_sam_saas_int`\].
3.  Select **Repair** on the currently installed version.
4.  Wait for the repair process to complete. This reinstalls all associated plugins, including the Microsoft Extension, and updates the **SampO365Admin** Script Include to the correct version.

### Option B: Upgrade the Plugin

If your instance is not running the latest version of **SaaS License Management**, upgrade instead of repairing:

1.  Navigate to **Application Manager** on your instance.
2.  Search for **SaaS License Management** \[`sn_sam_saas_int`\].
3.  Select **Update** to install the latest available version.
4.  Wait for the upgrade process to complete. This reinstalls all associated plugins, updates the **SampO365Admin** Script Include, and provides the additional benefit of upgrading to the latest release.

### Verification

After the repair or upgrade completes, verify that the missing function has been restored:

1.  Navigate to **System Definition > Script Includes**.
2.  Search for **SampO365Admin**.
3.  Open the Script Include and confirm that the `getProfileTypeFromAttachment` function is present in the code. The function should appear as follows:

`SampO365Admin.getProfileTypeFromAttachment = function(recordID) {     var gr = new GlideRecord('samp_sw_subscription_profile');     if (gr.get(recordID)) {         return gr.getValue('profile_type');     }     return null; };`

4.  Attach a file in Service Portal and confirm that the error no longer appears in the system logs.

## Additional Resources

-   [ServiceNow Documentation: SaaS License Management](https://docs.servicenow.com/bundle/latest/page/product/software-asset-management2/concept/saas-license-management.html)
-   [ServiceNow Documentation: Repairing Applications](https://docs.servicenow.com/bundle/latest/page/build/applications/task/t_RepairAnApplication.html)
-   [ServiceNow Community](https://www.servicenow.com/community/)
-   [ServiceNow Support](/)
