---
title: "How to automate/automatically create CAB meetings (\"Set it and forget it\" method)"
aliases:
  - KB0997893
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997893
kb_number: KB0997893
last_modified: 2024-08-28
---

## How to automate/automatically create CAB meetings ("Set it and forget it" method)

  

### Issue

The user has CAB meetings every Tuesday and Thursday. They wanted to know if it was possible to automatically generate new CAB meetings so that they did not have to continually refresh the CAB definition to produce new meetings. They needed the system to do this automatically, and wanted to know if ServiceNow shipped any Out of Box (OOB) method to do so.

### Resolution

In short, **no**, ServiceNow does not ship any method to automatically generate CAB meetings.

That said, while there is no OOB method to automatically "set it and forget it" refresh (typically a user would have to manually click the "Refresh CAB meetings" UI Action), it was suggested to the user that they could create a custom Scheduled job that runs every X amount of time (whatever time interval the user preferred) - which calls the same logic that the UI Action does - against the desired CAB Definition(s).

The Script in the UI Action is set to use the "current" object, so the user needed to change that to either (1) hard-code a sys\_id if they just had the one CAB definition and it is fine for them to just target and refresh that one, or (2) the user would have to write a more dynamic script to pull all definitions and auto-refresh them (the second method is preferred, as it is more sustainable and easier to maintain).

The user was encouraged that this is possible, but through a small customization.

Support did reiterate that ServiceNow engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementation of customizations like this is not in the Support's area of expertise, and is out of scope for what Support handles.
