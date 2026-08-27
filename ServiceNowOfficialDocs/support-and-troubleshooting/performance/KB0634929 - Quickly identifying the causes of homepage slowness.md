---
title: "Quickly identifying the causes of homepage slowness"
aliases:
  - KB0634929
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634929
kb_number: KB0634929
last_modified: 2026-05-07
---

## Quickly identifying the causes of homepage slowness

  

### Issue

  

The number one performance issue that instance admins face is slow homepages. ServiceNow uses a very open homepage configuration model that allows most users unlimited access to set up and change their homepage.

### Release

All supported Releases

### Resolution

### Identifying the gauge or report causing homepage slowness

The following three-step process is a useful way to quickly identify which gauge or report is causing homepage slowness:  
  

1.  Navigate to **System Diagnostics > Session Debug > Debug Homepage Render**.  
      
    ![Debug Homepage Render](sys_attachment.do?sys_id=94f2f0d88730079857288519dabb3545 "Debug Homepage Render")  
      
    
2.  Impersonate the user reporting the issue.  
      
    
3.  At the bottom of the page, the render time per gauge/report is recorded. Anything over 2 seconds is too slow.  
      
    ![render time per gauge/report](sys_attachment.do?sys_id=a4f2f0d88730079857288519dabb354b "render time per gauge/report") 

  
  

### Improving homepage slowness after identifying problematic gauge or report

Following are three common ways to improve a slow homepage after identifying which gauge/report is slow:

-   Add the filter Active=True to make most gauges and reports much faster.
-   Remove the gauge or report from the user's homepage and move the list or report to the user's favorite list.
-   If the user reporting the issue has changed from the default row count to something greater than 20 and the slow gauge or report is a list, try changing the row count back to 20.  
    -   Navigate to **User Administration > User Preference**.
    -   filter on **Name = rowcount** and the user  
              or
    -   filter on the URL https://INSTANCENAME.service-now.com/sys\_user\_preference\_list.do?sysparm\_query=name%3Drowcount then filter on the user
