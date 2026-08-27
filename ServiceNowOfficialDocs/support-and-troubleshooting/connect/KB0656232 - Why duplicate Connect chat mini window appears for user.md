---
title: "Why duplicate Connect chat mini window appears for user?"
aliases:
  - KB0656232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656232
kb_number: KB0656232
last_modified: 2024-04-07
---

## Why duplicate Connect chat mini window appears for user?

  

### Issue

Why duplicate Connect chat mini window appears for user?

  
  

# Overview

* * *

Connect mini window for same task record appears many times for a user. For example, mini window is appears for incident record INC000001 for more than once.

# How To 

* * *

1.  Log on to affected instance
2.  Impersonate affected user
3.  Open the connect mini window via clicking on the connect overlay at the top right corner

Chat window appears multiple times for the same task record.

#### Observations: 

-   When a user follows a task record, a live\_group\_profile record would be created for it.
-   When another user follows the same task record, existing live\_group\_profile record should be updated instead of creating a new one.

# Cause

* * *

Duplicate live\_group\_profile records causing multiple chat mini window appear for the users who are all following the task record.

# Solution

* * *

Delete the duplicate live\_group\_profile record of the task record and it should resolve the issue with multiple connect mini window.

On out of the box, duplicate live\_group\_profile records never created, most of the time, it is caused by the customization. When you run into similar issue, please review the custom business rules which creates a live\_group\_profile record.
