---
title: "Customer Satisfaction Survey notification email is not getting triggered"
aliases:
  - KB0818378
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818378
kb_number: KB0818378
last_modified: 2024-04-08
---

## Customer Satisfaction Survey notification email is not getting triggered

  

### Issue

It was reported that the Customer Satisfaction Survey is not triggering notification emails for the user once the HR cases are getting resolved. The scenario is once a HR case gets resolved the trigger condition should initiate a notification email along with a survey link for the end user to fill it for his/her feedback.

From what we have noticed is that the assessment instances have been last created till 11th Feb and all the conditions look okay for the notification email to get triggered, yet this is not happening. The survey definitions and trigger conditions are "active" but it seems the assessment instances are not getting created post 11th Feb as well.

### Cause

It was determined while investigating that the relevant trigger condition had no auto assessment business rule.

I reviewed the Trigger Condition below  
Live Chat Survey (McCain)  
https://xxxxxxxx.service-now.com/nav\_to.do?uri=asmt\_condition.do?sys\_id=73b70b10db323f00b829fe052c96193e%26sysparm\_view=survey  
  
The issue with this trigger is that it has no Auto assessment BR associated with it.  
  
It is not clear how this trigger condition had no associated Business rule.  
  
  
  

Note:

The standard Platform behavior is that when a survey trigger condition is created to trigger a survey then a Business rule "Auto Assessment business rule" is created by the system.  
There should be one 'Auto assessment business rule' BR for each trigger condition.  
Within the code of this BR it references the AssessmentCreation method which is what generates the Assessment when the trigger condition is matched.

### Resolution

  
Create a new Trigger Condition for the Survey ' Customer Satisfaction Survey'.  
Confirm that when this Trigger Condition is created that you see that an Auto Assessment Business Rule gets created.  
  
The existing Trigger condition with no Business rule should then be inactivated because without the auto assessment br it will not trigger a survey.  
  

The above resolved the issue for the customer.
