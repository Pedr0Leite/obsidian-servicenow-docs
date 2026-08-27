---
title: "Extend Preview Document functionality to HR Case - Assignment Group users"
aliases:
  - KB0858731
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858731
kb_number: KB0858731
last_modified: 2025-09-03
---

## Extend Preview Document functionality to HR Case - Assignment Group users

  

### Issue

On HR cases, Preview and Generate Document functionality is only for the Assigned To users but when there is a requirement that the same functionality is required for the Assignment Group users of the HR case. How this can be achieved 

### Release

Orlando Patch 6

### Cause

The UI action 'Preview Document' is only for the 'Assigned To' user and Its condition need to be modified to allow the HR case.  -> Assignment Group users of the HR case.

This UI action calls script include HRSecurityUtilsAjax which is validating below condition

(gr.get(tableId) && gr.canRead() && gr.getValue("assigned\_to") == gs.getUserID())

### Resolution

As per the attached screenshot, see from line number 36 there is logic to be executed only for assigned to the user. So in this case, it is required to modify as per the need -> to check if the assigned to / user trying to attach pdf are from the same group.  

(gr.get(tableId) && gr.canRead() && gr.getValue("assigned\_to") == gs.getUserID())

to

(gr.get(tableId) && gr.canRead())

If there are any scope errors, then goto -> Restricted Caller Access and move the sate to Allowed for Source Script Include 'HRSecurityUtilsAjax'
