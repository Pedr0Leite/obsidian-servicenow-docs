---
title: "Flow Designer Issue on using a Data Pill Reference for Look Up Record Step"
aliases:
  - KB0814816
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814816
kb_number: KB0814816
last_modified: 2024-04-08
---

## Flow Designer Issue on using a Data Pill Reference for Look Up Record Step

  

### Issue

Using a DataPill->TableName to select a Table Name on a Action=Lookup Record instead of an actual Table Name causes the subflow to error out.

Steps to Reproduce:  
  
1\. Use Create Record to create a record on a Table (Custom or otherwise)  
2.Look up Record by defining the table name from dropdown (change\_request) and use condition->sys\_id of the record just created.- It works.  
3.Use Create Record to create a record on table change\_Request  
4.Look up record using Data Pill to select the table Name and use condition->sys\_id of the record just created   
it does NOT work  
  

It intermittently fails with Error:

\*\*\* Ops with errors \*\*\*  
Order Error Message  
12 GlideRecord.setTableName - empty table name

Issue happens on only testing the subflow but if executed on the Flow, works correctly with No Errors.

### Release

New York 

### Cause

Product Defect PRB1377769 - Fixed in Orlando

### Resolution

Workaround for New York:

This script is generic and same fix needs to be applied on instance where error is seen

var gr = new GlideRecord("sys\_variable\_value");  
gr.get("9752fc8cc3c632002841b63b12d3ae53");  
gr.value = "{{step\[e5afcb04-d05a-43b8-9afd-d8c79be98147\].table\_name}}";  
gr.variable = "4b27f01ec3c632002841b63b12d3ae3a";  
gr.insert();

### Related Links

**IMPORTANT:** 

Before Upgrading to Orlando , delete the workaround record that was created and then Upgrade. Its fixed in Orlando so we will not need the workaround anymore.
