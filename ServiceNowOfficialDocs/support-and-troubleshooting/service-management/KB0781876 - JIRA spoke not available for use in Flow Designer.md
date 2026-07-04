---
title: "JIRA spoke not available for use in Flow Designer"
aliases:
  - KB0781876
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781876
kb_number: KB0781876
last_modified: 2024-04-08
---

## JIRA spoke not available for use in Flow Designer

  

### Issue

JIRA Spoke is used to manage issues, users, stories, and groups in Jira. Retrieve Jira data to use in the ServiceNow flow designer. This KB talks about how to proceed when you need to use JIRA spoke in your flow designer actions on your sub-prod instance but witness the below prompt

![](/sys_attachment.do?sys_id=a33baf74db0cb0d016d2a345ca961977)

When clicked on install, the platform prompts stating the JIRA spoke is already available.

### Release

New York Patch 1 Hot Fix 1

### Cause

In Sub Prod environments , JIRA spoke is already downloaded from store onto your instance out of the box and you don't need to manually download from the store.

This is the reason the platform says 'JIRA Spoke" is already available 

### Resolution

Follow the below instructions in order to install JIRA spoke and use it as an action in your flow designer

i) Open the instance UI

ii) Filter for plugins in the Application Navigator

iii) Search for the name "JIRA Spoke" in the content frame

iV) The spoke appears in the results

V) Click on install button 

This will install the JIRA Spoke on your instance after which you can use this in your flow designer
