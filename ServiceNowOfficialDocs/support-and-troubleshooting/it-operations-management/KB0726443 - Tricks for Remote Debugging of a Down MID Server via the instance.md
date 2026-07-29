---
title: "Tricks for Remote Debugging of a \"Down\" MID Server via the instance"
aliases:
  - KB0726443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726443
kb_number: KB0726443
last_modified: 2026-02-27
---

## Tricks for Remote Debugging of a "Down" MID Server via the instance

  

### Issue

## Table of Contents

-   [Introduction](#mcetoc_1gikdq9t42e)
-   [Procedure](#mcetoc_1gikdq9t42f)
    -   [Use another 'Up' MID Server running on the same host](#mcetoc_1gikdq9t42g)
    -   [Use the Debug Mode Command Prompt feature of the Service Mapping Pattern Designer via another 'Up' MID Server](#mcetoc_1gikdq9t42h)
    -   [Use the Command Validation Tool from the Pattern Designer Enhancements app](#mcetoc_1gikdq9t42i)

## Introduction

Occasionally, there can be an issue with a MID Server installation causing the MID Server to lose communication with the instance and go Down. In this situation, the Restart, Grab Logs, Get MID Thread Dump functions and other useful tricks for debugging a MID Server can't be performed remotely via the instance.

In some of those situations, the customer may not immediately have access to the host server in order to help with the debugging, such as checking the agent logs and attaching them to a support incident for ServiceNow to help. 

Here are some ideas that may avoid delays in starting the investigation for high impact incidents. 

## Procedure

### Use another 'Up' MID Server running on the same host

Often more than one MID Server is installed on the same host. Perhaps a MID Server for Discovery and a separate one for LDAP, or another for a sub-production instance. If one of those is Up, then access to files and services is possible.

A MID server service usually logs in as a domain account with local administrator privileges (unless the log in as user has been changed, or the post-Paris MSI installer was used). Anything, including reading configuration and log files, and restarting windows services, is possible if "Command" jobs are sent. ["Command" topic is a documented feature](https://docs.servicenow.com/search?q=Basic+MID+Server+and+ECC+Queue+concepts "\"Command\" is a documented feature").

In general the "Command" jobs are set up like this:

1.  Open a new blank ECC Queue record form - /ecc\_queue.do
2.  Fill in the fields like so:  
    -   Agent = mid.server.<MID Server name>  
        remembering to use the MID Server that is still Up
    -   Topic = Command
    -   Name = <your command>
    -   Queue = Output
    -   State = Ready
    -   Sequence = (clear this value)
3.  Submit
4.  Look in the ECC Queue table for the Input response from that output. The output from the commands will be in the Payload.  
    /ecc\_queue\_list.do?sysparm\_query=topic%3dCommand

Useful commands to use in the Name field:

<table border="1"><tbody><tr><td><p>dir /s /b \mid.jar<br>dir /s /b \wrapper-override.conf<br>dir /s /b \config.xml</p></td><td><p>Find all MID Server installations on the same disk. Only a MID Server installation will have mid.jar.&nbsp;<br>Other java applications may also have config.xml and&nbsp;wrapper-override.conf files, so this may bring back other things.</p></td></tr><tr><td><p>type&nbsp;&lt;agent path&gt;\logs\&lt;log filename&gt;<br>type C:\MID Servers\Prod_Disco_MID\agent\config.xml<br>type C:\MID Servers\Prod_Disco_MID\agent\conf\wrapper-override.conf</p></td><td><p>Once you know what you have, you can list the contents of the settings files to figure out which&nbsp;MID Server is which.<br>config.xml will have a URL and Name parameter for the instance and mid server name.<br>wrapper-override.conf will have the windows service&nbsp;wrapper.name&nbsp;and&nbsp;wrapper.displayname.</p></td></tr><tr><td><p>type&nbsp;C:\MID Servers\Prod_Disco_MID\agent\logs\agent0.log.0<br>type&nbsp;C:\MID Servers\Prod_Disco_MID\agent\logs\wrapper.log</p></td><td>List log files. The agent log is the detailed MID Server applications log, including the AutoUpgrade logs. The Wrapper log has details of application start/stop, Upgrade Logs, and exceptions.</td></tr><tr><td><p>net stop "&lt;wrapper.name&gt;"<br>net stop "snc_mid_Prod Disco MID"</p></td><td>Stop a MID Server Windows Service.&nbsp;</td></tr><tr><td>net start "&lt;wrapper.name&gt;"</td><td>Start a MID Server&nbsp;Windows Service</td></tr><tr><td>tasklist -v</td><td>List all running processes, with their executable name, PID, memory usage, and run as user</td></tr><tr><td>wmic service</td><td>List all running and no-running services, wmic service gives all parameters of the service including PID, folders, display/service names, status. Finds MID Servers, WMI Collectors, Upgrade services, and helps identify the Anti-Virus running on the host.</td></tr></tbody></table>

It is possible to paste multiple lines into the Name field. It won't look right on the form, but the new line characters do get sent, and the lines will be run one after each other on the target.

### Use the Debug Mode Command Prompt feature of the Service Mapping Pattern Designer via another 'Up' MID Server

This is only available if Discovery or Service Mapping is installed, and if a Discovery Credential is available for the MID Server Host. You can explore both remote hosts and MID Servers.

This 'Command Prompt' feature can be useful for seeing what's going on with a Down MID Server, assuming there is a credential available for accessing the MID Server host. 

[Command Prompt and Debug Mode is a documented feature](https://docs.servicenow.com/search?q=explore+remote+host+Command+Prompt "in the documentation"), also mentioned in [KB0725806 CLI console for service mapping using "SaCmdManager"](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725806), and similar commands to the above could be used with it.

You can go directly to the Command Prompt page from: /SaCmdManager.do?ip=<ip address of mid server host>

There is a big limitation with this tool, which is that you cannot specify which MID Server should be used to run the probe. So use this instead....

### Use the Command Validation Tool from the Pattern Designer Enhancements app

Store link: [Pattern Designer Enhancements](https://store.servicenow.com/store/app/155b928e1b8f2a10f4b3dc28b04bcb9a "Pattern Designer Enhancements")  
Release note: [Docs: Pattern Designer Enhancements release notes](https://www.servicenow.com/docs/r/store-release-notes/store-rn-itom-pattern-designer-enhancements.html "Docs: Pattern Designer Enhancements release notes")

Documentation is in this KB article: [KB1123625 Command Validation Tool](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1123625)

This was released in 2023 and is compatible with Tokyo, San Diego Patch 5, Rome Patch 8, and later, and can be installed if Discovery, Service Mapping, or Cloud Management are installed.

### Release

Any for Command topic. Since approx Geneva for SaCmdManager. Since October 2023 for [Command Validation Tool](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1123625)

### Resolution

NA
