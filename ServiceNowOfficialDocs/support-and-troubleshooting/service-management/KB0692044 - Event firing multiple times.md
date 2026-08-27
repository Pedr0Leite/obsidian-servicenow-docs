---
title: "Event firing multiple times"
aliases:
  - KB0692044
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692044
kb_number: KB0692044
last_modified: 2024-09-20
---

## Event firing multiple times

  

### Issue

# Symptoms

* * *

Notification event is firing mulitple times 

# Release

* * *

KP4

# Cause

* * *

The "create event" workflow activity is called twice in the workflow

# Resolution

* * *

The event is created from the "Create event" workflow activity in the workflow. The reason we are seeing the event  being created two times for each RITM records is that the workflow activity "Create event" is being called twice, therefore we are seeing the event twice.

The reason the activity is called twice is due to the workflow path. There are two paths leading to the create event activity.

To resolve this issue we need to review the workflow transition
