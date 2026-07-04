---
title: "The sys_id of a specific user's sys_user record is not the same between Production and sub-Production after clone"
aliases:
  - KB0746228
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746228
kb_number: KB0746228
last_modified: 2024-09-20
---

## The sys\_id of a specific user's sys\_user record is not the same between Production and sub-Production after clone

  

### Issue

# Symptoms

-   After cloning, some sys\_user record's sys\_ids are different between Dev and Production. Due to that, some group memberships are having issues.

# Release

-   London Patch 4, Hot Fix 2

# Cause

The user has a Data Preserver for the sys\_user table on their sub-Production (Dev) instance. This will prohibit a clone from Production down to this sub-Production environment from syncing the sys\_ids in question.

# Resolution

In this case, a sys\_user record for one specific user was provided on each instance mentioned, both Production and sub-Production.  
  
On Production, Bucky Barnes' sys\_user record has a creation date of 2/23/2016. In the sub-Production instance, his sys\_user record has a creation date of 10/15/2015.  
  
The reason these are different, and the reason these have not been "corrected" or "synced" via a clone from Production down to Dev is that the user has Data Preservers set up on their Dev instance.  
  
What this does, as covered in documentation ( ref: [Data preservation on cloning target instances](https://docs.servicenow.com/csh?topicname=data-preservation.html&version=latest "Data preservation on cloning target instances") ), is protect data on the target instance from being overwritten (When cloning, the "Source" is Production and the "Target" is Dev).  
  
This is why the values are not synced, hence the issue with groups between the two instances.  
  
To resolve this, the user can remove the Data Preserver in their sub-Production instance on sys\_user to effectively "sync" the sys\_ids during their next clone.  
  
As a convenience, simply append the following to the affected instance to see any Data Preserver(s) on or related to sys\_user:  
  

-   /clone\_data\_preserver\_list.do?sysparm\_query=tableLIKEsys\_user
