---
title: "Resolve commands that fail to run on Windows servers during discovery in Service Mapping"
aliases:
  - KB0564296
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564296
kb_number: KB0564296
last_modified: 2026-05-26
---

## Resolve commands that fail to run on Windows servers during discovery in Service Mapping

  

### Issue

### Problem

In some cases, Service Mapping may be able to connect to Windows Management Instrumentation (WMI) but fails to run all or specific commands, such as netstat.

### Symptom

-   The business service map displays the warning icon (![Warning icon](sys_attachment.do?sys_id=e69d5d9e478dcfd0d1a5ab29736d433a "Warning icon")) on top or instead of the Windows Server.
-   The following error message displays for the Windows Server: 
    
    Failed to execute WMI command on host
    

### Possible Cause 1

The Administrators group on the Windows Server has reduced DCOM rights compared to the default Windows installation.

### Resolution 1

Perform the following steps:

1.  In the command-line shell, enter **exe**.
2.  In the Component Services window, go to **Component Services > Computers**.
3.  Right-click on **My Computer** and select **Properties**.
4.  Select the **COM Security**
5.  Select **Edit Limits**.
6.  In the Access Permission window, select **Add**.
7.  In the Select Users or Groups window, enter **Distributed COM Users**, and then select **OK**.
8.  In the Access Permission window, select **Distributed COM Users** and verify that the following permissions are allowed:  
    -   Local Launch
    -   Remote Launch
    -   Local Activation
    -   Remote Activation  
          
        ![Launch and Activation Permission widow](/LaunchActivationPermission.pngx "Launch and Activation Permission widow")

### Possible Cause 2

Appropriate security policies are not configured correctly for the Service Mapping user or the group to which this user belongs.

### Resolution 2

Perform the following steps:

1.  On the Windows Server that you discover, select **Start > Run**, and then enter **secpol.msc**.
2.  In the Local Security Policy window, go to **Security Settings > Local Policies > User Rights Assignment**.
3.  Right-click **My Computer** and select **Properties**.
4.  Right-click **relevant policies** and check the Service Mapping user configured for them. If necessary, click **Add User or Group** and add the Service Mapping user to this policy. Do this for the following policies:  
    -   Debug Programs
    -   Restore Files and Directories
    -   Logon as a batch job
    -   Logon as service  
          
        ![Debug programs Properties window](/DebutProgramsProperties.pngx "Debug programs Properties window") 

### Possible Cause 3

The Service Mapping user is not allowed to access the administrative share drive C$.

### Resolution 3

Perform the following:

-   Configure the target host to allow the user to access the administrative share drive C$.

Or

-   On the firewall, allow the relevant MID server access to the target host on port 8585.  
       

### Possible Cause 4

The administrative share is not available for the current user.

### Resolution 4

Verify that the administrative share is not available for the current user and if so, fix the problem:

1.  On the MID Server, open the command line window.
2.  Run the following command: net use \\\\ip\_address\\C$ /USER:domain\\user password.
3.  Check that the command completes successfully. If it does, run the following command: net use \\\\ip\_address\\C$ /DELETE to clear this connection.
4.  If the net use \\\\ip\_address\\C$ /USER:domain\\user password command fails, allow access to the administrative share on the host.

### Possible Cause 5

There is a permission problem with the Windows Server.

### Resolution 5

Perform the following:

1.  Download the attached [run\_command.txt](sys_attachment.do?sys_id=fa9d5d9e478dcfd0d1a5ab29736d433f "run_command.txt") script and change the extension to .vbs
2.  In the run\_command.vbs script, change the IP, user, and password for those of the Windows Server.  
    -   These are indicated with <YOUR\_IP\_ADDRESS>, <YOUR\_USER>, and <YOUR\_PASSWORD>
3.  On the computer that the MID is installed on, open the command line window.
4.  Run the following command:  
    -   cscripts run\_command.vbs
5.  This script tries to create a process on the Windows Server. If it fails to create a process, it means that there is a permission problem with the Windows Server. Need to consult the windows administrator in order to solve the permission problem.

### Release

### Resolution
