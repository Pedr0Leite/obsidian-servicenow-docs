---
title: "In the To-dos section of the ESC, when clicking checkboxes in HR Tasks, the page reloads and throws the user to the top of the list of HR Tasks"
aliases:
  - KB0824654
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824654
kb_number: KB0824654
last_modified: 2024-04-08
---

## In the To-dos section of the ESC, when clicking checkboxes in HR Tasks, the page reloads and throws the user to the top of the list of HR Tasks

  

### Issue

The user is noticing an issue where, when they are creating some HR Tasks on their HR Cases, when viewing the HR Tasks in the To-dos section of the Employee Service Center (ESC) and clicking the checkboxes inside the tasks, the page reloads and redirects them back up to the top of the page unexpectedly. This can be very disorienting if the user is down the list of the HR Tasks and is suddenly back up at the top of the list.

### Cause

There is a custom Business Rule (BR) on the task table called "Set The Requestor Field" which is causing the issue.

### Resolution

As mentioned, the "Set The Requestor Field" is the root of the issue. The custom BR updates a custom field titled "u\_requestor", which triggers the record watcher from Service Portal to refresh the entire list of To-dos. The update behavior is expected.  
  
A possible workaround is listed below, and can be added to the _shouldReloadList()_ function on the _HRM Task List_ widget to accommodate the custom field:

```
function shouldReloadList(recordWatchUpdate) {    if (recordWatchUpdate.operation == "delete" || recordWatchUpdate.operation == "insert")        return true;    if (recordWatchUpdate.changes.length == 1)        return recordWatchUpdate.changes[0] != 'comments' && recordWatchUpdate.changes[0] != 'work_notes' && recordWatchUpdate.changes[0] != 'approval_history' && recordWatchUpdate.changes[0] != 'u_requestor';    return recordWatchUpdate.changes.length > 0;}
```
