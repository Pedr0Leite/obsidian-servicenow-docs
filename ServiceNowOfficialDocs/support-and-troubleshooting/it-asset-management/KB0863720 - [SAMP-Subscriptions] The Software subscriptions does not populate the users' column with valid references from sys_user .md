---
title: "[SAMP-Subscriptions] The Software subscriptions does not populate the users' column with valid references from sys_user table."
aliases:
  - KB0863720
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863720
kb_number: KB0863720
last_modified: 2024-10-26
---

## \[SAMP-Subscriptions\] The Software subscriptions does not populate the users' column with valid references from sys\_user table.

  

### Issue

When we run the Subscription integration profile jobs, we do get the user subscriptions along with "User principal name" and "Users" columns. The User column if the reference to sys\_user table and it will have the matching user for the User principal name. Sometimes, you might see records with no User populated.

### Release

Jakarta++

### Cause

When we run the subscriptions we get the "User principal name" which contains the emailID. We try to find a match on sys\_user table within serviceNow platform and if we find a match then we populate the user column. The below are the two cionditions it should match:

1\. User record with same EmailID

2\. User record should be Active

### Resolution

Make sure there are users with following conditins met.

1\. User record with same _**EmailID**_

2\. User record should be _**Active**_
