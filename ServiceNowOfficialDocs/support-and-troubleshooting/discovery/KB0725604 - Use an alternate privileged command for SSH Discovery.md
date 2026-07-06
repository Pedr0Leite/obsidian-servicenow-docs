---
title: "Use an alternate privileged command for SSH Discovery"
aliases:
  - KB0725604
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725604
kb_number: KB0725604
last_modified: 2026-06-22
---

## Use an alternate privileged command for SSH Discovery

  

### Issue

If your organization's security policy does not allow the use of sudo, you can configure the MID Server to use an alternate privileged command during SSH discovery. Supported alternatives include:

-   dzdo
-   pbrun
-   pfexec
-   sesudo

### Release

All versions

### Resolution

#### Step 1. Configure the MID Server to use a specific privileged command

1.  Go to the list of MID Servers using any of these paths:
    
    -   MID Server > Servers
        
    -   Discovery > MID Servers
        
    -   Orchestration > MID Servers
        
2.  Select the MID Server to configure.
    
3.  Open the More options menu in the header, then select View > Advanced.
    
4.  In the Privileged Command related list, select Edit.
    
5.  Choose the privileged command you want the MID Server to use and select Save.
    

**Tip:** The default command priority is 100. You can adjust the order value if needed. The command with the lowest order number is attempted first.

#### Step 2. Locate the file path of the alternate command on the target hosts

By default, ServiceNow searches for the sudo command in the following directories:

-   /usr/sbin
-   /usr/bin
-   /bin
-   /sbin

Your alternate privileged command might be in a different location depending on the device class.

To determine the correct path:

1.  On a representative device from each host class, run:

```
command -v alternate_privileged_command
```

 **Note**: You must include the word **command**

Example:

![](/sys_attachment.do?sys_id=ffdc028a93c36e908960fb2d6cba10ff)

2\. Note the directory returned. For example, /usr/seos/bin

#### 3\. Set the MID Server to use the alternate path

You must define the correct path by adding the mid.ssh.path\_override parameter to the MID Server configuration.

Available Value options:

-   **Append** – Adds the override path to the end of the host's path (default behavior)
-   **Prepend** – Adds the override path to the beginning of the host's path
-   **Replace** – Replaces the host path entirely with the override path
-   **None** – No override

Using the **Append** value, configure the path override following these steps:

1.  Go to the list of MID Servers using one of the following paths:
    -   **MID Server** > **Servers**
    -   **Discovery** \> **MID Servers**
    -   **Orchestration** \> **MID Servers**
2.  Select the appropriate MID Server to configure.
3.  In the **Configuration Parameters** related list, select **New**.
4.  Enter the following values:
    -   MID Server: (auto-filled)
    -   Parameter name: mid.ssh.path\_override
    -   Domain: global
    -   Value: Append:/usr/seos/bin (replace with your actual path)

**Note**: Repeat this configuration for each MID Server that will use the alternate privileged command.

![Sample configuration of alternate privileged command using Append value option](/sys_attachment.do?sys_id=48ec428a93c36e908960fb2d6cba1002)

 

### Related Links

[MID Server privileged commands - Configure the MID Server to use specific privileged commands](https://docs.servicenow.com/csh?topicname=c_PrivilegedCommandsForMIDServer.html&version=latest#t_ConfigMIDToUsePrivilegedCommand "MID Server privileged commands - Configure the MID Server to use specific privileged commands")

[MID Server Parameters - SSH Discovery parameters](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest#d1057412e1567 "MID Server Parameters - SSH Discovery parameters")
