---
title: "Impact of Extended Tables and Business Rules on Performance Analytics Data Collection"
aliases:
  - KB0551382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551382
kb_number: KB0551382
last_modified: 2024-04-07
---

## Impact of Extended Tables and Business Rules on Performance Analytics Data Collection

  

### Issue

Impact of extended tables and business rules on Performance Analytics data collection 

Overview

* * *

When viewing a Performance Analytics scorecard or dashboard, the number of records included in the score may be different from the number of records on the **Records** tab. The difference is most visible when using Count as the **Aggregate.** The difference can be caused by extended tables and business rules.

Extended tables

* * *

A table may extend another table to inherit fields from the parent table. When a record is created on the child table, a corresponding record is created with the same sys\_id value on the parent table. For more information and a list of default child tables, see [Tables and Classes](https://docs.servicenow.com/) in the product documentation.  

Impact of before query business rules

* * *

Some before query business rules may limit access to certain tables, such as by filtering the records a user can view. For example, if you extend the Incident table, you can filter the list of Incidents to show only the parent Incident table by adding the condition sys\_class\_name = 'incident' in a before query business rule.

Data collection for Performance Analytics is designed for high performance and accesses data without running business rules. When collecting scores from a table like Incident in the above example, the business rule filtering the list of records does not run. Records from the base Incident table as well as any child tables are counted.

Viewing queries

* * *

In the data collection log (**Performance Analytics > Job Logs**) you can view the query being sent to the database. When querying an extended table, the log entry appears similar to sys\_class\_name in (‘\[EXTENSION\_TABLE\]’,’\[BASE\_TABLE\]’) where the EXTENSION\_TABLE and BASE\_TABLE are queried to retrieve the indicator score.

Creating consistent queries

* * *

To create a data collection query that is consistent with what users experience when viewing records through a list or report, add a condition to the indicator source that filters based on the sys\_class\_name of the table you are querying. In the incident example, you can add the condition **\[Task type\]\[is\]\[Incident\]** to collect only data from the Incident table and not any child tables.
