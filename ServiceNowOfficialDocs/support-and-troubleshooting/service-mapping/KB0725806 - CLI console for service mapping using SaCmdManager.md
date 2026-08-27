---
title: "CLI  console for service mapping using \"SaCmdManager\"
aliases:
  - KB0725806
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725806
kb_number: KB0725806
last_modified: 2025-11-14
---

## CLI console for service mapping using "SaCmdManager"

  

### Issue

Note: This tool is effectively obsolete since the more capable Command Validation Tool was released in 2022:  
[https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/it-operations-management/reference/command-validation-reference.html](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/it-operations-management/reference/command-validation-reference.html)

## Table of Contents

-   [Overview](#mcetoc_1gikech3ba1)
-   [Pre-requisites](#mcetoc_1gikech3ba2) 
-   [How to activate /Inactivate](#mcetoc_1gikech3ba3)
-   [Usage](#mcetoc_1gikech3ba4)
-   [Example](#mcetoc_1gikech3ba5)

## Overview

-   The command line control uses for  executing the commands from service-now itself without login into the respective server.
-   It facilitates the search of information that may be needed when creating discovery pattern steps.
-   The command line console is not a real-time command line console, therefore commands like cd will not work.
-   The command line console can be intimidating since it appears like anyone can run any command on any host when in reality, only users with the proper permissions can use the console. 

## Pre-requisites 

-   Service mapping plugin "com.snc.service-mapping" must need to be activated.
-   The hosts which we are trying to communicate via "SaCmdManager" must need to be Discovered successfully and populated to CMDB.
-   Target IP must be reachable by the MID Server.

## How to activate /Inactivate

-     The interface will be provided by the processor, It can be activated or inactivated based on the requirement to use it.
-      Go to System Definition ->Processors  ,Search for "SaCmdManager".       

          ![](/sys_attachment.do?sys_id=3c6d8b4c935972105736b25d6cba1018)   

## Usage

To open the page, type this URL directly into the browser, substituting your instance URL, and target server IP address:

https://<instance\_name>.service-now.com/SaCmdManager.do?ip=<Target IP>                             

## Example

Windows Command Examples :

-   type "C:\\CloudDimensions\\mongoose.cfg.txt"
-   dir "C:\\CloudDimensions"

Unix Command Examples :

-   cat /usr/local/rvm/rubies/ruby-2.3.0/config
-   ls /usr/local2

![](/sys_attachment.do?sys_id=016d8b4c935972105736b25d6cba1037) 

### Release

Any

### Resolution

N/A
