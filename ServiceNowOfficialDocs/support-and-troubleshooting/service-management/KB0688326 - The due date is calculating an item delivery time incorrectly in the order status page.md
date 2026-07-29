---
title: "The due date is calculating an item delivery time incorrectly in the order status page"
aliases:
  - KB0688326
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688326
kb_number: KB0688326
last_modified: 2024-04-07
---

## The due date is calculating an item delivery time incorrectly in the order status page

  

### Issue

# Symptoms

* * *

The due date is calculating an item delivery time incorrectly in the order status page

# Release

* * *

Jakarta Patch 8b

# Cause

* * *

The expected days are converted into hours and then those hours are divided into 8 hours per day schedule. So we will be seeing a long due date

# Resolution

* * *

The delivery time in the order status page is being populated from a custom business rule. (customization)

When I looked at the business rule, it looks like we are taking in the expected time from the custom table and since we have four records for the catalog item "JIRA", in total the expected time turns out to be 8 days.

So now when we convert the 8 days into hours (8 \*24), we get 192 hrs. So we are passing this 192 hrs expected time to the 8 - 5-weekday schedule (i.e) 8 hours per day. So when we convert the 192 hours to 8 hours per day schedule, the due date now roughly is 24 Weekdays. 

Therefore when we spread 24 weekdays from today (adding the weekends) the delivery date exceeds to just over a month. Thus we see the delivery date more than a month on the order status page.

We can get over this issue, by mentioning the hours instead of days. For example, if we want to have the expected time as 1 day, we can specify in the "expected time" as 8 hours. 

Similarly, for 3 days, we can specify the "Expected time" as 3\*8 = 24 hours, which would be 1 day (it does not matter if the hours get converted to days by this way). By this way, we can avoid the long delivery time.
