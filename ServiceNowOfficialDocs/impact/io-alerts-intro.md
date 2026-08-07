---
title: Alerts in Instance Observer
description: ServiceNow Instance Observer provides a comprehensive set of alerts designed to monitor platform health, performance, and user experience. These alerts are categorized for easy consumption and actionability.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/io-alerts-intro.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
keywords: [Alerts in Instance Observer]
breadcrumb: [Monitoring instance health with Instance Observer, Platform Health, Using Impact, Impact]
tags:
  - impact
  - type-concept
---

# Alerts in Instance Observer

ServiceNow Instance Observer provides a comprehensive set of alerts designed to monitor [[platform-health-idi|platform health]], [[instance-observer-performance|performance]], and [[user-experience-insights|user experience]]. These alerts are categorized for easy consumption and actionability.

-   **Transactions**

    Monitors application transactions for anomalies, spikes, or degradations in performance such as:

    -   Transaction Decrease: Detects a drop in total transaction volume
    -   Transaction Decrease Node: Identifies transaction volume drop per node
    -   Transaction Increase: Flags unexpected transaction surges
    -   Transaction Increase Node: Highlights node-level transaction spikes
    -   Response Time: Triggers when system-wide response time increases
    -   Response Time Node: Flags nodes with degraded response times
    -   Database Response Time: Monitors database-level latency impacting transactions
    -   Slow Queries Per Second: Identifies the volume of slow database queries affecting responsiveness
-   **Node health \(CPU, memory, or garbage collection\)**

    Tracks node infrastructure health to avoid bottlenecks or failures:

    -   Node CPU time: High CPU usage alert for a node
    -   Node memory: Monitors memory consumption patterns
    -   Node garbage collection time: Tracks JVM GC delays
    -   Load balancer container CPU utilization: Flags CPU overload on LB containers
    -   Load balancer container memory utilization: Detects memory exhaustion on LB containers
-   **Database performance and health**

    Covers critical database indicators to verify query health and data reliability:

    -   Database host health CPU: High CPU on primary DB host
    -   Shards host health CPU: Resource issues on shard hosts
    -   Read replica host health \(CPU\): Read-replica CPU anomalies
    -   [[io-standby-replica-lag|Standby replication lag]]: Lag in standby DB replication
    -   InnoDB row lock: Frequency of row lock waits
    -   Primary database growth: Flags abnormal growth in primary DB
    -   Database table growth: Specific table-level growth indicators
-   **Inbound and outbound email**

    Promotes timely delivery and ingestion of email-based communications:

    -   Outbound email: Delays or failures in outbound email processing
    -   Inbound email: Issues in ingesting incoming emails
-   **Scheduler and job execution**

    Helps detect issues in the job execution life cycle:

    -   Scheduler stuck: Scheduler not progressing or blocked
    -   Long-running jobs: Jobs exceeding typical run time
    -   Specific long-running jobs: Custom job monitoring
    -   Thread running: Threads running unusually long or in high volume
-   **Session and user activity**

    Tracks user login behavior across instance and nodes:

    -   User session logged in – Instance: Log in activity across instance
    -   User session logged in – Node: Node-wise session metrics
-   **Event queue and semaphore management**

    Critical for debugging platform event handling and job execution throttling:

    -   Default semaphore mean: Semaphore wait time trends
    -   Default semaphore QDepth: Depth of queued semaphore requests
    -   Integrated semaphore: Monitors integrated semaphore contention
    -   Event queue check: Tracks backlog in event queues
    -   Specific queue for events: Custom event queue monitoring
    -   High priority event queue: Monitors mission-critical event queues
    -   ECC queue: External communication channel backlog alerts
-   **Asynchronous Messaging Bus \(AMB\)**

    Internal messaging bus observability for real-time app behavior:

    -   AMB send queue depth: Size of outgoing message queue
    -   AMB send in use: Utilization of AMB sending capacity
