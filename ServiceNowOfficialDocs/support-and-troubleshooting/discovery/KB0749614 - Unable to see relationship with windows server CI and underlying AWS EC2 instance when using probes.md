---
title: "Unable to see relationship with windows server CI and underlying AWS EC2 instance when using probes"
aliases:
  - KB0749614
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749614
kb_number: KB0749614
last_modified: 2026-05-22
---

## Unable to see relationship with windows server CI and underlying AWS EC2 instance when using probes

  

### Issue

# Symptoms

The "Virtualizes" relationship is not created between the windows Server CI and the amazon EC2 instance during discovery of the Windows Server CI

# Release

All

# Cause

\- The relationship between a windows server CI and EC2 instance would be populated by the "Windows - Amazon EC2" probe.

\- The probe executes a powershell command "Get-WmiObject Win32\_BIOS.SMBIOSBIOSVersion". If the result contains the string : "amazon", we will move further and trigger the probe "Windows - AWS Relationship" that creates the relationship. 

\- In Most of the cases , the SMBIOSBIOSVersion contains the string "amazon", but this is not always the case

\- For example : executing PS C:\\Windows\\system32> Get-WmiObject Win32\_BIOS |Format-List . may return the below result   
  
SMBIOSBIOSVersion : 1.0  
Manufacturer : Amazon EC2  
Name : Default System BIOS  
SerialNumber : ec27aa12-285c-38c6-a838-10311f9a10ae  
Version : AMAZON - 1

\- In this case, discovery fails to create the relationship between the windows server CI and underlying AWS EC2 instance.

### Release

Any

### Resolution

# Resolution

\- Navigate to the probe "Windows - Amazon EC2" 

\- In the WMI fields related list , Change the WMI path from Win32\_BIOS.SMBIOSBIOSVersion to Win32\_BIOS.Manufacturer 

\- Change the probe post processor script From :   
  
new ProbePostProcessor({   
  
/\*\*   
\* Runs the probe instance   
\*/   
process : function() {   
related\_data.isEc2 = false;   
if (JSUtil.notNil(output.Win32\_BIOS.SMBIOSBIOSVersion)   
&& (output.Win32\_BIOS.SMBIOSBIOSVersion.toLowerCase().indexOf('amazon') != -1))   
related\_data.isEc2 = true;   
}   
});   
  
to   
  
new ProbePostProcessor({   
  
/\*\*   
\* Runs the probe instance   
\*/   
process : function() {   
related\_data.isEc2 = false;   
if (JSUtil.notNil(output.Win32\_BIOS.Manufacturer)   
&& (output.Win32\_BIOS.Manufacturer.toLowerCase().indexOf('amazon') != -1))   
related\_data.isEc2 = true;   
}   
});\\ 

\- Once the above steps are completed rerun discovery on the windows server.
