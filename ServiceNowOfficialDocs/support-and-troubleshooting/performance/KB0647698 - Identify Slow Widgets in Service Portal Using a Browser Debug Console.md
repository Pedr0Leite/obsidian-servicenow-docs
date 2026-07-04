---
title: "Identify Slow Widgets in Service Portal Using a Browser Debug Console"
aliases:
  - KB0647698
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647698
kb_number: KB0647698
last_modified: 2026-03-31
---

## Identify Slow Widgets in Service Portal Using a Browser Debug Console

  

### Issue

To fix slow widgets on a Service Portal page, you can use the debug console within your browser to pinpoint which widgets are causing the delays, and determine if any queries can be optimized to improve their speed. 

### Release

### Resolution

Enable the debug console in your browser to obtain timing information for a widget.:

1.  Open Service Portal. [http://<yourInstance>.service-now.com/sp](http://\<yourInstance\>.service-now.com/sp)
2.  Observe the widgets loading on the page.  
      
    ![example Service Portal widgets](sys_attachment.do?sys_id=b563afb1839626d4cdbbc430feaad32e "example Service Portal widgets")
3.  Open the debug console within the browser:
    -   Firefox:  **Tools > Web Developer > Browser Console > console (sub tab)**
    -   Chrome:  **View > Developer > Developer Tools > console (sub tab)**  
          
        ![firefox web developer console](sys_attachment.do?sys_id=6d636fb1839626d4cdbbc430feaad3e5 "firefox web developer console")
4.  While holding the **Control** key down, select the header of each widget. The timing information is displayed at the top of the pop-out menu **Current Status generated in : 0.004**
    -   You can do this for each widget on the Service Portal. To obtain more detailed information for the widget, complete the remaining steps.
        1.  Select the last option **Log to console: $scope**
            
            ![](sys_attachment.do?sys_id=39636fb1839626d4cdbbc430feaad3e8)
            
        2.  The browser console populates with the widget object.  
              
            ![example console output](sys_attachment.do?sys_id=7d63afb1839626d4cdbbc430feaad32b "example console output")
        3.  Within the Widget instance, expand the Object branch
        4.  Look for the **\_server\_time**.  This is the timing information for that widget.
            
            ![observe the \_server\_time of the widget](sys_attachment.do?sys_id=3563afb1839626d4cdbbc430feaad329 "observe the _server_time of the widget")
            
        5.  To erase all console information, select the Trash Can icon within the browser console. Select another widget if required.

Repeat the process as necessary for each widget and determine which are the slower widgets on that particular Service Portal page.
