---
title: "How total cost is calculated for Entitlement"
aliases:
  - KB1212555
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1212555
kb_number: KB1212555
last_modified: 2025-09-30
---

## How total cost is calculated for Entitlement

  

### Summary

How total cost is calculated for Entitlement

### Facts

-   Total cost for the entitlement is calculated based on Unit cost \* purchased rights \* timespan
-   Entitlements with start & end date values will have a different calculation than Entitlements without start & end date values.

This code snippet will show how timeSpan is calculated:

if (subscriptioPeriod === 'annually') {  
startDate = this.\_addTimeSpan(startDate, yearDiff, 0);  
leftDays = this.\_subtractDays(startDate, endDate);  
timeSpan = yearDiff + leftDays / 365;  
} else if (subscriptioPeriod === 'quarterly') {  
startDate = this.\_addTimeSpan(startDate, yearDiff, leftQuarter \* 3);  
leftDays = this.\_subtractDays(startDate, endDate);  
timeSpan = totalQuarter + leftDays / 91;  
} else if (subscriptioPeriod === 'monthly') {  
var daysInStartMonth = this.\_getDaysInMonth(startDate);  
startDate = this.\_addTimeSpan(startDate, yearDiff, monthDiff);  
leftDays = this.\_subtractDays(startDate, endDate);  
timeSpan = yearDiff \* 12 + monthDiff + leftDays / daysInStartMonth;  
  
} else { // Entire subscription period  
timeSpan = 1;  
}

### Release

All

### Instructions

All calculations are done in "UI script" : CalculateTotalCost  
  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_ui\_script.do?sys\_id=e23df8f5e70b0300ab270558d2f6a93b
