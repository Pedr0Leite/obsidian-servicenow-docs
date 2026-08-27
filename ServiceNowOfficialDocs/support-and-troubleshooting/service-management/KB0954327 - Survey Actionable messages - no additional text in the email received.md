---
title: "Survey Actionable messages - no additional text in the email received"
aliases:
  - KB0954327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954327
kb_number: KB0954327
last_modified: 2026-06-24
---

## Survey Actionable messages - no additional text in the email received

  

### Issue

You have implemented the actionable messages functionality in your instance. However while testing you have observed on outlook email only the actionable message is displayed. And any information like String value, Response link does not display along with the actionable message.

Basically the text in the Survey Notification does not display, ONLY the embedded survey is shown when the email is received.  
You want to know if this is working as per the actionable functionality or its an issue.

  
STEPS TO REPRODUCE/OBSERVE BEHAVIOR:  
Configure the Customer Satisfaction Survey as an actionable embedded survey.

  
Notification has message below:  
++++++++++++++++++++++  
You have been invited to take the survey: ${metric\_type}.  
  
${mail\_script:include\_survey\_actionable}  
  
To view your survey queue at any time, sign in and navigate to Self-Service > My Assessments & Surveys.  
++++++++++++++++++++++++++++++++  
  
Result: is that the email received only shows the embedded survey WITHOUT ANY TEXT.

### Release

All

### Cause

Behavior is by design.

### Resolution

  
Development team have confirmed this is the expected behaviour.  
Since we are passing AdaptiveCard data in the notification, it will only show the AdaptiveCard at the receiver's end and the rest of the html data passed will not be visible.
