---
title: "Closing child Work Order task also closes parent work order"
aliases:
  - KB0721971
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721971
kb_number: KB0721971
last_modified: 2024-04-07
---

## Closing child Work Order task also closes parent work order

  

### Issue

# Symptoms

* * *

Closing child Work Order task also closes parent work order

# Release

* * *

London

# Cause

* * *

(Roll Up Changes) business rule

# Resolution

* * *

After further investigation, it seems that this behavior is expected behavior. The rolling up of states is handled by (Roll Up Changes) business rule below:  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=c4c336b747332100158b949b6c9a7150

This business rule is configured on parent (sm\_task) table and runs when a (sm\_task) record's state changes. There is logic hardcoded to rollup the state change to its parent.

If this behavior is not desired for Work Orders you may implement a Condition on this business rule similar to below to ensure this business rule does not run for (wm\_task/wm\_order) records.

Condition = current.sys\_class\_name != 'wm\_task' && current.sys\_class\_name != 'wm\_order'
