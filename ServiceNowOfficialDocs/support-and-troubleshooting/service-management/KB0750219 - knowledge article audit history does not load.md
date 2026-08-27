---
title: "knowledge article audit history does not load"
aliases:
  - KB0750219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750219
kb_number: KB0750219
last_modified: 2024-04-07
---

## knowledge article audit history does not load

  

### Issue

# Symptoms

On a knowledge article, the Related List : "Audit History" does not display any data

**Steps to Reproduce:**   
  
1\. Navigate to Knowledge > All   
2\. Open a knowledge article   
3\. Configure > Related Lists > add the 'Audit History'   
4\. Navigate to Related List > Audit History   
This displays no records. It is empty   
5\. Navigate to the context menu of the record > History > List   
The audit records are loaded   
6\. Navigate back to Related List > Audit History   
The audit records now display correctly 

# Cause

The first time the Related List : 'Audit History' is accessed, the Refresh button should be clicked.

# Resolution

Clicking on the 'Refresh' button on the 'Audit History' related list resolved the issue   
  
The first time the Related List : 'Audit History' is accessed, click the Refresh button. 

Please note that the Refresh button is available only to Administrators based on the condition of the UI Action.
