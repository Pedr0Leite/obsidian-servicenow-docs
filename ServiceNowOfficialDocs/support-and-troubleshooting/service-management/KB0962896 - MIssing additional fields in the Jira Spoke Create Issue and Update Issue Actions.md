---
title: "MIssing additional fields in the Jira Spoke \"Create Issue\" and \"Update Issue\" Actions"
aliases:
  - KB0962896
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962896
kb_number: KB0962896
last_modified: 2024-04-26
---

## MIssing additional fields in the Jira Spoke "Create Issue" and "Update Issue" Actions

  

### Issue

When adding the "Create Issue " or "Update Issue" Action from the Jira Spoke to a flow it is not possible to select all the desired additional fields.

In the below, for example, The field Due Date is not available

![](sys_attachment.do?sys_id=77c0b74edbd83490d58ea345ca9619bb)

### Cause

This action uses the [Jira editmeta API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-editmeta-get "Jira editmeta API") to obtain the data

![](sys_attachment.do?sys_id=e97633c6db9c3490d58ea345ca9619b6)

This api must return the fields for then to be selectable as additional fields.

The [Jira Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-editmeta-get "Jira Documentation") states

"Returns the edit screen fields for an issue that are visible to and editable by the user."

### Resolution

In order to allow the additional fields to be populated with the desired values ensure they are visible to and editable by the user within Jira.
