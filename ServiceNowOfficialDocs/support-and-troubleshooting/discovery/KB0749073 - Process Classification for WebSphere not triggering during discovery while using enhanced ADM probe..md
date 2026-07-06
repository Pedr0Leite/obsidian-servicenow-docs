---
title: "Process Classification for WebSphere not triggering during discovery while using enhanced ADM probe."
aliases:
  - KB0749073
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749073
kb_number: KB0749073
last_modified: 2024-04-07
---

## Process Classification for WebSphere not triggering during discovery while using enhanced ADM probe.

  

### Issue

# Symptoms

Process Classification for WebSphere not triggering during discovery.

# Steps to reproduce

01) Run discovery on Linux server which consists of WebSphere application.

02) Make sure you have enabled Enhanced ADM probe by setting the property 'glide.discovery.enable\_adme' to true.

# Cause

While using the Enhanced ADM probe, the functionality here is different. There is an extra condition that checks to see if we've encountered a given process enough times during the time ADME is running on the host and sampling the running processes. 

For example:

ADME Running Process example where count < threshold of 5 (the websphere server):   
  
{"count":"1","pid":"111XXXXX","ppid":"117XXXX","command":"/usr1/IBM/WebSphere/java\_1.7\_64/bin/java","parameters":"   
  
You can see here the count = 1

There must be some issue with counting the websphere processes when grabbing ADME results that is causing it to have a count of 1.

When running process classification from ADME probe, only classify those processes with high count number, since low count processes may already be dead. In this case, since we are getting the count as 1, discovery thinks it doesn't have the active processes running and doesn't launch the websphere pattern.

# Resolution

As a workaround, edit the script include DiscoveryJSONADMESensor to change the following property:   
  
https://instance-name.service-now.com/sys\_script\_include.do?sys\_id=b941e3e15352320023bdae4a16dc346e   
  
From:   
epac.checkCountForClassify = true;   
  
To:   
epac.checkCountForClassify = false;   
  
This disables the additional check described earlier and after re-running discovery with ADME enabled, it successfully launches websphere probes.

# Additional Information

System property: glide.discovery.enable\_adme

ADME: Enable enhanced ADM probe. If "yes", the ADM Enhanced probe will be triggered and only fall back to the ADM probe as needed.

-   **Type**: true | false
-   **Default value**: false
