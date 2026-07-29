---
title: "Some of the variables on catalog item are not showing for itil users"
aliases:
  - KB0714463
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714463
kb_number: KB0714463
last_modified: 2024-04-07
---

## Some of the variables on catalog item are not showing for itil users

  

### Issue

Some variables on the catalog item are not showing up when the user orders a catalog item.

### Release

London

### Cause

The use of both setDisplay() and setVisible() methods for the same variable.

### Resolution

In a client script, two methods are used to hide and show the variable.

  

g\_form.setDisplay and g\_form.setVisible.

  

Both the methods perform the same functionality (hiding/showing the variable) expect that one will leave the space black and the other will allow other variables to occupy the space.

  

Undesirable behavior will be experienced if both the methods are used on the same variable.

  

Please use one of the methods to hide/show the variables to resolve the issue.

  

Please refer to this documentation for more details on g\_form methods,

[https://docs.servicenow.com/csh?topicname=c\_GlideFormAPI.html&version=latest#r\_GlideFormSetVisible\_String\_Boolean](https://docs.servicenow.com/csh?topicname=c_GlideFormAPI.html&version=latest#r_GlideFormSetVisible_String_Boolean)

  

  

The reason this undesirable behavior is experienced in London is that a new performant g\_form was introduced from Kingston version and so this undesirable behavior is seen.

#
