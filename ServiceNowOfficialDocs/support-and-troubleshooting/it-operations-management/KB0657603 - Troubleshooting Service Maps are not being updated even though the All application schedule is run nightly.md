---
title: "Troubleshooting: Service Maps are not being updated even though the All application schedule is run nightly"
aliases:
  - KB0657603
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657603
kb_number: KB0657603
last_modified: 2024-04-07
---

## Troubleshooting: Service Maps are not being updated even though the All application schedule is run nightly

  

### Issue

Service Maps not updated even though All Application Schedule is run nightly | Troubleshooting

  
  

# Issue

* * *

Several discovered services that are not updating even though we have all applications set to operational and the scheduled job all applications is active and running.

# Cause

* * *

The All application discovery will look only for CIs that are extended form the cmdb\_ci\_appl table. Therefore, Service Maps are not being updated even though the All application schedule is run nightly.

# Resolution

* * *

If the application is not extended from the cmdb\_ci\_appl table, you can create an additional Service schedule.

1.  Navigate to **Service Mapping > Discovery Schedules**.
    
2.  Click **New**.
    
3.  Select the CI type.
    
    ![](sys_attachment.do?sys_id=b2c8e06edb02b450e515c22305961947)
