---
title: "Discovery schedules run even if the state is set to false post clone process"
aliases:
  - KB0784203
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784203
kb_number: KB0784203
last_modified: 2024-04-08
---

## Discovery schedules run even if the state is set to false post clone process

  

### Issue

After a clone of the instance, some of the discovery schedules that have been marked as inactive will continue to run or execute. 

### Cause

When a clone is created, the discovery schedule which is marked as true on the source instance for the clone, is imported into the target instance. Even though the discovery schedule is marked active = false in the target instance environment, the clone process creates a sys\_trigger event to run the discovery schedule after the cloning process.

This can be verified by finding the related discovery schedule record from sys\_triggers.list

### Resolution

One way to overcome this is to use Data Preservers during a cloning process. Set the theme for Discovery Schedules to True before cloning, so the discovery schedule runs retain their instance specific settings after the cloning process. More information for Data Preservers can be found at [https://docs.servicenow.com/csh?topicname=data-preservation.html&version=latest](https://docs.servicenow.com/csh?topicname=data-preservation.html&version=latest)  
  
  

In order to fix the schedules that are running, even-though being marked as inactive after the cloning process, mark the schedule as active and back to inactive on the recently cloned instance to rectify this behavior.
