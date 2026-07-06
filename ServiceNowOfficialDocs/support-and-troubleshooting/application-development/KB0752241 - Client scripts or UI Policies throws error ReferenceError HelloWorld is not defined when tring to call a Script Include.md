---
title: "Client scripts or UI Policies throws error ReferenceError: HelloWorld is not defined when tring to call a Script Include"
aliases:
  - KB0752241
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752241
kb_number: KB0752241
last_modified: 2024-01-28
---

## Client scripts or UI Policies throws error ReferenceError: HelloWorld is not defined when tring to call a Script Include

  

### Issue

# Symptoms

Cannot instantiate a Script Include object from a client script.  Error in console displays something like:

ReferenceError: HelloWorld is not defined

Where HelloWorld is the name of the Script Include

On the Client Script or UI Policy, we may have something like

var obj = new HelloWorld();

# Release

All

# Cause

The problem is the way client code is being prepared to call the Script Include

var obj = new HelloWorld()

is not the correct way to instantiate a Script Include object

# Resolution

The correct way to call a Script Include from a Client Script, or other client side code like UI Policies, is to use a GlideAjax object like so:

var ga = new GlideAjax("HelloWorld")

# Additional Information

[https://docs.servicenow.com/csh?topicname=c\_GlideAjaxAPI.html&version=latest](https://docs.servicenow.com/csh?topicname=c_GlideAjaxAPI.html&version=latest)
