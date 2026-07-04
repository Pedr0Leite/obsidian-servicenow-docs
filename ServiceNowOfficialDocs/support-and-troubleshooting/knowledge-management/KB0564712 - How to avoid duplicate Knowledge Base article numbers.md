---
title: "How to avoid duplicate Knowledge Base article numbers"
aliases:
  - KB0564712
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564712
kb_number: KB0564712
last_modified: 2025-03-04
---

## How to avoid duplicate Knowledge Base article numbers

  

### Issue

### Article number generation process

* * *

When new KB articles are created, they use a sequential number that is configurable from the \[sys\_number\_counter\] table. This table can be accessed from **System Definition > Number Maintenance**.

By default, when a user manually creates a new article, there is no risk of creating duplicate article numbers, because the number is incremented each time.

However, when articles have been imported from an external system, or have been entered as part of demo data, they may already have article numbers assigned that are not in sync with the existing article numbering mechanism, therefore creating a situation that potentially results in duplicate article numbers.

### Resolution

### Setting a high article start number

* * *

One way to avoid running into duplicate article numbers, is to set a high starting number for your articles, so to leave a gap for possible future data imports:

1.  In the Application Navigator, go to **System Definition > Number Maintenance**.  
      
    
2.  Open the **Knowledge** (kb\_knowledge) table.  
      
    
3.  In the **Controls** tab or section, set the **Number** field to a high value, such as 10000, according to the expected quantity of records the safety gap should consist of.

### Related Links

For more information, see [Record Numbering](https://docs.servicenow.com/bundle/sandiego-platform-administration/page/administer/field-administration/concept/c_ManagingRecordNumbering.html "Record Numbering") in the product documentation.
