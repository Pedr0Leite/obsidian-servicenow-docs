---
title: "The difference between Updated and Last login time in user list screen"
aliases:
  - KB0756449
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756449
kb_number: KB0756449
last_modified: 2024-08-14
---

## The difference between Updated and Last login time in user list screen

  

### Issue

Within the instance, there is a difference between Updated and Last login time on sys\_user list screen. The updated date shows its getting updated by system/admin, while no action is performed by anyone. Is Updated and Last login time same?

### Cause

-   "Last Login time" event won't update the "Updated" (sys\_updated\_on) column of "sys\_user" table.The steps below confirms it:   
      
    \- Search for "events" in "Navigator" window   
    \- Go to Events - Script Actions   
    \- Search for "\*last" and enter   
    \- Click 'Last login time'   
    \- There is a java script validation associated with the field not to update sys\_updated\_on, sys\_updated\_by and sys\_mod\_count columns.

-   Automatic update of "Updated" column can be triggered by background processes like "Session timeout", "Unauthorized session" etc. This seems to be related to "user's inactivity has reached maximum allowed time", which may have resulted in logging out of the session, and the system has updated the user record with the respective time.  

### Resolution

-   "Last Login time" event won't effect the "Updated" (sys\_updated\_on) column of "sys\_user" table.

-   Updated" column can be modified by background processes like "Session timeout", "Unauthorized session". This will show "Updated by" as        "system" in the users list screen.
