---
title: "Rest API fails to post attachment, if the name contains square braces (or other special characters)."
aliases:
  - KB0817665
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817665
kb_number: KB0817665
last_modified: 2024-04-08
---

## Rest API fails to post attachment, if the name contains square braces (or other special characters).

  

### Issue

-   Example filename 

https://\*\*\*\*api/v1/CreatAttachment?table\_name=sn\_customerservice\_case&table\_sys\_id=xxxxxxxx&file\_name=yyyyy\[zzzzz\].png

-   if the filename contains "\[" and "\]" , then API fails to post the attachments, but if the name of the filename is simple then it works perfectly fine.
-   Error Messages :

trax BR inc2.2: Error executing REST request: Invalid uri

  
and

  
Invalid query

### Cause

-   The square brackets ( \[zzzzz\] ) are not escaped and so the filename is not correct.

### Resolution

-   Solutions are to either escape the square brackets or use URL encoding 

e.g.  
  
Changed   
  
file\_name=yyyyy\[zzzzz\].png'  
  
to  
  
file\_name=yyyyy%5Bzzzzz%5D.png'
