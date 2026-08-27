---
title: "Error \"Error collecting for <integer> java.lang.IllegalStateException: Sparse storage format has one field, sys_id\" in Performance Analytics Data Collection job log"
aliases:
  - KB0550063
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550063
kb_number: KB0550063
last_modified: 2024-04-07
---

## Error "Error collecting for java.lang.IllegalStateException: Sparse storage format has one field, sys\_id" in Performance Analytics Data Collection job log

  

### Issue

The following error can appear in the Performance Analytics job logs:

**Sparse storage format has one field, sys\_id** 

  

Example:

  

Error collecting for 20180508 java.lang.IllegalStateException: Sparse storage format has one field, sys\_id  
at com.glide.db.meta.SparseStorage.getValue(SparseStorage.java:70)  
at com.snc.pa.dc.Row.getValue(Row.java:164)  
at com.snc.pa.dc.DataCollector.map(DataCollector.java:565)  
at com.snc.pa.dc.DataCollector.collect(DataCollector.java:355)

### Release

Any release

### Cause

This error can be caused by:

-   the fact table of the breakdown assigned to an indicator being different from the fact table from the indicator
-   the script used in an indicator referring to a table column that does not exist
-   an indicator using an aggregate combined with a column that does not exist

### Resolution

The instance localhost log will just show a stack dump, but nothing else, there is no trace of what table and field is attempted to be read. The following steps may be of help before creating an incident for SN support:

1.  View the job log in the instance localhost
2.  Search for the error message "**java.lang.IllegalStateException: Sparse storage format has one field, sys\_id**"
3.  Just after the error message, you should see a line with the field and table that can not be found "**Syntax Error or Access Rule Violation detected by database (Unknown column '<table>.<field>' in 'field list')**"
4.  Identify the first preceding row where the message contains "**Processing Indicator Source** ..."
5.  Use the indicator source mentioned, to search for associated automated indicators
6.  For each indicator verify the breakdowns and scripts used
