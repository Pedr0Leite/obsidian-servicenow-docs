---
title: "Users with sn_hr.basic or admin role are unable to update fields on HR Case record from form view"
aliases:
  - KB0755685
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755685
kb_number: KB0755685
last_modified: 2024-04-07
---

## Users with sn\_hr.basic or admin role are unable to update fields on HR Case record from form view

  

### Issue

# Symptoms

When a user with admin or a user with sn\_hr.basic role tries to update short description (or any other field to which they have write access), saving or updating the form does not reflect the changes made.

# Release

Any supported release

# Cause

Restricted Caller Access for the Update and Save UI Actions for Short Description field on sn\_hr\_core\_case table with Status as Invalidated

# Resolution

Change the Status from Invalidated to Allowed

# Additional Information

Updating from list doesn't go through these UI actions restrictions. So the issue does not happen from list view.

  
Links to the related documentation :

[https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest](https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest)   
[https://docs.servicenow.com/csh?topicname=scope-resource-access.html&version=latest#task\_mjf\_q2q\_zdb](https://docs.servicenow.com/csh?topicname=scope-resource-access.html&version=latest#task_mjf_q2q_zdb)
