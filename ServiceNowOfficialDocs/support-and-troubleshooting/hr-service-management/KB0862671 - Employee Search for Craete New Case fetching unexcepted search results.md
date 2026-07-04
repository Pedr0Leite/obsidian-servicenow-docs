---
title: "Employee Search for \"Craete New Case\" fetching unexcepted search results"
aliases:
  - KB0862671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862671
kb_number: KB0862671
last_modified: 2025-09-22
---

## Employee Search for "Craete New Case" fetching unexcepted search results

  

### Issue

Employee Search Prompt not working as expected for "Create New Case"

### Release

Orlando Patch 7

### Cause

When searching with user-id on the employee search field, there are multiple search results which are due to the below reason.

If the same used-id number is used for different users in different fields.

### Resolution

This is an expected result and its an OOB behaviour. Example: There is a user with user-id 12345 and another user with user-id 679890. Search with user-id 12345 on the employee search field. There will be two results on the search because the second user (67890) may have user data like cost centre contains 12345 and so the search results in these two users.

There is a restriction to the search functionality using the field 'Force partial search' on the  HR Administration > Case Creation Configuration. 

### Related Links

[https://docs.servicenow.com/csh?topicname=CreateModCaseCreationConfig.html&version=latest](https://docs.servicenow.com/csh?topicname=CreateModCaseCreationConfig.html&version=latest)
