---
title: "How to identify and resolve event processing job delays"
aliases:
  - KB0758422
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758422
kb_number: KB0758422
last_modified: 2026-04-29
---

## How to identify and resolve event processing job delays

  

### Summary

Identify and resolve delays in event processing jobs when events remain in a Ready or Queued state for an extended period, or when event processing is slow. This article explains how events are assigned to event processing scheduled jobs, how to troubleshoot when jobs are stuck or missing, and how to optimize event processing performance.

### How events are assigned to processing jobs

#### **Bucket assignment**

When events are received, each event is assigned a bucket number. This value is stored in the **bucket** field on the event record.

#### **Job distribution**

Buckets are distributed to the available event processing scheduled jobs. You can view the bucket range assigned to each job in the scheduled job record in the Schedule Item \[sys\_trigger\] table. The jobs are named "Event Management - Process events #_n_."

The bucket range is assigned to a particular job name. For example, "Event Management - Process events #1" may be assigned a range of 0–25. Each node in the cluster has the same job name.

When **Event Management** > **Properties** \> **Enable multi node event processing** is set to **Yes**, each job calculates a sub-range (in NodeloadInfo).Match.ceil(range\_size/#of nodes) based on the number of active nodes. For a four-node cluster, each "Event Management - Process events #1" job processes an exclusive sub-range of seven buckets (for example, Node 1: 0–6, Node 2: 7–13, Node 3: 14–20, Node 4: 21–24). If there are no changes in the cluster, no more than one node can process a particular bucket. 

**Note**: This design can result in unprocessed buckets if a child job is not re-created on a node, which may occur when nodes go down, restart, or are added to the cluster.

#### **Job count configuration** 

The number of event processing scheduled jobs is configured through the evt\_mgmt.event\_processor\_job\_count system property. You can also view this setting at **Event Management** > **Properties** \> **Number of scheduled jobs processing events**.

When multi-node event processing is enabled, the total number of "Event Management - Process events" jobs equals: (Number of scheduled jobs × active nodes) + Number of scheduled jobs with System ID = "ACTIVE NODES." Active nodes are nodes with a status of **Online** and scheduler set to **Any** in the Node State \[sys\_cluster\_state\] table.

#### **Event claiming** 

Events are claimed by the scheduled jobs according to their assigned buckets.

-   **Before the New York release**: When a job processed events, it first marked all events to be handled in the current run with a status of queued.<sys\_id\_of\_scheduled\_job>. This could result in stuck events if the scheduled job was no longer running on a specific node.
-   **Beginning with the New York release**: The queued status is no longer used. The "Event Management - Coordinator Job" runs every 30 seconds and verifies that all event processing jobs are running according to the configured settings. If it detects issues, it corrects the number of jobs. After the job count is corrected, all jobs waiting for the coordinator job can run.

#### **Table rotation** 

The Event \[`em_event`\] table is a rolling table configured for seven days, with the table changing every 24 hours. Event processing jobs process events that exist only in the current or previous tables (two days). Events are retained in these tables for approximately 5.5 days.

### How to identify an issue with event processing jobs

If events remain in a **Ready** or **Queued** state for an extended period, use the following steps to identify the issue:

1.  Open the record for the affected event in the Event \[em\_event\] table and note the value in the **bucket** field.
2.  Go to **System Scheduler** > **Scheduled Jobs** \> **Today Scheduled Jobs** and filter for jobs starting with "Event Management - Process events."
3.  For each job, verify the following:

-   -   **Job count:** Confirm the number of scheduled jobs matches the expected count based on the configuration described in the previous section. If a job is missing, identify the node that should have the missing job by grouping the Claimed by column and checking which node has fewer jobs than expected.
    -   **Next action:** Check the Next action column. Jobs should run every five seconds. If the next action is not within five seconds, the job may be stuck.
    -   **Claimed by:** If the job is claimed by a passive node, the job is stuck.
    -   **State:** Verify the job state is not set to **Error** or **Queued**.

### Workaround

If the number of running event processing jobs is not correct:

1.  Go to **Event Management** > **Properties** \> **Number of scheduled jobs processing events**. Change the value (for example, change from 2 to 3), then change it back to the original value. This recreates all running jobs according to the current settings.
2.  Run cache.do.
3.  Verify that the affected events begin changing their status to **Processed**.

If events remain in a Queued state and are not processed, recreate the events using a script to allow the event processing jobs to process them.

If events are in a Ready state with a creation time older than two days (meaning the jobs do not process them), set the evt\_mgmt.events\_processing\_all\_shards property to **true**. This causes event processing jobs to process events across all tables. Set the property back to **false** after all events are processed.

### Resolve slow event processing

Apply one or more of the following optimizations to improve event processing performance.

#### Disable debug logging

If the `evt_mgmt.log_debug` property is set to `true`, set it to `false`. Debug logging at this level can increase memory usage significantly.

**Note:** Leaving `evt_mgmt.log_debug` set to `true` can contribute to out-of-memory conditions. Set this property to `false` unless debug logging is actively needed for troubleshooting.

#### Optimize event rules

1.  Review and deactivate event rules that are no longer needed, or simplify their filter conditions to reduce processing complexity.
2.  Go to the Event `[em_event]` table and sort events by processing duration to identify the most resource-intensive rules.
3.  Open events with the longest processing durations and review the **Processing Notes** field to identify which rules are applied.
4.  Disable or simplify the rules identified in step 3.
5.  Set the `evt_mgmt.valid_processing_duration_of_event_rule` property to `25` or `22` to flag rules that exceed this threshold for review.

#### Optimize custom business rules

Review custom business rules on the Alert `[em_alert]` table that are not part of the base system configuration. Disable or simplify any rules that are contributing to processing delays.

#### Increase scheduled job count and enable multi-node processing

1.  Go to **Event Management > Properties > Number of scheduled jobs processing events** and increase the value — for example, from `3` to `10`, or up to `20` if needed.
2.  Go to **Event Management > Properties > Enable multi node event processing** and set the value to `Yes`.  
    **Note:** To configure more than four active nodes, disable the Event Management - Create Scheduled Jobs business rule. To configure more than ten nodes, also disable the Event Management - Validate Job Count business rule.

#### Process past events across all shards

If events from more than two days ago are not being processed because the event table is sharded, set the `evt_mgmt.events_processing_all_shards` property to `true`. This causes event processing jobs to process events across all tables. Set the property back to `false` after all events are processed.

### Event Management self-health monitoring

By default, Event Management includes a self-health monitoring feature that creates alerts when potential issues are detected. Two alerts are relevant to event processing delays:

-   Event Processing Job
-   Delay in event processing

To check for these alerts, search the Alert \[em\_alert\] table for records with the following values:

-   Source: EMSelfMonitoring
-   Description contains: "Delay in event processing:" or "Wrong Event Processing jobs count"

To verify whether self-health monitoring is enabled on your instance, go to **Event Management** > **Settings** \> **Properties** \> **Enable Event Management self-health monitoring**. 

### Related Links
