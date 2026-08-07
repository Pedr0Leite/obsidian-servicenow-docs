---
title: "Event rules are disabled by the system if it encounters invalid regex"
aliases:
  - KB0750340
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750340
kb_number: KB0750340
last_modified: 2024-04-07
---

## Issue

# Symptoms

1) Event rules are disabled by the system with the below error message on the event if it encounters invalid regex :

Invalid regex on event processing. Event rule: <event\_rule\_sys\_id> 

2) The event rule description will be changed to "Warning: Rule was disabled. Event rule processing failed due to a regex failure in Transform and Compose section. Exception message: null. "

# Release

Any

# Cause

1) The most likely root cause is that the event processing has encountered an invalid regex in the transform and compose section of the event rules.

2) The other most likely cause is that , if the event rule is created from an event directly or a recommendation available on the event rules list view, the event fields will be copied to the event rule directly. In this case, if the event fields have some invalid encoded data, the event processing fails with the same error

# Resolution

1) Please check the validity of the regex and replace the invalid regex with the correct regex in the event rule

2) In case , there is invalid encoded data in the events, do not create the event rule from the event by clicking on Create Event rule UI action on the event record . We need to create the event rule from scratch by clicking on new in the event rules list view
