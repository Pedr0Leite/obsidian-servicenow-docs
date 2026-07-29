---
title: "What is the best way to delete in bulk users and HR profiles?"
aliases:
  - KB0726244
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726244
kb_number: KB0726244
last_modified: 2024-04-07
---

## What is the best way to delete in bulk users and HR profiles?

  

### Issue

# Symptoms

* * *

How should one delete in bulk, user and HR profiles? If one deletes the sn\_hr\_core\_profile record, will the platform automatically delete any related record such as the sys\_user record?Are there other records which needs to be deleted to accomplish this task?

# Resolution

* * *

HR profile deletion does not initiate user profile deletion. But the reverse is true i.e deleting an user profile will delete hr profile also. 

For bulk deletion of hr profile, there is no documented way, however you can check the below community post for some pointers : 

[Deletion of Bulk HR Profiles](https://community.servicenow.com/community?id=community_question&sys_id=ba0b1a2edb8797c45ed4a851ca961915 "Deletion of Bulk HR Profiles")
