---
title: "Filtering in a List view and then creating a new record is applying the filter to the new record being created."
aliases:
  - KB0818388
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818388
kb_number: KB0818388
last_modified: 2025-04-17
---

## Filtering in a List view and then creating a new record is applying the filter to the new record being created.

  

### Issue

Filtering in a List view and then creating a new record is applying the filter to the new record being created.

Could you please identify, why we have such behavior with that UI Action.  
  
Steps to Reproduce :  
1\. Navigate to List of Incidents  
2\. Filter with "State = Closed" Or "State = Cancelled".  
3\. Once Filtered List of Incidents are shown, Click on "New" on the Banner.  
4\. Then u will be able to find the state as Closed even for a Newly Creating Incident.  
Once the Incident is Submitted, all the fields are Greyed Out as the state is in Closed.  
This is where No conditions for SLA are satisfied. We don't have any issue on SLA front.  
  
This issue is reproducible in Sub Prod Instances.

### Cause

  
This is a standard platform feature. The field value participating in filter condition is passed to the "new" form as well. When there are multiple values then platform seems to pick the first value in the list.

### Resolution

  
As per above, the behavior is by design.  
  
Workarounds:  
1\. You can create a dictionary attribute - "ignore\_filter\_on\_new=true" for that particular field (eg, state), which is retaining the value from the existing filter.  
  
  
![](/sys_attachment.do?sys_id=ea8f94688709e69057288519dabb3502)  
Go to the sys\_dictionary record of that field, click on Advanced view > Go to "Attributes" related list > Click on New > Enter as above screenshot > Submit.

  
OR

  
2\. You can try changing the filter condition on "State" from "is" to "contains".  
  
I tested this and it works. I used "is one of" operation.  
(see attached screenshots)  
  
  

![](sys_attachment.do?sys_id=302fd0288709e69057288519dabb35e6)
