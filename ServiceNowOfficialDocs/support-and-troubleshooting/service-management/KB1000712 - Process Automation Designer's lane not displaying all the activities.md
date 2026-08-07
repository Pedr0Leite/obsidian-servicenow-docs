---
title: "Process Automation Designer's lane not displaying all the activities"
aliases:
  - KB1000712
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000712
kb_number: KB1000712
last_modified: 2024-11-05
---

## Issue

Process Automation Designer's lane is not displaying all the activities, it only shows 20 activities.

Steps to Reproduce:  
1\. Create new Process in "Process Automation Designer"  
2\. Add new lane.  
3\. Add 24 or 25 activities to the lane  
4\. Activate the process  
5\. Leave designer  
6\. Open the process automation designer again and confirm that only 20 of the activities are displayed  
7\. Go to "sys\_pd\_lane" -table and select your lane-record  
8\. Check from the related list that there still is 25 activities which are all active

## Resolution

In versions of PAD from **Paris** to **Rome** the designer only supports displaying 20 activities per lane and 20 lanes per process even though the process could have more than 20 activities/lane or 20 lanes/process.  
In **San Diego** we modified the designer to **support displaying more than 20 activities** and lanes.  
  
Unfortunately the only workaround right now for a process with more than 20 activities or lanes is to follow the recommendations in one or both of the following:  
\* Investigate if the process can be broken up into multiple processes with less than 20 activities/lane or 20 lanes  
\* Break down the lanes with more than 20 activities into multiple lanes  
\* Investigate if the activities themselves could be collapsed into custom flows that perform the same function as multiple activities  
  
If the process being built must have more than 20 activities/lane or 20 lanes, then editing them must be done via the platform forms for lanes and activities.
