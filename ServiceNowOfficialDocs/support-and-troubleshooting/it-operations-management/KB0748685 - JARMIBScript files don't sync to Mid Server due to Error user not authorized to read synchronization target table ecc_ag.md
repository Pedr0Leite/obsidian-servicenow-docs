---
title: "JAR/MIB/Script files don't sync to Mid Server due to Error: user not authorized to read synchronization target table: ecc_agent_jar / ecc_agent_mib / ecc_agent_script_file"
aliases:
  - KB0748685
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748685
kb_number: KB0748685
last_modified: 2026-03-05
---

## JAR/MIB/Script files don't sync to Mid Server due to Error: user not authorized to read synchronization target table: ecc\_agent\_jar / ecc\_agent\_mib / ecc\_agent\_script\_file

  

### Issue

JAR, MIB, Script, etc. files are not synced to the MID Server, and we see the below errors in the agent logs of the MID Server. 

This examaple is from quite an old version, but the errors you see will be similar:

05/08/19 14:36:00 (195) File sync worker: ecc\_agent\_mib Starting file synchronization: ecc\_agent\_mib  
05/08/19 14:36:00 (195) File sync worker: ecc\_agent\_jar Starting file synchronization: ecc\_agent\_jar  
05/08/19 14:36:00 (492) File sync worker: ecc\_agent\_mib WARNING \*\*\* WARNING \*\*\* Could not get file sync snapshot because: Error: user not authorized to read synchronization target table: ecc\_agent\_mib  
05/08/19 14:36:00 (492) File sync worker: ecc\_agent\_mib Finishing file synchronization: ecc\_agent\_mib  
05/08/19 14:36:00 (492) File sync worker: ecc\_agent\_mib Setting countdown to 1800 seconds in com.service\_now.mid.filesync.MIBSyncer  
05/08/19 14:36:00 (546) File sync worker: ecc\_agent\_jar WARNING \*\*\* WARNING \*\*\* Could not get file sync snapshot because: Error: user not authorized to read synchronization target table: ecc\_agent\_jar

### Release

Any

### Cause

The MID Server login user will be failing the ACLs for the ecc\_agent\_sync\_file table, which is the parent table all of these other extending tables inherit, or one of those child tables.

### Resolution

1.  Confirm there are both 'read' and 'query\_range' ACLs that would allow the mid\_server role, for ecc\_agent\_sync\_file. If there are also specific ACLs for any of the child tables, then mid\_server role needs to be on at least one of those ACLs too:
    -   ecc\_agent\_sync\_file
    -   ecc\_agent\_ext\_jar 
    -   ecc\_agent\_jar
    -   ecc\_agent\_mib
    -   ecc\_agent\_script\_file
    -   mid\_server\_tools
    -   sa\_pattern
    -   sa\_uploaded\_file
    -   sn\_agent\_asset
    -   sn\_agent\_configuration\_file
2.  Then Restart the MID Server to Sync the JAR files.

This is a screenshot of a list of the relevant ACLs, from an instance with various ITOM features installed. The @@snc\_write\_audit@@ created ACLs for query\_range are likely to be the culprits, as these were created as a fix for a security vulnerability in 2025, and were added by an algorithm that tried to work out how tables were being used at the time to understand what needed adding, and it might not have got it completely right.

https://<instance\_name>.service-now.com/sys\_security\_acl\_list.do?sysparm\_query=operation%3Dread%5EORoperation%3De66cf897b7300210240b06dd1e11a9fd%5EnameSTARTSWITHecc\_agent\_sync\_file%5EORnameSTARTSWITHecc\_agent\_ext\_jar%5EORnameSTARTSWITHecc\_agent\_jar%5EORnameSTARTSWITHecc\_agent\_mib%5EORnameSTARTSWITHecc\_agent\_script\_file%5EORnameSTARTSWITHmid\_server\_tools%5EORnameSTARTSWITHsa\_pattern%5EORnameSTARTSWITHsa\_uploaded\_file%5EORnameSTARTSWITHsn\_agent\_asset%5EORnameSTARTSWITHsn\_agent\_configuration\_file&sysparm\_view=

![](/sys_attachment.do?sys_id=7a318f3f4793321427a3fac8736d43fa)
