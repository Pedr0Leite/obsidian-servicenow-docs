---
title: "Whenever we transfer and HR case to the other group in Service now, the whole conversation that was done before is being copied to additional comments"
aliases:
  - KB0996484
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996484
kb_number: KB0996484
last_modified: 2025-09-03
---

## Issue

Transferring an HR case to the other group , the whole conversation that was done before is being copied to additional comments.

## Resolution

This is OOB and the functionality seems to be expected behavior.  
OOB code does not differentiate based on any previous or new group

"transfer\_case.ignored\_fields" does not work for ignoring comments because the functionality to copy comments is hardcoded within  
**"hr\_TransferCase"** Script Include below:  
**/nav\_to.do?uri=sys\_script\_include.do?sys\_id=32678a3453b72300ff25ddeeff7b1213**

The code which performs this task is below.

```
copyWorkNotes: function(originalRecord, newRecord) {var originalWorkNotes = originalRecord.work_notes.getJournalEntry(-1);var originalComments = originalRecord.comments.getJournalEntry(-1);newRecord.work_notes = originalWorkNotes;newRecord.comments = originalComments;
```

If you wish comments should not be copied over , you might try to comment out line #198 and for worknotes line #197 of script include above.

You may try this and see if you are able to achieve this requirement.

  
If this doesn't ,this would be a good candidate for the Idea Portal. Our product team will evaluate the idea further and look into ways this can be updated in our upcoming releases. You can submit it here - https://community.servicenow.com/community?id=community\_static&content\_id=91acf933db9ff740d82ffb24399619f5
