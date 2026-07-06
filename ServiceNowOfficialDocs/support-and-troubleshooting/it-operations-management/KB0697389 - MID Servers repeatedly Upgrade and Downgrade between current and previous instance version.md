---
title: "MID Servers repeatedly Upgrade and Downgrade between current and previous instance version"
aliases:
  - KB0697389
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697389
kb_number: KB0697389
last_modified: 2026-06-16
---

## MID Servers repeatedly Upgrade and Downgrade between current and previous instance version

  

### Issue

After an instance upgrade, patch or hotfix, the MID Servers should upgrade themselves to match. MID Servers may upgrade to the new version, but then over the next hours or days downgrade again. They may then repeat that cycle. While upgrading/downgrading the MID Server will be unavailable. While the version is mismatched there is a chance of functional issues or data loss due to the version/API mismatches.

Australia update:  
Regardless of what the appnodes or properties are reporting the mid server version to be, the assigned JRE is hard-coded in the new version of the MIDAssignedPackages soap service record, and so the JRE will upgrade and then stay upgraded even after the mid server application then downgrades. The mismatch of MID Server application version and Java JRE version can cause the MID Server to go down after it has downgraded.

This has been seen for a Zurich (JRE 17) to Australia (JRE 21) upgrade. MID Server's Agent log on startup, after downgrading, will confirm if this has happened:

2026-06-03T09:46:18.163-0400 INFO  (MIDServer) \[Main:292\] Initializing MID Server
2026-06-03T09:46:18.165-0400 INFO  (MIDServer) \[Main:307\] Running under Java version: 21.0.7-sncmid1, java PID: 14416, args: start
2026-06-03T09:46:18.182-0400 WARN  (MIDServer) \[Main:209\] Detected JRE version 21.0.7-sncmid1 does not meet the recommended version. Please consider updating to 17.0.15 (or later). For more information, please see KB0719830.
2026-06-03T09:46:18.201-0400 ERROR (MIDServer) \[Bootstrapper:57\] terminating due to fatal error
java.lang.UnsupportedOperationException: The Security Manager is deprecated and will be removed in a future release
	at java.base/java.lang.System.setSecurityManager(System.java:430)
	at com.snc.llama.jvm.internal.SystemPassthrough.setSecurityManager(SystemPassthrough.java:39)
	at com.service\_now.mid.Main.initJvmSecurityManager(Main.java:287)
	at com.service\_now.mid.Main.run(Main.java:147)
	at com.snc.llama.bootstrap.api.Bootstrapper.run(Bootstrapper.java:52)
	at com.snc.llama.thirdparty.guice.boot.api.GuiceBootstrapper.run(GuiceBootstrapper.java:27)
	at com.service\_now.mid.Main.doStaticStartRequest(Main.java:547)
	at com.service\_now.mid.Main.doStaticCommandDispatch(Main.java:515)
	at com.service\_now.mid.Main.main(Main.java:122)
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
	at java.base/java.lang.reflect.Method.invoke(Method.java:580)
	at org.tanukisoftware.wrapper.WrapperStartStopApp.run(WrapperStartStopApp.java:429)
	at java.base/java.lang.Thread.run(Thread.java:1583)

2026-06-03T09:46:18.204-0400 INFO  (MIDServer) \[Bootstrapper:60\] the ServiceNow MID Server is now terminated

### Release

Any. Has been seen up to at least Australia.

### Cause

Most instances are made up of more than one application node. The load balancer will share the incoming requests from MID Servers among them, making it random which node a MID Server is currently connected to.

When an instance upgrades, each of those nodes is upgraded and restarted in turn to avoid an outage, **but if something goes wrong then a node may remain running the previous version**, and report that previous version to the MID Server when the MID Server checks what version it should be running. PRB1299098 and PRB1278372 have been known to cause this prior to the Madrid release, but once upgraded to Madrid you won't see those again.

