---
title: "How to hide the list collector (slushbucket) default filter from being usable in the 'Edit' button on related lists?"
aliases:
  - KB0635862
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635862
kb_number: KB0635862
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

Users with access to a table list view are by default able to modify the default filter using the "**Edit**" UI Action on the related list. For example, navigating to a Release record in your instance ( **/nav\_to.do?uri=rm\_release.do?sys\_id=5f18e2fe6fa6ba00141ada0cbb3ee428%26sysparm\_view=release** ), from the **Enhancements** related list at the bottom, and clicking **Edit**.

No List Control options will affect the filter displayed in the slushbucket. This is controlled by the Jelly variable **jvar\_no\_filter** which has to be added to the **URL** for the **sys\_m2m\_template** page. The only way to do that will be to override the 'Edit' UI Action for the specific table, and modify the action script.

Ref.   
[Next Topic Override a UI action for an extended table](https://docs.servicenow.com/csh?topicname=t_OverrideOrRmvAUIActionForExtTbl.html&version=latest "Next Topic  Override a UI action for an extended table")

# Procedure

* * *

In order to override the UI Action and hide the filter, follow the steps below:

**1 -** Open the '**Edit**' UI Action   
**/nav\_to.do?uri=sys\_ui\_action.do?sys\_id=7fff4c3d0a0a0b3400ad3f1a1d613f74**  
  
**2 -** In the script section, add the line below just **after line 6**:

**uri.set('jvar\_no\_filter', 'true');** 

**3 -** **Save** the UI Action. This should make the filter no longer visible. 

# Applicable Versions

* * *

All ServiceNow supported releases
