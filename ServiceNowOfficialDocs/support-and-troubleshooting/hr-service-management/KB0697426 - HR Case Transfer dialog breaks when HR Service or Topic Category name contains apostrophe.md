---
title: "HR Case Transfer dialog breaks when HR Service or Topic Category name contains apostrophe"
aliases:
  - KB0697426
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697426
kb_number: KB0697426
last_modified: 2024-04-07
---

## HR Case Transfer dialog breaks when HR Service or Topic Category name contains apostrophe

  

### Issue

# Description

* * *

When transferring an HR Case from one HR service to another, the Transfer Case modal dialog encounters errors when:

-   The transferred to HR Service or Topic Category contains an apostrophe character (') in the name.
-   The global sys property **glide.ui.escape\_all\_script** is set to false. 

# Steps to Reproduce

* * *

1.  Log in as admin.
2.  Navigate to **sys\_properties.list**.
3.  Search and view sys property **glide.ui.escape\_all\_script.**
4.  Change the value to **false**.
5.  Log out.
6.  Log in as HR Admin.
7.  Create a new HR service or edit an existing HR service that contains an apostrophe character (') in the name.
8.  Open an active HR case and click the **Transfer Case** option in the form context menu.
9.  The Transfer Case dialog is displayed, but the Transfer Case to dropdown does not render properly, and a browser error displays (see attachments).

# Workaround

* * *

Escape services object by add prefix JS to services object in jelly.

var services = '${**JS**:servicesString}';

# Additional information

* * *

The documentation topic [Jelly escaping types](https://docs.servicenow.com/csh?topicname=r_JellyEscapingTypes.html&version=latest "Jelly escaping types") has more information about escaping types in Jelly.
