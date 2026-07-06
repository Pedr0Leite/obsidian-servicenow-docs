---
title: "Discovery.device.complete events take a long time to process which causes the event queue to be backed up"
aliases:
  - KB0748609
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748609
kb_number: KB0748609
last_modified: 2025-09-09
---

## Discovery.device.complete events take a long time to process which causes the event queue to be backed up

  

### Issue

Discovery.device.complete events may take a long time to process, which causes the event queue to be backed up.

### Release

All currently supported releases.

### Cause

## **Layer 3 mapping**

The discovery.device.complete event is created when the discovery of a device completes. This event is used to trigger post discovery processing. The post discovery could include layer 3 connections, or possibly custom operations. Creating 3 relationships requires a lot of processing, going through different tables etc.

See the following documents for more information about  layer 3 mapping:

-   [Router and switch discovery](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoNWRouteAndSwitch.html&version=latest "Router and switch discovery")

The layer 3 discovery creates "IP Connection" relationships which can be seen on the BSM. To view these relationships, open the dependency view for the CI. On the dependency view from one of the CIs select the "Physical Network Connections" option for the "Dependency Type" in the map settings.

The layer 3 relationship provides a logical mapping of the TCP/IP layer for network gears. It loops through the IP addresses of the discovered CI. For each IP address, it searches for router interfaces of classes cmdb\_ci\_ip\_switch and cmdb\_ci\_ip\_router where lo\_ip <= IP address <= hi\_ip. If a match is found, a relationship is created from the router/switch to the CI.

Example stack excerpt seen when the issue is due to layer 3 mapping:

org.mozilla.javascript.gen.sys\_script\_include\_0aa00c84ef52210098d5925495c0fb7a\_script\_3781766.\_c\_anonymous\_5(sys\_script\_include.0aa00c84ef52210098d5925495c0fb7a.script:105)  
org.mozilla.javascript.gen.sys\_script\_include\_0aa00c84ef52210098d5925495c0fb7a\_script\_3781766.call(sys\_script\_include.0aa00c84ef52210098d5925495c0fb7a.script)  
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2651)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)  
org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
org.mozilla.javascript.gen.sys\_script\_include\_0aa00c84ef52210098d5925495c0fb7a\_script\_3781766.\_c\_anonymous\_2(sys\_script\_include.0aa00c84ef52210098d5925495c0fb7a.script:27)  
org.mozilla.javascript.gen.sys\_script\_include\_0aa00c84ef52210098d5925495c0fb7a\_script\_3781766.call(sys\_script\_include.0aa00c84ef52210098d5925495c0fb7a.script)  
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2651)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)  
org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
org.mozilla.javascript.gen.sysevent\_script\_action\_479933b7ef42210098d5925495c0fb96\_script\_3473637.\_c\_anonymous\_1(sysevent\_script\_action.479933b7ef42210098d5925495c0fb96s.cript:18)  
org.mozilla.javascript.gen.sysevent\_script\_action\_479933b7ef42210098d5925495c0fb96\_script\_3473637.call(sysevent\_script\_action.479933b7ef42210098d5925495c0fb96.script)  
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2651)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)  
org.mozilla.javascript.optimizer.OptRuntime.call0(OptRuntime.java:23)  
org.mozilla.javascript.gen.sysevent\_script\_action\_479933b7ef42210098d5925495c0fb96\_script\_3473637.\_c\_script\_0(sysevent\_script\_action.479933b7ef42210098d5925495c0fb96.script:1)  
org.mozilla.javascript.gen.sysevent\_script\_action\_479933b7ef42210098d5925495c0fb96\_script\_3473637.call(sysevent\_script\_action.479933b7ef42210098d5925495c0fb96.script)  
org.mozilla.javascript.gen.sysevent\_script\_action\_479933b7ef42210098d5925495c0fb96\_script\_3473637.exec(sysevent\_script\_action.479933b7ef42210098d5925495c0fb96.script)

**CI with large number of IP Addresses**

Some CIs may contains multiple IP addresses, dozens or more. If a device is discovered via multiple interfaces, each interface will trigger a device.discovery.complete event. Since the processing, layer 3 for example, loops through the IP addresses of the CI discovered there is a geometric increase in processing in relation to the number of IP addresses of a given CI when such CI is discovered via all interfaces on the same discovery status.

