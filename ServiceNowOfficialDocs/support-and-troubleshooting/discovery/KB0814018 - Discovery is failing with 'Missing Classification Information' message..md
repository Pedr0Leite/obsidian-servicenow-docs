---
title: "Discovery is failing with 'Missing Classification Information' message."
aliases:
  - KB0814018
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814018
kb_number: KB0814018
last_modified: 2024-04-08
---

## Discovery is failing with 'Missing Classification Information' message.

  

### Issue

Discovery is failing with below error message after upgrading to newyork:

Error evaluating C:\\Users\\svc\_cmdbdisc\\AppData\\Local\\Temp\\GenerateWMIScriptJS\_WMI\_FetchData3696280959267867313.js: Expected ';

"Missing Classification Information"

### Release

Newyork and Above Versions.

### Cause

-   The error was coming from "Windows - Classify" probe: 

https://Instance\_name.service-now.com/nav\_to.do?uri=discovery\_sensor.do?sys\_id=b11453f50a0a0ba500a72547a687189e

-   This error is coming from below code: 

if (JSUtil.nil(result.Win32\_OperatingSystem.Caption))  
this.processError("Missing Classification Information");

-   This is because the script was not able to decode the data though it is showing up properly in ECC Queue.

### Resolution

-   The Windows Classify sensor was older version and was modified because of which it didn't get upgraded.
-   There is a change in the format of the data sent by MID server in Newyork release and it is being sent in JSON format.
-   Older code just handles it assumes that it is in XML format.
-   Change the sensor and classify probes to Newyork versions for this to work and then the modifications can be applied after that if required.
