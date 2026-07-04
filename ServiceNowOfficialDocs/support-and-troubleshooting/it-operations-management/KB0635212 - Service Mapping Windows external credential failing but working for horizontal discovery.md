---
title: "Service Mapping Windows external credential failing but working for horizontal discovery "
aliases:
  - KB0635212
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635212
kb_number: KB0635212
last_modified: 2024-04-07
---

## Issue

# Issue

* * *

The WMI call randomly fails during the first attempt. Use the workaround in this article to ignore the first attempt so that all subsequent calls are successful.

# Workaround

* * *

1.  In the DiscoveryHostUtils script include, add the following code after line 85.
    
      
    if (sysClassName == 'cmdb\_ci\_win\_server')   
    return 'WINDOWS';
    
2.  Create a new external discovery command (sa\_mapping\_ext\_commands.list).
    
    var logger = Packages.com.snc.sw.log.DiscoLog.getLogger('ProcessOnPortWindows-issue');   
    logger.debugex("Executing dummy query");   
    wmi.lockPermissionProblems(true);   
    try {   
    wmi.executeQuery('select \* from win32\_computersystem');   
    } catch (e) {}   
    wmi.lockPermissionProblems(false);   
    output = 'null';
    
3.  Restart the MID Server for the changes to take effect
