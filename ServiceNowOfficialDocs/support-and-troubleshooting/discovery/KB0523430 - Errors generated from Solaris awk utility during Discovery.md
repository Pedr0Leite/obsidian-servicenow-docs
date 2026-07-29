---
title: "Errors generated from Solaris \"awk\" utility during Discovery"
aliases:
  - KB0523430
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523430
kb_number: KB0523430
last_modified: 2024-04-30
---

## Errors generated from Solaris "awk" utility during Discovery

  

### Issue

Errors Generated from Solaris "awk" Utility During Discovery

  
  
Error

* * *

During **Discovery** of a **Solaris 10** system, the following error was received: 

_System Configuration: Sun Microsystems sun4u_  
_awk: syntax error at source line 437_  
_context is_  
_modelname=10\*sprintf >>> "%d\\n" <<< , ((cpuclock/10)+0.5)_  
_awk: illegal statement at source line 437_  
_awk: syntax error at source line 444_

Workaround

* * *

The error was generated from the **Solaris** _**awk**_ utility. It appeared that the _**awk**_ binary generating the error was corrupt.

For a quick workaround, copy the _**awk**_ binary from another **Solaris 10** host server where the _**awk**_ utility is working correctly, and replace the _**awk**_ binary on the host server where it is not working correctly.

Replacing the _**awk**_ binary fixed the issue so **Discovery** could run normally.
