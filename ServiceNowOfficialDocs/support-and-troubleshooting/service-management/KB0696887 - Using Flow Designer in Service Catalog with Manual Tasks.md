---
title: "Using Flow Designer in Service Catalog with Manual Tasks"
aliases:
  - KB0696887
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696887
kb_number: KB0696887
last_modified: 2024-04-07
---

## Using Flow Designer in Service Catalog with Manual Tasks

  

### Issue

# Symptoms

* * *

Flow designer does not have a way of scripting a wait for condition to check to see if all task (created from Flow or manually created) are completed before continuing. 

# Release

* * *

London

# Cause

* * *

Unable to script a wait for condition in Flow Designer

# Resolution

* * *

1\. Add a Look Up Records action to pull all task related to the RITM   
2\. Add the For Each flow logic to iterate through the task records   
3\. For the path of the For Each, add a Wait for Condition to wait for the task to be active false (or any other condition).   
  
One potential downfall with this solution is the Look Up Records action will only run once. If a task is manually created after this action the flow will not know it exists. It is recommend to use this as one of the last steps in the flow.
