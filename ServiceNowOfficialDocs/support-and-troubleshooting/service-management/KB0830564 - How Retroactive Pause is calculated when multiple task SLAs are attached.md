---
title: "How Retroactive Pause is calculated when multiple task SLAs are attached"
aliases:
  - KB0830564
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830564
kb_number: KB0830564
last_modified: 2024-04-08
---

## How Retroactive Pause is calculated when multiple task SLAs are attached

  

### Issue

Consider that there are two active task SLAs (task SLA "Apple", and task SLA "Banana") concurrently attached on a task record, each having different pause conditions. Naturally, both task SLAs will have different business pause duration as a result.  
  
When a third task SLA gets attached (task SLA "Cantaloupe", with yet another different pause condition), how is the retroactive pause calculated? Is it based on task SLA Apple, Banana, or Cantaloupe?

The way to think about the retroactive pause calculation on a SLA Definition is that when a task SLA is attached it simulates that SLA Definition being attached from the retroactive start time up to "now" (current time) and checks to see if it would have been paused at any point during the historical updates (audit history of the task record). The amount of retroactive pause time is added into the newly created task SLA and instantly gives the user some extra time back on their task SLA (i.e. pushes out the Breach time like any normal pause would do).  
  
So, in the above case, the retroactive pause calculation when the "Cantaloupe" task SLA is attached will only check the pause conditions against the "Cantaloupe" SLA Definition.

### Release

All
