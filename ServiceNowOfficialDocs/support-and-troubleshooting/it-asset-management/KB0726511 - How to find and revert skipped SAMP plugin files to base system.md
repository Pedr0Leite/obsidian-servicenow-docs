---
title: "How to find and revert skipped SAMP plugin files to base system"
aliases:
  - KB0726511
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726511
kb_number: KB0726511
last_modified: 2026-02-05
---

## How to find and revert skipped SAMP plugin files to base system

  

### Issue

After you activate SAMP or its related plugins, you may receive an email about reverting customizations. You need to find the skipped files in your instance to validate and revert them to base system. This article shows you how to find and revert skipped files related to SAMP plugins and their dependent plugins.

### Release

Madrid and later

### Cause

The Revert Customizations module is located in the Software Asset application under Administration. To access it, go to All > Software Asse > Administration > Revert Customizations. This page provides a list of all customization files that you can review and revert.

![List of Software Asset Skipped Files](/sys_attachment.do?sys_id=3373684f9732b2d45ad8f6e11153afb8 "List of Software Asset Skipped Files")

### Resolution

### Method 1: Use the Revert to Base System action

1.  Go to All > Software Asset > Administration > Revert Customizations.
2.  Select the files you want to revert or select all skipped files.
3.  Select the Actions menu at the bottom of the page.
4.  Select Revert to Base System.

![Screenshot of 'Revert to Base System' option in list](/sys_attachment.do?sys_id=b373a84f9732b2d45ad8f6e11153af1d "Screenshot of 'Revert to Base System' option in list")

### Method 2: Manually revert files when base files are missing

If you do not see the Revert to Base System action (for example, after cloning an instance), follow these steps:

1.  Go to All > System Update Sets > Retrieved Update Sets or navigate to the sys\_update\_version table list view.
2.  Search for the file you want to revert.
3.  Open the latest version of the file by sorting the Recorded at column from Z to A.
4.  Compare the file contents with the source code.
5.  If the contents match, revert to this file.
6.  Mark the file as reverted in Upgrade history.

 ![Screenshot of list of Update Versions](/sys_attachment.do?sys_id=bb73a84f9732b2d45ad8f6e11153af18 "Screenshot of list of Update Versions")

![](/sys_attachment.do?sys_id=7373a84f9732b2d45ad8f6e11153af14)

### Method 3: Contact ServiceNow support

Contact ServiceNow technical support to run revert scripts that revert all related files to base system.  ServiceNow requires your approval before running scripts in Scripts - Background.

#### Validate reverted files

After you revert files, validate that the reversion was successful:

1.  Note the number of files before you revert the skipped files.
2.  Copy the following URL and replace INSTANCE\_NAME with your instance name: \`[https://INSTANCE](https://INSTANCE)\_NAME.service-now.com/sys\_upgrade\_history\_log\_list.do?sysparm\_query=sys\_updated\_onONLast%2030%20minutes@javascript:gs.beginningOfLast30Minutes()@javascript:gs.endOfLast30Minutes()%5Esys\_updated\_by%3Djavascript:gs.getUserID()%3B&sysparm\_view=\`
3.  Open the URL and verify that the count matches the number you noted earlier.
