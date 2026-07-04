---
title: "Assistance copying fields from Case to Problem"
aliases:
  - KB0954335
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954335
kb_number: KB0954335
last_modified: 2024-01-27
---

## Assistance copying fields from Case to Problem

  

### Issue

Assistance copying fields from Case to Problem

### Resolution

Go to the extension point \`CSMProblemIntegrations\`. Make sure the Scope is \`sn\_cs\_sm'.  
\--Click on \`Create Implementation\` related Link  
(A script include should be created, pertaining to the Extension Point - and that artifact should have been associated now - reference the docs for the complete scenario on what happens when you click \`Create Implementation\`)  
\--Now edit as per need and save this Script Include artifact.  
\--Go ahead and create the Problem from a Case (You can do that while in Global Scope as well)  
\--The fields should be copied over now.

### Related Links

[KB0953200](https://support.servicenow.com/kb_knowledge.do?sys_id=651c2e89db56e810679499ead39619a4&sysparm_view=case)
