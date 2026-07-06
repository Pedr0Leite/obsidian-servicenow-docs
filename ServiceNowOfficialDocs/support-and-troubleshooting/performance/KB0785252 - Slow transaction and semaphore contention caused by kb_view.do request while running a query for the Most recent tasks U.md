---
title: "Slow transaction and semaphore contention caused by /kb_view.do request while running a query for the \"Most recent tasks\" UI macro."
aliases:
  - KB0785252
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785252
kb_number: KB0785252
last_modified: 2025-02-13
---

## Slow transaction and semaphore contention caused by /kb\_view.do request while running a query for the "Most recent tasks" UI macro.

  

# Symptoms

Navigating to a knowledge article that is attached to an excessive number of tasks using the kb\_view page can be slow when trying to render the the "Most recent tasks" list.

# Release

All Releases

# Environment

If you have a KB article that is associated with hundreds or thousands of tasks.

# Cause

There is an OOB UI macro on the kb\_view.do page that lists the last 10 tasks which have been associated with the current kb\_knowledge record.

UI Macro: List of tasks to which a Knowledge article has been attached

https://\_\_INSTANCE\_\_.service-now.com/sys\_ui\_macro.do?sys\_id=66f0b492ff213100a822ffffffffff9e

The UI macro is responsible for showing the "Most recent tasks" section at the bottom of the knowledge base article.

The UI macro runs the following query:

SELECT m2m\_kb\_task0.\`sys\_id\` FROM (m2m\_kb\_task m2m\_kb\_task0 LEFT JOIN task task1 ON m2m\_kb\_task0.\`task\` = task1.\`sys\_id\` ) WHERE m2m\_kb\_task0.\`kb\_knowledge\` = 'ba62f655dbea2a407c3f76fabf961912' ORDER BY task1.\`sys\_created\_on\` DESC limit 0,10;

The query that gets run to find the most recent tasks is slower for KB articles that are attached to a higher count of tasks:

# Resolution

Workaround #1

Set the glide.knowman.recent\_tasks.display system property to false to completely disable listing the tasks to which articles have been attached.

Workaround #2

Enable versioning; this may improve the query by adding filters on the kb\_knowledge.summary and kb\_knowledge.sys\_created\_on

Workaround #3

Customize the code for the UI macro and filter out the top KB articles by task count (eg., add an additional filter before the "tasks.query();" call in the UI macro to filter out these top 10 KB articles)
