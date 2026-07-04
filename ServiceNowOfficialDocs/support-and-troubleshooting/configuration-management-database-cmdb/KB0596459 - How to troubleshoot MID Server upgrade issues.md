---
title: "How to troubleshoot MID Server upgrade issues"
aliases:
  - KB0596459
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596459
kb_number: KB0596459
last_modified: 2026-05-18
---

## How to troubleshoot MID Server upgrade issues

  

### Issue

Troubleshoot common MID Server upgrade issues that occur after an instance upgrade or Quarterly Patching Program (QPP) patch.

When an instance is upgraded, any MID Server pointing to that instance attempts to auto-upgrade to the same version. The QPP applies patches within the same release family and does not upgrade across release families. MID Servers attached to instances auto-upgrade at least once per quarter. The increased frequency of upgrades can lead to uncommon and unexpected conditions on the machines where the MID Server is installed.

This article provides a guided troubleshooting flow to identify and resolve common upgrade failures based on symptoms found in the MID Server agent log.

### Symptoms

-   MID Server status is **Down** in the MID Server list
-   Discovery scans get stuck
-   MID Server does not stay running
-   MID Server status is **Up** but the server is not responding

### Release

All supported releases

### Resolution

### Step 1: Verify whether the instance was recently upgraded

To determine whether a recent instance upgrade (either manual or with a QPP patch) triggered the MID Server issue:

1.  Go to **System Diagnostics** > **Upgrade History**.
2.  Search the **To** column for an entry that indicates the instance was upgraded to a new patch. The entry resembles the following format: glide-RELEASE\_FAMILY-03-09-2015\_06-22-2016\_1932.zip

If the instance was recently upgraded, the MID Server auto-upgrade may have failed. Continue with the following steps to diagnose and resolve the issue.

If the instance was not recently upgraded, see the following resources for additional MID Server troubleshooting:

-   [Continue debugging MID Server](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597571)
-   [MID Servers and Certificates](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863673)

### Step 2: Check the MID Server status

1.  Go to **MID Server** \> **Servers**.
2.  Locate the MID Server in the list. A green dot and **Up** status indicate the server is running.

### Step 3: Access the agent log

The agent log contains error messages that identify the cause of the upgrade failure. How you access the log depends on whether the MID Server is running.

**If the MID Server status is Up:**

1.  Go to **MID Server** > **Servers**.
2.  Locate and open the MID Server record.
3.  In the **Related Links** section, select **Grab MID Logs**.
4.  The External Communication Channel (ECC) Queue list displays two log commands: one for agent0.log.0 and one for wrapper.log.
5.  When the requests return, open the ECC Queue record and download the agent log.

**If the MID Server status is Down:**

1.  Log in to the host machine where the MID Server is installed.
2.  In the file system, go to the **Agent** \> **Logs** directory.
3.  Open the agent log.

If you cannot access the agent log using either method, contact your network or system administrator. The MID Server host machine may be powered off or disconnected from the network. After resolving any network or hardware issues, try the upgrade again.

### Step 4: Identify and resolve the error

Open the agent log and search for the following error messages to determine the root cause.

**"The MID Server was unable to download"**

This error indicates that communication between the MID Server and the instance has been disrupted.

To resolve this issue, troubleshoot the connection between the MID Server and the instance. After restoring communication, try the upgrade again.

See [How to resolve communication issues between MID Server and the instance](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597538)

**"Unable to delete file"**

During the upgrade process, the MID Server removes and replaces certain files. If a file cannot be deleted, the upgrade fails. In this scenario, the MID Server must be reinstalled after the file system issue is resolved.

To resolve this issue, identify and fix the file system issue on the MID Server host machine, then reinstall and upgrade the MID Server.

See [How to resolve local environment issues of the MID Server host](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597552)

**"User is unable to authenticate"**

MID Servers authenticate using the user name and password defined in the config.xml file on the host machine. The credentials are stored in the mid.instance.username and mid.instance.password parameters. The user defined in this file must also exist in the **System** > **Users** table on the instance and must have the mid\_server role at minimum. Authentication failure during an upgrade can cause both the MID Server and the Upgrade Service to stop responding.

To resolve this issue, verify the MID Server credentials in config.xml and in the **System** \> **Users** table, then try the upgrade again.

See [Troubleshooting MID Server user authentication issues](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597574) 

**File not found**

Search for both of the following messages in the agent log:

"SEVERE:com.snc.dist.mid\_upgrade.UpgradeExecption: java.io.FileNotFoundException:"

and

"\\bin\\mid.bat (Access is denied)"

A complete example: com.snc.dist.mid\_upgrade.UpgradeException: java.io.FileNotFoundException: D:\\ServiceNow\\agent\\bin\\mid.bat (Access is denied)

This error can indicate that the MID Server host is a Windows machine with the Application Experience service set to **Disabled**. Although this Windows service cannot be fully disabled—it continues to run in the background—setting it to **Disabled** prevents it from receiving requests. The Application Experience service evaluates compatibility of application updates with existing installed software. When the service does not receive the upgrade request, the compatibility evaluation does not occur and the MID Server upgrade fails.

To resolve this issue, verify that the Application Experience service is not set to **Disabled** on the Windows host machine, then try the upgrade again.

See [How to resolve local environment issues of the MID Server host](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597552 "Resolve local environment issues of the  MID Server host")  

### Related Links

-   [Continue debugging MID Server](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597571)
-   [MID Servers and Certificates](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863673)
-   [How to resolve communication issues between MID Server and the instance](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597538)
-   [How to resolve local environment issues of the MID Server host](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597552)
-   [Troubleshooting MID Server user authentication issues](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597574)
