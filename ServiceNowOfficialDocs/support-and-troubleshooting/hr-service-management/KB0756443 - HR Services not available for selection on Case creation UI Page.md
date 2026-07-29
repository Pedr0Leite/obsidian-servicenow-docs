---
title: "HR Services not available for selection on Case creation UI Page"
aliases:
  - KB0756443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756443
kb_number: KB0756443
last_modified: 2024-04-07
---

## HR Services not available for selection on Case creation UI Page

  

### Issue

A user with the sn\_hr\_core.case\_writer role is unable to see some options in the topic category.

### Cause

The subject user fails all read ACLs on the affected HR service table. The subject user has to be able to read the table so that the category can be selected.

### Resolution

Create a read ACL for the subject users that should be able to view the HR Service.
