---
title: "Unable to publish the subflow (Error: attempting to use undefined input = 'current' from <SUB FLOW NAME>)"
aliases:
  - KB0999792
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999792
kb_number: KB0999792
last_modified: 2025-02-19
---

## Unable to publish the subflow (Error: attempting to use undefined input = 'current' from )

  

### Issue

When attempting to Publish a Subflow following error is seen : 

"Error: attempting to use undefined input = 'current' from <SUB FLOW NAME>". 

### Cause

This is caused due to the improper usage of inline script under the fields of actions defined in a subflow.

### Resolution

 If you use sub flow, you will need to define Inputs in the sub flow so that the main flow can pass the trigger record to be updated to the sub flow. The "current" variable does not work in sub flow.

Please refer to the following community link to get more clear understanding of the solution.

[https://community.servicenow.com/community?id=community\_question&sys\_id=3840f2c61b17f4d0c552c8031d4bcb97](https://community.servicenow.com/community?id=community_question&sys_id=3840f2c61b17f4d0c552c8031d4bcb97)
