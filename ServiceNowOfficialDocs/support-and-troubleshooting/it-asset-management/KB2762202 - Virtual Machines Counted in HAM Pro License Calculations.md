---
title: "Virtual Machines Counted in HAM Pro License Calculations"
aliases:
  - KB2762202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2762202
kb_number: KB2762202
last_modified: 2026-02-17
---

## Issue

Virtual Machines Incorrectly Included in Hardware Asset Management (HAM) Professional License Count  
  

## Resolution

Virtual machines can be excluded from HAM Professional licensing using below method

#### Use "Exclude from HAM Features" Option

1.  Navigate to the hardware asset record: Asset > Portfolios > Hardware Assets or `alm_hardware.list`
2.  Open the virtual machine asset record
3.  Check the "Exclude from HAM Features" checkbox
4.  Save the record

  
For additional reference, review the documentation: [https://www.servicenow.com/docs/r/it-asset-management/hardware-asset-management/exclude-assets.html](https://www.servicenow.com/docs/r/it-asset-management/hardware-asset-management/exclude-assets.html)

**Additional information:**  
An internal product enhancement story  has been logged with the Product team to automatically exclude virtual machines from HAM license calculations in future releases based on the `is_virtual` attribute.
