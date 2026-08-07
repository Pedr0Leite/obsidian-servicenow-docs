---
title: "Service Mapping Discovery fails to start or initialize"
aliases:
  - KB0783641
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783641
kb_number: KB0783641
last_modified: 2025-07-29
---

## Service Mapping Discovery fails to start or initialize

  

### Issue

When you select Run Discovery on a Service Map, the "Starting discovery" message appears briefly and then disappears. The discovery process does not begin.

### Release

Any supported release 

### Cause

Service Mapping checks the sa\_endpoint\_status table to count active discovery jobs before starting new ones. Discovery will not start if the number of running jobs exceeds the limit set by:

-   The sa.max\_concurrent\_service\_discovery\_tasks system property (if configured)
-   100 jobs (the default limit when the property is not set)

This limit prevents system performance issues.

### Resolution

This issue may be caused by a large map that's being discovered.

To resolve the issue, follow these steps:

Check active discovery jobs.

1.  Go to **Service Mapping** > **Services** \> **Application Services.**
2.  Filter results by Discovery Status not equal to Done.
3.  Review which services are currently being discovered.
4.  Check the sa\_endpoint\_status table for records not in a **Completed** state.

Optimize large service maps.

-   Review large maps and mark unnecessary connections as **boundary** to exclude them from discovery.
-   See the documentation, [Remove CIs not belonging to application services](https://docs.servicenow.com/csh?topicname=remove-cis-not-belonging-business-services.html&version=latest "Remove CIs not belonging to application services")

**Additional resolution options**

-   Halt discovery on large maps that are currently running.
-   Change service discovery to run during off-peak hours.
-   Increase the concurrent task limit. To do this:
    -   Create or update the sa.max\_concurrent\_service\_discovery\_tasks system property and set it to the expected value.
    -   Default is 100. Increasing this will have an impact on performance.
-   Optimize batch processing. To do this:
    -   Create or update the sa.rediscovery.batch\_size system property to 150.
    -   Default is 100. This makes Mapping Discovery faster but sacrifices some in performance.
