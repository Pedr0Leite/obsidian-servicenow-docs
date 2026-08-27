---
title: "Cloud Insights  Billing:  Azure billing download failure with 429 error code"
aliases:
  - KB1262240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1262240
kb_number: KB1262240
last_modified: 2023-09-27
---

## Issue

Sometimes Cloud Insights Azure billing download fails due to the 429 error - "too many requests". This article would be helpful to

1\. Understand the reason for 429 error during billing download.

2\. Workaround to reduce the 429 error. 

## Resolution

**Workaround to reduce the 429 error.** 

Add \[consumption.usage\_details\_interval\_indays\] system property to handle 429 error while downloading the Azure bill. 

By default, each request downloads data for 3 days. For a month containing 30 days, there would be 20 (10 for Amortized and another 10 for Actual Cost) requests submitted to Azure. 

If the billing data volume is less on the customer environment, user can set the property to reduce the number of requests.   
   
To increase the interval for downloading Azure data per API request, follow these steps. The property change will be considered in the next billing download.

1\. Select the application Cloud Integration Azure. 

2\. Go to sys\_properties table and click the New button.  

3\. For the Suffix field, type in the property: consumption.usage\_details\_interval\_indays.   
The Name field should be populated automatically with: sn\_cld\_intg\_azure.consumption.usage\_details\_interval\_indays 

4\. For the Type field, select integer.

5\. For the Value field, type an integer value like 7 (If existing billing download gets completed in ~5hrs). Now 7 days of data will be downloaded per request. This configuration change would reduce the number of requests from 20 to 10 for a month having 30 days.

## Additional Information

**Recommendation:**

1\. Within 24hours, there should not be more than 2 billing download jobs started across all the instances for a given Azure Service Principal.

2\. If the error occurs, please wait for the time specified in the error message before triggering the billing download job again. 

    (ex: Please retry after 10 hour(s) and 23 minute(s) and 49 second(s))
