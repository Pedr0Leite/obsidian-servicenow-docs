---
title: "Display field effects on Discovery and SCCM integration"
aliases:
  - KB0794128
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794128
kb_number: KB0794128
last_modified: 2024-04-07
---

## Display field effects on Discovery and SCCM integration

  

### Issue

When using Discovery to add Configuration Items (Computers, Servers) to Service Now. We can use SCCM integration in order to add Computers/Servers that may not get picked up by Discovery.

And when it comes to importing the Disk information - rather than adding the disk data to existing Configuration Items, it might create new ones that contain no data except for Disk information.

From the import set data, it can be seen that the Computer name is there, but it will be creating new Empty computer items. 

### Cause

It is caused due to the display field in the Computer Table that was set to true for any new field added.

This could replace all the display for the computer reference everywhere.

### Resolution

Make sure the display field for any new field added to the Compute Table is set to false.  
  

Only Computer Name should be set to display true so that data will be showing up correctly now in both computer table and disk table.
