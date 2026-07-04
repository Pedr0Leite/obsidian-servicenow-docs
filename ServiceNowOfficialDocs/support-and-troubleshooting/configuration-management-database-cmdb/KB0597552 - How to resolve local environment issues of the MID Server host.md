---
title: "How to resolve local environment issues of the  MID Server host"
aliases:
  - KB0597552
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597552
kb_number: KB0597552
last_modified: 2025-04-07
---

## How to resolve local environment issues of the MID Server host

  

### Issue

## Table of Contents

-   [Symptoms](#mcetoc_1f4rm0d0d6)
-   [Issues with the MID host environment](#mcetoc_1f4rm0d0d7)  
    -   [MID Server is unable to delete files during an upgrade](#mcetoc_1f4rm1db59)
    -   [Application Experience is disabled on Windows](#mcetoc_1f4rm67ual)

## Symptoms

-   MID Server upgrade failed ([Troubleshooting](/kb_view.do?sysparm_article=KB0596459))
-   Discovery stopped working
-   Upgrade is stalled
-   MID Server appears as Up but not responding

## Issues with the MID host environment

### MID Server is unable to delete files during an upgrade

In order to successfully upgrade, the MID Server must be able to manipulate files in the /agent directory for the given MID Server. The MID Server user must have the mid\_server role on the instance to access the instance, and admin permissions on the local host to create directories, write files, and delete files. Deleting files should not be an issue. Another possible reason is the file that the MID Server is attempting to delete is in use by another application or service. If this is the case, close the application. 

#### SOLUTION 1: Verify user permissions

Log on to to the MID Server host machine as the MID Server user. Attempt to create a directory, create a file, and then delete that file. If you are unable to do these things as that user, the MID Server will not be able to either. Contact your system administrator and ensure that the MID Server user has no less than local admin permissions on a Windows system. On a Linux system, SSH on to the host machine using the MID user name and password. Navigate to the /agent directory where the MID Server was installed. Type ls -lg and examine the permissions list. Ensure that the user has **_\-rwx_** access either in the group the MID user belongs to or, if the MID user is the owner, as the owner. 

#### SOLUTION 2: Identify running services 

The wrapper log and agent log will both hint that a file cannot be deleted because it is in use by another application or service. For example, the log entry might read: "The process cannot access the file because it is being used by another process." In releases prior to Istanbul, executing integrations (such as JDBC import), Service Mapping, and the MID Installer that was left open could all potentially be sharing a .jar file or .dll file when the MID's auto-upgrade started. With the exception of the MID Installer, these issues have been addressed in Istanbul and in Geneva and Helsinki patches.

On Windows, open the services gear icon and search for **ServiceNow** in the services list. If there are other **ServiceNow** services running, such as Service Mapping, stop the service, reinstall the MID Server, and then restart all the services.

On Linux machines, use the **ps** command to list services. If a ServiceNow service is running, go to the **bin** directory of that service and execute the **_stop.sh_** command. Once the service is stopped, reinstall the MID Server, and then restart all the services.

**When to reinstall the MID Server:** Once an upgrade has failed for delete file permissions, the MID Server needs to be reinstalled. This is because, depending on where in the upgrade the failure happened, jar files necessary to execute the upgrade may have already been deleted by the failed upgrade process. You may preserve your config.xml and your agent wrapper files, reinstall the MID Server, and then restore those two files to avoid reconfiguration. Be sure that you remove the keystore directory if you do this.

### Application Experience is disabled on Windows

A log message similar to the following can indicate that the host machine of the MID Server is a Windows machine that has Application Experience disabled: _com.snc.dist.mid\_upgrade.UpgradeException: java.io.FileNotFoundException: D:\\ServiceNow\\agent\\bin\\mid.bat (Access is Denied)_

Per Microsoft's security documentation, this service is internal and cannot actually be disabled. Setting this to **Disabled** in the Windows environment only stops the service from being called. It does not stop the service from running. The purpose of the Application Experience, generally speaking, is to evaluate the incoming compatibility of application updates to existing installed software. Since the running service does not receive the request when the setting is set to **Disabled**, the evaluation never happens and the install of the update fails.

#### SOLUTION: Verify that Application Experience is enabled for MID Server Windows host machine 

1.  Log on to to the MID Server host machine as the MID Server user with local administrator permissions.
2.  Enter **+r**  (or **Windows + R** for windows) **-->** to open the Run window.
3.  Type "**msconfig**" in the Run window, and then click **Enter**.
4.  Select the **Services** tab.
5.  Verify that the Application Experience feature is enabled.  
    1.  If it is not enabled, enable it. This must be enabled for MID Server upgrades to succeed.
    2.  If it is enabled, keep troubleshooting. Application Experience is not the cause of the MID Server's failed upgrade.
