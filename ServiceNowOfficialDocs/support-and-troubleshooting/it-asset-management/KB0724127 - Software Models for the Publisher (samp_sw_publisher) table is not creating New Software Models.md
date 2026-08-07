---
title: "Software Models for the Publisher (samp_sw_publisher) table is not creating New Software Models"
aliases:
  - KB0724127
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724127
kb_number: KB0724127
last_modified: 2024-04-07
---

## Software Models for the Publisher (samp\_sw\_publisher) table is not creating New Software Models

  

### Issue

From this 'samp\_sw\_publisher' table it contains a list of publishers such as the 'Microsoft' Manufacturer.  
When attempting to create a new Software Model for Microsoft SQL Server CAL’s and going in the Publisher field we seem to be missing several Microsoft files that are in the 'core\_company'. Which, we have noticed the issue was with the incorrect reference Manufacturer it was using.  

### Resolution

From this ’samp\_sw\_publisher’ table, it contains a list of publishers.  
\- search for ‘Microsoft’  
\- In the Manufacturer, (this should have a field that it is in reference to) ‘Microsoft' should be the manufacturer.  
This Manufacturer is located in the ‘core\_company’ list and this seems to be a common issue were the 'core\_company' has the incorrect field added, it should be in reference to the the ’samp\_sw\_publisher’.
