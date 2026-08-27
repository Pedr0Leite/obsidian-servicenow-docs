---
title: "Agent Client Collector"
aliases:
  - KB0815247
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815247
kb_number: KB0815247
last_modified: 2026-06-26
---

## Agent Client Collector

  

### Summary

## Table of Contents

-   [The ACC Applications](#mcetoc_1fqda79ft2c)
    -   [Benefits](#mcetoc_1fqda79ft2d)
    -   [Features](#mcetoc_1fqda79ft2e)
    -   [Additional documentation and best practices](#mcetoc_1fqda79ft2e)
-   [High-Level Architecture with MID](#mcetoc_1fqda79ft2f)
    -   [Setup and Deployment](#mcetoc_1fqda79ft2g)
    -   [Extensibility](#mcetoc_1fqda79ft2h)
    -   [Performance & Footprint](#mcetoc_1fqda79ft2i)
    -   [Commands and Logs](#mcetoc_1fqda201os)
    -   [Agent Registration](#mcetoc_1js2a9vnh6)
    -   [Setup and Deployment](#mcetoc_1fqda79ft2g)
    -   [Special network considerations for ACC without MID](#mcetoc_1fqda79ft2g)
-   [Configuration](#mcetoc_1fqda201ot)
    -   [Agent Configuration](#mcetoc_1fqdaehph95)
    -   [Tables](#mcetoc_1fqdaehph96)
    -   [Instance Scheduled Jobs:](#mcetoc_1fqdaehph97)
-   [Checks](#mcetoc_1fqdaehph98)
    -   [Policies](#mcetoc_1fqdaehph99)
    -   [Agent Client Collector Plugins / Assets](#mcetoc_1fqdaehph9a)
-   [Web Server](#mcetoc_1fqdaehph9b)
    -   [MID Web Server Fail Over Configuration](#mcetoc_1fqdaehph9c)
-   [Lifecycles](#mcetoc_1fqda201ou)
    -   [How are the agents (sn\_agent\_cmdb\_ci\_agent and sn\_agent\_ci\_extended\_info) records created and updated?](#mcetoc_1fqdaehph9d)
    -   [How are the policies and checks updated in the agent?](#mcetoc_1fqdaehph9e)
    -   [How are the policies and checks updated to the MID Web Server?](#mcetoc_1fqdaehph9f)
    -   [How are assets downloaded to the agent?](#mcetoc_1fqdaehph9g)
    -   [How are results sent from the agent to the instance?](#mcetoc_1fqdaehph9h)
-   [Troubleshooting](#mcetoc_1fqda201ov)
    -   [Agent Down](#mcetoc_1fqdaehph9i)
-   [Instance Clones](#mcetoc_1fqdatodk2)
    -   [Q&A](#mcetoc_1g1ri8p3u2)

The Agent Client Collector (ACC) is a Sensu based agent which supports multiple use-cases. It can be used to monitor hosts where the agent is installed, monitor endpoints, discover the hosts where the agent is installed, and more.

## The ACC Applications

-   Agent-Client-Collector Framework (ACC-F)  
    -   The ACC-F is a store app that manages the agent fleet and provides UI as well as API for SN apps to interact with the agent program
-   Agent-Client-Collector Monitoring (ACC-M)  
    -   The ACC-M is a store app running on top of the ACC-F and monitors OS and applications running on servers in order to feed events into the ServiceNow Event Management
-   Agent-Client-Collector Visibility (ACC-V)  
    -   The ACC-V is a store app running on top of ACC-F and collects information on servers and endpoints in order to populate the CMDB
    -   For more information on ACC-V please see [Agent Client Collector Visibility](https://hi.service-now.com/kb_view.do?sysparm_article=KB0966481 "Agent Client Collector Visibility")
-   Agent Client Collector for Digital End-User Experience (DEX)
    -   Agent Client Collector for DEX collects endpoint information for DEX. ACC, when used for DEX, does not use a MID server and connects directly to the ServiceNow Cloud via ITOM Cloud Services.
    -   For more information please see [Digital End-User Experience](https://www.servicenow.com/docs/csh?topicname=dex-landing.html&version=latest)

### Benefits

Some of the benefits of the ACC are

1.  End-to-end monitoring
2.  Ability to leverage advanced capabilities
3.  Efficient CI binding
4.  Reduced dependency on 3rd party monitoring tool
5.  One-stop shop for end-to-end AIOps solution
6.  Credentials for agent hosts do not need to be stored on the instance

### Features

-   Monitor the health of servers, applications, endpoints network devices etc
-   Monitor non-servers devices (e.g. network devices) can be done using proxy agent that will send SNMP/REST calls to the monitored device
-   Entry points monitoring using remote HTTP calls from proxy agent​
-   Metrics collector and anomaly detection using Metric Intelligence

### Additional documentation and best practices

-   See [KB1122613](https://noderegister.service-now.com/kb?id=kb_article_view&sysparm_article=KB1122613) for webinars, best practices, and other helpful links.

## High-Level Architecture with MID

Note: as of early 2025, DEX and some ACC-V use cases do not require a MID server can can establish a connection to an instance via the ServiceNow Cloud. See "High-Level Architecture without MID" below for more details.

![High Level Architecture](sys_attachment.do?sys_id=dea1fd9047314f147947e551336d4399 "High Level Architecture")

**Note:** Clotho and Events on the image above represent some of the components used with ACC-M

### Setup and Deployment

![High Level Setup](sys_attachment.do?sys_id=12a17d9047314f147947e551336d4372 "High Level Setup")

1.  Install Required Plugins
2.  Install MID Servers
3.  Navigate to MID Servers and click on "Setup Agent Client Collector Listener"  
    -   This will install the "MID Web Servers" which the agents will be configured to connect to in later steps 
4.  Install Agents on hosts which will be monitored/discovered  
    -   Installation can vary slightly depending on the instance version. For installation steps see:  
        -   [Agent Client Collector Installation](https://docs.servicenow.com/search?q=Agent+Client+Collector+Istallation "Agent Client Collector Installation")
    -   The User/Password (If using user/password instead of key) combination for the command should match the user configured for the "MID Web Server", this is not the same as the MID server user
    -   Navigate to "Agent Client Collector > Deployment > Agent Downloads" to download the Agent Client Collector installer
5.  Configure policies and checks once MID, MID Web Server, and agents are installed and connected

**Note:** Configuring policies and checks could be done outside this order. However, without MID Servers and agents setup it would not be possible to test them.

### Extensibility

-   The agent framework is designed to allow the addition of flows that collect information from agents and save it in SN database
-   The framework provides the means for distributing to agent scripts/executables which are not part of the initial installation, AKA ‘Assets’​
-   Once a command is executed and a payload is created, developers can handle this payload by running scripts on the MID, the instance or both
-   The framework provides an API for running a check on a given agent, regardless if the check is part of a policy

### Performance & Footprint

See the Agent Client Collector Footprint docs page for the ACC version installed:

-   [Agent Client Collector Footprint](https://docs.servicenow.com/search?q=Agent+Client+Collector+Footprint "Agent Client Collector Footprint")

### Commands and Logs

<table style="width: 990px; height: 178px;"><tbody><tr style="height: 13px;"><td style="width: 105.219px; height: 13px;">&nbsp; &nbsp;</td><td style="width: 296.594px; height: 13px;">Windows</td><td style="width: 244.5px; height: 13px;">Linux</td><td style="width: 315.688px; height: 13px;">MacOS</td></tr><tr style="height: 26px;"><td style="width: 105.219px; height: 26px;"><div style="text-align: left;">Log Folder</div></td><td style="width: 296.594px; height: 26px;"><div>C:\ProgramData\ServiceNow\agent-client-collector\</div></td><td style="width: 244.5px; height: 26px;"><div>/var/log/servicenow/agent-client-collector/</div></td><td style="width: 315.688px; height: 26px;"><div><div>/var/log/servicenow/agent-client-collector/acc.log</div></div></td></tr><tr style="height: 48px;"><td style="width: 105.219px; height: 48px;">Installation Folder</td><td style="width: 296.594px; height: 48px;">C:\Program Files\ServiceNow\agent-client-collector\</td><td style="width: 244.5px; height: 48px;">/etc/servicenow/agent-client-collector/</td><td style="width: 315.688px; height: 48px;"><p>/opt/servicenow/agent-client-collector/</p></td></tr><tr style="height: 13px;"><td style="width: 105.219px; height: 13px;"><div>Stop</div></td><td style="width: 296.594px; height: 13px;">Via services, service Agent Client Collector</td><td style="width: 244.5px; height: 13px;">sudo systemctl stop acc</td><td style="width: 315.688px; height: 13px;"><p>sudo &lt;installPath&gt;/bin/acc stop</p></td></tr><tr style="height: 13px;"><td style="width: 105.219px; height: 13px;"><div>Start</div></td><td style="width: 296.594px; height: 13px;"><div>Via services, service Agent Client Collector</div></td><td style="width: 244.5px; height: 13px;"><div>sudo systemctl start acc</div></td><td style="width: 315.688px; height: 13px;"><div>sudo &lt;installPath&gt;/bin/acc start</div><div>Or at startup by configuring launchctl with&nbsp; "/Library/LaunchDaemons/com.sn.acc.plist"</div></td></tr><tr style="height: 39px;"><td style="width: 105.219px; height: 39px;"><div>Configuration File</div></td><td style="width: 296.594px; height: 39px;"><div>&lt;installation_folder&gt;\acc.yml</div></td><td style="width: 244.5px; height: 39px;"><div>&lt;installation_folder&gt;/acc.yml</div></td><td style="width: 315.688px; height: 39px;"><div>/Library/Application Support/servicenow/agent-client-collector/acc.yml</div></td></tr><tr style="height: 26px;"><td style="width: 105.219px; height: 26px;"><div>Allow list</div></td><td style="width: 296.594px; height: 26px;">Path found in acc.yml parameter allow-list</td><td style="width: 244.5px; height: 26px;"><div>Path found in acc.yml parameter allow-list</div></td><td style="width: 315.688px; height: 26px;"><div>/Library/Application Support/servicenow/agent-client-collector/check-allow-list.json</div></td></tr></tbody></table>

### Agent Registration

When using ACC with DEX or ACC-V (MID-less), mTLS authentication is used to establish a secure connection between ACC and the ServiceNow Cloud. This is a multiple step process that involves several steps. If any step fails due to network or instance configuration, the agent will not successfully register. See "Special network considerations" below for more information.

The Agent registration process involves the following steps.

1.  On the customer instance, a registration key is automatically generated for the Agent Client Collector (Agent).
2.  The Agent is installed in the customer instance using the registration key, instance URL, and public endpoint.
    
    _The instance URL corresponds to the INSTANCE\_URL variable in the one-line installer command. The public endpoint refers to the DNS name of the nearest ServiceNow Cloud Services endpoint, which is represented by the value of the ACC\_CNC variable in the one-line installer command. For information on the command and the parameters, see [Install Agent Client Collector on Windows using ITOM Cloud Services](https://www.servicenow.com/docs/csh?topicname=acc-cloud-service-install-windows&version=yokohama&pubname=yokohama-it-operations-management) and [Perform a single-line Agent Client Collector installation on macOS by using ITOM Cloud Services](https://www.servicenow.com/docs/csh?topicname=acc-install-macOS-itom-cloud&version=yokohama&pubname=yokohama-it-operations-management)._
    
3.  The Agent sends registration request to the customer instance.
4.  The Agent is registered in the customer instance and issued a certificate.
5.  The Agent saves both the issued certificate and the public key used for verifying code signing signatures.
6.  The Agent communicates with the customer instance through the ServiceNow Cloud Services by sending messages.
7.  ServiceNow Cloud Services determine the correct customer instance to which agent messages must be sent.

### Setup and Deployment

-   For ACC-VC, see [KB1702432](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1702432)
-   For DEX, refer to the [official DEX Documentation](https://www.servicenow.com/docs/csh?topicname=dex-landing.html&version=latest).

### Special network considerations for ACC without MID

If you're using ACC without the MID server, you may need to configure ACC to use a proxy in order to connect to the ServiceNow Cloud. See [KB1943452](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1943452) for details.

## Configuration

The agent can be used to monitor and discovery the host it is installed on. The actions performed by the agents are done via "Checks". An event can be created if a check fails and triggers an alert. The checks are grouped into policies. A policy will determine on what population of agents (Linux, windows, application, etc) to run the checks on as well as the frequency.

### Agent Configuration

The main configuration files for the agent are the acc.yml and check-allow-list.yml. The check-allow-list.yml determines what commands the agent is allowed to run. Once a check is created click on related link "Generate allow-list content", next update the check-allow-list.yml file with the values generated so that the check is allowed to run on the agent.

Log parameters:

<table id="ACC-Log-Rotation-reference__table_hw3_21d_ymb"><tbody><tr><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__1">log-file</td><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__2">The log file location. Default =<p>Windows:&nbsp;C:/ProgramData/ServiceNow/Agent-client-collector/log<br>Linux:&nbsp;/var/log/servicnow/agent-client-collector/acc.log</p></td></tr><tr><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__1">log-file-and-stdout</td><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__2">Write logs to the&nbsp;stdout&nbsp;file. Default:&nbsp;false.</td></tr><tr><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__1">log-file-max-age</td><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__2">Maximum age, in days, of the log file before it is rotated out of the system memory. Default:&nbsp;3.</td></tr><tr><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__1">log-file-max-backups</td><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__2">Maximum number of log files that can be stored before being rotated out of the system. Default:&nbsp;3.</td></tr><tr><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__1">log-file-max-size</td><td headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__2">Maximum size, in MB, of the log file before it is rotated out of the system memory. Default: 10.</td></tr><tr style="height: 49px;"><td style="height: 49px;" headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__1">log-level</td><td style="height: 49px;" headers="ACC-Log-Rotation-reference__table_hw3_21d_ymb__entry__2">The log level to be measured by the logs. Available options are:&nbsp;Panic, Fatal, Error, Warn, Info, Debug. Default:&nbsp;Info.<p>The specified log level represents the lowest level of events displayed in the log. For example, a user who specifies&nbsp;Error&nbsp;sees all Error events, as well as Fatal and Panic events.</p></td></tr></tbody></table>

### Tables

https://yourInstance.service-now.com/sys\_db\_object\_list.do?sysparm\_query=nameLIKEsn\_agent

### Instance Scheduled Jobs:

https://yourInstance.service-now.com/sysauto\_script\_list.do?sysparm\_query=sys\_package%3Ddeb59787c317030039a3553a81d3aee9&sysparm\_view=

<table id="sysauto_script_table" style="height: 91px; width: 320px; margin-left: 40px; border-style: solid;"><tbody><tr id="row_sysauto_script_ac512622c354130039a3553a81d3ae4d" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Agent Client Collector keepalive</td></tr><tr id="row_sysauto_script_4d546702737d20102535b7385ef6a728" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Calculate Agent Feature Support Status</td></tr><tr id="row_sysauto_script_126cee2bc3b513002a6f741e81d3ae87" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Refresh And Publish Monitoring Policies</td></tr><tr id="row_sysauto_script_e6349043b7961010c3608129ce11a9ba" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Sync MID servers and Delete Drafts after policy import</td></tr><tr id="row_sysauto_script_a2c39af8538210103f5fddeeff7b122f" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Update Mid List For All Agents</td></tr><tr id="row_sysauto_script_b63396f8538210103f5fddeeff7b1281" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Update Mid List For All New Agents</td></tr><tr id="row_sysauto_script_d56b80dd53ef3300086addeeff7b1216" style="height: 13px;"><td style="width: 310.398px; height: 13px;">Update Processed Checks of Request</td></tr></tbody></table>

## Checks

A check is a combination of a command and its configuration. The check is executed on the Agent Client Collector's servers. Checks are provided with the base system, and their commands execute scripts which provide monitoring data for your operating systems and applications. A check's default name indicates what is being monitored and measured, the entity, and the monitoring data. For example, a check named os.linux.check-system-cpu checks the CPU data on a Linux system. The identified command in the check runs on the monitored server, providing an output and status.

-   [Create a Check Definition](https://docs.servicenow.com/search?q=Create+a+check+definition "Create a Check Definition")

### Policies

Policies consist of the CIs monitored by the Agent Client Collector and the checks that run on those CIs. When creating a policy, you configure a filter which determines the specific CIs on which the checks are to run. For example, you can configure a policy to run checks on all Apache web servers. You can create new policies or edit the default policies, as needed.

-   [Create a New Policy](https://docs.servicenow.com/search?q=Create+a+new+policy "Create a New Policy")

#### Policy Lifecycle

![Policy Lifecycle](sys_attachment.do?sys_id=52a131d047314f147947e551336d435e "Policy Lifecycle")

### Agent Client Collector Plugins / Assets

An Agent Client Collector plugin is a script or group of scripts which provides additional agent capabilities. For example, collecting more metrics, performing more checks, or generating events when an application queue size is 60% or 80% full. You associate a check with a plugin by creating a dependency between the check and the plugin. A plugin can have a dependency with several checks at a time; similarly, checks can depend on several plugins at a time. Plugins run on the same agent as the check.

You create Agent Client Collector plugins, as needed. Plugins are formatted as tar.gz files and run together with their associated check.

The plugins/assets can be seen on table sn\_agent\_asset, or by navigating to "Agent Client Collector > Configuration > ACC Plugins".

-   [Create and Edit Plugins](https://docs.servicenow.com/search?q=create+and+edit+plugins "Create and Edit Plugins")

## Web Server

The Web Server is the "endpoint" to where the agents will connect. To view the web servers navigate to "Agent Client Collector > Deployment > MID Web Servers". There you will see the list of web servers running. Those are the servers to which the agents can connect, as well as the port.

Via the related links in this form you can stop, start, restart, test and update parameters.

### MID Web Server Fail Over Configuration

The Agent's configuration file, acc.yml, determines to what MID Web Server it will connect. The configuration file for the agent allows for multiple Web Servers to be configured. The next MID Web Server configured in the acc.yml file will be used when communication cannot be established to a MID Web Server. The agents can also connect to a virtual IP address behind a load balancer.

Specify one or more MID server failover URLs in the acc.yml. The agent will communicate with the MID server using these URLs. This list is iterative; meaning the agent will try the first URL, if failed will move to the second URL and so on. If Auto-MID-Selection feature is on (the file mid.list.json is present), the agent will perform a connectivity test and will re-write the backend-url list. The order of the list will be based on ping time and then the number of agents already connected to the MID. This means that if the feature is enabled: the first MID server in the list should be the one with the lowest ping and the lowest number of agents.

-   To disable sending periodic MID Server updates from the ServiceNow instance to existing agents:  
    1.  Navigate to System Properties > All Properties.
    2.  Set the sn\_agent.enable\_auto\_mid\_selection property to false.  
          
        
-   To disable automatic MID Server selection for individual agents:  
    1.  In the agent's acc.yml file, locate the enable\_auto\_mid\_selection property.
    2.  Set the property value to false.

## Lifecycles

### How are the agents (sn\_agent\_cmdb\_ci\_agent and sn\_agent\_ci\_extended\_info) records created and updated?

**Note:** On the agent set acc.yml file set log-level = "debug", and set mid.log.level = debug on the MID server, to see detailed debug messages.

1.  The agent uses the configuration from the acc.yml to connect to the MID Web Server
2.  The agent sends keepalive events to ip:port/ws/events, when the agent first starts up you can see the keepalive loop starting:
    
    {"component":"agent","level":"info","msg":"Starting keepalive loop","time":"2021-07-26T09:43:49-07:00"}
    
3.  On the MID Server agent logs we can see the MID Server receiving the request and the reply:
    
    07/26/21 10:29:53 (772) qtp540917385-156 DEBUG: (156) com.service\_now.mid.webserver.jetty.WebServer - SERVER onFillable()  
    ...  
    07/26/21 10:29:53 (773) qtp540917385-156 DEBUG: (156) com.service\_now.mid.webserver.jetty.WebServer - onBinaryMessage(HeapByteBuffer@4079c03a\[p=0,l=2293,c=2293,r=2293\]={<<<keepalive\\n{"timestamp":16...nse\_required":"true"}}}>>>})  
    07/26/21 10:29:53 (791) qtp540917385-156 DEBUG: handleKeepalive: payload \[{"timestamp":1627320593,"entity":{"entity\_class":"agent","system":{"hostname":"......"}}}\]
    
4.  The MID Server sends an update to the instance (Update "Last refreshed" field or any other fields which need to be updated)  
    -   On the instance:
        
          
        1.  The Agent Client Collector API (/api/sn\_agent/agents) receives the update sent by the MID server and updates the agent information
            
        2.  The API is defined in /sys\_ws\_definition.do?sys\_id=cf0d4208c3e3030039a3553a81d3ae9a
            
        3.  The REST resource will update/create the agent accordingly
            
5.  Finally the MID Server replies to the agent:
    
    07/26/21 10:29:53 (791) qtp540917385-156 DEBUG: Publishing message \[{ }\] to client:WIN-IHKAN2LQJE1. remote: org.eclipse.jetty.websocket.jsr356.JsrAsyncRemote@3efeb957  
    07/26/21 10:29:53 (792) qtp540917385-156 DEBUG: (156) com.service\_now.mid.webserver.jetty.WebServer - sendText("keep\_alive\_response  
    { }")
    
6.  On the agent we can see:
    
    {"component":"agent","content\_type":"application/json","level":"debug","msg":"message received","payload\_size":3,"time":"2021-07-26T09:46:54-07:00","type":"keep\_alive\_response"}  
    {"component":"agent","level":"debug","msg":"keepalive response received from the backend. Setting the read deadline to 1627318314","time":"2021-07-26T09:46:54-07:00"}
    

**Note:** Scheduled job "Agent Client Collector keepalive" runs every minute to check for agents which the last\_refreshed field has not been updated since the last keepalive and sets its statuses accordingly.

### How are the policies and checks updated in the agent?

1.  As part of the keep alive process, the MID Server checks for updates to the agent configuration (updates to checks, policies, etc)
2.  The MID Server will reply to the keepalive and send additional information if there are updates to be sent to the agent. In the MID Server agent logs we can see, for example:
    
    07/26/21 12:32:53 (776) qtp540917385-157 DEBUG: Publishing config {"checksum":"826562631",   
     "check\_requests":\[{  
      ...  
    }\]} to client: name {  
    ...  
    }, agent\_id 5d06b30ec6c4ce0b
    

### How are the policies and checks updated to the MID Web Server?

1.  Job "Refresh And Publish Monitoring Policies" (sysauto\_script.do?sys\_id=126cee2bc3b513002a6f741e81d3ae87) runs every minute
2.  The job calls MonitoringConfig.syncPoliciesToMid(); which checks if we need to send an update to the MID Servers
3.  If an update must be sent to the MID server, create an ecc\_queue output record with topic "MonitoringProbe" and source = "config\_publish"
4.  The MID server process the output and updates the agent policies

### How are assets downloaded to the agent?

1.  The assets files are synchronized to the MID servers via the FileSyncer  
    -   The FileSyncer is a process/thread that keeps MID Server files synchronized to instance files
    -   The assets can be seen in the MID server folder:
        
        %INSTALL\_FOLDER%/agent/static/acc\_plugin
        
2.  The keepalive process which keeps the agent record on the instance up to date, as well as policy/checks on the agent client, also contain an "assets" section
3.  The assets section of the payload tells the agent what assets need to be downloaded, for example:
    
      "assets" : \[ {  
        "sha512" : "c5149676070a227ab75a6c2979a568404e6710c9c8d57766d85a7c759504b833788ad133b99caa8d53cbd134fe42817b84eef1880b41d29a8e0e2f51fe8d5c73",  
        "url" : "{{MID\_URL}}/static/acc\_plugin/windows/all/all/all/acc-visibility-modules-windows.tar.gz",  
        "metadata" : {  
          "name" : "acc-visibility-modules-windows",  
          "namespace" : "default"  
        }  
      }
    
4.  The agent downloads the assets from IP:PORT/static
5.  In the agent, the files are downloaded to its "cache" folder   
    -   Windows: C:/ProgramData/ServiceNow/Agent-client-collector/cache
    -   Linux: /var/log/servicnow/agent-client-collector/cache

This file synching uses a pre-existing MID Server sync feature. Detailed information on how this works in general, known issues, and debugging tips can be found in:  
[KB0852276 How MID Server File Synchronisation works, to help when Troubleshooting](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852276 "KB0852276 How MID Server File Synchronisation works, to help when Troubleshooting")

### How are results sent from the agent to the instance?

1.  The checks will run as configured in the policies
2.  The agent sends the check result to the MID Server using the WebSocket connection  
    -   On the agent acc.log we can see the result being run and sent, for example:
        
        {"component":"agent","level":"info","msg":"Running check, name: policy: Windows OS Metrics, check:os.windows.metrics-system-cpu-load ...  
        {"component":"agent","level":"debug","msg":"{winchecks metric-windows-cpu-load \[AGENT\_DIR=C:\\\\Program Files\\\\ServiceNow\\\\agent-client...  
        {"component":"agent","content\_type":"application/json","level":"info","msg":"sending message","payload":"{\\"timestamp\\":1628002490,\\"...
        
    -   On the MID Server we can see the result received
        
        DEBUG: handle result from client \[WIN-IHKAN2LQJE1\] agent\_id \[5d06b30ec6c4ce0b\], check result is \[{"timestamp":1628004950,"check":{"co...  
        DEBUG: MID Script Include cache hit for name=MonitorResultParser
        
3.  On the MID Server the MID script include MonitorResultParser checks if the check result has the mid\_script field populated, this will be configured on table sn\_agent\_check\_type
4.  Is the mid\_script field populated?  
    -   Yes: Run the mid\_script to handle the result  
        -   Depending on the mid\_script the result may, for example:  
            -   Sent back to the ecc\_queue as an input
            -   Sent back as an event
            -   Sent back as a metric
    -   No: Send the result to the ecc\_queue
5.  Once the result is in the instance, the sn\_agent\_check\_type instance script will process the result

## Troubleshooting

**Note:** On the agent set acc.yml file set log-level = "debug", and set mid.log.level = debug on the MID server, to see detailed debug messages.

### Agent Down

1.  Make note of the MID web server the agent should connect to, this can be seen on the agent list or via table sn\_agent\_ci\_extended\_info
2.  Is the MID server up?  
    -   Yes: Continue to next steps
    -   No: Start the MID server  
        1.  Did MID Server start successfully and show as up?  
            -   Yes: Continue to next steps
            -   No: Troubleshoot MID server startup issues. See:  
                -   [MID Server Down Troubleshooting](https://hi.service-now.com/kb_view.do?sysparm_article=KB0661756 "MID Server Down Troubleshooting")
3.  Navigate to "Agent Client Collector > Deployment > MID Web Server"
4.  Is the MID web server started?  
    -   Yes: Continue to next steps
    -   No: Click on "Start" to start the MID web server  
        1.  Did MID web server start successfully and the operating system shows a process listening on the configured port?  
            -   Yes: Continue to next steps
            -   No: Review the MID server agent and wrapper logs for issues starting the web server
5.  Is the agent running on the host? (Can be checked via services.msc on windows or via tools like top or ps on unix/linux operating systems)  
    -   Yes: Review the acc.log file
    -   No: Review the acc.log file
6.  Does the acc.log display any network errors?  
    -   Yes: Check that the server where the agent is running can communicate too the web server host and port configured
7.  Resolve any other errors (the action to be taken will depend on the error)

## Instance Clones

MID Server and ACC installs are not Clones when an instance is Cloned over another instance, and their directly related files and configurations are preserved (or should be, but might not be), but a lot of code and settings is cloned over from the source instance. More details on the known issues, and how Clones work with ACC can be found in:

-   [KB1002549 Agent Client Collector and Clones](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002549 "KB1002549 Agent Client Collector and Clones")
-   [KB0786475 MID Servers and Clones](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786475 "KB0786475 MID Servers and Clones")

### Q&A

1.  What happens when the agent cannot connect?  
    -   The agent will queue up information until it can connect to the MID server again.
2.  What happens if agent sends data to MID, however MID server cannot connect to the instance?  
    -   For checks which write to the ecc\_queue, the MID server uses the same mechanism to send data to the instance and will retry up to so many times.
3.  What is the Agent Client Collector for windows user account password?  
    -   When installing the ACC for windows you can chose an existing account or let the installation create an account. The installation creates local account called "servicenow". This account password is dynamically generated. The password is not needed as the service can be started and stopped via windows services. If the password must be updated, this can be done via the windows user configuration, and then the service can be stopped and updated in order to have matching passwords.

[\[back to top\]](#mce-toc "[back to top]")
