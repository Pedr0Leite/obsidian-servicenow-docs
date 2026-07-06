---
title: "How can I run Automated Test Framework (ATF) on forms in a different view?"
aliases:
  - KB0687495
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687495
kb_number: KB0687495
last_modified: 2025-04-10
---

## How can I run Automated Test Framework (ATF) on forms in a different view?

  

### Issue

  
  

# Description

* * *

The Automated Test Framework (ATF) allows the user to create and automate tests for their ServiceNow instance. This article is for users that are looking to utilize multiple ATF form views.

Procedure

* * *

-   When creating a new test record, there will be a field called View. 
-   The user can manually select other views, but the user must have access to the specified view in order to utilize it.
-   If the selected view is invalid (incorrect spelling, insufficient privileges, etc.), it will reset to the default view.
-   For an individual test, only one view is available at a time. Users have the option to open the form in a different view, but the user must create additional tests for each individual view that they wish to utilize concurrently. 

# Applicable Versions

* * *

Jakarta+
