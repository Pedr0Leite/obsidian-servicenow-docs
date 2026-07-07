---
title: "Error on look up record action: \"GlideRecord.setTableName - empty table name\"
aliases:
  - KB0995965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995965
kb_number: KB0995965
last_modified: 2025-12-23
---

## Error on look up record action: "GlideRecord.setTableName - empty table name"

  

### Issue

Getting below error on lookup record action: "GlideRecord.setTableName - empty table name".

### Release

ANY

### Cause

-   The latest snapshot of the action is missing its element mappings
-   On the table, sys\_hub\_action\_type\_definition, search for Look Up Records action and pull in the main snapshot and the latest snapshot columns.

https://<instance\_name>.service-now.com/sys\_hub\_action\_type\_definition\_list.do?sysparm\_query=name%3DLook%20Up%20Records&sysparm\_view=

-   Copy the main snapshot and open flow designer and open any action and on the address bar replace the sys\_id with the main snapshot value you just copied.

https://<instance\_name>.service-now.com/$flow-designer.do?sysparm\_nostack=true#/action-designer/43400a1587003300663ca1bb36cb0b4b/var/input

-   This would open the Look Up Records action on the flow without any issues.
-   Repeat the same activity for the latest snapshot also, and you would observe issues on the action as below where the table name is empty.

![](sys_attachment.do?sys_id=1f13afa48302321ccdbbc430feaad3d7)

-   This means that the mapping for the latest snapshot is missing.
-   Search this latest snapshot id on the sys\_element\_mapping table. You need to search this on the 'ID' column.
-   You would see no results for this search.
-   The latest snapshot of the step is missing its element mappings.

https://<instance\_name>.service-now.com/nav\_to.do?uri=%2Fsys\_element\_mapping\_list.do

-   For comparison, you can check for the main snapshot which has the expected mappings.

### Resolution

The following script can be used to re-compile the action (table name: sys\_hub\_action\_type\_definition) without modifying their contents:

gr = new GlideRecord('sys\_hub\_action\_type\_definition');

gr.get("sys\_id"); //sys\_id of the Look Up Records action from the sys\_hub\_action\_type\_definition table

gs.print(gr.latest\_snapshot);

if (!JSUtil.nil(gr.getValue("master\_snapshot"))) {
	gr.latest\_snapshot = gr.master\_snapshot;

	gr.setWorkflow(false);

	gr.update();
}

This will update the latest snapshot value with the main snapshot value.

The action will recompile on the next execution and pick up the correct input mappings.  
  
Never clear the latest snapshot field if the master snapshot is empty, this current script on this KB prevents such an update.

### Related Links

[How to re-compile flows and actions without modifying their contents](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963031 "How to re-compile flows and actions without modifying their contents")
