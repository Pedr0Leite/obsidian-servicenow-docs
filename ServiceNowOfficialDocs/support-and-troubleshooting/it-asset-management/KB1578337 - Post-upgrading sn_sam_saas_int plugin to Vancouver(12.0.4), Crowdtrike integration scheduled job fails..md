---
title: "Post-upgrading sn_sam_saas_int plugin to Vancouver(12.0.4), Crowdtrike integration scheduled job fails."
aliases:
  - KB1578337
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1578337
kb_number: KB1578337
last_modified: 2023-11-28
---

## Issue

After upgrading instance to Vancouver version, the sn\_sam\_saas\_int version is upgraded to 12.0.4.  
If the crowdtsrike integration exists or is newly created in the upgraded instance, the scheduled job to download host information fails.  
Open the Crowdstrike Download Host Sensor Information subflow, observe the subflow shows -- action definition is missing -- error.

## Resolution

sn\_crowdstrk\_spoke version to 1.0.6 has the Look up Host details action  
Upgrading to sn\_sam\_saas\_int version 12.0.5 will update the dependent sn\_crowdstrk\_spoke version to 1.0.6, which has the action and the subflow works as expected.
