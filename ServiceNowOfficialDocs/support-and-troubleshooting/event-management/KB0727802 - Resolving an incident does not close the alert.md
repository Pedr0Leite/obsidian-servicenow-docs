---
title: "Resolving an incident does not close the alert"
aliases:
  - KB0727802
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727802
kb_number: KB0727802
last_modified: 2025-01-03
---

## Resolving an incident does not close the alert

  

### Issue

# Overview

* * *

We have an OOB scheduled job "Event Management - create/resolved incidents by alerts".

This job is responsible for calling the script includes that are responsible for checking the evt\_mgmt.incident\_closes\_alert sys property.

If the property is set but the alert still does not close when the incident is resolved/closed, see how it works below to potentially resolve your issue. 

# Incident to Alert Closure

* * *

Alert closure is controlled by this script include: 

https://\[INSTANCE\_NAME\].service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=c9c24f6453b003000238ddeeff7b128a

You will see that in line 27 after the join condition it checks to see if the incident's state field has a value of 6 or 7.   
This field is not to be confused with the incident\_state field. 

You will need to be sure that when the incident is resolved/closed the value of the 'state' field is 6 or 7. If you have customized this choice field then you will need to make sure to make the condition on the script to match you customization or change the value of choice of the state field to match the logic in the script include. 

# Example

* * *

If you look at the XML of the incident record after resolution/closure, you will see the "state" field still holds some value. Which may not be 6 or 7, which is what we expect. Not to be confused with incident\_state field. 

  
<incident\_state>{SOME\_VALUE}</incident\_state>   
<state>{SOME\_VALUE}</state>
