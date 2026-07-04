---
title: "SLA Async Queue is not processing, and all sla_async_queue records look to have a \"SLA Async Job\" Column value as \"(empty)\""
aliases:
  - KB0953473
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953473
kb_number: KB0953473
last_modified: 2024-01-16
---

## SLA Async Queue is not processing, and all sla\_async\_queue records look to have a "SLA Async Job" Column value as "(empty)"

  

### Issue

The user shared that no task SLA records had been attaching in their instance for some time. They shared that their SLA Async Queue table had 130K+ records on it, and the number was only rising. They needed to know how to fix this as quickly as possible.

### Cause

There were several broken state = processing sla\_async\_queue records where the "SLA Async Job" column had broken references. These sla\_async\_queue records were causing the rest of the queue to get stuck, and needed to be corrected.

### Resolution

As shared above, the root of the issue was that several sla\_async\_queue records were stuck in a state of "processing" with their "SLA Async Job" column value as "(empty)". However, there is a difference between this "(empty)" value, and the majority of the other "(empty)" SLA Async Job column values.   
  
To see the difference, the sla\_async\_queue list-view was opened, the "SLA Async Job" column was added to the list-view, and the "(empty)" value was right-clicked and selected to be "Filtered Out". After doing this, the below was shown:

![](sys_attachment.do?sys_id=92bc1f9adbda6858190b1ea66896191f)

Note that the Breadcrumbs in the filter at the top left already show that SLA Async Job "(empty)" values have been filtered out. This means that those which remain having an "(empty)" value are actually broken references, which can be proved by right-clicking the "SLA Async Job" Column name and selecting "Group By SLA Async Job". Here are the results below from doing that in the user's instance:

![](sys_attachment.do?sys_id=d6bc1f9adbda6858190b1ea668961917)

As per the above, it is seen that there are six broken references that need to be corrected. What happened here is that the async processing logic created 4 sys\_trigger jobs (as this is the standard limit of SLA Async Jobs allowed at one time) to process several sla\_async\_queue records, but then those sys\_trigger records disappeared before they finished updating the sla\_async\_queue records. Hence, the "(empty)" value is shown for these records because the sys\_id is still populated, but the reference to the sys\_trigger is broken/no longer exists.

\-----

These records can be corrected by the user by taking the below steps (or, Support can create a Change Request and perform the below steps):

1\. Go to the "sys\_trigger" table and temporarily disable the "SLA Async Delegator" job by change the "Trigger type" value to "On demand"

2\. Update the sla\_async\_queue records which are in a state of "processing" to have a truly empty "SLA Async Job" field value and set the state to "ready"

3\. Re-enable the "SLA Async Delegator" sys\_trigger record by updating the "Trigger type" back to "Repeat" (this will cause it to go back to its natural state and run every 5 seconds again)

  

One last thing to note is that Support can recommend, to better assist the user, that they create (or set, if it already exists in the user's instance - by default it does not) SLA system property "com.snc.sla.async.job.limit" from the default value of '4' up to a value of '8'. This will allow the user's instance to churn through the backlog of sla\_async\_queue records much more quickly.
