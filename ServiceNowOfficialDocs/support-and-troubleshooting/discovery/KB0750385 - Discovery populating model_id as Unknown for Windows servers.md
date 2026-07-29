---
title: "Discovery populating \"model_id\" as \"Unknown\" for Windows servers"
aliases:
  - KB0750385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750385
kb_number: KB0750385
last_modified: 2024-04-07
---

## Issue

# Symptoms

-   Discovery populates "model\_id" as "Unknown" for most of the Windows servers.

# Release

-   Any version.

# Cause

-   The default port "8585" used by WMI service was used by another service due to which the ServiceNow WMI Collector was down in the MID host.
-   Due to which discovery couldn't query the Windows servers and get the necessary information to populate with.

# Troubleshooting

In order to troubleshoot further follow the below steps,

-   Enable "mid.log.level" parameter to "debug" on the specific MID server and restart the MID server service.
-   Post service restart, run a quick discovery towards affected Windows CI and in the agent.log below error will be logged,

05/30/19 14:33:04 (971) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)WmiDotNetVersionChecker - Supported version: 3.5.1. Installed version: 3.5&#13;  
05/30/19 14:33:04 (971) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)WmiCollectorServiceStarter - WMI collector service name is ServiceNow WMI Collector&#13;  
05/30/19 14:33:04 (971) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)WmiCollectorServiceStarter - Running on Windows&#13;  
05/30/19 14:33:04 (971) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)LocalCommandRunner - Running local command: sc.exe query "ServiceNow WMI Collector"&#13;  
05/30/19 14:33:05 (003) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)LocalCommandRunner - Command response:  
**SERVICE\_NAME: ServiceNow WMI Collector**  
TYPE : 10 WIN32\_OWN\_PROCESS   
**STATE : 1 STOPPED**  
WIN32\_EXIT\_CODE : 0 (0x0)  
SERVICE\_EXIT\_CODE : 0 (0x0)  
CHECKPOINT : 0x0  
WAIT\_HINT : 0x0  
&#13;  
05/30/19 14:33:05 (003) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)LocalCommandRunner - Running local command: **netstat -ano | findstr LISTEN | findstr 8585**&#13;  
05/30/19 14:33:05 (128) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)LocalCommandRunner - Command response: TCP 0.0.0.0:8585 0.0.0.0:0 LISTENING 2288  
TCP \[::\]:8585 \[::\]:0 LISTENING 2288  
&#13;  
05/30/19 14:33:05 (128) Worker-Interactive:HorizontalDiscoveryProbe-afa6bd244f79bb8050cc05818110c751 DEBUG: (85)**WmiCollectorServiceStarter - Port 8585 is taken by another process and can't be used the the WMI collector service. Find a port which is not occupied and set the MID parameter mid.servicewatch.wmi.port accordingly**&#13;  
  

-   In order to check further to identify which service uses "8585" port on the MID server host, execute "**netstat -anb**" command in the ECC Queue as below,

![](sys_attachment.do?sys_id=362d6c62db82b450e515c223059619da)

-   In the respective input payload received we could identify which service is used by port 8585.

![](sys_attachment.do?sys_id=3a2d6c62db82b450e515c223059619df)

# Resolution

-   In order to resolve this issue, set the MID parameter "mid.servicewatch.wmi.port" to "8586" (or any available port) and restart the service once in order to make the changes effective.
-   Post setting the parameter and service restart, discovery will be able to query the Windows servers and populate the necessary fields.

# Additional Information

-   Please refer **[Create a dedicated WMI Collector service for MID Servers running on the same server](https://docs.servicenow.com/csh?topicname=configure-mid-service-mapping.html&version=latest "Create a dedicated WMI Collector service for MID Servers running on the same server")** for additional reference.
