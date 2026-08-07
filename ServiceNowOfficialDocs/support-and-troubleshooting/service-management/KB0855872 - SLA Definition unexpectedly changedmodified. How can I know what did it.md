---
title: "SLA Definition unexpectedly changed/modified. How can I know what did it?"
aliases:
  - KB0855872
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855872
kb_number: KB0855872
last_modified: 2025-01-02
---

## SLA Definition unexpectedly changed/modified. How can I know what did it?

  

### Summary

In many situations, a user may find that a SLA Definition has been modified/changed either unexpectedly or accidentally. Often, the user needs to know _when_, _how_, and _by whom_ a change was made.  
  
This Knowledge Article will provide a few tips/guidelines on what to check to answer those questions.

### Instructions

There are a few things that can be checked to see when, how, and by whom a change was made on a SLA Definition (or on any record):

-   First, the record itself can be checked for historical information. To do this:  
    -   Open the affected record. In this case, a SLA Definition, which lives on the **contract\_sla** table
    -   Once the affected record is open, right-click the header and select History ➛ List
    -   Once the audit history of the record is open, sort the "Update time" column from z to a
    -   The latest update may inform the user of the answers to _when_, _how_, and _by whom_ the record was updated
-   Next, and in the case that a record is completely deleted, the "Deleted records" (**sys\_audit\_delete**) table may be referenced. It is highly recommended that this list-view be opened as filter-only = true, though, by using the URL in step one below:  
    -   Open the "Deleted records" table via the URL provided: {instancename}.service-now.com/sys\_audit\_delete\_list.do?sysparm\_filter\_only=true
    -   Open the list filter and search against "Payload" "contains" and then in the last box where some value would be placed, search against the sys\_id of the affected record
    -   If there is no luck in this scenario, the user can raise a case in HI and share that a record may have been lost and that assistance is needed in understanding what happened. A case should only be raised if this happened within the last 14-16 days or earlier, as Support will not be able to assist past a certain point due to restrictions on how long logs/backups are kept, etc
-   Finally, and the most promising method of checking for answers to the main question (_who_, _how_, and _by whom_) is to check the "Customer Updates" table (**sys\_update\_xml**):  
    -   To do this, open the "Customer updates" table and in the "Name" column, search against the affected record. In this case, a SLA Definition is being searched against, so the value will be something like:  
        -   table\_name\_sysid or, as a real example, contract\_sla\_0ee3e17edbdc1810e215ec95ca9619fa  
            

If the above three options do not show any information, it is very likely that there will not be information elsewhere in the Platform to assist in uncovering _why_, _how_, or _by whom_ a change was made against a SLA Definition (or any affected record of concern).
