---
title: "Restore missing Flow Designer action step icons after cloning"
aliases:
  - KB0952307
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0952307
kb_number: KB0952307
last_modified: 2026-02-12
---

## Restore missing Flow Designer action step icons after cloning

  

### Issue

Flow Designer action step icons do not appear in non-production instances after cloning from production environments. This occurs because the system attachment records containing the icons are not transferred during the cloning process. 

![](sys_attachment.do?sys_id=594eb076932766d0080af35d6cba1076)

### Release

All supported releases

### Cause

The icon images are stored in the sys\_attachment table and are missing in the non-production instance.

To verify this, go to the sys\_attachment list in your non-production instance and search for records with the file\_name=step\_icon.

https://subprod\_instance\_name.service-now.com/sys\_attachment\_list.do?sysparm\_query=file\_name%3Dstep\_icon&sysparm\_view=

Check the clone settings in the clone\_instance table on the production instance. The Exclude large attachment data toggle switch is selected, which prevents these attachments from being cloned, even though they are not large files. 

### Resolution

To restore the missing icons:

1.  Repair the required plugins for the Flow Designer actions on the affected instance: 
    -   com.glide.hub.action\_step.crud
    -   com.glide.hub.action\_step.core
    -   com.glide.hub.action\_step.rest
2.  For additional action step icons other than the main plugins (com.glide.hub.action\_step.crud and com.glide.hub.action\_step.core), repair them using the following naming convention: 
    -   com.glide.hub.action\_step.STEPNAME.

For example, to repair the PowerShell plugin, repair the com.glide.hub.action\_step.powershell plugin. 

### Related Links

For more information about clone settings, see [Request a clone](https://docs.servicenow.com/bundle/paris-platform-administration/page/administer/managing-data/task/t_StartAClone.html "Request a clone")
