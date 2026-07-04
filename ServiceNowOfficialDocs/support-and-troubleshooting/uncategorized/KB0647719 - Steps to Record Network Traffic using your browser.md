---
title: "Steps to Record Network Traffic using your browser"
aliases:
  - KB0647719
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647719
kb_number: KB0647719
last_modified: 2024-01-03
---

## Steps to Record Network Traffic using your browser

  

### Issue

Many problems are not visible by only looking at the instance logs. Some problems can be captured in the network traffic between the browser and the relevant services. For example, instance, Identity providers, chat services, etc.  

One troubleshooting method that can help to narrow down what is happening on the client side is to record the details of the network traffic so it can be analyzed later.

You may benefit from providing a recording of the network traffic if you are having problems on:  

-   Chat
-   Live feed
-   SAML/SSO
-   Connect
-   AMB
-   Presence
-   Global search
-   Interfaces using REST against the instance
-   Problems related to network traffic

### Resolution

One popular method is creating a HAR file, HTTP Archive that captures the reproduced steps.  
  
Here are the steps to performs on Chrome, Firefox or Internet Explorer:

**Chrome**

1.  From the Chrome menu in the top right corner, choose **Tools** \> **Developer Tools**.
2.  Click the **Network** tab.
3.  Reproduce the problem.  
    Important: The log would clear every page open. If the logs need to be preserved, click the **Preserve log** checkbox below the tabs.
4.  If the time lags, navigate to the Developer tool, right-click the entry, and choose **Save As HAR with Content** from the context menu.

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Warning" src="/Warning_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Warning</strong>: Make sure to add the file extension .har to the filename.</td></tr></tbody></table>

**Firefox**

1.  Press **Ctrl+Shift+E** to display the Network developer tool.
2.  Reproduce the issue.
3.  Right-click anywhere in the resulting waterfall and choose **Save as HAR** in the context menu.  
    Make sure to add the file extension .har to the filename.

**Internet Explorer**

1.  Press the F12 key. A component appears at the bottom of the screen.
2.  Click the Network tab and press the green triangle, Play button.
3.  Reproduce the issue.
4.  To save, press the red square, Stop button, and click the disk arrow icon directly to the right.

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4">Only Microsoft Edge supports the HAR format. IE offers export only as an XML or CSV file. You can view CSV files in a spreadsheet tool such as Excel, or view XML files in any tool that can read HTTP Archive files, such as the Chrome extension HTTP Archive Viewer</td></tr></tbody></table>

**  
To View the HAR file log**

To view the HAR file log, you need a viewer application.

1.  Install the Google Chrome extension HTTP Archive Viewer or download this viewer from [http://www.softwareishard.com/har/viewer/](http://www.softwareishard.com/har/viewer/) .
2.  Remove the checkmark from **Validate data before processing?** 
3.  Drag the HAR file inside the **Preview** box.
