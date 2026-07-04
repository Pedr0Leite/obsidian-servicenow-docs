---
title: "Error: Publisher and Product manufacturer do not match - Invalid Insert"
aliases:
  - KB0720661
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720661
kb_number: KB0720661
last_modified: 2024-12-11
---

## Error: Publisher and Product manufacturer do not match - Invalid Insert

  

### Issue

Unable to create new software models or update existing software models.

1) Go to Software **Models > New**

2) In the product field, search and select software product (This will add the publisher)

3) Save or Submit Software Model 

4) A client script errors display, and model does not get created: **Invalid insert and Publisher and Product manufacturer do not match**.

### Cause

The reason is two parts:

1) There might be many records in core\_company table for the same manufacturer.

2) The manufacturer in the software publisher table is not set to the core\_company where normalization = true.

### Resolution

**PART 1:**

1) For the software you are trying to create, go to the core\_company table.

2) Find the company(manufacturer) for that product

3) Search for all records in that table to see if you have duplicates for that company

4) Add the 'normalization' column to the list view so you can see the value for that field (see sample below).

 ![](companycores.PNGx)![](/sys_attachment.do?sys_id=c566ad6cdb094990aa66a9fb139619ca)

5) Notice that only one of the 4 has field normalization = true. If you are getting the error, you may have more than one. 

6) To fix this, one way is to Export XML on those records   
\- In the XML modify the value inside the tags <canonical>true</canonical> to <canonical>false</canonical> for all of the records EXCEPT one of them (I would pick the one that is newest as the one you want to keep as true, if it is false then leave it as is). Note: You will not be able to change that value through the UI. 

7) Import that XML back into that table. This will change the values for you. 

**PART 2:**

1) Next, we have to be sure that the software publisher record points to that core company record where we have normalization = true.

2) Go to software publisher table (samp\_sw\_publisher.list)

3) Find the publisher in question. Open the record and do a 'Show XML' of that record. 

4) The value inside the tags "<manufacturer>\[sys\_id\]</manufacturer>" should be pointing to the core company record where we have normalization = true. 

5) If it is not update the field so it does point to the right record. 

Example: <manufacturer display\_value="TechSmith">0eb2f545db426740fb54fd7aae961931</manufacturer>

6) Save this record.

Now you should be able to create the software model record. 

### Related Links

HINT: to be sure you are picking the correct one in 'Part 2, step 5', you can look at the sys\_id of the core\_company record you selected to be normalized. Then in the software publisher record, you can show XML on it and see the Manufacturer field's value to make sure the sys\_id matches. That way you know you picked the right one.
