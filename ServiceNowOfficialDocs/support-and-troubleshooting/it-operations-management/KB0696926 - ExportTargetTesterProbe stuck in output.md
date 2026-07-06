---
title: "ExportTargetTesterProbe stuck in output"
aliases:
  - KB0696926
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696926
kb_number: KB0696926
last_modified: 2024-04-07
---

## ExportTargetTesterProbe stuck in output

  

### Issue

# Symptoms

* * *

MID Server does not pick up 'ExportTargetTesterProbe' output probes when testing Export Sets using MID Server

# Release

* * *

Kingston

#   

# Cause

* * *

On startup MID server makes a call to GetMIDInfo Scripted Soap Service on the instance to get check it's own validity. GetMIDInfo Scripted Soap Service wasn't upgraded for a while because it is modified a few years back. The old version is not compatible with Kingston's code thus no valid data is sent back to the MID Server prevented from validate itself. Due to this MID Server cannot go into full operational mode and won't pickup non-system probes which includes 'ExportTargetTesterProbe'.

# Resolution

* * *

1.  Goto System Web Services > Scripted Web Services > Scripted Soap Service > GetMIDInfo
2.  Revert the service to OOB version for Kingston.
3.  Restart MID Server

#
