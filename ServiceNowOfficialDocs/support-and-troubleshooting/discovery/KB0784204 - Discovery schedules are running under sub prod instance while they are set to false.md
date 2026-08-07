---
title: "Discovery schedules are running under sub prod instance while they are set to false"
aliases:
  - KB0784204
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784204
kb_number: KB0784204
last_modified: 2024-04-08
---

## Discovery schedules are running under sub prod instance while they are set to false

  

### Issue

Discovery schedules are set to false but still execute as per schedule.

### Release

All

### Cause

When an instance is cloned, the discovery schedule which is marked as true on the originating instance will be imported into the target instance. Because of this, even though the discovery schedule was marked active = false in the target environment, the clone process creates a sys\_trigger event to run the discovery schedule after the cloning process.

### Resolution

Mark the concerned discovery schedules as active, save it, and mark it inactive and save it again.

This action removes the entry for the discovery schedule from the sys\_triggers.list. This discovery schedule should not run again on the next schedule.   
  
One way to overcome this is to use Data Preservers during a cloning process. Check the data preserver setting on the instance, ensure that the Discovery Schedule is set to True so the discovery schedule runs retain their instance specific settings after the cloning process.
