---
title: "Troubleshooting Performance | Resetting the Slow Pattern Logs"
aliases:
  - KB0550593
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550593
kb_number: KB0550593
last_modified: 2025-01-03
---

## Issue

This article discusses how to troubleshoot performance and resetting the Slow Query logs. The Slow Query Logs table is one of a number of Slow Pattern Metric tables.

Slow Pattern Metrics: [London product documentation](https://docs.servicenow.com/csh?topicname=slow-pattern-metrics.html&version=latest "London product documentation")

There are multiple Slow Pattern Metrics and they store aggregate metrics, grouped by different pattern methods. The aggregations are running values that are calculated since the beginning of time, unless the tables are rest at some point.

-   sys\_pattern: base table from which all Slow Pattern Metric table extend  
    -   sys\_query\_pattern: groups SQL queries by hash of anonymized query
    -   sys\_transaction\_pattern: groups transactions by URL's, referenced by syslog\_transaction table
    -   sys\_script\_pattern: groups scripts by file name (Client Scripts, Transform Scripts, Business Rules, etc.)
    -   sysevent\_pattern: groups by event name
    -   sys\_cache\_build\_pattern: groups by cache name
    -   sys\_mutex\_pattern: groups by mutex name
    -   sys\_stacktrace\_pattern: groups by stacktrace pattern, inactive by default in London

## Resolution

#### Before resetting Slow Queries log

The following can be used as a back out plan:

\[Prior to the change\] Take an XML backup of the sys\_query\_pattern table

1.  Open the **System Diagnostics > Slow Queries** module
2.  Right + click the list header and select **Export > XML**

\[After the change, if necessary\] Restore the sys\_query\_pattern records 

1.  Log into the instance as "security admin"
2.  Open the **System Diagnostics > Slow Queries** module
3.  Right + click the list header and select **Import XML**
4.  From the upload screen select the local sys\_query\_patter\_list.xml file and click **Upload**

#### Resetting All Slow Pattern Tables Via Script 

The following script could be used to set the 3 key numeric fields of all pattern logs back to 1. You could also use this script to reset any particular table by replacing "sys\_pattern" with the name of the specific pattern table you wish to reset.

var patternGR = new GlideRecord("sys\_pattern");  
patternGR.query();  
patternGR.setWorkflow(false);  
patternGR.setValue("count", 1);  
patternGR.setValue("average", 1);  
patternGR.setValue("total", 1);  
patternGR.updateMultiple();

Instead of running a script, you could achieve the same effect through the UI by following the below instructions. They only cover resetting the Slow Queries Log table, but similar procedures could be derived for each of the slow pattern tables.

#### Resetting Slow Query Pattern Table via UI

When performing an analysis of slow queries, you may need to purge the Slow Queries log. If the Slow Queries log has not been purged, then many queries come to the top of the list that may not be an issue any more – they may have already been fixed or for some other reason are no longer relevant. To reset the Slow Queries Log, do the following:

1.  Navigate to **System Diagnostics > Slow Queries**.
2.  Right click on the list header and select **Update All** (see screenshot #1 below).
3.  In the form that opens, enter the number **1** for **Total execution time**, **Frequency** and **Average duration** (see screenshot #2 below).
4.  Click **Update**.

Once you have reset the query log, new queries start to be collected using the existing patterns. The most expensive ones begin to rise to the top. It generally takes a few days before you have enough information to make a good analysis.

![](/sys_attachment.do?sys_id=2abe38a2db0ab450e515c2230596190f)

![](/sys_attachment.do?sys_id=b6be38a2db0ab450e515c2230596191f)
