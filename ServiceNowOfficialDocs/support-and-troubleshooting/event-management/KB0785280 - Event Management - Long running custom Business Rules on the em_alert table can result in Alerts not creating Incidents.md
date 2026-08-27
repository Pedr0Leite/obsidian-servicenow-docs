---
title: "Event Management - Long running custom Business Rules on the em_alert table can result in Alerts not creating Incidents"
aliases:
  - KB0785280
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785280
kb_number: KB0785280
last_modified: 2026-04-22
---

## Event Management - Long running custom Business Rules on the em\_alert table can result in Alerts not creating Incidents

  

### Issue

Long-running custom business rules on "**em\_alert**" table may result in Alerts not creating Incidents.

### Release

Any

### Cause

Alert Management jobs pick the alerts from the **em\_alert** table based on the "**update**" time value.

For example, if the last timestamp for the alert management rules was 11:00:00, and now the time is 11:05:00 that job will fetch all the alerts from 11:00:00 to 11:04:00 (by default its 5 seconds).

If we have a custom business rule running for the em\_alert record, that takes a very long time, a minute for example, then the business rule won' thave updated the 'update' time yet, and given that we are fetching the records by the update time, we may come across a situation where that alert on which the business rule was running may not create an incident.

### Resolution

To resolve the issue, three is a system property: **evt\_mgmt.alert\_rule\_delay**, which can be set to a higher value of e.g. 60 seconds (default: 5 sec).

This will create a 60 seconds delay in triggering the alert management job, but it should not miss any alerts.

**How to add that property:**

1.  Go to sys\_properties table
2.  Click "**New**"
3.  **Name:** evt\_mgmt.alert\_rule\_delay
4.  **Value:** 60
5.  **Type:** Integer

However, as the docs state, you should never have added a custom businss rule that runs for so long in the first place. The correct solution is instead to either do whatever you need to do some other way, or optimise the performance and runtime of the business rule as much as you can. Minimising any query result sets and optimising query conditions to use Indexed fields for example.

### Related Links

[Docs: Create an alert management rule](https://www.servicenow.com/docs/r/it-operations-management/event-management/create-alert-management-rule.html)  
"Alert management rules run 5 seconds after an alert is updated, resetting the timer if updates occur within that window. **This delay ensures remediation actions, such as incident creation, are triggered only when the issue is clear and stable, reducing duplicates and unnecessary noise**. To change the default 5-second delay, create the evt\_mgmt.alert\_rule\_delay property on the All > System Properties > All Properties and change the value. To know how to create a property, see Add a system property."  
  
[Docs: Event Management configuration preferences and Best Practices](https://www.servicenow.com/docs/r/it-operations-management/event-management/r_EMBestPractice.html)  
"Business rules  
Avoid writing business rules for event \[em\_event\] tables, as they do not run in the current default REST URL that is used for event injection.  
**Business rules that are written for alert \[em\_alert\] tables must be highly efficient or they may result in performance degradation. Instead of writing a business rule, consider whether it is more appropriate to write a job. An inefficient business rule can cause incident creation for an alert to fail and the alert impact calculation to fail.**  
Do not write async business rules for alert tables.  
Business rules must not change the Category field on event \[em\_event\] tables."
