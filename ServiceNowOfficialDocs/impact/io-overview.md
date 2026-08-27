---
title: Monitoring instance health with Instance Observer
description: Instance Observer \(IO\) is an observability and performance monitoring tool that empowers you to track your instance health and performance in near real time, while also providing historical insights.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/io-overview.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Platform Health, Using Impact, Impact]
tags:
  - impact
  - type-concept
---

# Monitoring instance health with Instance Observer

Instance Observer \(IO\) is an observability and performance monitoring tool that empowers you to track your instance health and performance in near real time, while also providing historical insights.

IO helps Instance administrators, Platform Owners, and DevOps teams accelerate value and drive their desired business outcomes by increasing visibility into instance performance, helping customers push innovation with speed and confidence.

## Features and Benefits

-   **Key features**
    -   **24/7 Monitoring:** Instance performance monitoring provides awareness of issues within an instance before end users  are impacted.
    -   **24/7 Alerting:** Set up custom alerts to notify you when specific thresholds are crossed, so you can act before an issue becomes critical.
    -   **Multi-instance Availability:** Proactively visualize performance  telemetry across instances. Empowering  organizations to identify trends before  end users are impacted.
    -   **Triage:** Actionable point-in-time  instance metadata providing additional  context to instance performance and accelerating troubleshooting.
    -   **Off Instance Application:** Access to instance performance  telemetry off instance. When an  issue does arise, organizations can  access actionable data independent of  instance availability.
    -   **Reporting:** Visualize instance performance  telemetry over time and quickly generate reports to share with your business stakeholders, enabling organizations to manage instance performance faster, smarter, and better.
    -   **Analytics:** Compare metrics over time to see how performance is trending in general or to assess the before and after impacts of certain changes.

-   **Key Benefits**
    -   **24/7 availability:** Instance Observer is an off-instance, cloud-based application enabling customers to visualize instance telemetry across instances in a single application.
    -   **Improve Instance performance:** By monitoring instance performance metrics in real time, you can quickly identify and resolve issues that might be causing poor performance impacting end users.
    -   **Increase uptime:** Proactive monitoring through Instance Observer alerting you can be notified of potential issues before they cause downtime, enabling you to act before it affects your users.
    -   **Improve troubleshooting:** When issues do arise, have actionable point-in-time metadata accelerating root cause analysis and time to relief.
    -   **Remove distractions:** With near real-time data at your fingertips, you and your team can spend less time trying to find the information you need and more time driving your desired business outcomes

**Note:** Instance Observer is not available with ServiceNow® mobile, however, may be accessed with a browser on your mobile device.

## Instance Observer features

|Feature|Description|
|-------|-----------|
|[[user-configurable-dashboard|Instance Observer user configurable dashboard]]|Provides a snapshot of the overall health of your instance.|
|[[instance-observer-performance|Performance]]|Overviews Instance Health and Performance Metrics, and enables drill down into specific datasets with recommended troubleshooting.|
|[[io-availability|Availability]]|View live Instance Availability status tied to ServiceNow  monitoring— Up/Down Status|
|[[io-alerts|Key alerts – activation and notifications]]|Flexibility to set alerts with thresholds specific to your business needs, and configure who on your team receives notifications and the method.|
|[[io-analytics|Analytics]]|View comparisons for performance of key metrics over time.|
|[[io-triage|Triaged instance data]]|Point-in-time instance snapshot providing metadata to troubleshoot live issues|
|[[instance-observer-reporting|Instance performance telemetry reports]]|Quickly generate reports to download and share with your team business stakeholders.​|
|[[io-help|Help]]|Get assistance with Instance Observer tools, terminology review, how-to videos, and relevant documents.|

## Support matrix according to Impact package

Some Instance Observer reporting features vary between the [[impact-packages1|Impact packages]] that you’re subscribed to. Reference the support matrix chart or contact your account team for more information.

-   ✓ = Supported
-   X = Not supported

<table id="table_qf3_yby_hxb"><thead><tr><th>

Feature

</th><th>

Guided

</th><th>

Advanced

</th><th>

Total

</th></tr></thead><tbody><tr><td>

Instance availability \(Up/Down status\)See [Availability](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/io-availability.md) for details.

</td><td>

✓

</td><td>

✓

</td><td>

✓

</td></tr><tr><td>

Performance Visualization Charts \(KPIs\)See [Performance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/instance-observer-performance.md) for more details.

</td><td>

✓

</td><td>

✓

</td><td>

✓

</td></tr><tr><td>

ReportingSee [Instance performance telemetry reports](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/instance-observer-reporting.md) for details.

</td><td>

Selective

</td><td>

Full

</td><td>

Full

</td></tr><tr><td>

