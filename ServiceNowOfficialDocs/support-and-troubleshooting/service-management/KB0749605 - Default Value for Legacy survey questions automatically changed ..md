---
title: "Default Value for Legacy survey questions automatically changed ."
aliases:
  - KB0749605
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749605
kb_number: KB0749605
last_modified: 2024-04-07
---

## Default Value for Legacy survey questions automatically changed .

  

### Issue

# Overview

Default Value configured for Legacy survey questions are automatically changed to 1  if "scale max" value is selected.

# Additional Information

We already have a PRB raised for this issue - PRB1329745   
  
PRB1329745- In London, the default value for a numeric scale type question in a Legacy survey is not working if "scale max" value is selected.   
  
The PRB is closed as 'Won't fix' , According to dev team-   
  
The reason we told to use new survey management is that we deprecated legacy survey long time ago and we are not currently fixing any issues.   
Since Legacy Survey is deprecated, we suggest the customers to move to new Survey Managements where none of these issues are there.   
  
Due to this survey designer does not have any field known as "set default value " . One of the reason we are not supporting is , we send survey to get the user's feedback and populating default value in the question is not useful . 

Enhancement request FTASK42571 in raised in the platform which is submitted and is on Priority P2.
