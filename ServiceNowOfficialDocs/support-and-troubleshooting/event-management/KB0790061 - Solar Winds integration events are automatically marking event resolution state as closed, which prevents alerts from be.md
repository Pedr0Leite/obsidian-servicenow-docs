---
title: "Solar Winds integration events are automatically marking event resolution state as closed, which prevents alerts from being created"
aliases:
  - KB0790061
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790061
kb_number: KB0790061
last_modified: 2026-05-22
---

## Solar Winds integration events are automatically marking event resolution state as closed, which prevents alerts from being created

  

### Issue

While generating events from Solarwinds, the event is automatically set to a resolution state of closed. Therefore alerts are not created. 

### Release

All

### Cause

This is because, In the Solar Winds JS script include, we are setting the event state as closing when the additional information contains "icon":"Start"  
  
https://instancename.service-now.com/ecc\_agent\_script\_include.do?sys\_id=1a2b610f93230200b200b9ab357ffbf9&sysparm\_view=  
  
**Logic**

  
if (eventTypes\[rawEvent.EventType\] != null) {  
var icon = eventTypes\[rawEvent.EventType\]\[0\];  
event.setField("icon", icon);  
if (icon === "Add" || icon === "Green" || icon === "Start")  
event.setResolutionState("Closing");  
else  
event.setResolutionState("New");

} else {  
event.setResolutionState("New");  
}

### Resolution

This is expected when the additional information has "icon":"Start". Need to check with your SolarWinds integration team & figure out why the events are generating with icon as start.
