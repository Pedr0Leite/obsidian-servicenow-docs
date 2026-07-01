---
title: HealthScan definitions updates: October 2024 hotfix
description: Some HealthScan definitions are deprecated or updated between releases.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/healthscan-definitions-oct-hotfix.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [HealthScan definitions, HealthScan tech KPIs, HealthScan, Impact Delivery Instance reference, Impact reference, Impact]
tags:
  - impact
  - type-reference
---

# HealthScan definitions updates: October 2024 hotfix

Some HealthScan definitions are deprecated or updated between releases.

## Updated definitions

Some HealthScan definitions have been updated for the October hotfix to improve accuracy and [[instance-observer-performance|performance]], and reduce the number of false positives to ensure more reliable and precise results.

<table id="table_fbf_t21_ldc"><thead><tr><th>

Number

</th><th>

Short description

</th><th>

Rating

</th><th>

Category

</th><th>

Update description  

</th></tr></thead><tbody><tr><td>

HSD0001372

</td><td>

Too many fields on a form

</td><td>

Recommend

</td><td>

[[user-experience-insights|User Experience]]

</td><td>

-   Set threshold to 75 fields
-   Out-of-box reporting remains as is
-   Improved display message in findings
-   Limited to a max of 1000 findings

</td></tr><tr><td>

HSD0002128

</td><td>

Same field twice on one form

</td><td>

Act

</td><td>

User Experience

</td><td>

-   Removed common out-of-boxOB views that appear to be false positives
-   Improved performance
-   Limited to a max of 1000 findings

</td></tr></tbody>
</table>**Parent Topic:**[[healthscan-definitions|HealthScan definitions]]

## Related

- [[healthscan-definitions|HealthScan definitions]]
- [[instance-observer-performance|Performance]]
- [[user-experience-insights|User Experience]]
