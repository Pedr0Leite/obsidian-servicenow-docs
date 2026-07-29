---
title: Transaction quota properties
description: An administrator can add the following system properties to manage transaction quotas.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/platform-performance/r\_ConfigureTransactionQuotaProps.html
release: australia
product: Platform Performance
classification: platform-performance
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Platform performance, Maintain and monitor, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - performance
  - diagnostics
  - tuning
  - queries
  - type-reference
---

# Transaction quota properties

An administrator can add the following [[r_SetArchiveRuleProcessingBehavior|system properties]] to manage [[c_TransactionQuotas|transaction quotas]].

<table id="table_l2r_nx1_rp"><thead><tr><th>

Property

</th><th>

Description

</th></tr></thead><tbody><tr><td>

glide.quota.manager.heartbeat

</td><td>

The number of seconds between the start of each Quota Manager heartbeat. This value determines how often the Quota Manager checks for transactions that exceed a quota and how often it writes status in the log file.Type: Integer

 Default value: 1

 Location: Add to the \[sys\_properties\] table

</td></tr><tr><td>

glide.quota.manager.minimum\_transaction\_time

</td><td>

The minimum number of seconds a transaction must run before the Quota Manager matches it to a transaction quota. ServiceNow recommends setting this value to at least 1 second to avoid performance issues. For optimal performance, set this value to the value of your most restrictive quota. For example, if your most restrictive quota cancels transactions longer than 1 minute, set the minimum transaction time to 60 seconds.Type: Integer

 Default value: 1

 Location: Add to the \[sys\_properties\] table

</td></tr><tr><td>

glide.quota.manager.debug

</td><td>

Controls whether to display \(true\) or hide \(false\) additional debugging information related to the Quota Manager. Debugging information includes running transactions, canceled transactions, and what quotas are matched to transactions.Type: True \| False

 Default value: True

 Location: Add to the \[sys\_properties\] table

</td></tr></tbody>
</table>**Parent Topic:**[Platform performance reference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/platform-performance/platform-performance-references.md)

**Related topics**  


[[t_AddAPropertyUsingSysPropsList|Add a system property]]

## Related

- [[t_AddAPropertyUsingSysPropsList|Add a system property]]
- [[r_SetArchiveRuleProcessingBehavior|System properties]]
- [[c_TransactionQuotas|Transaction quotas]]
