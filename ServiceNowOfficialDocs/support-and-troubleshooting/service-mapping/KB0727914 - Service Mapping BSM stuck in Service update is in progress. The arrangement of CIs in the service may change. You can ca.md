---
title: "Service Mapping: BSM stuck in \"Service update is in progress. The arrangement of CIs in the service may change. You can carry on working\""
aliases:
  - KB0727914
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727914
kb_number: KB0727914
last_modified: 2024-04-07
---

## Issue

On the BSM, the following message is displayed: "Service update is in progress. The arrangement of CIs in the service may change. You can carry on working"

## Resolution

To prevent this issue from happening in future:  
Goto System Definition -> Scripts - Background and execute the below script.

var utils = new ServiceMappingRecomputationUtils();  
utils.removeScheduledJobs();  
utils.deployScheduledJobs(2); //2 refers to no.of jobs
