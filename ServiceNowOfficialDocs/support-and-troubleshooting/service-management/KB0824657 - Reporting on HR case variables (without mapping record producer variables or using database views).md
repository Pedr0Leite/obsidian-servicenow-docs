---
title: "Reporting on HR case variables (without mapping record producer variables or using database views)"
aliases:
  - KB0824657
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824657
kb_number: KB0824657
last_modified: 2024-04-08
---

## Reporting on HR case variables (without mapping record producer variables or using database views)

  

### Issue

The user has a process where HR Cases are created per a Record Producer in their system. They needed a way to report on the variable question and answers provided by the creator of each HR Case without having to map record producer variables or utilize a database view.

### Resolution

After speaking with the HR Product Owners, the below guidance was provided:  
  
The user can accomplish this by creating an extra column in the HR case table for the corresponding question (for example a column for u\_do\_you\_feel\_sick, which is True/False type), and then the user can handle the mapping logic in sn\_hr\_core.hr\_ServicesUtil().createCaseFromProducer().

Currently, createCaseFromProducer is only mapping some default HR fields (e.g. opened\_for, hr\_service, etc) to a HR case, and all the other information will be stored in the HR Case payload column (in JSON format). If the user handles the custom questions by mapping them to the extra columns they create, they can do a query on the columns just like how a query is done to OOB columns.