**Find CIs which had discovery.device.complete events triggered multiple times**

**Note**: Always test any script in non-production first.

1.  Navigate to scripts - background, "System Definition > Scripts - Background".
2.  Run script:  
    
    var ga = new GlideAggregate('discovery\_device\_history');  
    ga.addAggregate('count', 'cmdb\_ci');  
    ga.orderByAggregate('count', 'cmdb\_ci');  
    ga.orderBy('cmdb\_ci');  
    ga.addQuery('sys\_created\_on','>=','javascript:gs.beginningOfToday()');  
    ga.addQuery('sys\_created\_on','<=','javascript:gs.endOfToday()');  
    ga.addNotNullQuery('cmdb\_ci');  
    ga.addHaving('count','>','50');  
    ga.query();   
    while (ga.next()) {  
    gs.print(ga.getValue('cmdb\_ci') + ' ' + ga.getAggregate('count', 'cmdb\_ci'));  
    }
    
3.  Result will display list of CIs which had over 50 device histories triggered on today.

**Find discovery.device.complete events which took a long time to process**

1.  Navigate to sysevent table, "System Logs > Events".
2.  Show events where field name = discovery.device.complete.
3.  Sort by "Processing Duration" to get the events which took the longest to process.
4.  Event Parm1 is the sys\_id of the discovery\_device\_history record.
5.  Event Parm2 is the sys\_id of the discovery\_status record.
6.  The cmdb\_ci for which L3 mapping took long to process can be found in the discovery\_device\_history record.

### Resolution

**Turn off L3 Mapping:**

Often the relationships created by layer 3 mapping are not clear to the team managing the CMDB. The layer 3 mapping can be turned off via system property glide.discovery.L3\_mapping (set the value to false). The impact would be that such relationships would no longer be created.

NOTE: If you need to turn off this L3 Mapping to provide relief, do not do it for extended period of time (weeks). Cumulative changes in the network could cause events processing after re-enabling to be slow.

**Create a dedicated queue for discovery.device.complete**

Open a support incident to have our Performance team create a separate event queue only for “discovery.device.complete” events, so that a delay in processing these events do not create a backlog for other system events. Performance team to evaluate the correct number of Jobs for dedicated queue based on event generation rate and historical events processing rate.

**Stop duplicated L3 mapping for the same CI**

Update the discovery.device.complete script actions, "System Policy > Events > Script Actions", to check on the last\_state of the discovery device history. If the last state is "Identified, ignored extra IP" there should be no need to process this event, as it is already processed via another discovery device history event.

For example, add following to script action "Discovery - map device to netgears":

var lastState = current.last\_state;  
if (lastState == "Identified, ignored extra IP"){  
return;  
}

Script action "Discovery - map device to netgears" start would look like:

(function() {  
var ciid = current.cmdb\_ci + '';  
if (!ciid)  
return;  
  
var lastState = current.last\_state;  
if (lastState == "Identified, ignored extra IP"){  
return;  
}

**Apply patches which resolve issues regarding slow processing of "discovery.device.complete" events:**

There have been several Known Problems which could cause slowness when processing discovery.device.complete events. Check the following articles to make sure you are not affected by them:

-   PRB1319185: Performance improvements for the layer 2 connections algorithm
-   PRB1309396: Issues with the event queue performance due to slow discovery.device.complete events
-   PRB1371401: Script Include 'DeviceL3Mapping' may trigger slow queries on CMDB
-   PRB1334573: If the macAddress parameter is empty or null, a query will display all ports
-   PRB1397581: Discovery.device.complete events may take a long time to process when CI has large number of IP addresses
-   PRB1459906: "Queue layer 2 connection calculations" script action causes delay in sysevent processing

### Related Links

Other knowledge articles which relate to discovery.device.complete:

-   [discovery.device.complete events take long time to process because of unnecessary IP range set](https://support.servicenow.com/kb_view.do?sysparm_article=KB0727785 "discovery.device.complete events take long time to process because of unnecessary IP range set")
-   [Discovery: Troubleshooting - DeviceL3Mapping](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598422 "Discovery: Troubleshooting - DeviceL3Mapping")
