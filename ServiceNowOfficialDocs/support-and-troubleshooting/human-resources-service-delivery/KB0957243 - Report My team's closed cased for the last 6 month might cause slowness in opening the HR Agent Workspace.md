---
title: "Report \"My team's closed cased for the last 6 month\" might cause slowness in opening the HR Agent Workspace "
aliases:
  - KB0957243
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957243
kb_number: KB0957243
last_modified: 2026-03-17
---

## Issue

The OOB Report "My team's closed cased for the last 6 month" might cause slowness in opening the HR Agent Workspace.

![](sys_attachment.do?sys_id=c771c7bb47abb214b7832920326d439d)

## Resolution

The report can be safely removed and there would be no negative impact.  
  
To remove the report from the landing page:

  
1\. Navigate to Workspace Experience > Administration > Landing Pages

2\. Open the HR Landing Page (CD) page (sys id = ba76fd8f53b200101fb2ddeeff7b12ed)  
https://instance\_name.service-now.com/sys\_ux\_custom\_content\_root\_elem.do?sys\_id=ba76fd8f53b200101fb2ddeeff7b12ed%26sysparm\_view=landing\_page

3\. Switch to the Human Resources: Workspace scope

4\. Click "Open in UI builder"

5\. Click the "Page actions" button in the upper left-hand corner and click "Copy Page"

6\. In the confirmation dialog, rename the page, set the protection to "None", and click "Create Copy"

7\. Remove the undesired element (see attached screenshot)

8\. Save the page

9\. Navigate back to Workspace Experience > Administration > Landing Pages

10\. Deactivate the original landing page (sys id = ba76fd8f53b200101fb2ddeeff7b12ed) and activate the new landing page  
  
Now, when you open the HR Agent Workspace, you should arrive on your new landing page with that report removed.
