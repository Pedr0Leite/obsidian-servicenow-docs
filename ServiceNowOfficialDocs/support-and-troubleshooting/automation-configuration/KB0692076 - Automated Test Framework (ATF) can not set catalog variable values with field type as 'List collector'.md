---
title: "Automated Test Framework (ATF) can not set catalog variable values with field type as 'List collector'"
aliases:
  - KB0692076
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692076
kb_number: KB0692076
last_modified: 2024-04-07
---

## Automated Test Framework (ATF) can not set catalog variable values with field type as 'List collector'

  

### Issue

Automated Test Framework (ATF) can not set catalog variable values with field type as 'List collector' when trying the following steps:  
  

1\. Create a test impersonating any user (administrator or a user with certain limitations).  
2\. Add a test step 'Open a Catalog Item' and add any Catalog Item with a Mandatory List collector field.  
3\. Add a test step 'Set Variable Values' and fill the List collector field with a value that is certain to be found.  
4\. Add a test step 'Order Catalog Item'.  
5\. Run the test.

The catalog item is not ordered with values selected in the List collector field. To ensure this, the field in question can be made mandatory. This way the test will fail.  

### Resolution

Add a variable attribute "**glide\_list**" to your List collector variable.
