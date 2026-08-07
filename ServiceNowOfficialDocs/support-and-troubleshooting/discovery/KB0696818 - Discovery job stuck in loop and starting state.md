---
title: "Discovery job stuck in loop and starting state"
aliases:
  - KB0696818
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696818
kb_number: KB0696818
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Discovery schedule(DS) starts by itself even thought schedule is inactive.

DS will start multiple times almost at the same time (within seconds of previous start).

There will be no ECC queue entries created for that schedule.

Once started it will stay in a "Starting" state. 

The Discovery job that started first will cancel itself out and immediately another instance of that DS will start again. 

# Release

* * *

Any

# Cause

* * *

Usually this may happen if you import via update set from another instance, the discovery schedules. 

There is a disconnect between the schedule and the scheduled jobs table. 

# Resolution

* * *

Delete that schedule and recreate it.

If you have trouble deleting the DS via the UI you can do the following.

1.  Go to Discovery Schedules table
2.  Use the filter to isolate that schedule so it is the only one appearing on the list
3.  Export XML
4.  In the XML change the tag **<discovery\_schedule action="INSERT\_OR\_UPDATE">** to **<discovery\_schedule action="DELETE">.**
5.  Save the XML
6.  Upload back into the instance (this will quickly delete the schedule). 

Before:

![Tag before change](sys_attachment.do?sys_id=8f5a2066db42b450e515c223059619ea "Tag before change")

After:

![Tag after change](sys_attachment.do?sys_id=c75a2066db42b450e515c223059619f0 "Tag after change")