The situation where not all appnodes are on the same version might also happen after an AHA transfer, some time after an instance upgrade, where standby nodes come into use, and a standby nodes (which now becomes an active one) was on an old version still.

The Stats page (/stats.do) is specific to the node, and the clue is that you may see the previous version still reported on that page. It is not usually possible to select which node you log into so having several of your users check stats.do may be required before you see all the nodes. 

The "Upgrade Monitor" page "Node Upgrades" section, will also show if any nodes are not upgraded.

## Example:

These are the bits from the top of the /stats.do pages from a normal 2 node instance, which was upgraded from "Kingston Patch 6" to "Kingston Patch 6 Hotfix 5" on Sep 01.

Note how this node 001 reports the correct version, and indicates that it was restarted as part of the upgrade process on Sep 01. A MID Server connecting to this node will Upgrade.

Statistics for: Demo Server @ appXXXXXX.iadXXX.service-now.com:16054 at: Wed Sep 05 06:17:09 PDT 2018 (Refresh)  
Connected to cluster node: appXXXXXX.iadXXX.service-now.com:**instancename001**  
Build name: Kingston  
Build date: 07-31-2018\_0903  
Build tag: glide-**kingston-10-17-2017\_\_patch6-hotfix5**\-07-28-2018  
Instance name: **instancename  
**Instance ID: 123456510a0a3c560094215d720219d5  
Node ID: 3d27d8123456c66530025f6c009930cb  
IP address: 10.XX.XX.XX  
MID buildstamp: kingston-10-17-2017\_\_patch6-hotfix5-07-28-2018\_07-31-2018\_0903  
  
**Servlet Statistics**  
**Started: Sat Sep 01 13:24:13 PDT 2018**

This is node 002, and is still reporting the previous version. It was not restarted on the day of the upgrade. The MID Server will not upgrade after the instance upgrade, or downgrade again, if it happens to connect to this node.

Statistics for: Demo Server @ appXXXXXX.iadXXX.service-now.com:16047 at: Wed Sep 05 06:17:10 PDT 2018 (Refresh)  
Connected to cluster node: appXXXXXX.iadXXX.service-now.com:**instancename002**  
Build name: Kingston  
Build date: 05-24-2018\_1317  
Build tag: glide-**kingston-10-17-2017\_\_patch6**\-05-16-2018  
Instance name: **instancename**  
Instance ID: 123456510a0a3c560094215d720219d5  
Node ID: 3d27d8123456c66530025f6c009930cb  
IP address: 10.XX.XX.XX  
MID buildstamp: kingston-10-17-2017\_\_patch6-05-16-2018\_05-24-2018\_1317  
  
**Servlet Statistics**  
Started: Fri Aug 17 10:39:52 PDT 2018

### Resolution

This is not something customers should try to resolve themselves. Please open a Case with Customer Support to have the Instance Upgrade issue fixed.

Once all nodes are reporting the current version, then the MID Servers will upgrade to that version too, and stay that way.

Temporary adding a MID Server Properties record for mid.pinned.version would prevent the MID Servers downgrading to the previous version. Once instance appnodes are all upgraded, that would need to be deleted again.

If the MID Server is down due to a JRE version mismatch after downgrading again, there are 2 solutions, to allow the MID Server to get back up, at which point it can then upgrade again.  The first is specific to pre-Australia to Australia.  The second should work in general.

-   Add a line to wrapper.conf, to workaround the deprecated java class in Java 21, that the pre Australia mid server expects:  
      
    wrapper.java.additional.150=-Djava.security.manager=allow   
      
    Note: Don't edit wrapper-override.conf. Wrapper.conf will get replaced with the OOTB version as soon as the MID Server comes up and upgrades, so it is allowed to edit wrapper.conf in this specific situation.  
      
    
-   Replace the agent/jre folder with one from the previous version. Links to JRE zip files for several versions are in [KB0719830](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719830). The jre/lib/security/cacerts file would first need backing up, and replacing after the JRE folder is replaced.
