---
title: "SLA Reporting - how to handle tasks that aren't viewed regularly (where timings still need to be accurate for reports)"
aliases:
  - KB0867118
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867118
kb_number: KB0867118
last_modified: 2023-11-03
---

## SLA Reporting - how to handle tasks that aren't viewed regularly (where timings still need to be accurate for reports)

  

### Issue

The user had a scenario where they create development-related task records that are not viewed regularly. Unfortunately, this caused reports to not be accurate due to the fact that viewing the task form is what refreshes task SLA timings (per SLA system property "glide.sla.calculate\_on\_display" being set to a value of "true"). The user needed to know how to handle getting accurate timings in this case.

### Resolution

[Documentation](https://docs.servicenow.com/bundle/paris-it-service-management/page/product/service-level-management/concept/c_ScheduledJobsForSLA.html "Documentation") was provided to the user which explained all of the Scheduled Jobs shipped Out of Box (OOB) for SLAs.

Unfortunately, these OOB Scheduled Jobs did not cover the use-case of the user which was for SLA Definitions with very long durations (100+ days). In these unique cases, a new Scheduled Job with a greater date/time range would be required.

The user was counseled to review the scripts within the OOB-shipped SLA-related Scheduled Jobs, such as the below, and to create a new Scheduled Job with their needed date/time range:

```
calculate30daysSLAs();function calculate30daysSLAs() {   var start = gs.daysAgo(-30);   var end = gs.daysAgo(-365);   SLACalculatorNG.calculateSLArange(start, end);}
```

The user was also counseled to test this in a sub-Production environment for any performance-related impact (confirmed via conversation with ServiceNow SLA Developers). Any query used should be thoroughly tested first in a sub-Production environment using background scripts to ensure the right date/time range is selected.

Some consideration should also be given to SLA system property "com.snc.sla.calculation.percentage" (Actual elapsed percentage at which scheduled jobs stop refreshing Task SLA timings) to reduce redundancy.
