---
title: "PA Data Collection job fails with error like:  Invalid configuration. Unable to process indicator com.snc.pa.dc.InvalidConditionException: Invalid query conditions for indicator INC: Number of incidents resolved in time: taskslatable_business_percenta<=1"
aliases:
  - KB0622241
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622241
kb_number: KB0622241
last_modified: 2024-04-07
---

## PA Data Collection job fails with error like: Invalid configuration. Unable to process indicator com.snc.pa.dc.InvalidConditionException: Invalid query conditions for indicator INC: Number of incidents resolved in time: taskslatable\_business\_percenta<=1

  

### Issue

PA Data Collection job fails with error like:  Invalid configuration. Unable to process indicator com.snc.pa.dc.InvalidConditionException: Invalid query conditions for indicator INC: Number of incidents resolved in time:taskslatable\_business\_percenta<=1

Symptoms

* * *

A Performance Analytics Data Collection job fails every time it runs and the log contains an error message similar to this example:

Invalid configuration. Unable to process indicator com.snc.pa.dc.InvalidConditionException:  
 Invalid query conditions for indicator INC: Number of incidents resolved in time: taskslatable\_business\_percenta<=100^EQ  
at com.snc.pa.dc.Indicator.<init>(Indicator.java:91)  
at com.snc.pa.dc.DataCollector.loadDefinitions(DataCollector.java:646)  
at com.snc.pa.dc.DataCollector.<init>(DataCollector.java:74)  
at com.snc.pa.dc.DataCollector.<init>(DataCollector.java:78)  
at com.snc.pa.dc.DataCollectorJob.collect(DataCollectorJob.java:158)  
at com.snc.pa.dc.DataCollectorJob.collectWithMutex(DataCollectorJob.java:94)  
at com.snc.pa.dc.DataCollectorJob.execute(DataCollectorJob.java:80)  
at com.glide.schedule.JobExecutor.execute(JobExecutor.java:83)  
at com.glide.schedule.GlideScheduleWorker.executeJob(GlideScheduleWorker.java:204)  
at com.glide.schedule.GlideScheduleWorker.process(GlideScheduleWorker.java:142)  
at com.glide.schedule.GlideScheduleWorker.run(GlideScheduleWorker.java:59)

Similar errors can occur for different indicators, depending on their definition.

Cause

* * *

This issue occurs only in instances that at some point were upgraded from the Dublin release. It happens for indicators that are based on an indicator source that uses a database view as the facts table (for example, incident\_metric). During the upgrade from Dublin, condition references to columns were truncated to 30 characters. The column name used in the indicator conditions would consist of the table alias in the view definition (tasklatable in the example message) followed by an underscore and then the field name (business\_percentage in the example message). The full name was originally taskslatable\_business\_percentage but was truncated to taskslatable\_business\_percenta, which is not valid to use in a filter because the field business\_percenta does not exist.  
  

Resolution

* * *

Manually fix the conditions on the affected indicators.

1.  Navigate to **Performance Analytics** > **Indicators** > **Automated Indicators**.
    
2.  Find the indicator mentioned in the error and open it.
    
    Note that any condition affected by this issue will NOT be displayed in the form because it is not valid, although it can be seen in the raw data.
    
3.  Click the Additional Actions (hamburger) icon in the header and select **Show XML**.
    
4.  In the XML window, find the '<conditions>' tag, which shows the original conditions that were entered, including the one that causes the error.
    
    For the example message, the conditions include "**taskslatable\_business\_percenta<=100**". That condition does not appear on the form, so it needs to be re-entered.
    
5.  Go to the Additional Conditions tab and add a condition in the form by selecting the appropriate field (label) and the appropriate predicate.
    
    For the example message, for example, you would enter **\[Business elapsed percentage\] \[less than or is\] \[100\]**.
    
6.  Repeat this process for all indicators that have the error.
    
7.  Save all changes.
    
8.  Run the daily job (execute now).
    
    Confirm that it now runs successfully.
