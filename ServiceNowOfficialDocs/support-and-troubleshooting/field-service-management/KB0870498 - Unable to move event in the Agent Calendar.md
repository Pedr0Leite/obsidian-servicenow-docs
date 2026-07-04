---
title: "Unable to move event in the Agent Calendar"
aliases:
  - KB0870498
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870498
kb_number: KB0870498
last_modified: 2024-04-12
---

## Unable to move event in the Agent Calendar

  

### Issue

When viewing the Agent Calendar (Field Service > Agent > My Schedule), the Event is unable to click and drag.

If clicking anywhere and drag it will create a new event.

[task/move-agent-calendar DOC](https://docs.servicenow.com/bundle/paris-field-service-management/page/product/customer-service-management/task/move-agent-calendar-event.html "task/move-agent-calendar DOC")  

### Cause

The Drag and Move action was controlled by Event Configuration:

/agent\_schedule\_task\_config\_list.do

Each event type needs to have Can Edit Events as True to make the event to drag and move on calendar.

  

### Resolution

OOB Business rule : Block OOB Event functionalities  needs to be deactivated before making the changes on the event configuration.

Then proceed below steps:

1\. Go to Event Configuration  
2\. Pick the specific Event type, for example:Event - Appointment  
3\. Go to configure form layout and bring up "Can edit event"  
5\. Tick the "Can edit event" field and Save  

The Event modified above should be able to drag and move to a new time slot or date.
