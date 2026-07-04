---
title: "In business rules on the Location [cmn_location] table, previous is the same as current"
aliases:
  - KB0553121
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0553121
kb_number: KB0553121
last_modified: 2024-01-28
---

## In business rules on the Location \[cmn\_location\] table, previous is the same as current

  

### Issue

In business rules on the Location table, previous is the same as current 

Problem

* * *

For After business rules on the Location table \[cmn\_location\] table with an order of 100 or higher, "previous" is the same as "current."

Steps to reproduce

* * *

1.  Log in to a Fuji instance.
2.  Create a business rule:
    -   Table: Location \[cmn\_location\]
    -   When: After
    -   Update: true
    -   Order: 100
    -   Condition: current.contact.changes()
    -   Script: gs.log("Contact field has been updated");
3.  Navigate to a Location record.
4.  Update the **Contact** field.
5.  Navigate to the system log.  
    Note that the message was not recorded.

  
Solution

* * *

The business rule fails to run because "previous" is the same as "current" and therefore the condition is not satisfied. The problem seems to be caused by the base system business rule named **Location - generate full name**. As a workaround, change the order of the custom business rule to a value lower than 100 (for example, 90).   
  
The business rule **Location - generate full name** also calls HierarchicalReference to generate the full\_name on Locations. This performs an update (to generate the full\_name for hierarchy location) so previous = current on contract change.  
  
For more information, see [Defining Locations](https://docs.servicenow.com/csh?topicname=c_MapPages.html&version=latest "Defining Locations") in the product documentation.
