---
title: "ITAM: Asset – Create Asset Delayed Sync: Scheduled Job Run Frequency"
aliases:
  - KB3024352
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3024352
kb_number: KB3024352
last_modified: 2026-05-17
---

## ITAM: Asset – Create Asset Delayed Sync: Scheduled Job Run Frequency

  

### Issue

 

A request has been made to increase the run frequency of the **Asset – Create asset delayed sync** scheduled job from its default interval of 15 minutes to a shorter interval. This article explains what the job does, why the 15-minute default exists, and the performance implications of increasing the frequency.

### Symptoms

 

-   Asset records are not created immediately after a CI is inserted into the CMDB.
-   A delay of up to 15 minutes is observed between CI creation and the corresponding asset record appearing in the system.
-   Pending asset creation records accumulate in the Asset Creation Queue between scheduled job runs.
-   Users or downstream processes that depend on asset availability encounter records that are not yet present.

### Facts

 

How the Job Works

The system property `glide.create_alm_asset.async` controls whether assets are created immediately when a CI is inserted, or asynchronously via a queue:

-   **`false`** (default prior to Washington DC) — Asset is created immediately upon CI insert.
-   **`true`** — A queue record is written to the Asset Creation Queue. The _Asset – Create asset delayed sync_ scheduled job processes this queue every 15 minutes and creates the corresponding asset records.

Job status can be monitored in the `asset_job_log` table. Assets waiting to be created or in an error state can be viewed at **Asset > Administration > Asset Creation Queue**.

Why Is the Default 15 Minutes?

The 15-minute interval is an intentional design choice that balances two competing concerns:

-   **Throughput** — Batching CI inserts into a queue allows large Discovery runs to complete faster, eliminating the per-CI overhead of synchronous asset creation.
-   **System load** — A 15-minute interval ensures the job runs infrequently enough to avoid constant background thread contention on the scheduler.

### Release

All Releases

### Cause

 

When `glide.create_alm_asset.async` is set to `true`, the system deliberately defers asset creation to a batch process. The 15-minute run interval is the configured schedule for that batch job. Any perceived delay in asset availability is a direct result of this asynchronous design — assets are not created until the next scheduled job execution processes the queue.

### Resolution

 

Impact of Increasing the Run Frequency

Changing the interval to a shorter duration causes the job to run more frequently. The actual performance impact depends heavily on instance size and queue volume.

**Potential Risks**

**Increased scheduler load** — More frequent executions consume more background worker threads, competing with other scheduled jobs and system processes.

**Mid-queue-flush overlap** — On high-volume instances, a shorter interval may trigger a new job run before the previous one finishes, particularly during or after large Discovery imports.

**Diminishing returns at very short intervals** — At very short intervals, behavior approximates setting `glide.create_alm_asset.async = false`, but without the cleaner built-in handling of synchronous asset creation.

Low vs. High Volume Environments

| Environment | Expected Impact |
| --- | --- |
| **Low volume** — Small queue between runs | Negligible performance impact. Increasing frequency is generally safe. |
| **High volume** — Large Discovery imports, many CIs | Higher risk. Job overlap is possible. Monitor closely after any change. |

Recommended Steps

ServiceNow does not officially recommend changing the default 15-minute interval. Before making any change, follow these steps:

1.  **Review the Asset Creation Queue.** Navigate to **Asset > Administration > Asset Creation Queue** and check how many records are typically queued between runs. A consistently small queue indicates a shorter interval carries low risk.
2.  **Test in a non-production environment first.** Validate the new interval in a sub-production instance during a representative Discovery run before applying the change to production.
3.  **Adjust the scheduled job interval.** Navigate to **System Scheduler > Scheduled Jobs**, locate _Asset – Create asset delayed sync_, and modify the run interval to the desired frequency.
4.  **Monitor the Asset Job Log after the change.** Review the `asset_job_log` table to confirm jobs are completing cleanly and not overlapping between runs.
5.  **Consider setting `glide.create_alm_asset.async` to `false`.** If the goal is to eliminate the delay entirely, immediate synchronous asset creation may be a cleaner solution — provided the instance is not processing very large Discovery batches where queuing provides a performance benefit.

Any modification to scheduled job intervals or system properties is a custom configuration change. Validate all changes through your organization's standard change management process. ServiceNow Professional Services can assist with high-volume or complex implementations.

### Related Links

 

-   [Work with asset and CI](https://www.servicenow.com/docs/r/it-asset-management/asset-management/work-with-asset-ci.html)
-   [Asset management overview](https://docs.servicenow.com/bundle/latest/page/product/asset-management/concept/c_AssetManagement.html)
