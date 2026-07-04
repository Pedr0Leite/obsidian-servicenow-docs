---
title: "Metric Instance Cleanup"
aliases:
  - KB0538882
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538882
kb_number: KB0538882
last_modified: 2025-06-25
---

## Issue

A [metric instance](https://docs.servicenow.com/csh?version=latest&topicname=c_MetricInstance.html "metric instance") is a record in the metric\_instance table. A record holds one instance of a metric.

Metric instance records get created and updated in one of two ways:

1.  If the metric is a duration, the system automatically populates the metric instance table with duration values.
2.  If the metric is calculated from a script, the script itself must populate the metric\_instance table.

### The Metric Instance table

Similar to any data stored within the system, we need to determine how long captured values for metrics are relevant to current business needs.

For example, task records and their metrics from a year ago are typically less relevant than currently active tasks and their associated metrics.

This is particularly important for metrics since **the number of metric instances captured for a single task can easily grow at a factor of 5-10 (depending on the changes that are captured)** and old data will eventually cause performance issues by:

-   consuming system resources
-   slowing down queries
-   slowing down reports

### Table cleaner

If there are no auditing requirement for the metric data, the recommended practice for the cleanup of metric\_instance table is to use Table cleanup.  
A custom table cleanup rule will need to be set up to cleanup stale metric\_instance records regularly.

### Archiving

The recommended practice for data that need to be kept for auditing or historical purposes is to use the archive application. Metrics in themselves are not the system of records for task history. Auditing keeps track of all modifications, and when they were performed on a task, doing this independently of metrics.

Since auditing cannot be reported on, the intent of metrics is to provide a reportable view of the timing of recent activities. Archiving or deleting Metric Instance does not cause loss of data or history, it only removes reportable timing information that is redundant with other data in the system. Also metrics that are a year old or older are typically much less relevant than metrics from today or last month. Therefore the recommendation is to set up a table cleaner to delete old metrics from the system, keeping the size of the metric\_instance table reasonable. This ensures that the performance of associated view and reports remains constant.

**If historical, long-term analysis is needed, either the reports that are only used as Scheduled Reports or Performance Analytics can be used to visualize trends on metrics.**

The preferred solution is to use the Performance Analytics feature, which has been optimized for storing and analyzing performance indicators over several years.  
  

## Resolution
