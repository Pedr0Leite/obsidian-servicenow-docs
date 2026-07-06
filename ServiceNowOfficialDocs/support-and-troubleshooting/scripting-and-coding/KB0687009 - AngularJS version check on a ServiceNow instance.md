---
title: "AngularJS version check on a ServiceNow instance"
aliases:
  - KB0687009
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687009
kb_number: KB0687009
last_modified: 2026-06-17
---

## AngularJS version check on a ServiceNow instance

  

### Issue

 

# Description

* * *

How to find out what version of AngularJS is running on your ServiceNow instance

# Procedure

* * *

1.  Open your web browser and open your ServiceNow instance.
2.  Open the web browser's Developer Tools\*
3.  Click the Console tab.
4.  Clear the Console.
5.  Run the following command: _angular.version.full_

The result is the version of AngularJS running on your ServiceNow instance.

# Applicable Versions

* * *

All

# Additional Information

* * *

TypeScript requires Node.js support. There are no plans to include Node.js servers as part of the ServiceNow platform.

* * *

\* For Chrome on Mac: ⌘ + Shift + C - on Windows/Linux: Ctrl + Shift + C.

Firefox on Mac: ⌘ + Option(Alt) + K - on Windows/Linux: Ctrl + Shift + K

### Release

Any

### Resolution

N/A
