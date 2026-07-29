---
title: "SLA Definition"
aliases:
  - KB0818381
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818381
kb_number: KB0818381
last_modified: 2026-06-03
---

## SLA Definition

  

### Issue

Question regarding changes to SLA Definition:

\- Impact of changes to the details of the definitions (both the schedule and the duration) and have that apply to future tickets (not to past tickets, closed or still open).

Example: If a copy of the current definition is made, then disabled the current definition, will it have any impact on previous incidents, closed or still open?

### Cause

For existing Task slas that were already inflight, any new changes do not impact until a repair is run. Hence the sla being set to inactive does not impact the existing task sla.

This has been tested to verify the impact on previous incidents, closed or still open,  after disabling/inactivating the current sla definition.

Test used was to attach an sla to an Incident, and then after it had attached, inactivated the sla definition.

On the existing incident, changed it's values to have the task sla paused as per the sla definition pause condition. It worked fine.

Also changed it's values so that the task sla meets the Stop conditions. The task sla completed.

Also tested creation of a new Incident to match the Start condition of the inactive sla definition and confirmed it did not attach.

However it is a bad practice to modify configuration records for an SLA after it is attached, i.e. the contract\_sla record or its related schedule records.  SLA repair will need to be run on all of the task\_sla records that were created prior to changes made that are still in play, i.e. not completed or cancelled. (Assuming need to apply changes to existing records).

When you make changes to an existing SLA definition or a Schedule used by SLA definition it will have no impact on in-flight task slas (these are basically task slas already attached prior to making the Changes) UNTIL you run a repair sla.  
The repair will delete the existing task sla and will recreate it using the CURRENT/Latest sla definition during a repair.

### Resolution

1\. It is recommended to make a copy of the current definition and apply new changes to create a new sla definition. You may also need to add as part of the condition a date condition that ensures this new SLA attaches to newly created Incidents (if that is your requirement). So that this new sla does not attach to existing Incidents that are using the old sla.

2\. As per the old sla definition, consider adding a date condition so that it no longer attaches to any new Incident record.  
Once all the existing task sla which are associated have completed, then it can be inactivated.

Alternatively current SLA definition can be inactivated immediately after creation the new SLA. As per above testing, it will not attach to any new incidents and will still continue to function for existing task slas that have not completed.

NOTE: Please test any changes a sub-prod instance to verify any scenarios you anticipate, before applying to a Production instance.
