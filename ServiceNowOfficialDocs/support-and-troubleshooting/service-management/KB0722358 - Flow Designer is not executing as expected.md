---
title: "Flow Designer is not executing as expected"
aliases:
  - KB0722358
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722358
kb_number: KB0722358
last_modified: 2025-02-14
---

## Flow Designer is not executing as expected

  

### Issue

Flow Designer is not executing as expected

### Release

London Patch 2

### Cause

The user had 2,800 events pending which made it look as though Flow designer Action "Aperture Science TCIAL" was not working. In actuality, the events needed to process the above Action were created successfully.  
  
Rather, the real issue was that the event queue was backed up which prevented the processing of the event, and thus the execution of the Action.

### Resolution

When an Action is fired in Flow designer (like "Aperture Science TCIAL"), it creates an event to execute that job. The "flow.start" events get processed by the "Flow Engine Event Handler" job in the sys\_trigger table.  
  
The problem is that while there were four of these "Flow Engine Event Handler" jobs in sys\_trigger, all of them were in a state of "queued". They needed to instead be in a state of "ready". When the state of one of them was manually updated to "ready", the system immediately picked up the "flow.start" events and started processing them.  
  
The entire backlog of events is now clear, and it did not take much time at all. The issue, the why and how of this blockage, was due to the state being in "queued" rather than in "ready".  
  
After the backup was cleared, a secondary test was run to ensure that everything worked as expected - and it did. The "Aperture Science TCIAL" Action processed perfectly.
