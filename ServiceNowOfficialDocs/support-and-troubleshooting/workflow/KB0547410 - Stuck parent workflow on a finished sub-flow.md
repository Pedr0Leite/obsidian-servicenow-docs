---
title: "Stuck parent workflow on a finished sub-flow"
aliases:
  - KB0547410
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547410
kb_number: KB0547410
last_modified: 2026-05-19
---

## Stuck parent workflow on a finished sub-flow

  

### Issue

Stuck parent workflow on a finished sub-flow

### Symptoms

The parent workflow is stuck. Sub-flow has finished but the parent workflow is still waiting on the sub-flow activity.  

### Release

Probably any.

### Cause

Exception caused after the sub-flow has completed.   

### Resolution

This pushes the parent workflow forward signaling that the sub-workflow has finished.  

1.  Get the sys\_id of the completed sub-flow context.
2.  Get the sys\_id of the finished context. 
3.  Copy the sys\_id of the record.
4.  Navigate to wf\_context table.
5.  Choose ID field from the filter and place the sys\_id of the record.  
    This gathers all the contexts attached to the record.
6.  Locate the finished sub-flow and run the script below:  
    
    stuckSubFlow('SYS\_ID');  // <<<<<<<<<Place the sys\_id of finished sub-flow here>>>>>>>>>>>>
    
    function stuckSubFlow(subFlowSysId){  
      
    var gr = new GlideRecord('wf\_context');  
    gr.addQuery("sys\_id",subFlowSysId);  
    gr.query();  
    if (gr.next()) {  
    gs.print("Processing Flow for: " + gr.id.getDisplayValue()+ "\\n Workflow Name: " +gr.workflow\_version.getDisplayValue());  
    new Workflow().handleSubflowComplete(gr);  
       }  
    }
