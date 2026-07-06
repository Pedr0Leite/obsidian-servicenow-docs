---
title: "vCenter Discovery automatically creates Service Account"
aliases:
  - KB0688853
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688853
kb_number: KB0688853
last_modified: 2024-04-07
---

## vCenter Discovery automatically creates Service Account

  

### Issue

# Symptoms

* * *

vCenter automatically creates an default Service Account with just the vCenter UUID even though there is already a Service Account created for the vCenter.

# Release

* * *

Jakarta and newer

# Cause

* * *

-   There are two options to discover vCenter  
    1.  Through **Cloud Service Account**
    2.  Through **vCenter host discovery**
-   Both options create default service accounts.
-   Option 1 was a bug that was fixed
-   Option 2 was due to incorrect Account ID configured for vCenter Service Account. The way vCenter Host discovery identify existing Service Accounts are through their Account ID which has to be the vCenter UUID.

# Resolution

* * *

Deleting the default account that was created:

1.  Go to relationship table: cmdb\_rel\_ci\_list.do
2.  Find the relationship record(s) with the following conditions:  
    1.  Parent is the Datacenter(s) hosted on the vCenter
    2.  Child is the service account that was automatically created
3.  Export for backup then delete the relationship records found.
4.  Go to **Cloud Management > Service Account**
5.  Locate the default Service Account that was created and delete

Correcting existing Service Account

1.  Go to **Cloud Management > Service Account**
2.  Identify the configured Service Account that was duplicated
3.  Obtain the vCenter UUID for the Service Account
4.  Under the Service Account's Account Id field, enter the correct vCenter UUID found in step 3 and save.

# Additional Information

* * *

[Create a service account for Cloud Management](https://docs.servicenow.com/ "Create a service account for Cloud Management")
