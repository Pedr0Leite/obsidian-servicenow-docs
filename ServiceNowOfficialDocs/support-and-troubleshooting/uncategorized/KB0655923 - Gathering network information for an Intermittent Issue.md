---
title: "Gathering network information for an Intermittent Issue "
aliases:
  - KB0655923
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0655923
kb_number: KB0655923
last_modified: 2024-01-03
---

## Gathering network information for an Intermittent Issue

  

### Issue

This article gives a quick explanation on how to gather client-side network information so that Technical Support can diagnose intermittent issues which are not logged in the Application Log Files.

### Cause

This usually applies to cases that may be being caused by console errors or network issues.

### Resolution

# Procedure (Chrome)

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 845px;" align="left"><tbody><tr><td style="text-align: center; width: 28.8px;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="text-align: left; width: 801.6px;"><strong>Note</strong>: You can take similar steps in other browsers but the buttons might be slightly different. Note that you cannot copy HAR from Internet Explorer.</td></tr></tbody></table>

1.  In the tab in which you want to reproduce the issue, go to **Chrome Options** (top right corner) **\> More Tools > Developer Tools**.
    
2.  Click the Options menu (three dots) in the top right of the Developer Tools and select the option to **Undock in a Separate Window**.
    
    This choice enables you to have the tools in the background without disrupting your work.
    
3.  Select the Network tab at the top of the developer tools.
    
4.  Check the **Preserve Log** checkbox.
    
    This setting will gather all network traffic for that specific tab in Chrome so you need to complete these steps in the tab that has the issue. At that point, you can move the dev tools to the background.
    
    ![](sys_attachment.do?sys_id=c05d344d97abb9d0539e35d11153afa3)
    
5.  Once the issue happens, right-click on the network section where the request name is and choose to **Save a HAR with content.**
    
    This file will be larger depending on the time you have the tools open. Therefore, if the issue is intermittent, try to clear out the log every few minutes by clicking the **Clear** button.
    
    ![](sys_attachment.do?sys_id=085d744d97abb9d0539e35d11153af6d)
    

# Procedure (Firefox)

1.  Press **Ctrl+Shift+E** to display the Network developer tool.
    
2.  Reproduce the issue.
    
3.  Right-click anywhere in the resulting waterfall and choose **Save as HAR** in the context menu.
    
    Make sure to add the file extension .har to the filename.
    

# Procedure (Edge)

1.  Press the F12 key.
    
    A component appears at the bottom of the screen.
    
2.  Click the Network tab and press the green triangle, Play button.
    
3.  Reproduce the issue.
    
4.  To save, press the red square, Stop button, and click the disk arrow icon directly to the right.
    
    <table style="width: 805.213px;" align="left"><tbody><tr><td><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td>Only Microsoft Edge supports the HAR format. IE offers export only as an XML or CSV file. You can view CSV files in a spreadsheet tool such as Excel, or view XML files in any tool that can read HTTP Archive files, such as the Chrome extension HTTP Archive Viewer</td></tr></tbody></table>
    

# Procedure to view the HAR file log(Chrome)

To view the HAR file log, you need a viewer application.

1.  Install the Google Chrome extension HTTP Archive Viewer or download this viewer from [http://www.softwareishard.com/har/viewer/](http://www.softwareishard.com/har/viewer/) .
2.  Remove the checkmark from **Validate data before processing?** 
3.  Drag the HAR file inside the **Preview** box.
