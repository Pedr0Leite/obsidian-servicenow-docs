---
title: "Can a \"Web service access only\" user allow this user to connect to the instance ?"
aliases:
  - KB0792532
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792532
kb_number: KB0792532
last_modified: 2024-04-08
---

## Can a "Web service access only" user allow this user to connect to the instance ?

  

### Issue

When a user is used only for technical purpose and API access to ServiceNow it shouldn't be allowed to be used as an end user.

Expected results and actual results: User shouldn't be allowed to connect ot the instance pages. The user used for only technical purposes is able to sign in to the instance if a plugin is not correctly set up, see more information below.

### Release

All releases

### Cause

If the instance does not have "non-interactive sessions" plugins installed, then it is technically possible for the web service user to login.

  
Here is how to set up "non-interactive sessions" plugins:

STEPS:

  
\- Adds a column Web Service Access Only \[web\_service\_access\_only\] to the User \[sys\_user\] table.  
\- Changes all existing users to be interactive users (web\_service\_access\_only=false).  
\- Updates the User form to display the Web Service Access Only \[web\_service\_access\_only\] field by default.  
  

Note: If the **sys\_user** table of the customer instance has the **web\_service\_access\_only** column already and the behaviour still stands. Then it's likely that the plugin was uninstalled.

### Resolution

Verify if the plugin 'Non-interactive Sessions' plugin is installed.  If it is not, then install it, it is best to install in a non production instance first to test.
