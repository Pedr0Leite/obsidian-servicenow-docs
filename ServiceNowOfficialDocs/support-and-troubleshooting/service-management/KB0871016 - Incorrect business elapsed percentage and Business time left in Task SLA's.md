---
title: "Incorrect \"business elapsed percentage\" and \"Business time left\" in Task SLA's"
aliases:
  - KB0871016
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0871016
kb_number: KB0871016
last_modified: 2023-12-29
---

## Incorrect "business elapsed percentage" and "Business time left" in Task SLA's

  

### Issue

The issue is with the Resolution Task SLA for the customer is not showing the correct "business elapsed percentage" and "Business time left" in incidents.

It is not showing the correct information while checking for the business elapsed percentage & business time left under Resolution SLA. The actual elapsed percentage looks fine.  

You expect it should run the 24\*7 schedule, which makes both business elapse time and actual elapse time same.

### Cause

It is identified that the Sla definition is using a Schedule  'CTS Schedule 24X7' that is not properly defined causing the task sla to not correctly calculate the business timings.

Hence the business time left field is set to 0 Seconds at task sla creation.

The reason the business timing fields could not be correctly calculated is because CTS Schedule 24X7  has no valid entries. 

For example, The schedule has been defined to run from 3-5th August 2020 and does not repeat. So basically it has entries for only 3 days back in 2020 and no current valid entries.

### Resolution

To resolve this issue define your Schedule correctly as a 24/7 schedule or to meet your requirement.

1\. Navigate to the relevant schedule on your prod instance and correct the values in schedule entry record.

In the 'When' field select same day value for e.g 03/08/20 to  03/08/20. Then check the box 'All day'

In the 'Repeats' field, select 'Daily'

You can verify your schedule is correctly configured as you expect by clicking the Related Link 'Show Schedule' on your Schedule record.   
This will open the calendar and show the valid span entries.

  

2\. Once you have done the above you will need to run a 'repair sla' to fix the impacted task slas.   
 For the Incidents where this issue has occurred you can run repair slas if you require to fix these.

Generally it is expected that if you have incorrectly defined slas or schedules which you modify, you need to repair slas for existing task slas to apply the changes. For new task slas which attach they will pickup the new definitions.  
The Repair Slas can be run from the Task\_sla list view which would enable you to do this for multiple slas in one go.

Note: as documented the repair feature deletes the existing task sla and recreates a new one using the audit history and latest sla definition.

### Related Links

  

Please reference the below documentation.  
[https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/service-level-management/task/t\_RepairSLAFromAList.html](https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/service-level-management/task/t_RepairSLAFromAList.html)
