---
title: "Manually pull Software Aseet management (SAM) contents"
aliases:
  - KB0832627
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832627
kb_number: KB0832627
last_modified: 2025-01-02
---

## Manually pull Software Aseet management (SAM) contents

  

### Summary

How to pull the latest SAM content manually onto each instance

### Instructions

Access CDS schedule list.

https://<INSTANCE\_NAME>.service-now.com/nav\_to.do?uri=%2Fcds\_client\_schedule\_list.do

Please ignore if any table is missing; move onto executing next table in the list.   
Please make sure column - 'Last updated on' on the record is updated to current time to confirm the download is complete.   
Once download of a table is complete, you can move on to the next one. We have to wait for execution of one job to be finished ('last updated on' willl be updated)and then execute the subsequent one in the order.   
  
  
Tables to be executed in order:   
\-----------------------------------------   
cds\_client\_name   
cds\_client\_mapping   
samp\_content\_version   
samp\_sw\_publisher   
samp\_sw\_product\_category   
samp\_sw\_product   
samp\_sw\_package   
samp\_sw\_entitlement\_definition   
samp\_product\_map   
samp\_package\_map   
samp\_sw\_product\_definition   
samp\_sw\_product\_process   
samp\_m2m\_suite\_entitlement\_def   
samp\_lifecycle\_definition   
samp\_price\_list   
samp\_named\_user\_type   
samp\_dmap\_downgrade\_model   
samp\_file\_name   
samp\_file\_map   
samp\_file\_set   
samp\_sw\_subscription\_integration   
samp\_sw\_subscription\_product\_definition   
samp\_sap\_license\_metric
