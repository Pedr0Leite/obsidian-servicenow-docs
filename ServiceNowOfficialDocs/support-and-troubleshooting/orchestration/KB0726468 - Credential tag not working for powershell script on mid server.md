---
title: "Credential tag not working for powershell script on mid server"
aliases:
  - KB0726468
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726468
kb_number: KB0726468
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Credential debug info logs success in Powershell Orchestration activity even when the powershell execution shows exception for "The operation failed due to insufficient access rights"

 \["credentialDebugInfo": "2019-02-12 09:40:07 Tried Credential: name=\[_CREDENTIAL\_NAME_\], affinity: no, status=success, sysid=600be6eadbd7234037bc1cb51b961989, username=\[_USER\_NAME_\]\\\\\[_PASSWORD_\], type=Windows, order=100\\r\\n",   
"eccSysId": "dcc1dfcedbab278095d0a6e51b96199f", \] 

# Release

* * *

All supported releases

# Environment

* * *

Microsoft Active Directory

# Cause

* * *

\=> The above "status=success" indicates the following script execution of "cd C:\\Scripts\\Azure ; .\\SN-RemoveFromAD.ps1 -Credential $cred" resulted in a "waitFor() is 0". See the snippet from the agent log:   
  
\==========================   
02/12/19 09:40:07 (524) Worker-Standard:PowershellProbe-03b1538edbab278095d0a6e51b961974 DEBUG: Executing command: C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -executionpolicy unrestricted -noninteractive -nologo -noprofile -command "&amp; {&amp; 'scripts\\PowerShell\\PSScript.ps1' -computer '10.90.16.4' -script 'C:\\Windows\\TEMP\\script4641618113149492766.PS1' 'use\_mid\_service\_account' $false -useCred $true -ismid $true -isDiscovery $false -debug $true -logInfo $false; exit $LASTEXITCODE}"&#13;   
...   
02/12/19 09:40:09 (407) Worker-Standard:PowershellProbe-03b1538edbab278095d0a6e51b961974 DEBUG: The exit value from waitFor() is 0&#13;   
02/12/19 09:40:11 (448) Worker-Standard:PowershellProbe-03b1538edbab278095d0a6e51b961974 DEBUG: Execution status: success&#13;   
02/12/19 09:40:11 (448) Worker-Standard:PowershellProbe-03b1538edbab278095d0a6e51b961974 DEBUG: Username <domain>\\<user> worked!&#13;   
\========================== 

# Resolution

* * *

Here are two example why credential debug info logs status=success even though the powershell execution is thrown an exception.

  
Example 1.   
path and content:   
c:\\temp\\helloworld.ps1   
"hello world!"   
  
Command in Powershell activity   
cd c:\\temp\\; .\\helloworld.ps1 -credential $cred   
  
\=> ServiceNow passes $cred to "C:\\Windows\\TEMP\\script<randomnumber>.PS1" file.   
\=> ServiceNow passes $cred to "C:\\Windows\\TEMP\\script<randomnumber>.PS1" file.   
\=> Powershell will execute it as is even though "helloworld.ps1" has no knowledge of what "-credential" is. This will stil return a "waitFor() is 0"   
  
Example 2.   
  
path and content:   
C:\\temp\\createaduser.ps1   
\=======================   
try {   
if($cred){   
new-aduser -name "employeeofthemonth" -erroraction stop   
}   
else {   
Write-Host "failed, try again"   
}   
}   
catch {   
Write-Host "fubar says " $Error\[0\].Exception   
}   
\=====================   
Command in Powershell activity   
cd c:\\temp\\; .\\createaduser.ps1 -credential $cred   
\=====================   
  
\=> ServiceNow passes $cred to "C:\\Windows\\TEMP\\script<randomnumber>.PS1" file.   
\=> ServiceNow passes $cred to "C:\\Windows\\TEMP\\script<randomnumber>.PS1" file.   
\=> Powershell will execute it "as is" even though "createaduser.ps1" has no knowledge of what "-credential" is. "new-aduser" does but since there is no parameter passing between the "C:\\Windows\\TEMP\\script<randomnumber>.PS1" and "createaduser.ps1", "new-aduser" can't use it. The "$cred" will not be the value from ServiceNow. It is the value of the MID Server service "logon as" service account with which "createaduser.ps1" will run. This is a custom scripting issue.   
  
If this account does not have sufficient privilege it will return the following.   
  
\===============================   
\*\*EXCEPTION: System.UnauthorizedAccessException: Access is denied ---&gt; System.ServiceModel.FaultException: The operation failed due to insufficient access rights.   
\--- End of inner exception stack trace ---   
at Microsoft.ActiveDirectory.Management.AdwsConnection.ThrowExceptionForExtendedError(String extendedErrorMessage, Exception innerException)   
at Microsoft.ActiveDirectory.Management.AdwsConnection.ThrowExceptionForFaultDetail(FaultDetail faultDetail, FaultException faultException)   
at Microsoft.ActiveDirectory.Management.AdwsConnection.ThrowException(AdwsFault adwsFault, FaultException faultException)   
at Microsoft.ActiveDirectory.Management.AdwsConnection.Create(ADAddRequest request)   
at Microsoft.ActiveDirectory.Management.ADWebServiceStoreAccess.Microsoft.ActiveDirectory.Management.IADSyncOperations.Add(ADSessionHandle handle, ADAddRequest request)   
at Microsoft.ActiveDirectory.Management.ADActiveObject.Create()   
at Microsoft.ActiveDirectory.Management.Commands.ADNewCmdletBase\`3.ADNewCmdletBaseProcessCSRoutine()   
at Microsoft.ActiveDirectory.Management.CmdletSubroutinePipeline.Invoke()   
at Microsoft.ActiveDirectory.Management.Commands.ADCmdletBase\`1.ProcessRecord()   
</output>   
<debug\_info>2019-02-12 18:33:00 Tried Credential: name=<credential name>, affinity: no, status=success, sysid=27f5dc5edba32300328fdc965e961967, username=<domain>\\<user>, type=Windows, order=100&#13;   
</debug\_info>   
\===============================   
  
\=> Even though the "new-aduser" cmdlet itself fails due to lack of privilege, the exception is properly handled in the try block, so the overall script execution will result in a "waitFor() is 0".   
  
  
\=> There are two valid formats in ServiceNow platform passing $cred:

  
1\. You can execute the entire script in the command where $cred is included.   
2\. You can create a mid server script file for powershell where $cred is included.
