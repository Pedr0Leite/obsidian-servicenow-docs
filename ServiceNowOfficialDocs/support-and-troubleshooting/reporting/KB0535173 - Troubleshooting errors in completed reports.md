---
title: "Troubleshooting errors in completed reports"
aliases:
  - KB0535173
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535173
kb_number: KB0535173
last_modified: 2024-04-30
---

## Troubleshooting errors in completed reports

  

### Issue

Troubleshooting errors in completed reports

  
Description  

* * *

This article guides you through the process of troubleshooting errors in completed reports. It provides steps to help you eliminate common causes for your problem by verifying that the configuration of your networking is correct.

Symptoms

* * *

Symptoms may include the following:   

-   The data I expected is missing.
-   Report results are missing data.
-   Data is not displaying.
-   There are errors in a completed report.

Resolution

* * *

If your data is missing from a column during the export of a completed report, some common causes and solutions may include the following: 

1.  Go the table that you are reporting on. 
2.  Check the column to see if there are any restrictions on this column. If the user can see the data in the column, the data should show on the report. An ACL might be preventing access to this column. 
3.  Has the data changed in the column? Verify that the correct data is there. 
4.  Turn on SQL debug and verify that the search criteria is correct.
