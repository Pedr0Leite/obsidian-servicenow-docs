---
title: "Calculate mean (average) time to acknowledge (assign) incidents per assignment group"
aliases:
  - KB0695994
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695994
kb_number: KB0695994
last_modified: 2024-04-07
---

## Calculate mean (average) time to acknowledge (assign) incidents per assignment group

  

### Issue

# Release

* * *

Kingston Patch 6

# Resolution

* * *

The user recently created a SLA defintion to track how long incidents remained unassigned, specifically for two assignment groups. The user would like to know how to, prior to that SLA's creation, track the same information about older incidents.  
  
Metrics with a custom Script may be able to resolve this issue for the user. However, this is a customization.

The user could create some sort of metric based on the "assigned\_to" field with a type of "Script calculation", and see how long the field was in an empty state. The user and their internal development team would handle the creation, debugging, and implementation of this custom Script.  
  
After contacting the Subject Matter Experts for this type of Reporting, it was confirmed that there is no OOB method to do this. It is only through a custom Script, and again, that would be handled internally with the user's development team (it is out of scope for Support as Support does not have the expertise needed to assist with custom implementation).  
  
If the user requires assistance with Scripting, refer them to the Professional Services team who are Experts in such customizations, and they would be happy to assist the user (note: there is a fee with this service).

\--  
  
If the user has not set up any Response SLAs and desires to track how long it takes for an engineer to acknowledge an incident, recommend them as such metrics are typically handled and measured using Response SLAs. This is the best and recommended method to track such things.
