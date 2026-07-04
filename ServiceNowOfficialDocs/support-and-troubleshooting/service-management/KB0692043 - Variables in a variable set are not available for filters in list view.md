---
title: "Variables in a variable set are not available for filters in list view"
aliases:
  - KB0692043
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692043
kb_number: KB0692043
last_modified: 2024-04-07
---

## Variables in a variable set are not available for filters in list view

  

### Issue

Variables from variable set not showing up in the filter 

### Release

KP3

### Cause

Read ACL was preventing the display of variable sets in the filter

### Resolution

The variable set was not visible to "itil" users as the ACL was preventing it. After adding the itil role to the "read" ACLs namely, "io\_set\_item" and "item\_option\_new\_set"  the issue was resolved.

#
