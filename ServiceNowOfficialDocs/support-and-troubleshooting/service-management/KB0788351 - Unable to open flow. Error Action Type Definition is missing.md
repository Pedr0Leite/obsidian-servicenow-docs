---
title: "Unable to open flow. Error: Action Type Definition is missing"
aliases:
  - KB0788351
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788351
kb_number: KB0788351
last_modified: 2024-04-08
---

## Unable to open flow. Error: Action Type Definition is missing

  

### Issue

After deleting a Flow Designer action definition, some flows cannot be opened and it shows the error: Action Type Definition is missing

### Release

New York

### Cause

Deleted action definition makes a flow action empty.

We don't recommend to delete any flow Action Type Definition records, but if the issue happens, you can try the following options.

### Resolution

Option 1:

1.  Go to System Definition > Deleted Records and in the list, try to find the deleted action type definition and recover it.

Option 2:

1.  Go to \[instance URL\]/sys\_hub\_action\_instance\_list.do
2.  Search for the flow that is giving the error message, e.g. filter on flow name.
3.  Further filter the list, search for any record that has empty Action type
4.  Make a backup (export XML) of the found sys\_hub\_action\_instance record, and delete it.
5.  Repeat until the error is gone.

note: for option 2, you will have to do the same for any subflows that are being called
