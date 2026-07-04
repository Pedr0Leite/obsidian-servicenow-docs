---
title: "Resolving missing DLL errors with the ODBC Driver on 64-bit Windows"
aliases:
  - KB0546126
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546126
kb_number: KB0546126
last_modified: 2024-04-30
---

## Issue

Resolving missing DLL errors with the ODBC Driver on 64-bit Windows

Problem

* * *

The ODBC Driver may be unable to access the MSVCR71.dll file when using the 32-bit ODBC Driver on a 64-bit Windows version.

Symptoms

* * *

One of these errors appears when using the 32-bit ODBC driver:

-   \[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK Client\]Failed to initialize the Service component
-   The program cannot start because MSVCR71.dll is missing from your computer - try reinstalling the program to fix this problem

Cause

* * *

The MSVCR71.dll file is not included by default in the 64-bit Windows system PATH.

Resolution

* * *

Add this file path to the Windows PATH system variable:   
  
**C:\\Program Files (x86)\\ServiceNow\\ODBC\\ip\\Java\\jre\\bin**

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><b>Note</b>: <span>The "</span><strong>C:\Program Files (x86)\ServiceNow\"&nbsp;</strong><span>portion of the file path above may vary depending on where you installed the ODBC Driver</span>.</td></tr></tbody></table>
