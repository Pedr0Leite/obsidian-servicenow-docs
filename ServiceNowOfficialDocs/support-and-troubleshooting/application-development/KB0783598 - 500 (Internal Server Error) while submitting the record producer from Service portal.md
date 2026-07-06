---
title: "500 (Internal Server Error) while submitting the record producer from Service portal"
aliases:
  - KB0783598
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783598
kb_number: KB0783598
last_modified: 2024-04-08
---

## 500 (Internal Server Error) while submitting the record producer from Service portal

  

### Issue

Unable to submit the record producer from Service Portal on checking browser console shows 500 (Internal Server Error)

### Resolution

Check for below probable causes:

1.  Defining a default value of a variables as 'null'
2.  Catalog Client scripts or UI policies Run scripts used in record producer has setValue() method passing 'null'

If no value to be passed on the variable leave the default value or setValue () as empty instead of 'null'

Example:

g\_form.setValue('variable\_name', null);

change this to

g\_form.setValue('variable\_name', '');
