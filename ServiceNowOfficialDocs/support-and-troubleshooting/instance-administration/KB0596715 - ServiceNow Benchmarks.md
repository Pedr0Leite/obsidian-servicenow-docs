---
title: "ServiceNow | Benchmarks"
aliases:
  - KB0596715
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596715
kb_number: KB0596715
last_modified: 2024-11-14
---

## Issue

### Content

-   [Benchmarks Overview](#overview)
-   [Using in-product Benchmarks](#using)
-   [Advantages of using Benchmarks through your instance](#advantages)
-   [In-Product Benchmarks FAQ](#faq)

### Benchmarks Overview

ServiceNow Benchmarks gives you instant visibility into your IT service management key performance indicators (KPIs) and trends as well as comparative insights relative to industry averages of your peers. You can contrast your performance with recognized industry standards or peer groups.

#### Benefits to ServiceNow Customers

1.  Real-time comparison with monthly Benchmarks reports
2.  Provide actionable recommendations and personalized guidance on achieving service excellence
3.  Quick and easy to turn on in production with no development resources or risk
4.  At no extra cost. Benchmarks is available as part of your existing ServiceNow Subscription.

### History of ServiceNow Benchmarks

**Benchmarks on Now Support (HI):** The first version of ServiceNow Benchmarks was launched in October 2016 via Now Support (HI).  **This Benchmarks is retired now**. The HI Benchmarks was primarily for Customers who were on pre-Jakarta releases 

**In-Product Benchmarks:** Starting with Jakarta release, we introduced Benchmarks as part of the product. The in-product Benchmarks brings advanced feature/functionality and more KPIs. Benchmarks offering is now getting better and more powerful with each release. See the section below "Advantages of using Benchmarks through your instance" for more details.

### Using In-Product Benchmarks starting from the Jakarta Release

-   [Benchmarks in Tokyo](https://docs.servicenow.com/bundle/tokyo-it-service-management/page/product/benchmarks/reference/r_Benchmarks.html "Benchmarks in Tokyo")
-   [Benchmarks in Utah](https://docs.servicenow.com/bundle/utah-it-service-management/page/product/benchmarks/reference/r_Benchmarks.html "Benchmarks in Utah")
-   [Benchmarks in Vancouver](https://docs.servicenow.com/bundle/vancouver-it-service-management/page/product/benchmarks/reference/r_Benchmarks.html "Benchmarks in Vancouver")
-   [Benchmarks in Washington](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/benchmarks/reference/r_Benchmarks.html "Benchmarks in Washington")

#### Opt-In from a ServiceNow Instance

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><p>•&nbsp;&nbsp;Opt-in to Benchmarks is allowed only from production instances.</p><p>•&nbsp;&nbsp;Benchmarks data and charts are not currently available for Federal customers and customers with on-premise (self-hosted) instances.</p></td></tr></tbody></table>

### Advantages of using Benchmarks through your instance

The advantages are:

-   One-click manual Opt-in to participate from any production instance. Ability to enable/disable individual KPIs to control KPI based participation.
-   Ability to change KPI definition source/condition to match your custom implementation.
-   Service Portal-based Dashboard, which makes it mobile-friendly.
-   Benchmarks Recommendation starting from Kingston release. Customers get recommendations specific to their Instance and Continuously improve service performance with recommendation-based proven practices.
-   For detailed information about the available KPIs and data information, see the product documentation topic Benchmark KPIs.
-   More ways to compare. Kingston release also provided Geo/Region and percentile based comparisons.
-   Integration with Performance Analytics for daily data collection and extensive details on KPI data.
-   Email notifications when new aggregate monthly data is available.
-   Ability to Download KPI reports.

### In-Product Benchmarks Frequently Asked Questions

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Note</strong>: For detailed information about the features and benefits of Benchmarks, and about using Benchmarks in Product, see the product documentation topic <a title="Benchmarks" href="https://docs.servicenow.com/csh?topicname=r_Benchmarks.html&amp;version=latest" target="_blank" rel="noopener noreferrer">Benchmarks</a>.</td></tr></tbody></table>

#### What Data is Used in Benchmarks Reports?

We use anonymous, aggregated, usage data to calculate global benchmark KPIs from the ServiceNow cloud. Benchmarks KPIs only use the Usage count data (e.g., the total number of Incidents) and no sensitive data (like CI's, names, IP-addresses, etc) is used. The aggregation happens at a very high levels: Global, 10 Industry Category, 5 User Size buckets and 3 Geo Region buckets, to calculate the monthly Benchmarks value. Each Industry Category/Size/Geo cohort buckets are big enough with couple hundred customers in each and we do not allow to use more than one filter on Benchmarks UI to maintain the full anonymity.

#### **Why is my opt-in to Benchmarks not working?**

##### Benchmarks opt-in is not allowed from the following instances:

-   Non-production Instance (Opt-in from non-prod Instances will fail with authentication failure message)
-   Federal customers
-   Customers with on-premise instances
-   Managed Service Providers (MSPs) and MSP Managed Instances for pre-Kingston release instance. MSP support was added from Kingston release.

#### How and What data is pulled from our ServiceNow instance?

Benchmarks uses anonymous, aggregated, usage data to calculate global benchmark KPIs from the ServiceNow  
cloud. Benchmarks KPIs only use the Usage count data (e.g., the total number of Incidents) and no sensitive data (like CI's, names, IP-addresses, etc.) is used. The aggregation happens at a very high level: Global, 10 Industry Category, 5 User Size buckets, and 3 Geo Region buckets, to calculate the monthly Benchmarks value. Each Industry Category/Size/Geo cohort buckets are big enough with couple hundred customers in each and we do not allow to use more than one filter on Benchmarks UI to maintain the full anonymity.

#### Where the data is stored and how it is secured during transit?

The Benchmarks KPI data stays on a central Benchmarks instance in aggregated and anonymized form. ServiceNow Benchmarks instance is governed by the same security requirements as are customer instances. Only designated roles within the organization have access to the organization’s Benchmarks data. A customer cannot see another customer’s Benchmarks data.  When local data gets downloaded into a customer instance, the reports are only viewed by people with Benchmarks roles (Viewer, Admin). Customers can choose who is allowed to see the Benchmarks reports within their company.

The monthly KPI count info is uploaded by participated instances using a scheduled job in the first of the month. Customers can pick and choose on which KPI they want to participate after opting in. Data is sent using secure REST API calls.

#### Do I need a Performance Analytics Premium license to see Benchmarks data?

  No. Benchmarks collection and visualization are built on the Performance Analytics complimentary offering that is available to all customers starting from Geneva release.

#### When would I see the latest month data in my instance?

  Data for the latest month is made available for customer instance download starting from the 13th of every month.

#### Can I use Benchmarks without enabling Service Portal?

  No. Service Portal is a required prerequisite in order to see the Benchmarks Dashboard.

#### Why do I see partial data on some KPIs?

  Check your Benchmarks PA collection job status.

#### I just deployed ServiceNow, can I participate in Benchmarks?

  Yes, you can opt-in to Benchmarks at any time. However, it may take 1-2 months before you can see all the data on your KPIs.

#### What if I do not want to participate in all Benchmarks KPIs?

  For information about enabling and disabling individual KPIs, see the product documentation topic [Enable a benchmark KPI](https://docs.servicenow.com/csh?topicname=t_EnableABenchKPI.html&version=latest).

#### Why can I not see Benchmarks on HI once I am opted-in from an instance?

  Benchmarks on HI is disabled once you opt-in from an instance because the in-product Benchmarks data has all the KPIs from HI benchmarks plus new KPIs and an additional feature set.

#### Industry displayed on Benchmark UI for my Instance is not correct. What can I do?

  Write an email to your ServiceNow Sales Account Representative asking to correct the Industry mapping you see on Benchmarks Dashboard UI. They should be able to correct the Industry mapping in your account record without a need to file an incident on HI.

#### Why can't I opt-in from Managed Service Providers (MSPs) and MSP Managed Instances?

  Benchmarks support for MSP managed Instances are added in Kingston. You should be able to opt-in to Benchmarks if you are on Kingston or above versions.

## Additional Information

See [Benchmarks troubleshooting](https://docs.servicenow.com/csh?topicname=c_BenchTroubleshooting.html&version=latest "Benchmarks troubleshooting") for more details.
