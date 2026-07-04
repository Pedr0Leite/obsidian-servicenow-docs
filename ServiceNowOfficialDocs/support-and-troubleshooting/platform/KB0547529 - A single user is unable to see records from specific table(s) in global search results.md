---
title: "A single user is unable to see records from specific table(s) in global search results"
aliases:
  - KB0547529
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547529
kb_number: KB0547529
last_modified: 2025-03-31
---

## A single user is unable to see records from specific table(s) in global search results

  

### Issue

A single user is unable to see records from specific table(s) in global search results

* * *

### Release

All releases

### Cause

The user has set text search group user preferences to restrict certain groups or tables within groups from being found.

### Resolution

If a single user is unable to see records that should be appearing from a global search, this may be because they have adjusted their search groups. Before the Jakarta release users could select specific search groups or tables within a search group to not be searched when a global search was done. It is very likely that the user has made these kinds of selections and a quick check of the user preferences will confirm that. To see if the user has any preferences which may be restricting their global search results take the following actions:

1)  Go to the sys\_user\_preference table

2)  Filter the list where the User is your affected user and the name starts with "ts.group" or name starts with "ts.table"

If you find records that are ts.group.<sys ID> or ts.table.<sys ID> where the value is false it means that the group or specific table has been restricted for that user. Here are some sample preference names:

ts.group.8c59970e0a0a0b07013feb5e0d09c952

ts.table.8c5906a90a0a0b0700f8f2a9cc9ebce0

3) Deleting these user preference records will resolve the issue.

The sys ID in the ts.group entry above refers to a record in the ts\_group table to exclude while the sys ID in the ts.table preference refers to a record in the ts\_table to exclude.
