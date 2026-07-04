---
title: "HR Cases displaying record not found and cannot be deleted"
aliases:
  - KB0760341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760341
kb_number: KB0760341
last_modified: 2024-04-08
---

## HR Cases displaying record not found and cannot be deleted

  

### Issue

The following KB provides information on how to resolve an issue in HR when a user/admin views a record and is provided with the 'record not found' message.

### Release

All

### Cause

It is possible that the HR case record has a corrupt sys\_class\_name.

For example:

Record in sn\_hr\_core\_case\_talent\_management (HR Talent Management Case). If for some reason the sys\_class\_name is changed the record will not be viewable from a list view but can still be seen from the database. This results in an orphan record.

### Resolution

Since the class name is corrupted, the user or admin can run the a simple script to alter the sys\_class\_name of the record which would then insert a new record into a respective table that would make the record viewable which can then be successfully removed.

```
var gr = new GlideRecord(‘tablename’);gr.addEncodedQuery(‘you_query_for_the_corrupted_record’);gr.query();var count = gr.getRowCount();if (count > 0) {while (gr.next()) {//gr.sys_class_name = ‘new_target_class’;//gr.update();}gs.print(count);}The script will query the table for the corrupted record. Once it finds the record the sys_class_name of therecord will be updated to a new sys_class_name value. This inserts a brand new record into the class specified which willnow make the record visible and eligible for removal.
```
