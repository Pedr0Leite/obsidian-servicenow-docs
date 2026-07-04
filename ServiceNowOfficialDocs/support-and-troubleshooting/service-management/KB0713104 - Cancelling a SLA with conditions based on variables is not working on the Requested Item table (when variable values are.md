---
title: "Cancelling a SLA with conditions based on variables is not working on the Requested Item table (when variable values are updated through the Variable Editor on the child sc_task record)"
aliases:
  - KB0713104
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713104
kb_number: KB0713104
last_modified: 2024-04-07
---

## Cancelling a SLA with conditions based on variables is not working on the Requested Item table (when variable values are updated through the Variable Editor on the child sc\_task record)

  

### Issue

# Symptoms

* * *

-   Cancelling a SLA that has conditions (Start, Stop, Pause, etc) based on variable values is not working on the Requested Item table (when variable values are updated through the Variable Editor on the child sc\_task record)

# Release

* * *

Jakarta Patch 9c 

# Cause

* * *

This is expected behavior.

# Resolution

* * *

In the above case, there is a Variable Editor which is shown both on the sc\_req\_item and the sc\_task records.

There is a SLA Definition set on the sc\_req\_item table, which has conditions based on variable values within the Variable Editor.

When an update is made to some variable within the Variable Editor on the child sc\_task record, this change is reflected in the audit history of each record (sc\_req\_item and sc\_task) and the change is visibly seen in the Variable Editor as well - the variable value is updated.

Interestingly, though both of the above areas are updated, the sys\_updated\_on field in the XML of the parent sc\_req\_item is not being changed when we make an update to a variable's value within the Variable Editor on the child sc\_task record.

The same behavior can be seen (and is also expected in this case) with an incident. Say a user, James Jones, creates an incident. The user's name is in the Caller field ("James Jones"). If another user, Angela Applewood goes into Jame's sys\_user profile and updates his name to be "Angela Applewood, Jr." and saves that record - without making an update to the incident, the user's name will still be listed "James Jones" in the Caller field.

Only when an update to that incident is made will the change be reflected. After the update, the name in the Caller field will then appear as "Angela Applewood, Jr.", not "James Jones".

The same is seen in the original case for which this Knowledge Article was written. A user is making and saving a change to a variable value in the Variable Editor (sc\_item\_option\_mtom table - like the sys\_user table in the fictitious example) and expecting to see an update on the parent RITM (like the incident's Caller field in the fictitious example).

The update won't truly be reflected until the user makes an update to the RITM record itself. When that update is made, the RITM recognizes the change and the SLAs on the RITM record are impacted appropriately (Stage value will move to "Cancelled").
