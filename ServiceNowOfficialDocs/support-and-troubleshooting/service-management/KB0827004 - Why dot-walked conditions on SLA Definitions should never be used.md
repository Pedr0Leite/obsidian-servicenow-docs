---
title: "Why dot-walked conditions on SLA Definitions should never be used"
aliases:
  - KB0827004
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827004
kb_number: KB0827004
last_modified: 2026-07-03
---

## Why dot-walked conditions on SLA Definitions should never be used

  

A very common use case for many users is to have, for example, SLA Definitions on the _sc\_task_ table with at least some portion of the Start, Pause, Stop, or Reset conditions based on values from fields/variables in the _sc\_req\_item_ table.

This is never a good idea and will break core SLA functionality for task SLAs based on those SLA Definitions where dot-walking is used. This theory of never using dot-walked conditions in SLA Definitions is not exclusive to the above example - but covers all dot-walked fields across all tables when building SLA conditions.

The reason this kind of implementation should never be used, at minimum, is that it will break SLA Repair and SLA Timeline functionality for the task\_sla records where dot-walked values are used in their related parent SLA Definitions. For example, when utilizing Repair SLAs on the example SLA Definition (based on the sc\_task table, but taking values in some of the conditions from sc\_req\_item fields), is that when SLA Repair is utilized, it will never walk back through the history of dot-walked values. The SLA Engine is only ever going to run against the current record and the audit history on that current record. Because dot-walked fields are never walked through like the audit history of a record is walked through, this will break the SLA Repair and SLA Timeline functionalities by providing inaccurate results.

The "Repair SLA" functionality can successfully reattach a new task\_sla only if the current values of the fields referenced in the SLA start conditions still evaluate to true. However, if a dot-walked field referenced in the start conditions has changed and no longer satisfies the SLA definition, the SLA engine cannot evaluate the historical values of that referenced record. As a result, it cannot determine that the start conditions were previously met, and the task\_sla will not be reattached.

Example: SLA Definition ABC on the sc\_task table has start conditions as "request.request\_state = Approved"

Scenario 1:

SCTASK123 previously had SLA ABC attached.  
The current value of request.request\_state is still Approved.

Result:  
Running Repair SLA successfully reattaches the task\_sla, as the current start conditions still evaluate to true.

Scenario 2:

SCTASK123 previously had SLA ABC attached.  
The request.request\_state value has since changed to Closed Complete.

Result:  
Running Repair SLA does not reattach the task\_sla. Although the start conditions may have been true in the past, the SLA history walker cannot evaluate historical values of dot-walked fields on the referenced sc\_request record. Since the current value no longer satisfies the start condition, the SLA engine cannot recreate the task\_sla.  
  
The **correct and recommended** **method** to create SLA Definitions and to build the conditions therein is to only utilize fields from the table specified in the "Table" field of the SLA Definition. In other words, do not dot-walk Start, Pause, Stop, or Reset conditions away to any other table value, ever. When building conditions, use only the fields on the table the SLA Definition is created to run against.
