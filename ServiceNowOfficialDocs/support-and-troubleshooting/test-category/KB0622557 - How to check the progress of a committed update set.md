---
title: "How to check the progress of a committed update set"
aliases:
  - KB0622557
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622557
kb_number: KB0622557
last_modified: 2025-02-11
---

## How to check the progress of a committed update set

  

### Issue

When an update set is committed in the target instance, a message pop up states that the update set is committed. More often than not, the update set would actually be committed but if the updates within the update set is huge, it might take a while to complete the commit process. In some cases the update set is actually still running in the backend. The UI action sets the state of the update set to Committed, while it is still running.

This could create some issues if there are more update sets to be committed one after the other, so the chances are that a second update set would be committed before the first one actually finished completely. In some cases, the results would not be favorable.

### Resolution

There is a way to check the progress of the update set, to confirm that the commit process has successfully completed. The update sets are picked up by the progress workers to process, in order to get to the progress workers do the following:

1.  Navigate to progress workers, System Diagnostics > Progress Workers
2.  Search for the name of the update set in the name field in the form  
    -   Otherwise, access via this URL (after replacing _<instancename>_): _https://<instancename>.service-now.com/sys\_progress\_worker\_list.do?sysparm\_query=messageLIKEupdate%20set_
3.  Look for the update set name and the state should be Completed and not 'Running' 

If the progress worker above states that it is completed, it should have completed the process in the backend as well. If the update set says it is Running, please wait for the update set to complete. The state changes to Completed.
