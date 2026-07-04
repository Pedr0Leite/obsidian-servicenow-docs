---
title: "Calculating SLA Actual and Business values in the 2011 SLA Engine"
aliases:
  - KB0550769
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550769
kb_number: KB0550769
last_modified: 2024-08-28
---

## Calculating SLA Actual and Business values in the 2011 SLA Engine

  

### Issue

Calculating SLA Actual and Business values in the 2011 SLA Engine

  
  

# Fields to be recalculated

* * *

Task SLA records that are not completed or paused have six fields that need to be recalculated on a regular basis:

-   Actual elapsed time
-   Actual elapsed percentage
-   Actual time left
-   Business elapsed time
-   Business elapsed percentage
-   Business time left

# Issue

* * *

By default, the task\_sla records are shown in a related list on their associated task. These can appear like a list of timers, but frequently the question is asked: Why isn't my actual elapsed time moving?

The answer is because these are not timer widgets like the Time Worked field on a task record but rather must be calculated to advance. The code to do those calculations is in the SLACalculatorNG script include.

# Calling the SLACalculatorNG script include

* * *

SLACalculatorNG is called in several ways:

-   Some updates to the task will cause the 2011 SLA Engine to run. The engine calls SLACalculatorNG to recalculate some of the task\_sla records depending on the update.
    
-   The Calc SLAs on Display display business rule on the task table – If the system property _**glide.sla.calculate\_on\_display**_ is set to **true**, this business rule calls SLACalculatorNG to recalculate the task\_sla records associated to the task whenever the task form is reloaded. (This property is set to **false** by default.)
    
    This behavior is the closest the system has to making the SLA records appear to count like a timer.
    
    Note that there is a warning on the property that it can cause the form to load slowly because it waits while the calculations are done
    
    Another side effect is that all of the task\_sla records will show that they were updated by the last person to view the task.
    
-   The **Run SLA Calculation** UI Action on the task\_sla record can force the calculation on a particular record as long as it is not completed or paused. This action is useful for correcting or forcing an update to a single record.
    
-   SLA default scheduled jobs (sys\_trigger records) – The six default scheduled jobs for SLA are the default method for recalculating SLAs. They query to select the records to recalculate based on how close the records are to their planned end time (breach). The jobs run more frequently if the records being queried are closer to their breach.
    
    The jobs exclude inactive or paused records because either of these conditions will cause the values in the task\_sla records to be corrupted by the default calculations.
    
    The default scheduled jobs are:
    
    -   SLA update (breach after 30 days) - Selects records more than 30 days away from breaching.  It runs once every five days.
        
    -   SLA update (breach within 30 days) - Selects records 30 days or less away from breaching down to 1 day away from breaching.  It runs once a day.
        
    -   SLA update (breach within 1 day) – Selects records between 24 hours and 1 hour away from breaching. It runs once an hour.
        
    -   SLA update (breach within 1 hour) – Selects records between 60 minutes and 10 minutes away from breaching. It runs every ten minutes.
        
    -   SLA update (breach within 10 min) – Selects records that are 10 minutes or less from breaching. It runs to update the records every minute.
        
    -   SLA update (already breached) – If the task\_sla is still active but is already breached, this job keeps updating these records. It runs once a day.  Unless the default settings are changed, this job stops selecting the task\_sla records when the elapsed percentage reaches 1000.
