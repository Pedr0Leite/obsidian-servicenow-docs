---
title: "\"Duration of Active Breached SLAs\" report on the SLA Premium dashboard shows no results"
aliases:
  - KB0855882
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855882
kb_number: KB0855882
last_modified: 2024-04-08
---

## "Duration of Active Breached SLAs" report on the SLA Premium dashboard shows no results

  

### Issue

When the user was viewing the "Duration of Active Breached SLAs" report on the SLA Premium dashboard, no results were showing. They wanted to know why this was.

### Cause

There were no matching records on the table being reported off of for the query being run against the table.

### Resolution

The "Duration of Active Breached SLAs" report on the SLA Premium dashboard is running against the "sla\_breakdown\_by\_assignment" table, and checking against three specific things:  

-   Task SLA's "Has breached" Flag = true
-   Task SLA's "Stage" value = In progress **OR** Paused
-   Task SLA's SLA Definition "Type" = SLA

If that same filter is run against the aforementioned table in the Platform view, no results return. Hence, no data will return on the report:  

-   /sla\_breakdown\_by\_assignment\_list.do?sysparm\_query=task\_sla.has\_breached%3Dtrue%5Etask\_sla.stageINin\_progress%2Cpaused%5Etask\_sla.sla.type%3DSLA&sysparm\_view=  
    

Therefore, this is the designed behavior based on the configuration of the report (albeit perhaps not the _expected_ behavior).
