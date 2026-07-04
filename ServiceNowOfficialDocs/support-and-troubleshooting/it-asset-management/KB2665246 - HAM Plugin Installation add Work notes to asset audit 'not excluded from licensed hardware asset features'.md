---
title: "HAM Plugin Installation add Work notes to asset audit 'not excluded from licensed hardware asset features'"
aliases:
  - KB2665246
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2665246
kb_number: KB2665246
last_modified: 2026-05-21
---

## HAM Plugin Installation add Work notes to asset audit 'not excluded from licensed hardware asset features'

  

### Issue

During installation of the Hardware Asset Management (HAM) Plugin work notes as 'excluded from licensed hardware asset features' are being automatically added to asset records. This triggers the 'Asset and CI Synch' Business rules, causing asset data to be copied to CI records. The issue occurs when assets are updated, particularly during job runs such as 'HAM - Optin/Optout\_End User Computers'.![](/sys_attachment.do?sys_id=18c7a02693edf6947c79b36d6cba1093)

### Release

HAM Plugin installed on Yokohama

### Cause

The work notes are added due to the 'Handle exclude from ham change' business rule, which is triggered when asset records are updated to reflect changes in HAM licensing status. 

The business rule calls the HAMLicensingUtility script include to generate work notes indicating whether assets are excluded from licensed hardware asset features. 

This process is part of the HAM plugin installation workflow, specifically during job runs like 'HAM - Optin/Optout\_End User Computers', which modify asset records and inadvertently trigger the business rule.

### Resolution

This is happening when Asset gets updated  and it triggers business rule = Handle exclude from ham change. This calls method = getAssetWorkNotesMessage from SI = HAMLicensingUtility  
  
\====  
1\. Why are work notes being added to the asset records records during the plugin installation?  
This happens when Asset is mapped to check for Hardware feature.  
This update happened for job run "HAM - Optin/Optout\_End User Computers"  
  
2\. How can we prevent the "Asset and CI Sync" business rule from being triggered during the plugin installation process?  
This will happen on asset update OR any thing is change on HAM product which could cause business rule to trigger
