---
title: "How to use Script Debugger for Script Includes"
aliases:
  - KB0696131
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696131
kb_number: KB0696131
last_modified: 2024-12-17
---

## Issue

When troubleshooting sensors and script include it's not possible by default to use the built-in Script Debugger with breakpoints. This is because the breakpoints are in the context of the user session. When Discovery is executing sensor processing on probes, however, it's using the MID user session or the Scheduled Job system user session, so the breakpoints will never be tripped. This results in having to manually add a lot of system logging commands to the scripts and then having to revert them, creating additional tedium.

The following script can be executed in the background to launch the probe sensor processing in your user session so that breakpoints and the Script Debugger can be utilized.

## Resolution

1.  Set up breakpoints in Script Include and activate Script Debugger
2.  Copy sysID of Probe input record that user wishes to debug the sensor processing for
3.  Go to Scripts Background
4.  Execute the following script, substituting in the correct value:  
    
    var sysId = "ENTER SYSID HERE";   
    var ecc = new GlideRecord("ecc\_queue");  
    if (ecc.get(sysId)) {  
      var ssp = new SncSensorProcessor(ecc);  
      ssp.process();  
    }
    
5.  Debug/troubleshoot as needed
