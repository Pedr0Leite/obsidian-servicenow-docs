---
title: "When Exporting a file. How to Check the size of a file which is being downloaded"
aliases:
  - KB0657509
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657509
kb_number: KB0657509
last_modified: 2024-04-07
---

## When Exporting a file. How to Check the size of a file which is being downloaded

  

### Issue

How to check the size of a file downloading

# General Information

* * *

When using the export feature to export a file it can take some time to download depending on the size of the file. Whenever using any of the options within export the file is saved within the sys\_attachment table

  

## Example:

1.  Navigate to the file to download. In this instance, all active users are exported to XML

![Export to XML example](export%20to%20xml.pngx "Export to XML example")

2\. If navigating to the browser's downloads, determine the name of the file

![File Fownloaded](Screen%20Shot%202018-02-15%20at%205.46.35%20PM.pngx "File Fownloaded")

3\. Whilst the file is downloading, the session is locked so it is not possible to navigate to another area of the application. Open a new browser and login to the instance of login to the instance again using the browser's incognito mode

[How to open google chrome in incognito mode](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DDesktop&hl=en-GB "How to open google chrome in incognito mode") 

4\. Navigate to the sys\_attachment table, provided appropriate roles/security rights are available to access the table, and search for the attachment

To perform this task, enter sys\_attachment.list in the filter of the instance

![filter example](Screen%20Shot%202018-02-15%20at%206.02.12%20PM.pngx "filter example") 

5\. Search for the attachment using the filter:

In the example, the following filter options were used:

\-> created on today

\-> file name = the name fo the file i dowloaded (see step2)

\-> created by = my user ID

  

![attachment information](sys_attachment.do?sys_id=72ae74a2db0ab450e515c2230596197e "attachment information") 

 The attachment table contains a field named **Size in bytes** which contains the size of the attachment you downloaded in bytes
