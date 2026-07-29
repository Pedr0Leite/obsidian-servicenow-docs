---
title: "ODBC Error Messages: Verifying that your credentials are correct"
aliases:
  - KB0538975
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538975
kb_number: KB0538975
last_modified: 2024-08-15
---

## ODBC Error Messages: Verifying that your credentials are correct

  

### Issue

ODBC Error Messages: Verifying that your credentials are correct

Symptoms are listed below:

-   unable to connect to the URL due to a user authentication error
-   driver unable to connect to URL  
     

### Cause

you receive an authorization required error message, it is likely that there is a user authentication issue with your instance.

### Resolution

If you receive the following error message while using the ODBC driver, 

_\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Method failed:_ 

**_(https://demo.service-now.com/sys\_user.do?SOAP&displayvalue=all) HTTP/1.1 401 Authorization Required with code:_ 401**, make sure that the credentials (user name/password) supplied in the login dialog are correct and that the user exists in the targeted instance.
