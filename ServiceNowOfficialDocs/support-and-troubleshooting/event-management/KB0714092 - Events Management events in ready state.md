---
title: "Events Management events in ready state"
aliases:
  - KB0714092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714092
kb_number: KB0714092
last_modified: 2025-09-09
---

## Events Management events in ready state

  

### Issue

Event Management events are not processed. Because such events are not processed, alerts will not be created nor incidents which are created by such alerts.

### Cause

#### 01 Scheduled job "Event Management - process event" issues such as stopped, stuck or claimed by a passive node.

It is also possible the jobs are not recreated properly after the number of jobs is updated, or after an instance upgrade.

To confirm this is the correct root cause for which the events are stuck in "ready" state:

1.  Go to "System Scheduler > Scheduled Jobs > Today's Scheduled Jobs". 
2.  Search for jobs like "Event Management - process events". 
3.  Check the "Next action" and the "Claimed by" columns. 
4.  This job out of box (OOB) should run every 5 seconds. Therefore, the "Next action" should be a few seconds from now. If "Next action" is a time in the past, then likely the job is stuck.  
    -   Jobs which the "System ID" is "ACTIVE NODES" can have the "Next action" in the past, that is ok. These are the "parent" jobs and do not actually run.
5.  If the job was claimed by a passive node, then the job is stuck as well.
6.  Lastly, if "Enable multi node event processing = true", confirm that there are (<number\_of\_jobs\_configured> \* (1 + <active\_worker\_nodes>)) jobs.  
    -   Example: an instance with 6 active worker nodes configured to have 4 jobs processing events per node would have (4 \* (1 + 6)) = 28.

**Note**: The 1 above, added to the number of active worker nodes, is because a job is also created for system "Active Nodes".

When "Enable multi node event processing = true" multiple event processing jobs are created. The events are divided into "buckets" to be processed by the jobs. If there are issues with any job, then the events of the related "bucket" are not processed. Therefore, in some cases it may happen that some events are being processed and some are not.

#### 02 Node cache not synced and one or more nodes has incorrect information regarding node count.

#### 03 Custom Business Rules and Script Includes adds extra overhead delaying event processing

As best practice, we do not recommend having Custom Business Rules on em\_event and em\_alert table. If Custom Business Rules have to be added, make sure it runs fast. Under high event load, minimal overhead added can add up to major delay to event processing even if Multi Node Event Processing and multi thread is enabled.

### Resolution

#### 01 Scheduled job "Event Management - process event" issues such as stopped, stuck or claimed by a passive node.

A simple solution is to recreate the jobs as follows:

1.  Go to "Event Management > Settings > Properties" 
2.  Find option "Number of scheduled jobs processing events" and update to a number different then the current value and save. 

The above will recreate the jobs to be claimed by an active node. The value can be reverted back afterwards.

Event management by default processes events created within the last two days (current and previous shard). Therefore, even if after the jobs are recreated successfully there may be older events which are not processed. This behavior can be modified, so that event management will process events on all shards. Setting the following property will have event management process events older than two days (process events on all shards). We recommend reverting back to the default behavior after event processing is caught up.

-   evt\_mgmt.events\_processing\_all\_shards = true

#### 02 Node cache not synced and one or more nodes has incorrect information regarding node count.

Flush the cache by typing cache.do in the navigation filter.

#### 03 Custom Business Rules and Script Includes adds extra overhead delaying event processing

-   Add timing logic in Custom Business Rules and Script includes to see how much delay is being added for each event.
-   Factor in the event rate and event processing cycle of the scheduled job and optimize the Customization as much as possible.

### Related Links

See the following document for a review of the Event Management event process flow:

-   [Event process flow](https://docs.servicenow.com/csh?topicname=c_EMEvent.html&version=latest "Event process flow")

Keep in mind, also, the following information about **Event Processing Jobs creation**:

1.  How event processing jobs are created:  
    -   By default, we create one job (that not tie to specific node), “Enable multi node event processing” is false and “Number of scheduled jobs processing events” is 1. When one of these properties changed, the business rule “Event Management - Create Scheduled Jobs” delete old jobs and create new ones. If “Enable multi node event processing” set to yes, we create jobs that tied to specific nodes. From now on, it’s the platform responsibility to delete/insert when nodes up/down/add/remove.
2.  Events processing if it’s in READY state and created within the last 2 days (event is a rolling table for 7 days and we process events only for today and yesterday) so if you have events with state READY before 2 days it will not be processed. From London we have a property that can control if to process all table shared for such cases (look in PRB PRB1235220. In Istanbul, the only way is to create all those events again (but then the order will not be correct, and you can end with wrong alert states, etc ..)
3.  Event Management has 2 options to configure how many processing jobs to run  
    -   In “Event Management” properties if “Enable multi node event processing” if false the number of jobs should be the numbers defined in “Number of scheduled jobs processing events” property.
    -   In “Event Management” properties if “Enable multi node event processing” if true, the number of jobs should be the numbers defined in “Number of scheduled jobs processing events” property multiply by the active nodes (nodes in state “online” and scheduler “any”), i.e 2 jobs defined to run and you have 2 active nodes the number of jobs should be 2\*2=4 + 2 (another job for every node with “System ID” = “All Nodes” ) = 6.
4.  In case you have events in READY state, you should check if the number of jobs correct (according to EM properties as described above). If it’s not correct try to change the number defined in “Number of scheduled jobs processing events” (for example from 2 to 3) and then back to the old number. This should fix the problem. (delete old jobs and create new ones)
5.  If you have such Situation (you create new processing jobs by changing the property) and you have events in state QUEUED within the last 2 days, you can change these events to state READ and then they should be processed.
6.  In case the number of jobs is not correct, (or job is not running at all) most of the time it’s a platform issue (jobs should be deleted/inserted by the platform when nodes goes up down, etc).

### Additional Links

-   [Incident creation delayed or incident not created from alert](https://support.servicenow.com/kb_view.do?sysparm_article=KB0864635 "Incident creation delayed or incident not created from alert")
