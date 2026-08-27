---
title: "InstallLocation field is blank on the Software installations [cmdb_sam_sw_install] table"
aliases:
  - KB0724289
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724289
kb_number: KB0724289
last_modified: 2026-05-19
---

## InstallLocation field is blank on the Software installations \[cmdb\_sam\_sw\_install\] table

  

### Issue

After running Discovery the InstallLocation field remains blank

### Facts

#### Windows

This field was not populated via Discovery until that enhancement was added in the San Diego release. Since then it has been.

#### Linux

As of Australia, and probably later, Linux Discovery does not populate Install Location.

### Release

Since San Diego.

### Resolution

#### Windows

Update your instance to a minimum of the San Diego release and this field should populate. 

note: Discovery relies on data being present in the registry to capture.  If you are still experiencing issues please verify the Windows host you are attempting to get InstallLocation information on has data in the respective registry keys:

HKEY\_LOCAL\_MACHINE/Software/Microsoft/Windows/CurrentVersion/Installer/UserData/\*/Products/\*/InstallProperties/InstallLocation  
HKEY\_LOCAL\_MACHINE/Software/Microsoft/Windows/CurrentVersion/Uninstall/\*/InstallLocation

#### Linux

Currently OOTB Discovery does not capture the InstallLocation for Linux hosts.  If this is an enhancement you would like to see added please submit an idea through the Idea Portal.  There have been requests in the past, but there is no harm asking again. With enough up-votes these are looked at and sometimes actioned.

[Idea Portal](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1156757 "Idea Portal")

### Related Links

[PRB1487224 Install location field is not populated in cmdb\_sam\_sw\_install table with "Installed Software" probe (Fixed in San Diego)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1180456 "KB1180456 - Install location field is not populated in cmdb_sam_sw_install table with \"Installed Software\" probe")
