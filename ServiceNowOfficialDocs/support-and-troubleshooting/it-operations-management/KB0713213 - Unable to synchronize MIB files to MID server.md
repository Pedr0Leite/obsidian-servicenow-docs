---
title: "Unable to synchronize MIB files to MID server"
aliases:
  - KB0713213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713213
kb_number: KB0713213
last_modified: 2024-04-07
---

## Unable to synchronize MIB files to MID server

  

### Issue

# Symptoms

* * *

At MID server folder (<MID\_server\_installation\_path>/work/mibs), no mibs files being synchronize from instance.

# Release

* * *

Any version

# Cause

* * *

Some of the MIB file at instance side have 0kb causing the instance unable to sync the file to MID server.

[https://<INSTANCE\_NAME>.service-now.com/ecc\_agent\_mib\_list.do?sysparm\_query=](https://empkchookkingston.service-now.com/ecc_agent_mib_list.do?sysparm_query=)

# Resolution

* * *

Check all MIBs file in instance and ensure all attachments in records are valid.

![](sys_attachment.do?sys_id=351c682edb42b450e515c2230596191b) 

# Additional Information

* * *

You can also check mid server agent log to get an idea on where the synchronization failed. In following example, the mibs record "FOUNDRY-SN-ROOT-MIB" in table "ecc\_agent\_mib" is causing the synchronisation issue as the attachment in the record is having 0Kb.

ie:

08/20/18 21:04:24 (084) File sync worker: ecc\_agent\_mib Downloading D:\\EMS\\MID Server\\agent\\work\\mibs\\FOUNDRY-SN-ROOT-MIB from XXXXXXXXXX

08/20/18 21:04:24 (099) File sync worker: ecc\_agent\_jar Finishing file synchronization: ecc\_agent\_jar

08/20/18 21:04:24 (224) File sync worker: ecc\_agent\_mib WARNING \*\*\* WARNING \*\*\* Could not complete file synchronization: 0

...

08/20/18 21:04:32 (229) MIB Initializer WARNING \*\*\* WARNING \*\*\* MIB loader errors when loading MIB: FOUNDRY-SN-ROOT-MIB

\---line 1, column 1: unexpected end of file
