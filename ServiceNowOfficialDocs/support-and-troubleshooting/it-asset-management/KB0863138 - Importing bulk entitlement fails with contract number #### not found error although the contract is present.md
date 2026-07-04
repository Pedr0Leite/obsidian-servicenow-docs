---
title: "Importing bulk entitlement fails with \"contract number #### not found \"error although the contract is present"
aliases:
  - KB0863138
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863138
kb_number: KB0863138
last_modified: 2024-04-08
---

## Issue

Importing an entitlement fails for "Contract number" not found. The contract number is selectable from the contract list. 

## Resolution

The solution would be to:  
1\. Either update the excel column to have the contract number value of the record you want updated.

  
or

2\. Ensure that in contracts table you have a record where contract number matches the value you have provided.
