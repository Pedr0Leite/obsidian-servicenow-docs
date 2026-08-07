---
title: "ServiceNow application and the Leap second UTC time changes"
aliases:
  - KB0549732
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549732
kb_number: KB0549732
last_modified: 2023-07-12
---

## ServiceNow application and the Leap second UTC time changes

  

### Issue

ServiceNow application and the leap second UTC time change  
  
For fresh information about this, you can base google for "when is the next leap second".

  

This will give you information like:

Based on **current** predictions, the next **leap second** should be added on June 30, 2020.  
However, since the speed of the Earth's rotation is subject to unpredictable short-term variations, the date may still change  
  
Due to this unpredictability future leap seconds are not yet announced.  

### Release

Any version

### Cause

What is a leap second?

* * *

A leap second is a one-second time adjustment that is added to Coordinated Universal Time (UTC) in order to keep its time of day in synch with the mean solar time, or UT1.

The one-second adjustment is applied to accommodate the very minor slowing in the Earth's rotation. Since the leap second was introduced in 1972, 26 such leap seconds have been inserted.

For more information, see [https://en.wikipedia.org/wiki/Leap\_second](https://en.wikipedia.org/wiki/Leap_second).

### Resolution

Does the leap second affect ServiceNow?

* * *

The ServiceNow application obtains the time and date from the operating system. As long as the operating system does the time change successfully, the application will function properly.

There has been no reported issues with the ServiceNow platform about recent leap second changes.
