---
title: "Mid Server issue after clone and upgrade: \"Unable to subscribe to AMB channel: /mid/server/<sys_id>\""
aliases:
  - KB0814684
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814684
kb_number: KB0814684
last_modified: 2024-04-08
---

## Mid Server issue after clone and upgrade: "Unable to subscribe to AMB channel: /mid/server/"

  

### Issue

When finding the warning "Unable to subscribe to AMB channel: /mid/server/<sys\_id>", specially if the error is present with all the mid servers in the same Environment after an upgrade following a clone.

Agent log message will look like below:

2020-02-18 09:08:43 (019) StartupSequencer Initializing AMB client...  
2020-02-18 09:08:43 (023) AMBClientProvider Connecting AMB client to instance...  
...  
2020-02-18 09:08:43 (796) StartupSequencer StartupSequencer: setting sysId: <sys\_id>, command: sudo, password prompt: as default privileged command  
...  
2020-02-18 09:08:43 (930) AMBClientProvider WARNING \*\*\* WARNING \*\*\* Unable to subscribe to AMB channel: /mid/server/<sys\_id>  
...  
2020-02-18 09:09:50 (264) ECCQueueMonitor.40 WARNING \*\*\* WARNING \*\*\* Reconnecting AMB channel..

And repeats again...

2020-02-18 09:09:50 (265) ECCQueueMonitor.40 Initializing AMB client...  
2020-02-18 09:09:50 (272) AMBClientProvider Connecting AMB client to instance...

### Release

-   Any release that uses AMB (Helsinki and later, which is when the AMB Channel was implemented).
-   This issue is related to the clone performed in the instance combined to the version upgrade of the MID server.

### Cause

After a clone in the instance and upgrade. Once the MID server has upgraded accordingly the combination of a new upgraded version in the mid with an old key in the instance side made the issue appear.

### Resolution

The solution to this issue is to rekey the MID server, using the steps described in [Rekey a MID Server](https://docs.servicenow.com/csh?topicname=t_RekeyAMIDServer.html&version=latest "Rekey a MID Server")
