---
title: "\"Preview Document\" UI Action loading a blank popup"
aliases:
  - KB0998325
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998325
kb_number: KB0998325
last_modified: 2025-09-03
---

## Issue

"Preview Document" UI Action loading a blank popup

## Resolution

This issue was happening because of customization done to the **"hr"** Script Include.  
Once reverted, everything worked as expected.  
  
To do so, follow the steps below.

###   
Next Steps:

1.  Navigate to System Definition > Script Includes
2.  In the **"Name"** column search for **"hr"** and go to the record
3.  In the Versions-related list, Right-Click the most recent record with the Source of **"Store Application: Human Resources: Core"**
4.  Select **"Revert to this version"**
5.  Select OK when prompted
