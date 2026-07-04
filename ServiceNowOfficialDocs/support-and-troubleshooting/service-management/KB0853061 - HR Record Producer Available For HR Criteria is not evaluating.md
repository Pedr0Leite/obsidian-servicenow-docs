---
title: "HR Record Producer \"Available For\" HR Criteria is not evaluating"
aliases:
  - KB0853061
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853061
kb_number: KB0853061
last_modified: 2025-12-01
---

## HR Record Producer "Available For" HR Criteria is not evaluating

  

### Issue

The customer was finding that for user "Tony Stark", even though on their Record Producer "HR Reporting" they had configured restrictive "Available For" criteria which should block Tony from seeing the Record Producer, he was still able to see it in the Portal. The customer wanted to know why this was.

### Resolution

As HR Criteria is an extension of Service Catalog criteria, system property "glide.sc.use\_user\_criteria" was checked to ensure that it was "true". Unfortunately, it was set to "false", meaning that the evaluation of the "Available For" was effectively "turned off" until the property was set to "true".  
  
Once the property was set to "true", the behavior was resolved and the User Criteria evaluated perfectly.
