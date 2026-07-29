---
title: "Determining the time zone for ODBC processing"
aliases:
  - KB0538951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538951
kb_number: KB0538951
last_modified: 2024-05-19
---

## Determining the time zone for ODBC processing

  

### Issue

Determining the time zone for ODBC processing

Symptoms

* * *

-   Queried information lost
-   Error message received during processing

  
Cause

* * *

The instance and the machine that the ODBC driver is installed on may be using two different time zones, which causes a loss of queried information if the correct time is not used in the query. 

Resolution

* * *

When you are performing time/date-bounded queries, it is important to ensure that you query in accurate time zones for both the instance and the machine that hosts the ODBC driver. GlideRecord performs filtering based on the instance time zone and the ODBC client is filtered based on the Windows time zone. 

  

For example, if an instance is in Central Standard Time (CST) and the ODBC driver is installed on a machine that is in Pacific Standard Time (PST), and an incident is created on the instance at 

“2014-05-20 10:00:00”, the time that the incident was created displays in the UI as 10:00:00 for users in both time zones. However, in order to successfully query this incident by creation date and time, a user on the machine in PST must query“2014-05-20 08:00:00” instead of “2014-05-20 10:00:00."
