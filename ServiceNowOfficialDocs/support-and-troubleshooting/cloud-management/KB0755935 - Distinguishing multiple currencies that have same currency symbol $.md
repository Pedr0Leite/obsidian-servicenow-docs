---
title: "Distinguishing multiple currencies that have same currency symbol \"$\""
aliases:
  - KB0755935
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755935
kb_number: KB0755935
last_modified: 2026-04-14
---

## Issue

When using multiple currencies that have the same symbol like "$", the currency dropdown list shows the same $ sign multiple times and it is difficult to distinguish whether it is  US dollar or Canadian dollar or Australian dollar, etc.

  

                                                ![](sys_attachment.do?sys_id=abfa242adb42b450e515c2230596195e)

#   

## Resolution

Update the symbol column value in Currencies \[fx\_currency\] table. Update the '$' as USD for US dollar, AUD for Australian dollar or CAD for Canadian dollar, etc.
