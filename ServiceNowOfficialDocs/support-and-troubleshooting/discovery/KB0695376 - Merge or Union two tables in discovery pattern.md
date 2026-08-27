---
title: "Merge or Union two tables in discovery pattern"
aliases:
  - KB0695376
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695376
kb_number: KB0695376
last_modified: 2025-01-03
---

## Issue

  

You have two temporary tables in your discovery pattern

You want to merge them into one table

## Resolution

1.  Use the "Union Table" step
2.  Select your first table in "First table" field
3.  Select your second table in "Second table" field
4.  In "Target table" field, you can type in the table you want to be created with these two tables merged.

                  ![Union Table Step Example](sys_attachment.do?sys_id=965586791b458114ccc253da234bcb8c "Union Table Step Example")

## Additional Information

-   If you have Data in either of the first or seconds tables that is not needed into resulting table do one of the following:  
    -   Use the Filter Table step before the Union step to filter out unneeded data
    -   OR use the Filter step after the Union step to filter out unneeded data from Union-ed table.
