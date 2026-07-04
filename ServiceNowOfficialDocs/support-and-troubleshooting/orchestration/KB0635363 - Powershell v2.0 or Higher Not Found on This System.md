---
title: "Powershell v2.0 or Higher Not Found on This System"
aliases:
  - KB0635363
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635363
kb_number: KB0635363
last_modified: 2024-04-07
---

## Powershell v2.0 or Higher Not Found on This System

  

### Issue

Powershell v2.0 or Higher Not Found on This System

  
  

# Issue

* * *

Powershell Orchestration activities fails with error **Powershell v2.0 or higher not found on this system**.

# Solution

* * *

1.  PowerShell must be installed on any MID Server that uses powershell activities. MID Servers using PowerShell must be installed on a supported Windows operating system. ServiceNow supports PowerShell 2.0 and above. The MID server service checks the powershell version installed on the MID server before running a powershell activity. The following command is executed:
    
    **powershell.exe -noninteractive -nologo -noprofile -command "(get-host).version.major"**
    

![](sys_attachment.do?sys_id=f02de862db82b450e515c22305961933)

The output from the above command should be an integer greater than or equal to 2. In some cases, a non-integer value or an integer less than 2 is returned. A solution in such cases is to install version 2 or above of powershell on the MID server host.

2.  The parameter **mid.powershell.path** can be added to the MID server configuration. This parameter enables an administrator to point to a specific PowerShell on a MID Server in cases where more than one PowerShell is installed. However, if this parameter points to an incorrect path, then the error **Powershell v2.0 or higher not found on this system** is returned, an incorrect path is a folder where powershell cannot be found. In such cases, the solution is to either remove the parameter or point to the correct path.
