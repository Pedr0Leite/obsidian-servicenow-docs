---
title: "Custom' tab or workflow palette missing in the instance workflow editor"
aliases:
  - KB0693323
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693323
kb_number: KB0693323
last_modified: 2024-04-07
---

## 'Custom' tab or workflow palette missing in the instance workflow editor

  

### Issue

# Symptoms

* * *

'Custom' tab or workflow palette missing in the instance workflow editor

# Release

* * *

Any

# Cause

* * *

1\. Orchestration \[com.snc.runbook\_automation\] plugin is not activated.

2\. Check if there are recent clone done between the instances where the Orchestration plugin is not active in the Source instance.

# Resolution

* * *

Request plugin Orchestration \[com.snc.runbook\_automation\] activation via HI.

# Additional Information

* * *

Check on the docs.service-now.com topic '[Activate Orchestration](https://docs.servicenow.com/csh?topicname=t_ActivateOrchestration.html&version=latest "Activate Orchestration")' on how to activate the plugin.
