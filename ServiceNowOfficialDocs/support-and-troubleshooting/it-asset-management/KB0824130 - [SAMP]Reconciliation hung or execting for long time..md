---
title: "[SAMP]Reconciliation hung or execting for long time."
aliases:
  - KB0824130
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824130
kb_number: KB0824130
last_modified: 2024-11-14
---

## \[SAMP\]Reconciliation hung or execting for long time.

  

When Running SAM reconciliation either for all publishers or just Microsoft, the reconciliation is getting hung up on the Microsoft suites and taking hours to process. All other items finish in seconds. 

**Technical Details**:

1.  SAMPSuiteEngine uses DMToSM to cache the software models for a discovery model. However, getCollateralSuiteParents corrupts the cache by updating the array returned from \_getSoftwareModelsFromDiscModel
2.  Also, when looping over cmdb\_m2m\_suite\_model, SampAggregate should be used instead of SampRecord when getting the parent suite models

**Cause**: 

1.  The root issue is with the suite engine cache (DMToSM) being corrupted resulting in thousands of extra queries being executed. More granular is that hundreds of extra queries are executed for each install resulting in the suite engine taking ~5 seconds to process each install. So 5 sec \* 7000 installs ~ 10 hours.

**Troubleshooting**:

1.  Check the sys\_trigger table and could not find "SAM - Software License Reconciliation" job executing on the worker thread
2.  [Kill](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/platform-performance/task/t_ViewAndKillAnActiveTransaction.html "Kill") the Job for a quick resolution
