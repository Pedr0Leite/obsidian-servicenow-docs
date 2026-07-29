---
title: "Workflow is not trigger every time as needed."
aliases:
  - KB0792314
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792314
kb_number: KB0792314
last_modified: 2026-04-24
---

## Workflow is not trigger every time as needed.

  

### Issue

Workflow on the "cmdb\_ci\_computer" table does not trigger every time.

### Release

All releases

### Cause

The workflow triggered earlier on the records as we can see workflow binding records present.

Once the workflow triggers on any record, there is an entry in wf\_context and wf\_workflow\_binding table as well.

Through Table cleanup script, workflow context gets deleted after 180 days.

But the workflow\_binding table will still have the associated data.

### Resolution

A workflow will not start if it currently has a record in the "workflow context" or in "workflow binding" tables.  
  
If you want the workflow to get triggered multiple times on the computer record, you may have to delete the workflow context that has been completed. Starting from London, if you manually delete the workflow context, the workflow binding associated with it also gets deleted.  
  
So, deleting the workflow context through script will also delete the record in workflow binding.  
  
If the contexts are deleted through the table cleanup script then those will still have the workflow binding records existing in the table.
