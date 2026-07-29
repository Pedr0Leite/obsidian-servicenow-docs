---
title: "Catalog Client Script Not working on Service Portal"
aliases:
  - KB0760420
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760420
kb_number: KB0760420
last_modified: 2024-04-08
---

## Catalog Client Script Not working on Service Portal

  

### Issue

An onChange Catalog Client Script for a variable not working on Service Portal

### Cause

The issue is seen because of some problems with the script. There were the following issues with the script: 

UI Type was set to Desktop

Variable name was empty  
  

### Resolution

To fix the script, the issues mentioned above need to be resolved:

UI Type should be set to All   
Variable name should be set to the correct variable onChange of which it should be triggered.

  
The script part itself needed to be corrected.

The condition to check for the boolean variable's value was as below:

if (newValue == true)

This needs to be changed to the following:

if (newValue == 'true')
