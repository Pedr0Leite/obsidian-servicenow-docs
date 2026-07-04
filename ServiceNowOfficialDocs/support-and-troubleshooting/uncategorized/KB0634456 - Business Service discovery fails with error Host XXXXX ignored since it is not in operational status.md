---
title: "Business Service discovery fails with error \"Host XXXXX ignored since it is not in operational status\""
aliases:
  - KB0634456
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634456
kb_number: KB0634456
last_modified: 2024-04-07
---

## Business Service discovery fails with error "Host XXXXX ignored since it is not in operational status"

  

### Issue

Business Service discovery fails with error "Host XXXXX ignored since it is not in operational status"

# Issue

* * *

Business Service discovery fails with error: **Host XXXXX ignored since it is not in operational status** as illustrated below:

![](sys_attachment.do?sys_id=f379e022db42b450e515c223059619a4)

# Solution

* * *

When running a discovery of the Business Service, the engine expects that the operational status of the target CI be operational. If another operational status is set, then this issue can occur. For example, if Business Service is run against the target CI below, it fails because its operational status is **DR Standby**:

![](sys_attachment.do?sys_id=0089e022db42b450e515c223059619d3)

To change this behavior and add some other valid operational statuses for the Business Service discovery, add the **sa.active\_operational\_status** property into the System properties (sys\_properties) table and fill in a comma separated list of values considered valid for service mapping discovery.
