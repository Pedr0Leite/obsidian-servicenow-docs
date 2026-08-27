---
title: "Duplicate IIS Virtual Directories (VDIRs) when using both Horizontal Discovery and Top Down Discovery Patterns"
aliases:
  - KB0791272
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791272
kb_number: KB0791272
last_modified: 2024-04-08
---

## Issue

When running OOTB discovery of IIS in both horizontal and top-down mode, two CI records are created for the same virtual directory with slightly different names - <vdir\_name\> and <vdir\_ID\-vdir\_name\>

## Resolution

Added the following two steps to IIS OOTB pattern to cause it to name virtual directories in the same format as the Top Down IIS Virtual Directory pattern:

![](sys_attachment.do?sys_id=44f93774db00f0d016d2a345ca9619e9)

Set the virtual directory name to $cmdb\_ci\_iisdirectory\[\].id + "-" + $cmdb\_ci\_iisdirectory\[\].name

![](sys_attachment.do?sys_id=c8f93774db00f0d016d2a345ca9619ea)

Then set deletion strategy for IIS Virtual directory in the IIS pattern as 'mark as **absent':**  
  
![](sys_attachment.do?sys_id=40f93774db00f0d016d2a345ca9619ec)

After these changes, run IIS horizontal pattern again. Now the horizontal virtual directory records will be created with a name matching the virtual directories discovered via top-down IIS Virtual Directory discovery. 

  
The old duplicate CI records will be marked as **absent**, and client can manually delete them.  
  
If client wishes - they may set deletion strategy to **'delete'** instead, and then those CI records will be automatically deleted by the discovery process.

Attached an [update set](sys_attachment.do?sys_id=c4f93774db00f0d016d2a345ca9619ed "update set") that can be imported on client instance that does the 3 changes mentioned above.

After removing all the duplicate IIS Virtual Directory CI Records - the deletion strategy may be changed back to **'Keep'**.

## Additional Information

Currently, we are not preforming this change in the family release as this can cause a large impact on client CMDB. Client should use this update set after understanding the changes it will do to existing CI records of IIS virtual directory.
