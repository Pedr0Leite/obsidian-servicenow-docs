---
title: "Resolve AWS price sheet download failures caused by insufficient MID Server memory in Cloud Cost Management"
aliases:
  - KB2635169
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2635169
kb_number: KB2635169
last_modified: 2026-05-21
---

## Resolve AWS price sheet download failures caused by insufficient MID Server memory in Cloud Cost Management

  

### Issue

Resolve AWS price sheet download failures in Cloud Cost Management (CCM). Failures occur across multiple regions and produce one or more of the following errors:

-   "Error retrieving price sheet data from AWS"
-   "Price sheet download for ap-southeast-1 timed out. Max duration is 2 hours"
-   "java.lang.OutOfMemoryError: GC overhead limit exceeded"

**Review the failure**

Before applying the resolution, confirm the root cause by reviewing the execution and API request records:

1.  Open the Cloud Integration Core PS Execution \[sn\_cld\_intg\_core\_ps\_execution\] table and locate the relevant failed execution.
2.  Open the Cloud Integration Core API Request \[sn\_cld\_intg\_core\_api\_request\] table and filter by the execution failure to find the API call at the time of the failure.
3.  Locate the failed action — for example, GetPriceSheet — then open the related list and review the Request Error record on the Cloud Integration Core API Request Error \[sn\_cld\_intg\_core\_api\_request\_error\] table to find the exact error message.

**MID Server capability requirements**

The MID Server must be configured with the correct supported applications and capabilities for Cloud Cost Management. The minimum JVM heap size is 4 GB.

Set Supported Applications and Capabilities as follows:

Supported Applications ==> Cloud Actions

Capabilities ==> The ALL setting includes all required applications and capabilities. Alternatively, specify the following settings:

Note: You can specify the following settings for any number of MID Servers. If you specify multiple MID Servers, Discovery, billing data download operations, and actions recommended by Cloud Cost Management are assigned to one of the MID Servers at random.

Option 1: To use this MID Server only for AWS, specify both of the following values: Cloud Actions AWS

Option 2: To use this MID Server for all providers, specify the following values: Cloud Actions AWS Azure

### Release

All CCM plugin versions

### Cause

AWS price sheet download failures are caused by insufficient JVM heap size on the MID Server. When JVM memory is configured below the recommended minimum of 4 GB (or 8 GB for larger environments), the MID Server cannot handle the download process, resulting in timeouts and out-of-memory errors.  

### Resolution

Verify that the MID Server JVM heap size is set to a minimum of 4 GB. For environments with high data volumes, set the JVM heap size to 8 GB. See the Related Links section for MID Server memory configuration steps.

Verify that the MID Server Supported Applications and Capabilities are configured for Cloud Cost Management. Refer to the MID Server capability requirements in the Issue section above for the required settings.

### Related Links

-   [MID Server memory and configuration requirements for Cloud Cost Management](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/cloud-insights/reference/aws-midserver-config-cloudin.html#d27904e116)
-   [Quick start guide to Cloud Cost Management](https://www.servicenow.com/community/cloud-cost-management-blog/quick-start-guide-to-cloud-cost-management-your-essential/ba-p/3075620)
-   [Cloud Cost Management setup video](https://youtu.be/gv5yEBr8oTg?si=IF4nFQVu6B4IFkZV)
