---
title: "Why do my integrations via MID Servers sometimes take up to 40 seconds longer to run, or timeout?"
aliases:
  - KB0695359
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695359
kb_number: KB0695359
last_modified: 2024-04-07
---

## Why do my integrations via MID Servers sometimes take up to 40 seconds longer to run, or timeout?

  

### Issue

You may find Integrations, such as REST or SOAP Message via MID Server, LDAP or Import Sets etc., **which would normal take a second or two, take longer to run than usual**. After looking at the ecc\_queue Output records, and comparing the Created time with the Processed time, you may see a delay in the MID Server picking up the job of **up to around 40 seconds**. 

This can be a big problem if you are doing the bad practice of waiting in a script for a response to a MID Server job. MID Servers may sometimes take longer than usual, and this causes instance threads to be blocked, which can quickly lead to a backlog and performance issue for the whole instance. RESTMessageV2 allows you to do that, even though you shouldn't. Instead execute the message 'async' and allow your script to end at that point, and write a 'sensor' ecc\_queue business rule to read the response instead (which is how Discovery and Orchestration do it).

### Release

Helsinki and later, which is when the AMB Channel was implemented, and the default fallback Polling time was set at 40s.

### Cause

The **AMB Channel may have disconnected** for some reason. This is the real-time connection from the MID Server to the Instance, which lets the MID Server know when new jobs have been created for it.

The MID Server Agent log will show all instances of when the AMB Channel has had to reconnect, and where it fails to.

08/15/18 21:24:45 (404) ECCQueueMonitor.40 WARNING \*\*\* WARNING \*\*\* Reconnecting AMB channel..
08/15/18 21:24:45 (404) ECCQueueMonitor.40 Initializing AMB client...
08/15/18 21:24:45 (405) AMBClientProvider Connecting AMB client to instance...
08/15/18 21:24:45 (468) AMBClientProvider WARNING \*\*\* WARNING \*\*\* **Unable to subscribe to AMB channel**: /mid/server/bd27969913068bc036aff4d2e144b0a7

If your timeout set for the job assumes the job will be run immediately, and is shorter than the time it takes the MID Server to notice and run the job, then it will timeout. Otherwise the job will still run, but be delayed starting.

### Resolution

There may be many potential causes of "Unable to subscribe to AMB channel". It could be a problem with network conditions or devices between the MID Server and Instance interfering with the connection/session which would need investigating. There may be exceptions or further errors in the agent or wrapper log of the MID Server that may help explain it.

There have been some known problems with the AMB Channel in general, and specifically for MID Servers in certain network environments which can be seen in the release notes. Most are already resolved for most customers, so it is worth applying the current patch to your instance to discount those first.

Workaround:

1.  **Restarting the MID Server** is one way to force it to attempt to reconnect the AMB Channel. That may be all that needs doing if the cause was a temporary network issue that is now resolved.
2.  If you simply **cannot get the AMB Channel working, you can turn it off**, and the pre-Helsinki behavior will be used. With this MID Server Parameter set, the poll time will be 5s by default, and no attempt will be made to create an AMB connection.  
    **mid.disable\_amb=true**
3.  If the AMB channel is intermittent, and does work most of the time, then instead of turning it off, you can **set the poll time to 5s so that if the AMB channel is down then it will poll every 5 seconds**, instead of the default 40s. You can reduce that to 5 seconds by setting the MID Server Parameter:**  
    mid.poll.time=5**
