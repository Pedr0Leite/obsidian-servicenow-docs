---
title: "A backlog of Text Index events causing Global Search issues"
aliases:
  - KB0786040
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786040
kb_number: KB0786040
last_modified: 2026-04-07
---

## Issue

Backlog of text index events

## Resolution

To resolve this we can either

-   Delete/set to error the relevant created events so they don't get processed
-   Allow the events to process

1.  Backlog of text index events https://<INSTANCE>/sysevent\_list.do?sysparm\_query=state%3Dready%5EORstateSTARTSWITHq%5Equeue%3Dtext\_index
2.  Hourly processing (change created accordingly - to estimate when it finishes):

https://<INSTANCE>/sysevent\_list.do?sysparm\_query=state%3Dprocessed%5Equeue%3Dtext\_index%5EprocessedONLast%20hour%40javascript%3Ags.beginningOfLastHour()%40javascript%3Ags.endOfLastHour()%5Esys\_created\_onONToday%40javascript%3Ags.beginningOfToday()%40javascript%3Ags.endOfToday()
