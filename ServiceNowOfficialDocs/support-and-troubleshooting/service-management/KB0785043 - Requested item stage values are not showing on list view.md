---
title: "Requested item stage values are not showing on list view"
aliases:
  - KB0785043
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785043
kb_number: KB0785043
last_modified: 2024-04-08
---

## Requested item stage values are not showing on list view

  

### Issue

Requested item stage values are not showing on list view when there is an flow designer attached to the item

### Cause

Stages on the flow designer are not imported/added

### Resolution

1.  For a stage field to report stages on a record-based flow, a stage field must be present on the same table as the triggering record.
2.  Import the stages to the flow designer and add them next to the actions will solve the issue.
3.  Please see the below documentation URL to know more about the configure stages and adding them to the flow designer
4.  [Configure stages and add them to flow](https://docs.servicenow.com/csh?topicname=add-stages.html&version=latest "Configure stages and add them to flow")
