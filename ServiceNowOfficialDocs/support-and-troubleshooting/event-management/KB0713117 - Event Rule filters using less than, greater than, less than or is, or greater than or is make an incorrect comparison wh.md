---
title: "Event Rule filters using \"less than\", \"greater than\", \"less than or is\", or \"greater than or is\" make an incorrect comparison when the value is numeric"
aliases:
  - KB0713117
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713117
kb_number: KB0713117
last_modified: 2024-04-07
---

## Event Rule filters using "less than", "greater than", "less than or is", or "greater than or is" make an incorrect comparison when the value is numeric

  

### Issue

# Symptoms

* * *

Event Rule filters using "less than", "greater than", "less than or is", or "greater than or is" make an incorrect comparison when the value is numeric.   
  
  
Steps to Reproduce:   
\=================   
1\. Create a new event rule   
2\. Check the "Ignore events that match this filter" checkbox   
3\. Set the filter to:   
    some\_value is greater than or is 2000   
4\. Set the event rule to active and save   
5\. Create a number of events to test. 

Set the Additional information to {"some\_value":"100"} (this value will need to be updated in each additional event 150, 200, 201, 300, 1000, 2000, 2001, 50)

6\. Wait for event management to process the events. 

  
The rule ignored the events with the following values: 201, 300, 2000, 2001, 50, but only two of those events should have been ignored. 

# Release

* * *

All

# Cause

* * *

The the event filters for Additional Info performs a comparison using a string value only.  It does not work with numeric value. If you're using numeric value it will not perform the correct comparison.

# Work Around

* * *

1.The work around is to use the Event Management, Advanced Scripts

2.The "EvtMgmtCustom\_PostTransformHandler" script include could be modified to perform the evaluation.

3\. Below is an example script to ignore events with the "num\_value" < 200

\---start

(function postTransformHandler(event, origEventSysId){

    gs.log('PostTransformHandler custom script is active'); 

// Make any changes to the alert which will be created out of this Event

// Note that the Event itself is immutable, and will not be changed in the database

// event.setValue('source', 'New Source'); 

var additonal\_info = event.getValue("additional\_info");

var jsonInfo = JSON.parse(additional\_info);

var number = jsonInfo.num\_vaule;

var my\_field = jsonInfo.my\_field;

gs.log("Test " + jsonInfo.num\_value + " " + jsonInfo +" " + my\_field);

if (my\_field === 'test' && number <200)

return false;

else

return true;  

\----end

 ![](/sys_attachment.do?sys_id=a96c686edb42b450e515c22305961988)

Results

![](/sys_attachment.do?sys_id=3d6c686edb42b450e515c2230596198d)