-   **Historical or list data volume**

    Monitors growth of historical or list data that can [[impact-landing-page|impact]] performance:

    History list length: Flags excessive record count in history tables.

-   **Application host health**

    Monitors health at the application layer:

    Application host health CPU: Application-tier CPU overload alerts.

-   **AI/ML or intelligent alerting**

    Includes alerts generated via AI/ML-based behavior analysis:

    Auriga Intelligent: AI-driven anomaly or pattern detection alerts.


-   **[[io-alerts|Key alerts – activation and notifications]]**  
Use the Instance Observer Key Alerts Activation functionality for flexibility to set alerts with historical thresholds from four week increments specific to your business needs and configure who on your team receives notifications.
-   **[[manage-io-alerts|Manage Instance Observer alerts]]**  
Act on Instance Observer \(IO\) threshold alerts directly from the notification.
-   **[[io-app-monitor-alert-card|Set an alert to monitor the average response time of applications]]**  
Set an alert to monitor the application performance when the average response time of applications that run on an instance exceeds the configured threshold.
-   **[[io-alerts-guided-cust|Track instance performance with the top six timely alerts – Guided users]]**  
Use the Instance Observer alerting feature to receive notifications on the performance of your instance. Monitor the alerts that are system driven.
-   **[[io-alerts-popular-total-adv-cust|Use popular alerts to receive notifications – Advanced and Total users]]**  
Get started with the popular alerts that are most widely used to receive notifications about your instance performance if you’re new to the Instance Observer \(IO\) alerting system. The most popular alerts appear on the first page of your Configure Alerts page.
-   **[[i-o-notifications|Instance Observer Notifications]]**  
Notifications for alerts and other system activity are displayed on the Instance Observer banner.
-   **[[io-long-pending-jobs|Configure long pending jobs alert by job priority]]**  
Get notifications when jobs that are pending exceed your defined overdue thresholds by configuring the **Long Pending Jobs** alert. Set up conditions by job priority to take action on groups of jobs—such as all discovery jobs or system cleanup jobs—in one go, rather than managing them individually.
-   **[[io-receive-notification-customer-conf-webhook|Configure IO alert notifications for a ServiceNow instance]]**  
Set up a basic integration between Instance Observer \(IO\) and ServiceNow to route IO alert notifications to a ServiceNow instance.
-   **[[io-receive-notification-third-party|Configure IO alert notifications for a third-party application]]**  
Set up a basic integration between Instance Observer \(IO\) and third-party integrations to route IO alert notifications to an external system in addition to emails and SMS.
-   **[[custom-payload-help-guide-impact|Custom payload in alerts integration]]**  
Instance Observer integrations enable you to define and manage custom JSON request payload for ServiceNow and third-party integrations.

**Parent Topic:**[[io-overview|Monitoring instance health with Instance Observer]]

## Related

- [[io-alerts|Key alerts – activation and notifications]]
- [[manage-io-alerts|Manage Instance Observer alerts]]
- [[io-app-monitor-alert-card|Set an alert to monitor the average response time of applications]]
- [[io-alerts-guided-cust|Track instance performance with the top six timely alerts – Guided users]]
- [[io-alerts-popular-total-adv-cust|Use popular alerts to receive notifications – Advanced and Total users]]
- [[i-o-notifications|Instance Observer Notifications]]
- [[io-long-pending-jobs|Configure long pending jobs alert by job priority]]
- [[io-receive-notification-customer-conf-webhook|Configure IO alert notifications for a ServiceNow instance]]
- [[io-receive-notification-third-party|Configure IO alert notifications for a third-party application]]
- [[custom-payload-help-guide-impact|Custom payload in alerts integration]]
- [[io-overview|Monitoring instance health with Instance Observer]]
- [[platform-health-idi|Platform Health]]
- [[instance-observer-performance|Performance]]
- [[user-experience-insights|User Experience]]
- [[io-standby-replica-lag|Standby replication Lag]]
- [[impact-landing-page|Impact]]
