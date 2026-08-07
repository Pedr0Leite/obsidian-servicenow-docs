---
title: "Email showing choice field value instead of label"
aliases:
  - KB0790297
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790297
kb_number: KB0790297
last_modified: 2024-04-11
---

## Email showing choice field value instead of label

  

### Issue

In some cases the notifications show the value of the choice list filed instead of the label .

For example if the incident record has state with value of '8' and label of 'Assigned' , the notification displays value (8) instead of 'Assigned'

### Cause

If there is a choice list definition ( value and label ) for a domain and if this state and value definition does not exist in the domain you are then the label value will not be displayed.

You can confirm this from the UI from list view from a different domain, you will see value instead of label .

### Resolution

  
The best solution is to have the state with value in the choice list definition for that domain for best practice.   
The workaround is to add the property _glide.sys.domain.use\_record\_domain\_for\_choice\_list_ with a boolean value of true, which will go through all the domains and display the choice list label.