AlertsSee [[io-alerts-intro|Alerts in Instance Observer]] for details.

</td><td>

✓**Note:** Six alerts are available. For more information, see [[io-alerts-guided-cust|Track instance performance with the top six timely alerts – Guided users]].

</td><td>

✓

</td><td>

✓

</td></tr><tr><td>

AnalyticsSee [Analytics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/io-analytics.md) for details.

</td><td>

X

</td><td>

X

</td><td>

✓

</td></tr><tr><td>

[[anomalies-detection|Anomalies Detection]]

</td><td>

X

</td><td>

X

</td><td>

✓

</td></tr><tr><td>

Data retention

</td><td>

45 days

</td><td>

6 months

</td><td>

6 months

</td></tr></tbody>
</table>To access the Instance Observer page, navigate to **[[impact-landing-page|Impact]]** &gt; **Platform Health** &gt; **Monitor** &gt; **Instance Observer**.

**Note:** For more information on subscription support, see .

## Serviceability limitations

**Note:** Instance Observer is available for customers in Commercial and Government Community Cloud \(GCC\) environments. IO is currently not available in other regulated or on-premise environments.

Instance Observer is applicable or available for ServiceNow Platform instances only.

-   **[Instance Observer user configurable dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/user-configurable-dashboard.md)**  
The All Instances Summary Dashboard is the home page that provides a snapshot of the overall health of your instances. You can create your own dashboard according to your preferences for metrics that help you to analyze the health of your system in a snapshot.
-   **[Performance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/instance-observer-performance.md)**  
Monitor all your instances 24x7 in one place with near real-time metrics and alerts on performance and availability in Instance Observer. Generate various charts of overview Instance Health and Performance Metrics and drill down into specific data points with recommended troubleshooting.​
-   **[Availability](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/io-availability.md)**  
The Availability section shows instance level availability on a geographic map and instance level ServiceNow generated alerts \(limited alert types\) since the past 7 days.
-   **[Alerts in Instance Observer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/io-alerts-intro.md)**  
ServiceNow Instance Observer provides a comprehensive set of alerts designed to monitor platform health, performance, and [[user-experience-insights|user experience]]. These alerts are categorized for easy consumption and actionability.
-   **[[generative-ai-root-cause-anal|Generative AI powered Root cause analysis]]**  
Root cause analysis in Instance Observer provides automated detection and summarization of issues. It includes built-in [[root-cause-correlation|root cause correlation]] and root cause summary using a large language model \(LLM\), which helps reduce troubleshooting time, improve incident transparency, and generative AI driven root cause recommendation by analyzing similar historical incidents.
-   **[Analytics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/io-analytics.md)**  
View comparisons for performance of key metrics over time with the Impact Total package.
-   **[[io-triage-sn-instance|Triage a ServiceNow instance]]**  
Perform a triage on a ServiceNow instance to gather point-in-time telemetry data for troubleshooting using Instance Observer. The triage feature gives a summary of ongoing operations at the time of its execution.
-   **[Instance performance telemetry reports](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/instance-observer-reporting.md)**  
Quickly generate reports to download and share with your business stakeholders, making  organizations faster, smarter, and better in their  instance performance management.
-   **[Help](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/io-help.md)**  
Access release notes, how to videos, and more from the Instance Observer Help Center page.
-   **[[instance-observer-reference|Instance Observer reference]]**  
Reference topics provide information about roles installed with the Impact Instance Observer application and the key metrics that are used to monitor infrastructure health, track application performance, measure latency to understand user experience, and use historical data for capacity planning.

**Parent Topic:**[[platform-health-idi|Platform Health]]

## Related

- [[user-configurable-dashboard|Instance Observer user configurable dashboard]]
- [[instance-observer-performance|Performance]]
- [[io-availability|Availability]]
- [[io-alerts|Key alerts – activation and notifications]]
- [[io-analytics|Analytics]]
- [[io-triage|Triaged instance data]]
- [[instance-observer-reporting|Instance performance telemetry reports]]
- [[io-help|Help]]
- [[io-alerts-intro|Alerts in Instance Observer]]
- [[io-alerts-guided-cust|Track instance performance with the top six timely alerts – Guided users]]
- [[generative-ai-root-cause-anal|Generative AI powered Root cause analysis]]
- [[io-triage-sn-instance|Triage a ServiceNow instance]]
- [[instance-observer-reference|Instance Observer reference]]
- [[platform-health-idi|Platform Health]]
- [[impact-packages1|Impact Packages]]
- [[anomalies-detection|Anomalies detection]]
- [[impact-landing-page|Impact]]
- [[user-experience-insights|User Experience]]
- [[root-cause-correlation|Root cause correlation]]
