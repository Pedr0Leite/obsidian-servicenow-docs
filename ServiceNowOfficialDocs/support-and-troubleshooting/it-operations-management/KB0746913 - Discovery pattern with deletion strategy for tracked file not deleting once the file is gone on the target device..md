---
title: "Discovery pattern with deletion strategy for \"tracked file\" not deleting once the file is gone on the target device."
aliases:
  - KB0746913
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746913
kb_number: KB0746913
last_modified: 2024-04-07
---

## Discovery pattern with deletion strategy for "tracked file" not deleting once the file is gone on the target device.

  

### Issue

# Description

Customer can configure File Tracking on a specific pattern, in these case for Windows - OS Servers. Once the file is gone on target he has set the strategy to Deletion. But when discovery is run, it doesn't delete those files.

This KB address how the deletion strategy works and when. Please review the additional information.

# Procedure

1.  Navigate to the sa\_pattern.LIST
2.  Open the pattern where you want to set the strategy for
3.  In this case, the field is "Tracked Files" and set this strategy to Delete

# Applicable Versions

All versions.

# Additional Information

  
The way deletion strategy works is by comparing the previous discovery result for a given device with the current one, and the defined deletion strategy is executed based on the delta. 

  
So, if in previous discovery device X was discovered, and in the current one it's missing, and deletion strategy defined to be "Delete", then the device is deleted. On the same note, if it's defined to be "Keep", then the device is kept in the CMDB.   
The deltas are being calculated only between two consecutive discoveries. So, if now I take the same device X, which was kept in the CMDB based on its deletion strategy, and now I change it to "Delete", it won't be deleted on the next discovery since it has already been missing from the previous one.   
  
So, in this specific case, you should remove the file manually.   
In the future, if you have any files on Windows Server that are currently still being discovered, once they're removed from the machine they'll be removed from the CMDB as well, as expected.
