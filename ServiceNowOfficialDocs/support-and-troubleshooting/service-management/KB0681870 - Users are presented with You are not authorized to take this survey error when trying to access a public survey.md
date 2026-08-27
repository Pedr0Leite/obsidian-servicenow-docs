---
title: "Users are presented with \"You are not authorized to take this survey\" error when trying to access a public survey"
aliases:
  - KB0681870
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0681870
kb_number: KB0681870
last_modified: 2026-06-08
---

## Users are presented with "You are not authorized to take this survey" error when trying to access a public survey

  

### Issue

Users are presented with "You are not authorized to take this survey" error when they try to access a public survey.

### Cause

Even though the survey is public, it is assigned to a few users. This makes the survey only available to these users.

### Resolution

As soon as you add users in "Survey Users" the survey is no longer public. It is available only for the users within that "survey users" users.  If you want to distribute the public survey URL to the users to access and take the survey, you should remove the users in "survey users."

1.  Remove the users within "survey users" related list
2.  "Remove Public Access" on the survey
3.  Re-enable public access.

### Related Links

Product documentation: [Survey users and groups](https://docs.servicenow.com/csh?topicname=c_SurveyUsersAndGroups.html&version=latest "Survey users and groups")
