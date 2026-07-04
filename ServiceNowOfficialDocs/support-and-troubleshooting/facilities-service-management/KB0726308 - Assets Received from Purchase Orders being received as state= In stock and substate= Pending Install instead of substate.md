---
title: "Assets Received from Purchase Orders being received as state= \"In stock\" and substate= \"Pending Install\" instead of substate= \"Available\""
aliases:
  - KB0726308
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726308
kb_number: KB0726308
last_modified: 2024-04-07
---

## Assets Received from Purchase Orders being received as state= "In stock" and substate= "Pending Install" instead of substate= "Available"

  

### Issue

# Symptoms

* * *

After receiving the Purchase orders, the assests are created with a substate of "Pending Install". The configuration item of the Assest is also in "Pending Install" status.

# Release

* * *

London Patch 4

# Cause

* * *

This is expected behavior and is caused due to the business rule "Assign from Stock"

# Resolution

* * *

Asset received from PO is created with the substate of "Pending Install" as the related CI is created with the Status of "Pending Install"  
  
This is caused due to the OOB business rule "Assign from Stock"  
  
When a PO is received, the configuration item is created and is added to the Requested Item's 'configuration Item' field.   
  
This triggers the business rule, "Assign from Stock" and it sets the CI's status to "Pending Install".  
  
Due to this reason, the Assest's substate is set to "Pending Install" as it is in sync with the CI's status.
