---
title: "Now Assist case summarization not displaying in Agent Workspace"
aliases:
  - KB2700610
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2700610
kb_number: KB2700610
last_modified: 2026-05-19
---

## Now Assist case summarization not displaying in Agent Workspace

  

### Issue

After enabling the Now Assist case summarisation feature, it functions correctly and is visible when using the native view interface; however, it is currently not appearing or displaying as expected within the Agent Workspace environment.  
  

### Release

Xanadu & Above

### Cause

Case summarization is not appearing in the agent workspace because the macroponent responsible for this functionality has been customized. As a result, it has not received the most recent out-of-the-box (OOB) version during system upgrades, since customized records are intentionally skipped to prevent overwriting user changes.  
  
To investigate this further, you can access the specific macroponent record directly using the following URL: https://<<Instance Name>>.service-now.com/now/nav/ui/classic/params/target/sys\_ux\_macroponent.do%3Fsys\_id%3D1d033475eb3011106eb96bf3a252287f  
  
Additionally, to gain a comprehensive understanding of all the customizations applied to this record, you can review the related update history and changes stored in the sys\_update\_xml table. This will help identify what modifications have been made and assist in troubleshooting why the latest OOB updates have not been applied.

### Resolution

To resolve the issue, we have carefully followed the steps outlined below to ensure data integrity and proper restoration:  
1\. First, need to take  a complete backup of the affected record to preserve its current state before making any changes. This step is crucial to prevent any data loss and to allow rollback if needed.  
2\. Next, need to revert the record to the latest Out-Of-the-Box (OOB) version, also known as the store version, which is the default system version provided by the platform. This helps in restoring the record to a stable and supported state.  
Here is the link to the specific record version for your reference:  
https://<<Instance name>>.service-now.com/now/nav/ui/classic/params/target/sys\_ux\_macroponent.do%3Fsys\_id%3D1d033475eb3011106eb96bf3a252287f  
3\. After reverting, we verified that the summarization now displays correctly as expected, confirming that the issue has been resolved.  
  
Note: If you require any customizations that were previously applied, you can test adding them back carefully on top of the most recent OOB version to ensure compatibility and stability.
