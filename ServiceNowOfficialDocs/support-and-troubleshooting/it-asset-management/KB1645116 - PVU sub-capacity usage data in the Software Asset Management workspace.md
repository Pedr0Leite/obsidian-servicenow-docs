---
title: "PVU sub-capacity usage data in the Software Asset Management workspace"
aliases:
  - KB1645116
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645116
kb_number: KB1645116
last_modified: 2026-05-22
---

## PVU sub-capacity usage data in the Software Asset Management workspace

  

### Summary

 

The Top 10 products by PVU (Processor Value Unit) sub-capacity usage widget in the Software Asset Management (SAM) workspace is populated by a Performance Analytics indicator included in the Performance Analytics – Content Pack – Software Asset Management Professional. This data updates weekly based on values calculated during a scheduled job run.

### Indicator source

The indicator named **PVU usage for top 10 products** queries the SAM License Metric Result \[`samp_license_metric_result`\] table with the following conditions:

-   Software model result.Latest = true
-   License Metric = Processor Value Unit (PVU)

It calculates the sum of the **Rights consumed** field across all matching records.

### View the widget

To view the Top 10 products by PVU sub-capacity usage widget:

1.  Go to **Asset Workspace** > **License Usage**.
    
2.  Search for **IBM**.
    
3.  The summary page displays the **Top 10 products by PVU sub-capacity usage** widget.
    

### Verify dashboard data against backend records

To verify that the widget value matches backend data, query the SAM License Metric Result \[`samp_license_metric_result`\] table directly using the same conditions the indicator uses.

In your instance, go to the SAM License Metric Result table and apply the following filters:

-   Software model result.Latest = true
-   License Metric = Processor Value Unit (PVU)
-   Software Product = MQ (IBM MQ)

Check the value in the **Rights consumed** field. This value should match the number shown in the dashboard widget.
