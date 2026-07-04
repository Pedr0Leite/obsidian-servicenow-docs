---
title: "Troubleshoot canceled discovery due to maximum concurrent invocations reached"
aliases:
  - KB0623510
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623510
kb_number: KB0623510
last_modified: 2025-07-02
---

## Troubleshoot canceled discovery due to maximum concurrent invocations reached

  

### Issue

After running several scheduled discovery tasks, subsequent tasks are canceled citing a maximum number of scheduled invocations reached. 

Canceled discovery of <schedule name>. Already at maximum number of active 'Scheduled' invocations (3) for a given schedule

### Cause

This error occurs when a discovery schedule reaches its maximum of three concurrent runs, preventing a backlog if discovery does not finish before the next invocation is scheduled to run. When this happens, subsequent scheduled invocations are canceled. 

**Note**: You can change the default value in the system properties as described in the product documentation topic [Configure Discovery properties](https://docs.servicenow.com/csh?topicname=r_DiscoveryProperties.html&version=latest).

### Resolution

To troubleshoot this error, do the following:

1\. Navigate to **Discovery > Status** and filter the following fields:

-   Schedule: <schedule name>
-   State: Active

2\. Run the filter.

A result of three active entries indicates the cause of the error. To resolve, either cancel them or investigate why they are not completing on time. 

### Related Links

[Configure Discovery properties](https://docs.servicenow.com/csh?topicname=r_DiscoveryProperties.html&version=latest)
