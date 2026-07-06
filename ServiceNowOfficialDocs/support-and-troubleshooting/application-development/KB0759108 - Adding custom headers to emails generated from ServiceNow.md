---
title: "Adding custom headers to emails generated from ServiceNow"
aliases:
  - KB0759108
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759108
kb_number: KB0759108
last_modified: 2025-01-03
---

## Adding custom headers to emails generated from ServiceNow

  

### Summary

In some cases there maybe a need to add a custom header to emails generated from ServiceNow platform. This can be achieved via business rules.

### Instructions

To add custom header, do the following:

1.  Create a business rule on the sys\_email table ("on before", "insert/update")   
2.  The script is below. It is important to put your headers BEFORE ServiceNow headers.  
    If you simply append your headers, they will be cut off.  
      
    /\* add headers \*/  
      
    if(current.headers.indexOf("X-My-Header-Here") < 0){  
           current.headers = "X-My-Header-Here: " + headerValue + "\\n" + current.headers;  
    }
