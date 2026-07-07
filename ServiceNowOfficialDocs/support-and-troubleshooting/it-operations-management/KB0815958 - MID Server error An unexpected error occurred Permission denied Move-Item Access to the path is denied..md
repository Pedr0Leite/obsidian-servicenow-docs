---
title: "MID Server error: \"An unexpected error occurred: Permission denied Move-Item : Access to the path is denied.\"
aliases:
  - KB0815958
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815958
kb_number: KB0815958
last_modified: 2025-08-31
---

## MID Server error: "An unexpected error occurred: Permission denied Move-Item : Access to the path is denied."

  

### Issue

After upgrading to Orlando version there is additional security feature added to restrict what folders/files can be accessed and by which user/group for the MID server's agent directory. You can read a little about it here:

[File permission enforcement for Windows MID Servers](https://docs.servicenow.com/csh?topicname=mid-non-admin-permission.html&version=latest "File permission enforcement for Windows MID Servers")

 For the "agent" folder and its sub-folders, the access control entries (or ACEs) are restricted  
 to a allow list of these groups:  
 - SYSTEM  
 - Builtin/Administrators (local Administrators)  
 - if applicable, the specific user running the MID Server Windows service ("Log on as" user)

In some cases, you may be running the MID server as a different user than the local administrator (The last point above). 

In such a case, after the upgrade you may encounter the following error:

An unexpected error occurred: Permission denied  
Move-Item : Access to the path is denied.  
At \[PATH\_TO\_MID\_INSTALL\_DIR\]\\agent\\bin\\scripts\\EnforceFilePermissions.psm1:135 char:9  
\+ Move-Item -Force -Path "$WHITELIST\_HASH\_FILE.temp" -Destinati ...  
\+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
\+ CategoryInfo : PermissionDenied: (\[...\]\\Service...rm.grphash.temp:FileInfo) \[Move-Item\], UnauthorizedAccessException  
\+ FullyQualifiedErrorId : MoveFileInfoItemUnauthorizedAccessError,Microsoft.PowerShell.Commands.MoveItemCommand

### Release

Orlando+

### Cause

The cause is related to how folder permissions would need to be set before making the service run as the desired user. See below to resolve this error. 

### Resolution

1.  Switch the MID server back to running as admin account.  
    2\. Add the non-admin user to the inclusion list (see doc below for format).  
    3\. Restart the MID Server.  
    4\. Once the new enforcement rules run, switch MID Server back to non-admin account.

Note: Even though you got the error message, the MID server will still function normally, it just won't lock down access to the agent dir.
