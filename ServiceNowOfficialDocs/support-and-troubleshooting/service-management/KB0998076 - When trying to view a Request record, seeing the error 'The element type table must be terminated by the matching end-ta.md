---
title: "When trying to view a Request record, seeing the error 'The element type \"table\" must be terminated by the matching end-tag \"</table>\"
aliases:
  - KB0998076
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998076
kb_number: KB0998076
last_modified: 2024-08-28
---

## When trying to view a Request record, seeing the error 'The element type "table" must be terminated by the matching end-tag ""'

  

### Issue

When the user was trying to open a sc\_request record (REQ) in self-service view, the page would open as a standard white HTML page with just the text error below:

`The element type "table" must be terminated by the matching end-tag "</table>"`

### Cause

This is a newly discovered problem, <a href="[https://support.servicenow.com/problem.do?sys\_id=a9687819db9bb490770be6be139619fa&sysparm\_view=case](https://support.servicenow.com/problem.do?sys_id=a9687819db9bb490770be6be139619fa&sysparm_view=case)"><span style="color:#00F">PRB1533260</span></a>.

### Resolution

The current workaround to this, as the issue happens when the Request is in "self-service" view (as per the problem details), is to go to the list-view for requests (_sc\_request\_list.do_) and set the view in the top left hamburger icon to "Default". Then, on opening the Request, the form will render properly.
