---
title: "Schedule flows on weekdays only"
aliases:
  - KB0961745
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961745
kb_number: KB0961745
last_modified: 2025-08-28
---

## Schedule flows on weekdays only

  

### Summary

The Flow Designer daily trigger runs flows every day, but you can use a scheduled job with a subflow to run flows only on weekdays. This article explains the solution.

### Release

All supported releases

### Instructions

The daily trigger does not support excluding weekends. To run flows only on weekdays, create a subflow and trigger it from a scheduled job. The subflow runs via script, and the scheduled job provides more scheduling flexibility.

1.  Create and publish a subflow.
2.  Create a scheduled job that runs daily.
3.  To run the job only on weekdays, add this condition:  
      
    var answer = false;   
    var now = new GlideDateTime();   
    if(now.getDayOfWeek() < 6){   
    answer = true;   
    }   
    answer;  
      
    
4.  Add this script to the scheduled job:  
      
    var inputs = {};   
    var contextId = sn\_fd.FlowAPI.startSubflow('global.CS5405755', inputs);
