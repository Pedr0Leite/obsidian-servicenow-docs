---
title: "List of out-of-box MID Server Script Files, in order to help avoid creating files with Duplicate Names"
aliases:
  - KB0718048
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718048
kb_number: KB0718048
last_modified: 2024-04-07
---

## List of out-of-box MID Server Script Files, in order to help avoid creating files with Duplicate Names

  

### Issue

# Symptoms

* * *

The platform prevents more than one MID Server Script File (ecc\_agent\_script\_file) with the same name. Unless you have all the relevant plugins installed, you will have no way of avoiding creating files that clash with out-of-box ones.

The "Prevent Duplicate,Spaces & Colon in name" Business Rule gives this error message:  
Duplicate file name is not allowed

# Release

* * *

This list was compiled from a code search of ServiceNow core code and Plugins on 16th November 2018, close to the end of the 'M' development cycle. It will not include files added by Store Applications or other 3rd party Apps.

# The List

* * *

MalwarebytesMalwarescan  
ActionAddUserToADGroup.ps1  
ActionCreateADObject.ps1  
ActionCreateNewGroup.ps1  
ActionCreateNewUserAD.ps1  
ActionGetComputerAccountOU.ps1  
ActionIsAccountEnabled.ps1  
ActionIsAccountLocked.ps1  
ActionIsUserFromGroup.ps1  
ActionLookupGroup.ps1  
ActionLookupUser.ps1  
ActionMoveADObjecttoOU.ps1  
ActionMoveComputerAccountToOU.ps1  
ActionQueryAD.ps1  
ActionRemoveADObject.ps1  
ActionRemoveUserFromGroup.ps1  
ActionUnlockUserAccount.ps1  
ActionUpdateADObject.ps1  
ActionUpdateADUser.ps1  
ActionUpdateUserHomeDir.ps1  
ActiveDirectoryMain.psm1  
ADSpoke  
ChangeADUserPasswordSpoke.ps1  
GetUserAndManager.ps1  
ResetADUserPasswordAction.ps1  
ExecuteProcdump.ps1  
GetExchangeEmailDetails.ps1  
GetExchangeOnlineEmailDetails.ps1  
GetNetworkStatistics.ps1  
GetRunningProcesses.ps1  
GetRunningProcessesBsd.sh  
GetRunningProcessesPosix.sh  
GetRunningServices.ps1  
RemoteUtils.ps1  
SearchExchangeForEmails.ps1  
SearchExchangeOnlineForEmails.ps1  
SecurityApplications  
SecurityUtils.psm1  
AddSoftwareDeployment.ps1  
GetDeviceCollectionsSecOps.ps1  
Credentials  
PSRemoteScript  
PSRemoteScript.psm1  
RegistryAPI  
RegistryAPI.psm1  
ScriptAPI  
ScriptAPI.psm1  
WinRMAPI  
ADME  
adme\_collector.sh  
adme\_post\_processor.sh  
ADMELauncherWinRM.psm1  
ADMELauncherWMI.psm1  
ADMEnhanced  
aix\_lsof\_command.sh  
aix\_lsof\_parser.sh  
aix\_netstat\_command.sh  
aix\_netstat\_parser.sh  
aix\_ps\_command.sh  
aix\_ps\_parser.sh  
CollectConnectionsAndProcessesInfo.ps1  
connection\_info\_segmenter.sh  
connections\_dns\_lookup.sh  
connections\_json\_formatter.sh  
Credentials.psm1  
DiagnosticsUtil.psm1  
ExecuteRemote  
ExecuteRemote.psm1  
filter\_adme\_processes.sh  
Get-PEB.psm1  
hpux\_lsof\_command.sh  
hpux\_lsof\_parser.sh  
hpux\_ps\_command.sh  
hpux\_ps\_parser.sh  
LaunchProc.psm1  
linux\_lsof\_command.sh  
linux\_lsof\_parser.sh  
linux\_netstat\_command.sh  
linux\_netstat\_parser.sh  
linux\_ps\_command.sh  
linux\_ps\_parser.sh  
NmapInstallation.ps1  
PowerShell  
process\_info\_segmenter.sh  
processes\_json\_formatter.sh  
PSRemoteSession.psm1  
PSScript.ps1  
segment\_aggregator.sh  
solaris\_lsof\_command.sh  
solaris\_lsof\_parser.sh  
solaris\_netstat\_command.sh  
solaris\_netstat\_parser.sh  
solaris\_ps\_command.sh  
solaris\_ps\_parser.sh  
unify\_aggregated\_chunks.sh  
WMI  
WMIFetch.psm1  
WMIRunner.js  
WMIScanner.js  
XMLUtil.psm1  
ActiveDirectory.psm1  
AD  
AddUserToADGroup.ps1  
ChangeADUserPassword.ps1  
ChangeServiceState.ps1  
CreateADObject.ps1  
DisableADUserAccount.ps1  
EnableADUserAccount.ps1  
Exchange  
Exchange.psm1  
Exchange-CreateAddressList.ps1  
Exchange-CreateMailbox.ps1  
Exchange-DisableMailbox.ps1  
Exchange-EnableMailbox.ps1  
Exchange-GetAddressList.ps1  
Exchange-GetMailbox.ps1  
Exchange-MoveAddressList.ps1  
Exchange-RemoveAddressList.ps1  
Exchange-RemoveMailbox.ps1  
Exchange-SetAddressList.ps1  
Exchange-SetMailbox.ps1  
Exchange-UpdateAddressList.ps1  
InstallWindowsApp.ps1  
IsAccountLocked.ps1  
JoinDomain.ps1  
QueryAD.ps1  
RemoveADObject.ps1  
RemoveUserFromADGroup.ps1  
ResetADUserPassword.ps1  
ResetADUserPasswordUnlock.ps1  
RestartWindowsServer.ps1  
Shell  
UninstallWindowsApp.ps1  
UnlockAccount.ps1  
UpdateADObject.ps1  
AWS  
S3  
S3UploadDownload.ps1  
Scripts  
BourneAgainShell  
EchoDecryptedVars.ps1  
hello.bash  
helloworld.bash  
PowerShellEncryptedParam.ps1  
script\_attachment\_file.txt  
script\_field\_file.txt  
GetNetIPAddress.ps1  
GetPSNetIPAddress.ps1  
MyTestPSCode.ps1  
TestPSCodeForExplicit.ps1  
TestPSCodeForImplicit.ps1  
AddToDeviceCollection.ps1  
AddToUserCollection.ps1  
GetApplications.ps1  
GetDeployments.ps1  
GetDeviceCollections.ps1  
GetUserCollections.ps1  
IsDeviceInCollection.ps1  
IsUserInCollection.ps1  
RemoveFromDeviceCollection.ps1  
RemoveFromUserCollection.ps1  
SCCM  
SCCM.psm1  
access\_denied.properties  
check\_priv\_command  
command\_validation.properties  
cpus.sh  
DiscoveryUtilityFiles.properties  
get-zones.sh  
Groovy  
HPOMconnector.groovy  
HypericConnector.groovy  
Invoke-UpdateAlert.ps1  
linux\_fqdn.sh  
memory.sh  
NetcoolConnector.groovy  
pattern\_order.txt  
pkg\_munger.bash  
SCOMConnector.groovy  
ServiceWatch  
SolarwindsConnector.groovy  
SSHSciptFiles  
SSHScriptFiles  
Sstorage.bash  
storage.bash  
suntype.sh  
TestTpcon.groovy  
TibcoFilesParser.ksh  
trace\_port.d  
unix\_fqdn.sh  
wminamespaces.properties
