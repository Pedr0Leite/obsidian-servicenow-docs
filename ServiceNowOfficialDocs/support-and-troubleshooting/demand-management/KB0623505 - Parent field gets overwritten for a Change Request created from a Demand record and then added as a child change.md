---
title: "Parent field gets overwritten for a Change Request created from a Demand record and then added as a child change"
aliases:
  - KB0623505
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623505
kb_number: KB0623505
last_modified: 2024-04-07
---

## Parent field gets overwritten for a Change Request created from a Demand record and then added as a child change

  

### Issue

Parent field is overwritten for a Change Request created from a Demand record and then added as child change to another change

Problem

* * *

When a change request is created from a demand record, the demand number is stamped on that change request in the Parent field so that the change request can be linked back to the demand it was created from and can be displayed in the Change request related list on the demand record. However, when the change is added as a child to another change, the parent field is overwritten to the new parent change and the link to the demand record is lost.

Cause

* * *

The demand application and the change application are both using the same parent field and updating that field independent of each other.

Resolution

* * *

Note that although this behavior is as designed, an enhancement request has been submitted to change this design so that the originating demand record and a parent change can be tracked at the same time.

Workaround

* * *

Create an additional reference field either on the change\_request table or the \[dmn\_demand\] table where the link between the Demand record and the Change Request record is stored. This field can be populated automatically through a business rule or client script that populates the field only when the change request is submitted from the demand record. The value for this field would not be expected to change after initially being populated.
