---
title: "Discovery status record will never set to complete.  In Discovery Status \"Started\" number has highter value than \"Completed\" value."
aliases:
  - KB0781699
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781699
kb_number: KB0781699
last_modified: 2024-04-08
---

## Discovery status record will never set to complete. In Discovery Status "Started" number has highter value than "Completed" value.

  

### Issue

-   Discovery status record will never set to complete and discovery status shows 5 ECC records started and 4 completed. Had to manually cancel discovery.
-   Linux discovery status shows 5 ECC records started and 4 completed. But there are only 8 records in the ECC queue ! This causes the discovery status record to never be set to complete. 

**Expected Resul**t: Discovery should complete matching the started and completed records.  
**Actual Result**: Discovery never completes and status shows 5 ECC records started and 4 completed.

![](sys_attachment.do?sys_id=938ba3f4db0cb0d016d2a345ca9619a4)

### Release

London Patch 10

### Cause

-   Upon investigating found the instance is trying to trigger 2 probes, but only one of them appears to exist on the instance.
-   It is triggering the "Unix - Application Dependency Mapping" as normal, but is also trying to trigger:
-   "4f64c6389f230200fe2ab0aec32e7068$$$$UNIX Cluster - VERITAS Cluster"
-   Since it can't find this probe it does not fire an ECC queue record, but still updates the status started by 2.

### Resolution

Following changes are made in the script include.  
Script Include name: "**DiscoveryIDSensor**"  
  
~line 384  
**OLD**:  
var probeIDs = ('' + this.getParameter('triggered\_probes')).split(',');  
for (var i = 0; i < probeIDs.length; i++) {  
var probeID = probeIDs\[i\];  
var probe = SncProbe.getById(probeID, this.values);  
if (probe == null)  
continue;  
  
probe.addParameter('ecc\_breadcrumbs', this.getParameter('ecc\_breadcrumbs'));  
probe.addParameter('port', this.getParameter('port') );  
probe.setSource(this.getSource());  
probe.create(this.getAgent(), this.getEccQueueId());  
}  
  
var statusId = g\_probe.getCorrelator();  
DiscoveryStatus.updateStatusStartedCount(statusId, parseInt(probeIDs.length));  
  
**Replace with below code**:  
var launchedProbes = 0;  
var probeIDs = ('' + this.getParameter('triggered\_probes')).split(',');  
for (var i = 0; i < probeIDs.length; i++) {  
var probeID = probeIDs\[i\];  
var probe = SncProbe.getById(probeID, this.values);  
if (probe == null) {  
gs.info("Probe with ID " + probeID + " was not found and will not be launched");  
continue;  
}  
  
probe.addParameter('ecc\_breadcrumbs', this.getParameter('ecc\_breadcrumbs'));  
probe.addParameter('port', this.getParameter('port') );  
probe.setSource(this.getSource());  
probe.create(this.getAgent(), this.getEccQueueId());  
launchedProbes += 1;  
}  
  
var statusId = g\_probe.getCorrelator();  
DiscoveryStatus.updateStatusStartedCount(statusId, parseInt(launchedProbes));  
  
**Save Script Include and run discovery.**

  
**Expected Result**: Discovery should complete with Started and Completed matching.  
**Actual Result**: Discovery completed successfully with started and completed records matching.

![](sys_attachment.do?sys_id=9f8ba3f4db0cb0d016d2a345ca9619a1)
