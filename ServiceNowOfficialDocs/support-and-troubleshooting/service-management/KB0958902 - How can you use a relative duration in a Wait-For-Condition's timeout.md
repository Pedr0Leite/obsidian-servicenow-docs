---
title: "How can you use a relative duration in a Wait-For-Condition's timeout?"
aliases:
  - KB0958902
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958902
kb_number: KB0958902
last_modified: 2025-01-02
---

## How can you use a relative duration in a Wait-For-Condition's timeout?

  

### Summary

In Flow Designer's Wait-For-Condition you can set a timeout. Sometimes you need to make this duration relative to something else? For example, you want to move forward if a certain date is reached. How do you do this?

### Instructions

It's not a date field, it's a duration field. You need to treat it as such. For example, if you have a date field you want to wait until, the following code should work:  
  
var sgd1 = new GlideDate();  
sgd1.getDisplayValueInternal();  
var duration= GlideDate.subtract(sgd1, fd\_data.trigger.current.u\_test\_date);  
  
return duration;  
  
So we get the current date (sgd1), the date we should wait until (fd\_data.trigger.current.u\_test\_date) and we subtract. If you check the flow execution, look for the execution data. The duration should look as follows:  
  
1 Day 12 Hours 18 Minutes
