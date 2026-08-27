---
title: "How does Total cost being calculated for Entitlements?"
aliases:
  - KB2486358
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2486358
kb_number: KB2486358
last_modified: 2026-03-27
---

## How does Total cost being calculated for Entitlements?

  

The Total cost is NOT just calculated as unit cost \* purchased rights, instead it is unit cost \* purchased rights \* timeSpan.  
  

Here timeSpan is calculated based on the start date and end date and subscription period. See the below code snippet from the UI script (CalculateTotalCost):  
/sys\_ui\_script.do?sys\_id=e23df8f5e70b0300ab270558d2f6a93b  
  
var value = unitCost \* purchasedRights;  
var inputStartDate = getDateFromFormat(g\_form.getValue('start\_date'), g\_user\_date\_format);  
var inputEndDate = getDateFromFormat(g\_form.getValue('end\_date'), g\_user\_date\_format);  
var timeSpan = this.getTimeSpan(inputStartDate, inputEndDate, g\_form.getValue('subscription\_period'));  
value \*= timeSpan;  
.  
.  
.  
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
  

Refer:  
[https://www.servicenow.com/docs/csh?topicname=software-entitlement-fields.html&version=latest](https://www.servicenow.com/docs/csh?topicname=software-entitlement-fields.html&version=latest)

  
Below examples for easier calculation:  
  
Unit cost: 50  
Purchased rights: 100  
Subscription period: Monthly  
Start date: 2023-01-01  
End date: 2024-12-31  
  
The above timespan is exactly for 2 years  
Total cost = \[ unit price \* purchased rights \* timeSpan \]  
i.e. Total cost = 50 \* 100 \* 24 months = 120,000.00  
  
If Subscription period: Annually, then:  
i.e. Total cost = \[50 \* 12\] \* 100 \* 2 years = 120,000.00  
  
If Subscription period: Quarterly, then:  
i.e. Total cost = \[50 \* 12/4\] \* 100 \* 8 quarters = 120,000.00  
  
If Subscription period: Entire Subscription Period, then:  
i.e. Total cost = \[50 \* 24\] \* 100 \* 1 = 120,000.00  
  
But if you want to use Subscription Period as "Annually" when the timestamp is 39 months for example. This is not how it is designed.  
  
You are providing 39 months as a timeSpan and expecting that Annually should calculate the Unit Cost for 3 years and 3 months, which is not feasible.  
  
If you have 39 months, then provide Subscription Period as either "Monthly" or "Entire Subscription Period" to get exact Total Cost value. And opt for Annually when you want to calculate yearly. ex 12, 24, 36 months  
  
In the example,  
Start Date: 22/06/2024  
End Date: 21/09/2027  
  
Which is exactly 39 months.  
  
So go with:  
Subscription Period as "Monthly" and Unit Cost as "21.84". --> Total Cost will be $2,342,340.00  
Subscription Period as "Entire Subscription Period" and Unit Cost as "21.84 \* 39 = 851.76". --> Total Cost will be $2,342,340.00
