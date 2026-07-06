---
title: "Discovery schedules stuck in \"Starting\" state"
aliases:
  - KB0749017
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749017
kb_number: KB0749017
last_modified: 2024-04-07
---

## Issue

# Symptoms

-   Discovery schedules which are created using Transform Maps were stuck in "Starting" state.

![](sys_attachment.do?sys_id=57fb202edb42b450e515c22305961912)

# Release

-   Any version.

# Cause

-   The cause is that the discovery schedules which were created using Transform Map have empty "script" field.
-   This can be verified by clicking on any Discovery Schedule form header >> Configure >> Form Layout.
-   And add the "Run this Script" field from the slush bucket. 

![](sys_attachment.do?sys_id=1bfb202edb42b450e515c22305961917)

# Behavior

-   When the discovery schedule kicks off, the script in the "Run this script" field is executed and discovery is triggered.
-   When creating the discovery schedule, the Business Rule "Discovery - Set schedule script" populates the "Run this script" field automatically.

var rt = new global.DiscoveryScheduleRunType(current.disco\_run\_type + ''); if (rt.match() || new global.DiscoveryJob(job).isRunOnce()) { var dd = new global.Discovery(); dd.discoveryStartJob(); }

# Resolution

-   In order to fix the issue for the Discovery schedules which are created using Transform Maps, cancel the corresponding discoveries which are in "Starting" state and populated the field "Run this script" with below script and re-run the schedule.

var rt = new global.DiscoveryScheduleRunType(current.disco\_run\_type + ''); if (rt.match() || new global.DiscoveryJob(job).isRunOnce()) { var dd = new global.Discovery(); dd.discoveryStartJob(); }

  
  
![](sys_attachment.do?sys_id=abfb202edb42b450e515c2230596191c)
