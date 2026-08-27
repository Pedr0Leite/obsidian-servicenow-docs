---
title: "Why business rule is not seting the priority field as expected? "
aliases:
  - KB0696710
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696710
kb_number: KB0696710
last_modified: 2024-01-28
---

## Why business rule is not seting the priority field as expected?

  

### Issue

# Symptoms

* * *

When we try to set the "Priority" field via before update / insert business rules as shown below, it doesn't work.

![](sys_attachment.do?sys_id=88eca022db82b450e515c223059619d6)

# ![](sys_attachment.do?sys_id=8ceca022db82b450e515c223059619db)

# Release

* * *

Any supported release. 

# Cause

* * *

**Priority look up definition** ("https://<instance name>/dl\_definition.do?sys\_id=302849102b031000de0aba36a3fd5631") is active on all out of the box instance by default and it will override the priority value set by the business rule. 

# Resolution

* * *

As per business use case, if the priority value needs to be set only by business rule, make sure,

-   Business rule is either **before insert/update** (should not be after insert/update as the current object will not be available).
-   **Priority look up definition** is inactive

# Additional Information

* * *

[Incident Priority and data look up rules](https://docs.servicenow.com/ "Incident Priority and data look up rules")

[Data look up and record matching](https://docs.servicenow.com/csh?topicname=c_DataLookRecMatchSupport.html&version=latest "Data look up and record matching")

[Business Rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business Rules")
