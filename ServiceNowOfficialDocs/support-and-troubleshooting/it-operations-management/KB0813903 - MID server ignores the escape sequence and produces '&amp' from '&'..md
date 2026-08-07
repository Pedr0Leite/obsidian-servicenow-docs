---
title: "MID server ignores the escape sequence \"\\" and produces '\&amp' from '&'."
aliases:
  - KB0813903
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813903
kb_number: KB0813903
last_modified: 2024-04-08
---

## Issue

MID server ignores the escape sequence "\\" character and produces '\\&amp' from '&'.

## Resolution

Solution: Modify wrapper.conf file  
  
1 - Modify the file \[wrapper.conf\] on MID Server (configuration on client side):  
\*\* Edit the file C:\\\\conf\\wrapper.conf  
\*\* Find a line starting with wrapper.java.additional.xx (xx could be 1, 2, or 3...depending on your configuration)  
\*\* Note this number xx  
\*\* Add a line wrapper.java.additional.xx+1=-Dfile.encoding=UTF-8  
  
So if the last line was wrapper.java.additional.1  
the new line to add after should be: wrapper.java.additional.2=-Dfile.encoding=UTF-8  
  
2 - Additionally via MID server configuration on your ServiceNow instance, please add the capability REST on the "Capabilities" Tab.
