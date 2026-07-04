---
title: "How to resolve high JVM memory utilization caused by Flow Designer flows"
aliases:
  - KB0960726
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960726
kb_number: KB0960726
last_modified: 2026-01-01
---

## Issue

Flow Designer flows are causing high JVM memory utilization. This issue is typically caused by flow design issues or misconfiguration, such as actions that query large numbers of records and process them in for-each loops.

## Resolution

**Identify the problematic flow**

1.  Check the Memory Heap Dump to get the flow ID.
2.  Alternatively, review the Flow Context \[sys\_flow\_context\] table and identify flows with the highest runtime.
3.  Review the identified flow for actions that query large numbers of records and process them in for-each loops.

**Optimize the flow design**

-   Refactor the flow to move the loop body into a subflow, which runs in a separate context.

**Adjust flow reporting settings**

1.  Reduce the number of iterations kept in memory by lowering the value of the com.snc.process\_flow.reporting.iteration.lastn property. The default is 50 iterations.
2.  Lower the flow reporting level by adjusting the com.snc.process\_flow.reporting.level property. Do not use TRACE level on production.
3.  Optionally, configure reporting on a per-flow or per-action basis using a Flow Execution Setting \[sys\_flow\_execution\_setting\] record.

**Note**: Flow Reporting should be turned off on production instances and enabled only on a per-flow basis. 

## Additional Information

[Flow execution details when flow reporting is turned off or on](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1113176)
