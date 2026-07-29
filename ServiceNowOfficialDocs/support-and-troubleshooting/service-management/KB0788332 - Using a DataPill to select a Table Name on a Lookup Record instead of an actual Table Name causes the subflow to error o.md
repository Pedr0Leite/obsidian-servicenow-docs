---
title: "Using a DataPill to select a Table Name on a Lookup Record instead of an actual Table Name causes the subflow to error out while testing"
aliases:
  - KB0788332
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788332
kb_number: KB0788332
last_modified: 2024-04-08
---

## Using a DataPill to select a Table Name on a Lookup Record instead of an actual Table Name causes the subflow to error out while testing

  

### Issue

Using a DataPill to select a Table Name on a Lookup Record instead of an actual Table Name causes the subflow to error out while testing

### Cause

PRB1377769 

### Resolution

This is working as expected in Orlando and Paris

  

You can run the workaround to run this background script to fix the issue on the instance.  

This script fixes it on OOB instance and would fix it on other instances as well.  
  
var gr = new GlideRecord("sys\_variable\_value");  
gr.get("9752fc8cc3c632002841b63b12d3ae53");  
gr.value = "{{step\[e5afcb04-d05a-43b8-9afd-d8c79be98147\].table\_name}}";  
gr.variable = "4b27f01ec3c632002841b63b12d3ae3a";  
gr.insert();
