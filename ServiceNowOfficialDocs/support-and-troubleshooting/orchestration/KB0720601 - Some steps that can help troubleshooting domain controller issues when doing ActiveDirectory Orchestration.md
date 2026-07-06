---
title: "Some steps that can help troubleshooting domain controller issues when doing ActiveDirectory Orchestration"
aliases:
  - KB0720601
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720601
kb_number: KB0720601
last_modified: 2024-04-07
---

## Issue

The purpose of this article is to help identify a domain controllers in an environment. This will help to troubleshoot issues when doing ActiveDirectory orchestration where you are not sure if the IP or DNS name you are hitting is the correct domain controller. 

## Resolution

1) Go to the Probes table (discovery\_probes.list)

2) Find the probe where ECC queue topic = Command

3) Open it:

-   In this, whatever you write in the field "ECC queue name" field will execute that command on the MID server or from the MID server to a target. 

4) Use the following commands based on the reason:

-   nltest /parentdomain <--- this will tell you the parent domain
-   nltest /dclist:\[domain from first command above\] <--- this will tell you all potential DCs
-   nltest /dsgetdc:\[Pick on if the DNS name from above list\] <--- this will tell you information about that DC, like IP address. 

5) After you write the command in that field, there is related link "test probe".

6) In that select the MID server you want to use and the target IP. (see additional information section below)

7) Run the probe. This will NOT save the value in the field where you put the command (it is not supposed to) but it will execute with that command via ecc queue. 

8) Based on that you can see if the DC you are hitting is the right DC that should be used for orchestration. 

  

## Additional Information

The Command probe can be used to run any command on a MID server to a target IP or on the MID itself if you select 127.0.0.1 (loopback) as the target.
