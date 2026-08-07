---
title: "MID Server Down | A guide on how to restore the MID Server"
aliases:
  - KB0535040
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535040
kb_number: KB0535040
last_modified: 2026-01-29
---

## MID Server Down | A guide on how to restore the MID Server

  

### Issue

Whether it is a MID Server that is being deployed for the first time or one that has been active for a while, there may be an occasion when the MID Server record on the instance reports that the MID Server is "Down." This guide was written to address common scenarios and assist in restoring the MID Server's operation.

### Troubleshooting Flowchart

![](/MID%20Server%20Troubleshooting.pngx)

### Additional Details

**Starting the MID Server Service on Windows**

1.  Log in to the host machine as a privileged user.
2.  Start the Services console (**Start > Run > services.msc**).
3.  Right-click on the service name (by default it starts with **ServiceNow MID Server**) and select **Start** from the context menu.

**Starting the MID Server Service on Unix/Linux**

1.  Log in to the host machine as a privileged user.
2.  Change the directory to the path of the parent agent folder (_/service-now/<mid server name>/agent_).
3.  Execute the shell script start.sh.

**The MID Server is Upgrading**

When the MID Server service has correct access to an auto-upgrade and it detects a discrepancy between its reported version and the instance version, it will upgrade. During this time, the service may be running, but the MID Server is not very responsive. Do not interrupt the upgrade process. Review the agent and wrapper logs for details. To troubleshoot errors that may occur, see [MID Server Upgrades](https://docs.servicenow.com/csh?topicname=c_UpgradeAndTestMIDServer.html&version=latest "MID Server Upgrades") in the product documentation.

**Common Windows Service Issues**

On Windows, a service is installed when the MID Server is started. In order for this service to be installed, typically a (domain) administrator account is required. Once the service is installed, it can run as a local user or a domain user. If there is an issue with starting the service and or having the service remain in a running state, check that the "run as" user has proper write access to the agent folder and its subfolders.

If not, contact your Windows administrator. Alternatively, deploying a new MID Server as an administrator with a fresh download on the installation files will typically resolve service issues.

**Common Network Issues**

The MID Server connects to a ServiceNow instance via the SOAP web service (TCP port 443). Typically, opening a web browser on the host machine and navigating to the URL **https://<instance name>.service-now.com** should be successful. Additionally, from a command prompt, verify that the following commands are successful:

-   ping <instancename>.service-now.com
-   telnet <instancename>.service-now.com 443

If not, contact your network administrator.

**Common Security Configuration Issues**

-   Verify that the user name and password combination that is being used by the MID Server is correct. This can be accomplished by logging into the target ServiceNow instance with the same set of credentials.
-   Verify that the user name used by the MID Server has the mid\_server role. From the ServiceNow instance, navigate to the sys\_user record of the MID Server user and verify that the Roles related list has the mid\_server and soap roles. Without these proper roles, the MID Server will have insufficient rights when accessing the instance.
-   Verify that the MID Server user has sufficient rights to the required tables. Log into the ServiceNow instance as the MID Server user. Check to see if you are able to navigate to the following tables and successfully read and create records: ecc\_queue, sys\_data\_source.
-   If granting the MID Server user the admin role resolves the issue, then this points to an issue with ACLs on the instance.

 **Note:** Changes on the roles of the MID Server user do not take effect for an active MID Server service until it is restarted. 

**Verifying that the Instance Allows MID Server Communication**

-   The MID Server uses SOAP Web Service with basic authorization to communicate with the instance.  Verify that System Properties > Web Services > "Require basic authorization for incoming SOAP requests" is checked
-   The following Scripted Web Services must be active: _GetMIDInfo, InstanceInfo, MIDAssignedPackages, MIDFieldForFileProvider, MIDFileSyncSnapshot, MIDServerCheck, MIDServerFileProvider_.  To view the list of available scripted web services, navigate to System Web Services > Scripted Web Services
-   The Public Page _InstanceInfo_ is required to allow the MID Server to validate its version.  Verify that this page is active by navigating to sys\_public.list

 **Note:** Starting in Fuji, the mentioned Public Page and Scripted Web Services require the _maint_ role to modify.

**Contacting Technical Support**

When contacting ServiceNow Support for assistance with MID Server issues, please include the agent and wrapper logs of the MID server. Also, to expedite the investigation, the caller should have access to make changes on the MID Server host.
