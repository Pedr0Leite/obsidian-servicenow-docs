---
title: Overview of Instance Observer metrics
description: Instance Observer \(IO\) metrics are real-time and historical telemetry data points used to monitor, triage, and troubleshoot ServiceNow instance performance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/instance-observer-ovr-metric.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Instance Observer reference, Monitoring instance health with Instance Observer, Platform Health, Using Impact, Impact]
tags:
  - impact
  - type-concept
---

# Overview of Instance Observer metrics

Instance Observer \(IO\) metrics are real-time and historical telemetry data points used to monitor, triage, and troubleshoot ServiceNow instance [[instance-observer-performance|performance]].

The key metrics include transaction response time, semaphore usage, database growth, and node health, allowing administrators to identify slow jobs and optimize system health. Moreover, the metrics are designed to [[io-help|help]] administrators identify and fix performance issues.

-   **[[i-o-reports|Instance Observer reports overview]]**  
Reports in Instance Observer offer insights into the health of the instances, tracks database growth, and encryption status. The reports help you to analyze trends, and to schedule, download, and share these reports.
-   **[[addl-inf-io-anomaly|Anomaly insights]]**  
The reference topic gives additional information for anomaly charts.
-   **[[io-feature-availability|Feature availability based on package]]**  
The table outlines the access permissions for Performance [[io-analytics|Analytics]] features across production and sub production instances.
-   **[[auriga-intelligent-report|Auriga Intelligent Alert report]]**  
Auriga Intelligent Alert is an advanced multivariate machine learning \(ML\) model that learns from historical issues on your instance to provide real-time insight. Auriga monitors your performance metrics to deliver notifications of noteworthy events or deviations from anticipated data patterns.
-   **[[io-core-performance-metrics|Transaction or response metrics]]**  
The metrics provide a performance snapshot of classic UI transactions within the ServiceNow AI Platform®.
-   **[[io-database-performance-metrics|Database performance metrics]]**  
The metrics provide the database performance snapshot within the ServiceNow AI Platform®.
-   **[[io-semaphores-performance-metrics|Semaphores performance metrics]]**  
The metrics provide the key performance indicators calculated at the instance level for the selected duration.
-   **[[io-events-performance-metrics|Event queues performance metrics]]**  
The metrics provide the event performance snapshot within the ServiceNow AI Platform®.
-   **[[io-ecc-queue-perf-metrics|ECC Queue performance metrics]]**  
The metrics provide the ECC Queue performance snapshot within the ServiceNow AI Platform®.
-   **[[io-emails-performance-metrics|Email performance metrics]]**  
The metrics provide the Email performance snapshot within the ServiceNow AI Platform®.
-   **[[io-schedulers-perf-metrics|Scheduler performance metrics]]**  
The metrics provide the Schedulers performance snapshot within the ServiceNow AI Platform®.
-   **[[io-job-details-perf-metrics|Job details performance metrics]]**  
The metrics provide the job details performance snapshot within the ServiceNow AI Platform®.
-   **[[io-node-health-perf-metrics|Node health performance metrics]]**  
The metrics provide the node health performance snapshot within the ServiceNow AI Platform®.
-   **[[io-host-health-perf-metrics|Host health performance metrics]]**  
The metrics provide the host health performance snapshot within the ServiceNow AI Platform®.
-   **[[io-standby-replica-lag|Standby replication Lag]]**  
A read replica is a copy of the primary DB that reflects changes to the primary in almost real time, in normal circumstances. The lag represents the database server of the instance that is behind in seconds.
-   **[[io-pool-replica-lag|Pool Replication Lag]]**  
Pool replication lag is the number of seconds that a Standby database or a read replica database lags behind the primary database.
-   **[[io-chat-details|Chat details performance metrics]]**  
For the operations team to get the insights of current load across main components of AWA channel infrastructure like queues and agents, and to monitor load during events of chat spikes.
-   **[[io-cluster-details|Cluster details performance metrics]]**  
The metrics provide the cluster details and Encryption status snapshot within the ServiceNow AI Platform®.
-   **[[io-load-balancer|Load balancer performance metrics]]**  
The metrics provide the load balancer performance snapshot within the ServiceNow AI Platform®.
-   **[[io-user-info-metrics|User information metrics]]**  
The metrics provide the user information performance snapshot within the ServiceNow AI Platform®.
-   **[[instance-observer-metrics|Instance Data Replication]]**  
The Instance Data Replication \(IDR\) copies data updates from one instance, called the producer instance, to one or more other instances called the consumer instances.

**Parent Topic:**[[instance-observer-reference|Instance Observer reference]]

**Related topics**  


[Roles installed with Instance Observer]()

## Related

- [[i-o-reports|Instance Observer reports overview]]
- [[addl-inf-io-anomaly|Anomaly insights]]
- [[io-feature-availability|Feature availability based on package]]
- [[auriga-intelligent-report|Auriga Intelligent Alert report]]
- [[io-core-performance-metrics|Transaction or response metrics]]
- [[io-database-performance-metrics|Database performance metrics]]
- [[io-semaphores-performance-metrics|Semaphores performance metrics]]
- [[io-events-performance-metrics|Event queues performance metrics]]
- [[io-ecc-queue-perf-metrics|ECC Queue performance metrics]]
- [[io-emails-performance-metrics|Email performance metrics]]
- [[io-schedulers-perf-metrics|Scheduler performance metrics]]
- [[io-job-details-perf-metrics|Job details performance metrics]]
- [[io-node-health-perf-metrics|Node health performance metrics]]
- [[io-host-health-perf-metrics|Host health performance metrics]]
- [[io-standby-replica-lag|Standby replication Lag]]
- [[io-pool-replica-lag|Pool Replication Lag]]
- [[io-chat-details|Chat details performance metrics]]
- [[io-cluster-details|Cluster details performance metrics]]
- [[io-load-balancer|Load balancer performance metrics]]
- [[io-user-info-metrics|User information metrics]]
- [[instance-observer-metrics|Instance Data Replication]]
- [[instance-observer-reference|Instance Observer reference]]
- [[instance-observer-performance|Performance]]
- [[io-help|Help]]
- [[io-analytics|Analytics]]
