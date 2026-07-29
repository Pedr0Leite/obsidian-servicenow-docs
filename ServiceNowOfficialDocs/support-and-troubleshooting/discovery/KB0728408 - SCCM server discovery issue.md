---
title: "SCCM server discovery issue"
aliases:
  - KB0728408
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728408
kb_number: KB0728408
last_modified: 2024-04-07
---

## SCCM server discovery issue

  

### Issue

# Description

* * *

1.  Open the SCCM Server record from list

                 _https://<INSTANCE>.service-now.com/sn\_client\_sf\_dist\_cmdb\_ci\_sccm\_server\_list.do?sysparm\_query=_

             2. Click "**Discover Now**" button (as shown below in the screenshot)

             3. Workflow context return **error** as below:  

_The term 'Get-CMUserCollection' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again._  
HRESULT: \[-2146233087\]

# ![](/sys_attachment.do?sys_id=ea6ca86edb42b450e515c223059619ce)Solution

* * *

1\. Get-Command : module ConfigurationManager --  Name “Get-CMDeviceCollection”, “Get-CMUserCollection” from their powershell console within the SCCM server to proof issue is resided in the cmdlet.

**Error return as below**:

_@@@_

_The term 'Get-CMUserCollection' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again._

_@@@_ 

2\. Customer needs to update cmdlet library.

3\. If issue persist, powershell admin need to repair the library from console.

**Root Cause:**

The root cause of the issue is the cmdlet unavailableRun following command

# Applicable Versions

* * *

London
