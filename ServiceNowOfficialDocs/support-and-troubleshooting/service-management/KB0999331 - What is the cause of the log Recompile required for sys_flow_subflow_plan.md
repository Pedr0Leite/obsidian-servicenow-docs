---
title: "What is the cause of the log \"Recompile required for sys_flow_subflow_plan\"
aliases:
  - KB0999331
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999331
kb_number: KB0999331
last_modified: 2025-01-02
---

## What is the cause of the log "Recompile required for sys\_flow\_subflow\_plan"

  

### Summary

The below flow log is seen -   
  
  
Recompile required for sys\_flow\_subflow\_plan with id xxxxxxxxxxxxxxxxxxxxxxxx because not compiled on latest build, instance build: glide-rome-06-23-2021\_\_patch1-hotfix1a-09-21-2021\_10-12-2021\_1252.zip != flow build:glide-rome-06-23-2021\_\_patch1-hotfix1-09-15-2021\_09-16-2021\_1434.zip  
  

According to our dev team, we internally log "Recompile required for sys\_flow\_subflow\_plan" if flow/subflow needs to be recompiled and system itself recompiles the flow without user intervention and log this for information only.
