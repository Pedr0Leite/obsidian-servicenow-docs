---
title: "Why is SQL Server Developer Edition marked as inactive in product license expection rule"
aliases:
  - KB2637083
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2637083
kb_number: KB2637083
last_modified: 2026-05-22
---

## Why is SQL Server Developer Edition marked as inactive in product license expection rule

  

### Summary

SQL Server Developer Edition is a fully featured version of SQL Server software—including all the features and capabilities of Enterprise Edition—licensed for development, test and demonstration purposes only. SQL Server Developer Edition may not be used in a production environment.  
  
It is set as a downgrade of SQL Server enterprise from ServiceNow content services so that if a SQL Server developer installation is found in your production environment – it would require licenses for SQL Server enterprise. 

The best practise to configure SQL Server developer (also covered in guided setup for SQL server) is to have 2 software model for SQL server developer  
  
1\. One with Install condition stating that the when environment= development or testing- it should have LUM= false – so that the SQL Server developer installation on development/testing environment are ignored from licensing  
  
2\. One with Install condition stating that when environment=production it is restricted. This is done so that the system would auto create reclamation candidates to remove SQL server developer installation found in production environment
