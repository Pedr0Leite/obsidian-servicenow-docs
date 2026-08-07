---
title: "Question on \"g_aw.openrecord\" Params on \"Create HR Case\" UI Action"
aliases:
  - KB0955940
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955940
kb_number: KB0955940
last_modified: 2024-02-10
---

## Issue

There is a requirement to pass some values to the HR Case form while using g\_aw.openRecord function.This function should be able to pass values by the use of a parameter called "query".  
However, this does not work with sn\_hr\_core\_case form, ONLY when HR Agent Workspace is installed.On instances where HR Agent Workspace plugin is NOT installed, there is no issue.  

## Resolution

If you deactivate those policies associated with it you can expect the short\_description to remain unchanged.
