---
title: "How To: Update a cmdb_ci_vm_instance record post-Cloud Provisioning using Policies"
aliases:
  - KB0751397
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751397
kb_number: KB0751397
last_modified: 2025-04-07
---

## How To: Update a cmdb\_ci\_vm\_instance record post-Cloud Provisioning using Policies

  

### Issue

# Description

* * *

Post-provisioning it may be desirable for to update/modify VM instance (or other) records with custom information as it relates to your business needs. While it may be obvious to create Business Rules for this, it's not immediately clear what to do if information is needed from the Catalog Item when provisioning the cloud resources.

One use case for this would be to assign ownership of a VM to the user group responsible for provisioning it.

# Solution

* * *

We can accomplish this using a Cloud Policy.

This is easier on London+ due to the "on Catalog item request end" Policy Trigger, which we'll use for this example. The initial steps are to do the following (assuming a basic familiarity with Cloud Policies, see Docs otherwise):

1.  Create new Policy
2.  Set trigger "on Catalog item request end"
3.  Set Blueprint as desired blueprint
4.  Set Operation as "Provision"
    1.  Note that if you want this to work on all Blueprints, you leave Blueprint empty. But this means you cannot select the "Provision" operation. Additional code will be required in the Policy Action Script to filter so you aren't executing on other catalog item operations
5.  Create new policy rule to execute a script
6.  Create new Policy Action Script (then set Policy Rule to execute script)
7.  Now modify the script.  
      
    

When writing a Cloud Policy there are two pertinent variables available to us: "formData" and "current". The formData object contains the data passed from the Blueprint during provisioning and the current object contains the data from the RITM record.

The crux of it can be seen here, but basically clients will need to use either formData or information from the current object to make GlideRecord calls to the records they want to call and then make the desired updates/modifications:  
  
gs.info("formData: " + JSON.stringify(formData));  
gs.info("current: " + JSON.stringify(current));  
  
var vmGr = new GlideRecord("cmdb\_ci\_vm\_instance");  
vmGr.addQuery("name","=",formData.Virtual\_Server\_NodeName);  
vmGr.query();  
if (vmGr.next())  
gs.info("vmGr: " + vmGr.sys\_id);  
else  
gs.info("VM record not created at this time: " + new GlideDateTime().getLocalTime());

# Applicable Versions

* * *

All CMPv2 (easier in London+ due to "on Catalog item request end" option)
