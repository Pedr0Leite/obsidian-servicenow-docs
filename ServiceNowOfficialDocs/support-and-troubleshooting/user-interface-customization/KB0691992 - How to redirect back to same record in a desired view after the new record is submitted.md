---
title: "How to redirect back to same record in a desired view after the new record is submitted"
aliases:
  - KB0691992
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691992
kb_number: KB0691992
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

By default OOB there's a global "Submit" UI Action that would insert a record into a table and would usually redirect the user back to the list.

This article details the steps on how to customize this behavior so that the redirection can be controlled to redirect back to the newly submitted record as well as make it open in a desired view (i.e. Self-Service view).

# Procedure

* * *

1) Create a new "Submit" UI Action that would override the global one:

Name: My Submit Button (can be named anything)

Table: The table form where you'd like to have this behavior

Action name: sysverb\_insert (it's important that it has the same action name as the global one, otherwise, there would be two Submit UI Actions on the form).

Show insert: Checked

Form button: Checked

Condition: Whichever conditions the UI Action should be visible

Script:

action.setRedirectURL(current);  
current.insert();  
gs.include('ActionUtils');  
var au = new ActionUtils();  
au.postInsert(current);

The "action.setRedirectURL(current);" code can be updated to the following if the record needs to be redirected to a specific view:

action.setRedirectURL("<table\_name>.do?sys\_id=" + current.sys\_id + "&sysparm\_view=<view\_name>);

Replace <table\_name> with the proper table and <view\_name> with the name of the view (i.e. ess).

# Applicable Versions

* * *

All versions

# Additional Information

* * *

More information regarding UI Actions: [UI actions](https://docs.servicenow.com/csh?topicname=c_UIActions.html&version=latest "UI actions")
