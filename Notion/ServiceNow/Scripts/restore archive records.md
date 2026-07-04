---
aliases:
  - "restore archive records"
area: "Scripts"
source: custom
tags:
  - archiving
  - glide-record
  - background-scripts
  - data-management
  - scripts
---

# restore archive records

Restores archived records via `GlideArchiveRestore().restore(sys_archive_log_sys_id)`, looping an archive table (e.g. `ar_incident`), finding the matching un-restored `sys_archive_log` entry, and confirming the record reappears on the original table afterward. Note the loop query is marked as needing a fix in the original snippet (`archiveTicket.get('')` before `.query()` is redundant/wrong).

```javascript
var archiveTicket = new GlideRecord('ar_incident'); //or another table
archiveTicket.get('');
archiveTicket.query();
var count = 0;

while(archiveTicket.next()){ // this needs to be fixed

count++;
var archiveLog = new GlideRecord('sys_archive_log');
archiveLog.addQuery('id', archiveTicket.sys_id);
archiveLog.addNullQuery('restored');
archiveLog.query();
if (archiveLog.next()) {
var und = new GlideArchiveRestore().restore(archiveLog.sys_id);
if (!und) {
gs.addInfoMessage(gs.getMessage("The restore failed"));
// action.setRedirectURL(current);
} else {
var gr = new GlideRecord(archiveLog.from_table);
if (gr.get(archiveLog.id)) {
// action.setRedirectURL(gr);
} else {
gs.addInfoMessage(gs.getMessage("Could not locate the restored record"));
// action.setRedirectURL(current);
}
}
} else {
//action.setRedirectURL(current);
gs.addErrorMessage(gs.getMessage("No active archive log entry found. Record probably already restored"));
}
}
gs.print('Current count ' + count);
```

## Related

- [[Random Scripts]]
