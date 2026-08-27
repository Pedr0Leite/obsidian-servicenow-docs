---
title: "How to configure SCCM Import to use IRE (Identification and Reconciliation Engine) and Datasource Precedences"
aliases:
  - KB0721378
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721378
kb_number: KB0721378
last_modified: 2024-02-07
---

## How to configure SCCM Import to use IRE (Identification and Reconciliation Engine) and Datasource Precedences

  

### Issue

Out of the box, IRE (Identification and Reconciliation Engine) is partially used by SCCM, in transform map "SCCM 2012 v2 Computer Identity".  
It's used in the sys\_id script, to check whether a CI exists. Since it doesn't do update directly, the Datasource Precedence rules are **not** used.

The onBefore script in below link should NOT be used for SCCM  
[Apply CI Identification and Reconciliation to Import Sets](https://docs.servicenow.com/csh?topicname=identification-import-sets.html&version=latest "Apply CI Identification and Reconciliation to Import Sets")

### Workarounds

_Please note: We have developed new SCCM integration that uses IRE and RTE (Robust Transform Engine) (SG-SCCM)._

_Please try to setup new SCCM integration unless you have specific needs to use legacy SCCM._

If the aim is to make sure SCCM doesn't update CIs that were created/updated by Discovery, then the transform maps can be modified to check on the discovery\_source field of the CIs:

if discovery\_source value is 'ServiceNow', which means updated by Discovery, then SCCM will skip this record.

Attached "SCCM 2012 checking discovery\_source.zip" is a demonstration of how this can be achieved.

The demonstration is based on SCCM 2012 v2. 

Below is the list of modifications made:

_\*\*\*Transform Map: SCCM 2012 v2 Computer Identity_   
_modified field mapping sys\_id_   
  
_\*\*\*Transform Map: SCCM 2012 v2 Operating System_   
_modified field mapping sys\_id_   
  
_\*\*\*Transform Map: SCCM 2012 v2 Processor_   
_modified field mapping sys\_id_   
  
_\*\*\*Transform Map: SCCM 2012 v2 Disk_   
_modified transform map script_   
  
_\*\*\*Transform Map: SCCM 2012 v2 Network_   
_modified transform map script_ 

For SCCM 2016, make similar modifications to the relevant files.

### Related Links

[SCCM Integration transforms do not use the 'Identification & Reconciliation' engine for the CI Inserts/Updates, causing e.g. bypassing of the Precedence rules](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831225)
