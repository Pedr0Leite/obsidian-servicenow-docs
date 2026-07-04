---
title: "Resolving MSVCR100.dll error in the ODBC Driver"
aliases:
  - KB0597981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597981
kb_number: KB0597981
last_modified: 2024-04-07
---

## Resolving MSVCR100.dll error in the ODBC Driver

  

### Issue

Resolving MSVCR100.dll error in the ODBC Driver

Problem

* * *

ODBC Driver fails when testing or executing a query and displays an MSVCR100.dll error.  

Symptoms

* * *

After installing the 1.0.11 version of the ODBC Driver, the following error appears when you test the connection or execute a query:  
  
"The program can't start because MSVCR100.dll is missing from your computer. Try reinstalling the program to fix this problem."   
  
  
Cause

* * *

MSVCR100.dll is missing from the classpath.   
  
  
  
Resolution

* * *

Add or update the Java classpath JAVA\_HOME value to point to Java 1.8. The 1.0.11 version of the ODBC Driver includes the Java 1.8 runtime environment. Also ensure that %JAVA\_HOME%\\bin is included in your computer's Path environment variable.  
  
The 1.8 JRE is available at these paths for a default ODBC installation:  
  
ODBC 64-bit: C:\\Program Files\\ServiceNow\\ODBC\\ip\\Java\\jre  
ODBC 32-bit: C:\\Program Files (x86)\\ServiceNow\\ODBC\\ip\\Java\\jre
