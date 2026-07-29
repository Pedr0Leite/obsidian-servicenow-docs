---
title: "Determining if a request is approved"
aliases:
  - KB0538281
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538281
kb_number: KB0538281
last_modified: 2024-09-20
---

## Determining if a request is approved

  

### Issue

Determining if a request is approved  

Symptoms

* * *

Symptoms may include the following:  

-   Cannot publish workflow
-   Publishing workflow takes too long
-   Cannot modify checked out workflow
-   Cannot start workflow
-   Workflow does not start
-   Workflow does not trigger

Check in the list view

* * *

To determine if a request is approved using list view, check the **Request state** column in the **Requests** related list.

 ![](/sys_attachment.do?sys_id=a34ba46adb42b450e515c223059619f7)

Check in the Request form view

* * *

To determine if a request is approved using **Request** form view, check the **Request State** field.

  ![](/sys_attachment.do?sys_id=eb4be46adb42b450e515c22305961908)

Cause

* * *

If the **Request State** field does not show as **Approved**, it usually means that the request is still waiting for approval. Check the **Approver** related list in the **Request** form view to see who can approve the request.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><b>Note</b>: If the request is not approved, workflows will not start for any RITM (Requested Item) associated with that request.</td></tr></tbody></table>
