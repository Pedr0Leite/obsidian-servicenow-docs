---
title: "MID Servers and Worker Nodes"
aliases:
  - KB0815860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815860
kb_number: KB0815860
last_modified: 2026-03-19
---

## MID Servers and Worker Nodes

  

### Summary

The MID Server is fundamentally an integration for doing other integrations through, and generally uses SOAP/REST transactions to pass data to the instance. If for performance reasons an instance has been configured with application nodes split between **Worker Nodes** and **UI Nodes**, and a worker URL provided, then **all MID Servers should be reconfigured to use the worker URL**, just like the other inbound integrations to the instance.

### Release

Any, where Worker Nodes have been implemented.

### Instructions

MID Servers will have originally been configured to connect to the main instance URL, and that is set in the 'url' parameter of the MID Server config.xml file in its install folder. **Unless they are reconfigured to use the worker URL, they will now be using what has become the UI-specific URL.**

|  MID Server 'url' Parameter value: |  Generic Nodes only | Has Worker Nodes |
| --- | --- | --- |
|  Normal URL only | url = <instancename> |  url = <instancename> |
|  Has additional Worker URL |  N/A |  url = **<instancename>worker** |

The url parameter **cannot be changed from the MID Server form** in the instance (PRB1248643 - closed in 2025 unfixed). Customers need to **log into each MID Server host to reconfigure** them.

1.  Confirm the worker node URL is now active
2.  Navigate to **MID Server -> Servers**, to open a list of MID Servers
3.  Personalize columns, to add **Host name** and **Home directory** columns.
4.  **For each MID Server**:
    1.  Log into the host that the MID Server is installed on, and navigate to the Home directory.
    2.  **Open config.xml in a text editor.** If on Windows, use a an editor that understands UNIX line feeds e.g. Wordpad, not Notepad
    3.  Find the line with the 'url' parameter 

    <!-- Tells the MID server where to contact its associated ServiceNow instance.  Edit   
         this value to provide the URL of your organization's ServiceNow instance. -->  
    <parameter name\="**url**" value\="**https://<_instancename_\>.service-now.com/**"/>

1.  4.  Edit the value from your <instancename> to add 'worker' on the end.

    <parameter name\="**url**" value\="**https://<_instancename_\>worker.service-now.com/**"/>

1.  5.  **Save** the file
    6.  **Restart the MID Server**, either:
        -   Click the 'Restart MID' related link on the MID Server's form in the instance.
        -   or Restart the MID Server Service directly, either running stop.bat and start.bat from a command line, or from the Services Control Panel.

### Related Links

Every ServiceNow Instance has several application nodes, which share the work of the instance between them. These are multi-threaded, and threads share physical cpu and memory resources so can impact, or be impacted by, other threads. User transactions, such as loading forms in a browser, can be slow if the app node is busy on other things. For performance reasons, an instance may have been set up with what we call "Worker Nodes", as a way of offloading certain jobs, integrations and background tasks to a pool of dedicated nodes, so that those jobs won't affect the remaining nodes, which we then call "UI Nodes".

Our Load Balancers will direct requests to the original instance URL to the non-worker "UI Nodes", as before. An additional worker URL _may_ be created so that it is possible to direct inbound integrations to worker nodes instead. That URL will usually be the instance name appended with 'worker'. e.g. **http://<instancename>worker.service-now.com** (<instancename>soap has been used in the past). As part of a worker node implementation where inbound integrations are involved, where there is a large volume of SOAP/REST transactions compared to User transaction volume, inbound integrations will be changed to use the worker URL.

Changes will also be made to the Scheduler Worker configuration on the app nodes. UI Nodes will normally be set to run only specified background jobs, and the worker nodes will be set to run Any. Scheduled Jobs, such as Discovery Sensors or Event Management jobs, will now run in worker nodes, and no longer run in UI nodes.

If a worker node setup is approved and all inbound integrations are not directed to the worker URL, a P1 instance outage may occur. Where some existing nodes are reconfigured to become worker nodes, rather than add new ones, the UI node pool will reduce, and make the situation worse until the integrations are reconfigured for the new worker URL to move them away from that UI node pool.
