---
title: "Troubleshooting Power-shell Orchestration Workflow not working with new MID Server"
aliases:
  - KB0748533
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748533
kb_number: KB0748533
last_modified: 2024-04-07
---

## Troubleshooting Power-shell Orchestration Workflow not working with new MID Server

  

### Issue

# Description

If you are struggling with the setup of a new MID Server in that all integrations work fine except for orchestration workflow when pointing to a Power-shell activity then this may be a credential issue, configuration of the clients environment or even a ServiceNow issue.

# Procedure

Steps to reproduce:   
1\. Open Workflow Editor   
2\. Open workflow   
3\. Open the first "Run Powershell" activitity in workflow.   
4\. Configure "Hostname" to new MID-server.   
5\. Impersonate User  
6\. Go to service portal  
7\. Open item  
8\. Use default values and submit request.   
9\. Check in RITM that the orchestrations workflow fails. 

To troubleshoot:

Check if there are any credentials set up for the MID Server, otherwise, the MID Server is totally dependant on the Service credential on the MID Server service (right-click the service and select the Log On tab); you can also assign a tag to the Windows credential.

If you suspect this is more to do with the configuration of environment, when testing your scripts, you can run the same script from within Power-shell

-   if it works in Power-shell and your workflow fails, then this will be a ServiceNow issue and you should log a call with Support
-   if it fails in Power-shell then this is an environment issue
