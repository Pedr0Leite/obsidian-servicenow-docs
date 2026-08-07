---
title: "Business Impact Analysis Tab Missing - Policy Exception"
aliases:
  - KB0993293
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993293
kb_number: KB0993293
last_modified: 2024-08-28
---

## Business Impact Analysis Tab Missing - Policy Exception

  

### Issue

Business impact analysis tab is missing from policy exception request records.

### Cause

In versions prior to Version 10.1, the Risk assessment related list was called Business Impact Analysis and required that the GRC: Risk Management application be activated. Starting in Version 10.1, the dependency on Risk Management has been removed and the associated field names have changed.  

Reference:  
[https://docs.servicenow.com/bundle/quebec-governance-risk-compliance/page/product/grc-policy-and-compliance/task/request-policy-exception.html](https://docs.servicenow.com/bundle/quebec-governance-risk-compliance/page/product/grc-policy-and-compliance/task/request-policy-exception.html)

This specific tab/associated UI actions were clarified by development in the community post:  
[https://community.servicenow.com/community?id=community\_question&sys\_id=ae21cdc7dbd13c50190dfb243996198f](https://community.servicenow.com/community?id=community_question&sys_id=ae21cdc7dbd13c50190dfb243996198f)

### Resolution

The mentioned functionality can be performed in the 'Risk Assessment' tab of the policy exception request record. This tab has simply been renamed.
