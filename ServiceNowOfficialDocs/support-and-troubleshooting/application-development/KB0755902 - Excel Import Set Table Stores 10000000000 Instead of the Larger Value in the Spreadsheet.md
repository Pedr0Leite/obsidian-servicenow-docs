---
title: "Excel Import Set Table Stores 10000000000 Instead of the Larger Value in the Spreadsheet"
aliases:
  - KB0755902
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755902
kb_number: KB0755902
last_modified: 2024-04-07
---

## Excel Import Set Table Stores 10000000000 Instead of the Larger Value in the Spreadsheet

  

### Issue

When importing numeric values from an excel sheet, the import table shows 10000000000 instead of the (larger) number it should have been

### Cause

For numeric values with less than 12 digits, the import will create a field of type Floating number, or in the database double(18,7). If then larger numbers with more digits are imported later, they will default to 10000000000 instead.

### Resolution

To fix the import staging table for future imports:   
a) remove all records from the staging table (the table needs to be empty for the next step) (you can use the Delete all records option in the Tables module after selecting the correct table)   
b) Go to the dictionary record for the column that contained the wrong value in the staging table and change the Type from Floating Point Number to String.   
c) Go to the data source and load all records again   
d) Run the transform 

### Related Links

If the field that was overwritten with the wrong value was the coalesce value, you will need to manually repair the broken record(s) prior to loading the data again.
