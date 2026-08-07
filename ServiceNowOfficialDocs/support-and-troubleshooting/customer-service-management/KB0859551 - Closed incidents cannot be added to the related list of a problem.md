---
title: "Closed incidents cannot be added to the related list of a problem"
aliases:
  - KB0859551
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859551
kb_number: KB0859551
last_modified: 2026-06-26
---

## Closed incidents cannot be added to the related list of a problem

  

### Issue

You cannot add closed incidents to the related list of a problem record. The filter on the incident related list does not allow you to change the 'Active is true' condition.

### Symptoms

-   The incident related list on a problem record only displays active incidents.
-   The filter condition 'Active is true' cannot be removed or modified from the related list view.
-   Closed incidents do not appear as options when using the Add function on the related list.

### Release

All

### Cause

The base system UI action that controls this behavior references a script include (BulkAddIncidents) that includes a fixed query with active=true^. This condition filters out closed incidents and cannot be changed from the related list interface.

### Resolution

To allow closed incidents to be added to the related list of a problem, modify the BulkAddIncidents script include to remove the active filter.

Note: This change is a customization of a base system script include. You should be aware of this when upgrading, as upgrades may overwrite the change and it may need to be reapplied.

**Step 1: Open the UI action**

1\. Open a problem record and locate the incident related list.  
2\. Right-click any column header in the related list and select Configure > UI Actions.  
3\. In the UI Actions list, search for \`Add\` in the Name field.  
4\. [Open the Add UI action record](https://\<instance-name\>.service-now.com/nav_to.do?uri=%2Fsys_ui_action.do%3Fsys_id%3D69deb210874313007e31af1e36cb0be9%26sysparm_record_target%3Dsys_ui_action%26sysparm_record_row%3D1%26sysparm_record_rows%3D51%26sysparm_record_list%3Dtable%253Dincident%255EORtableINincident%252Ctask%255EORDERBYname)

**Step 2: Open the BulkAddIncidents script include**

1\. In the UI action script, locate \`BulkAddIncidents\` on line 2.  
2\. Right-click the reference or use the reference icon next to the field to open the script include in a new tab.  
3\. Alternatively, [open the BulkAddIncidents script include directly](https://\<instance-name\>.service-now.com/nav_to.do?uri=%2Fsys_script_include.do%3Fsys_id%3D9e926b94874313007e31af1e36cb0b30%26sysparm_view%3D%26sysparm_domain%3Dnull%26sysparm_domain_scope%3Dnull)

**Step 3: Remove the active filter**

1\. In the BulkAddIncidents script include, go to line 24.  
2\. In the \`var fixedQuery\` line, remove active=true^ from the query string.  
3\. Select Update to save the record.

After saving, you can add closed incidents to the related list of a problem record.
