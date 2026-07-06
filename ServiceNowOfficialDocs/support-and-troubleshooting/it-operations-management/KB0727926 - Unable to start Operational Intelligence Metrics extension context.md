---
title: "Unable to start \"Operational Intelligence Metrics\" extension context"
aliases:
  - KB0727926
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727926
kb_number: KB0727926
last_modified: 2024-04-07
---

## Unable to start "Operational Intelligence Metrics" extension context

  

### Issue

# Symptoms

* * *

Extension Context "Operational Intelligence Metrics" is not starting due to error

"Failed to start pipeline, java.lang.ExceptionInInitializerError"

The Extension Context can be found from module "Mid Server" -> "Extension Context" tab

"Operational Intelligence Metrics" will show down.

 ![](/sys_attachment.do?sys_id=c07ae466db42b450e515c223059619ba)

# Release

* * *

London and above

# Cause

* * *

Files in 'h2' folder corrupted. The h2 folder located in <MID\_SERVER\_INSTALL\_PATH>/agent/work/h2/

# Resolution

* * *

Delete files in folder <MID\_SERVER\_INSTALL\_PATH>/agent/work/h2/. You can backup the files before delete.
