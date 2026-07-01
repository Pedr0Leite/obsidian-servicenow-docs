---
title: Configuring Now Assist Analytics
description: Configure the Now Assist Analytics dashboard to view the usage, value, and performance indicators of Now Assist.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/configuring-now-assist-analytics.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [Now Assist Analytics, configuring, GenAI, GenerativeAI, CSM, Customer Service Management]
breadcrumb: [Analyzing Now Assist performance, Exploring Now Assist Admin, Now Assist, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-concept
---

# Configuring Now Assist Analytics

Configure the [[platform-now-assist-landing|Now Assist]] Analytics dashboard to view the usage, value, and performance indicators of Now Assist.

## Configuration overview

Now Assist Analytics requires at least one Now Assist application, for example, Now Assist for Customer Service Management \(CSM\), to be installed and configured on your instance. See [[installing-now-assist-analytics|Installing Now Assist Analytics]] for more information.

The following is an optional configuration task used to map a Now Assist skill to a dashboard.

[[map-a-skill-to-a-dashboard|Map a skill to a dashboard]] to view skill usage and performance indicators.

## Domain Separation

Now Assist Analytics supports domain separation only for indicators using the following data collection jobs.

-   \[GenAI Analytics\] Daily Data Collection
-   \[GenAI Analytics\] Historical Data Collection
-   \[Now Assist Analytics\] Daily Data Collection
-   \[Now Assist Analytics\] Historical Data Collection

See [Approaches to Performance Analytics with domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/pa-domain-configurations.md) for more information on applying domain separation configuration.

**Note:** Be sure to check the Run as field in the data collection job records has a valid user.

## Related

- [[installing-now-assist-analytics|Installing Now Assist Analytics]]
- [[map-a-skill-to-a-dashboard|Map a skill to a dashboard]]
- [[platform-now-assist-landing|Now Assist]]
