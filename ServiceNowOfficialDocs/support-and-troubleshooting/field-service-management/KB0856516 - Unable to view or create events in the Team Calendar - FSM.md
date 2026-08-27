---
title: "Unable to view or create events in the Team Calendar - FSM"
aliases:
  - KB0856516
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856516
kb_number: KB0856516
last_modified: 2024-10-12
---

## Issue

In Field Service Management there is a module called ‘Manager’ and a sub module called ‘Team Calendar’.  
Someone with the ‘agent\_schedule\_manager’ role not able to view/create events in FSM agent calendars.  
  
The documentation states that users with this role should be able to ‘view’ the calendar but also suggests that they should be able to add events to the agents calendar 

## Resolution

Disabling the custom acl or adding the custom role to user profile fixes the issue.
