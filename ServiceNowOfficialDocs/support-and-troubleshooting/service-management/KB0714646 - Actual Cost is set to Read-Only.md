---
title: "Actual Cost is set to Read-Only"
aliases:
  - KB0714646
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714646
kb_number: KB0714646
last_modified: 2024-04-07
---

## Actual Cost is set to Read-Only

  

### Issue

# Symptoms

* * *

When viewing a Project, the Actual Cost field is set to read-only

# Release

* * *

London

# Cause

* * *

Out Of Box UI Policy "Mark Capex/Opex Cost Read Only if Cost Plan Of Capex/Opex Exists" will set this field to read-only when there is a cost plan associated to the project

# Resolution

* * *

If the requirement is to not have the Actual Cost field set to read-only, this UI Policy can be turned off. A word of warning though. There may be some negative effects of recalculation if this is turned off. As always, we suggestkeepingp the Out Of Box configuration

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=c\_ActualProjectCosts.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ActualProjectCosts.html&version=latest)
