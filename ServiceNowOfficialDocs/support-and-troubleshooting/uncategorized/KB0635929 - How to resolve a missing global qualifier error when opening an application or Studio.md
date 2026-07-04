---
title: "How to resolve a missing global qualifier error when opening an application or Studio"
aliases:
  - KB0635929
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635929
kb_number: KB0635929
last_modified: 2026-02-16
---

## How to resolve a missing global qualifier error when opening an application or Studio

  

### Issue

Troubleshoot the error "\_ undefined, maybe missing global qualifier" that occurs when editing a custom application or opening ServiceNow Studio.

This error may appear on screen or in the localhost log. When opening an application in Studio, the Loading Application screen may display indefinitely without completing.

**Steps to reproduce**

1.  Go to **System Applications** > **Applications**.
2.  Select the edit button on an application. The system tries to open the application in Studio, which keeps loading.
3.  Select the application name. The system tries to open the application form, and the error message displays on the screen.

**Localhost log example**   
   
WARNING \*\*\* WARNING \*\*\* Evaluator: java.lang.SecurityException: \_ undefined, maybe missing global qualifier   
   
Caused by error in Script Include: '\_' at line 6   
   
3: // (c) 2009-2015 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors   
4: // Underscore may be freely distributed under the MIT license.   
5:   
\==> 6: (function() {   
7:   
8: // Baseline setup   
9: // --------------   
2017-07-10 07:12:55 (695) API\_INT-thread-1 58ABB5BEDBF332005D69F7671D9619D0 WARNING \*\*\* WARNING \*\*\* Evaluator: java.lang.SecurityException: \_ undefined, maybe missing global qualifier   
Caused by error in sys\_ws\_operation.cfb3fd7237930200612747efbe41f15e at line 25   
   
22: push = ArrayProto.push,   
23: slice = ArrayProto.slice,   
24: toString = ObjProto.toString,   
\==> 25: hasOwnProperty = ObjProto.hasOwnProperty;   
26:   
27: // All \*\*ECMAScript 5\*\* native function implementations that we hope to use   
28: // are declared here. 

error "\_ undefined, maybe missing global qualifier" is caused by script include with  name "\_".  
  

### Release

All supported releases with ServiceNow Studio

### Cause

A custom script include with the name "\_" conflicts with a base system script include that uses the same name.

### Resolution

1.  Search for script includes with the name "\_" by going to the following URL:  https://<instance\_name>.servicenow.com/sys\_script\_include\_list.do?sysparm\_query=GOTOname%3D\_  
    This should return two rows: one for Studio and one for Code Search.
2.  Rename, delete, or deactivate any additional script includes with the name "\_".
3.  Verify that the error no longer occurs.
