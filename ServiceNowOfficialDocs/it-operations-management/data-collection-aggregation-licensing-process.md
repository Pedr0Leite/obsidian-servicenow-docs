---
title: Data collection and aggregation for licensing process
description: ITOM/OT SU Licensing application counts CIs for ITOM applications and uses a daily average count for the last 90 days to produce license statistics for purchased subscription units.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/data-collection-aggregation-licensing-process.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Exploring ITOM/OT SU Licensing, ITOM/OT SU Licensing and subscriptions, IT Operations Management]
---

# Data collection and aggregation for licensing process

ITOM/OT SU Licensing application counts CIs for ITOM applications and uses a daily average count for the last 90 days to produce license statistics for purchased subscription units.

ServiceNow charges for various ITOM applications, including [[itom-visibility-landing-page|ITOM Visibility]], ITOM [[r-discovery|Discovery]], [[itom-health-landing-page|ITOM AIOps]], [[hla-landing-page|Health Log Analytics]], [[itom-cloud-accelerate-landing-page|ITOM Cloud Accelerate]], and [[itom-optimization-landing-page|ITOM Optimization]]. For specific information about the products and features covered by ITOM subscriptions, see [[itom-license-module|Subscriptions for IT Operations Management]].

The process of collecting and aggregating information for licensing purposes involves the following steps:

1.  The ITOM licensing mechanism counts the Configuration Items \(CIs\) managed by each ITOM product daily, categorizing them into licensable CI categories. For more details, see [KB0748149: ITOM Subscription Unit license calculation logic](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748149).
2.  If the same CIs are managed by different features within the same ITOM products, the CI count is adjusted to eliminate the duplication. For example, if both Discovery and [[c_ServiceMappingOverview|Service Mapping]] discover the same CIs, these CIs appear only once in the CI count. Container CIs are excluded from SU count if they have a relationship to a container image.
3.  The licensing module aggregates CI counts from ITOM applications to determine the average daily CI count for the last 90 days.
4.  The licensing module then compares the daily average CI counts for the last 90 days from ITOM applications with the licensing information in the customer contract to generate license statistics.

As a result, you can view the statistics on how your organization uses purchased subscription units.

\[Omitted image "itom-licensing-flow.png"\] Alt text: ITOM application license flow

## Related

- [[itom-license-module|itom license module]]
- [[itom-visibility-landing-page|ITOM Visibility]]
- [[r-discovery|Discovery]]
- [[itom-health-landing-page|ITOM AIOps]]
- [[hla-landing-page|Health Log Analytics]]
- [[itom-cloud-accelerate-landing-page|ITOM Cloud Accelerate]]
- [[itom-optimization-landing-page|ITOM Optimization]]
- [[c_ServiceMappingOverview|Service Mapping]]
