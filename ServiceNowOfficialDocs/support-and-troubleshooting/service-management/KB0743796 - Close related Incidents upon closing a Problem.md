---
title: "Close related Incidents upon closing a Problem"
aliases:
  - KB0743796
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743796
kb_number: KB0743796
last_modified: 2024-04-07
---

## Close related Incidents upon closing a Problem

  

### Issue

Related incident are not closed when the associated problem is closed.

### Release

All

### Cause

OOB business rule - "SNC - ITIL - Close Related" is deactivated.

### Resolution

Make sure to activate the OOB business rule which Closes any incidents that are related to the associated problem. Below is the name of the business rule:

-   **SNC - ITIL - Close Related:** https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=1c263220c6112275006955271bf6ba4f

### Related Links

[Once problem is set to resolved, all the associated incidents should be set to resolved](https://community.servicenow.com/community?id=community_question&sys_id=87bf14f1db702fc054250b55ca9619a8 "Once problem is set to resolved, all the associated incidents should be set to resolved") (Community)
