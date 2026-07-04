---
title: "'Task' and 'Trigger ID' fields are empty on the survey instance"
aliases:
  - KB0724450
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724450
kb_number: KB0724450
last_modified: 2024-04-07
---

## 'Task' and 'Trigger ID' fields are empty on the survey instance

  

### Issue

# The 'Task' and 'Trigger ID' fields on a Survey Instance \[asmt\_assessment\_instance\] record are empty.

### Release

All releases.

### Cause

If the survey instance is not created from a Trigger Condition, then the Task and Trigger ID fields would be empty.

For these surveys, the Task number is not displayed on the top of the survey when the survey is opened by the user.

### Resolution

Create surveys using a trigger condition.

### Related Links

Please see below community thread related to this topic:

[Trigger ID is missing on Survey assessment instances](https://community.servicenow.com/community?id=community_question&sys_id=bb04cbe5dbd8dbc01dcaf3231f961940&anchor=answer_5ca5dba9db501fc01dcaf3231f9619e4&view_source=searchResult "Trigger ID is missing on Survey assessment instances")
