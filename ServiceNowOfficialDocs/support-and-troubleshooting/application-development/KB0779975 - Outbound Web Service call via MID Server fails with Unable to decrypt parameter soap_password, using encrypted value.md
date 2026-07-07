---
title: "Outbound Web Service call via MID Server fails with \"Unable to decrypt parameter: soap_password, using encrypted value\"
aliases:
  - KB0779975
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779975
kb_number: KB0779975
last_modified: 2025-08-19
---

## Outbound Web Service call via MID Server fails with "Unable to decrypt parameter: soap\_password, using encrypted value"

  

### Issue

Outbound Web Service calls via MID Server fails with HTTP 500 and the following message can be seen in the MID Server Logs, in the general form "Unable to decrypt parameter: XXX, using encrypted value YYY".

SOAPProbe example:

Worker-Standard:SOAPProbe-<ecc\_queue sys\_id> WARNING \*\*\* WARNING \*\*\* Unable to decrypt parameter: soap\_password, using encrypted value enc:<encrypted value>== instead : Unable to decrypt value&

An older RESTProbe example:

Worker-Standard:MIDWorker WARNING \*\*\* WARNING \*\*\* Unable to decrypt parameter: rest\_password, using encrypted value 

### Cause

The message indicates that there is a mismatch between the Encryption keys on the instance and the MID Server.

### Resolution

-   If the MID Server remains UP:  
    -   Clicking the Re-Key related link on the MID Server form can sometimes resolve this.
-   If the MID Server is Down:  
    -   Shut down the mid server service
    -   delete the file **.\\agent\\keystore\\agent\_keystore.jks**, or **.\\agent\\security\\agent\_keystore.jks** (save this file elsewhere first)
    -   Open **.\\agent\\config.xml** in an editor, and clear the **keypairs.mid\_id** parameter value. (record this value first)
    -   Start the MID Server service. A new good file should be created automatically on startup.
    -   The MID Server might still need Validating from the MID Server record in the instance. Click 'Validate' in the Related Links.

The MID Server will now restart, and you should now be able to execute the Web Service call successfully if re-executed. 

Notes:

Old ecc\_queue output records, that might still be in ready state, where the password in the payload had been encrypted with the old key, will probably not re-run. A new output needs creating by re-running the request, or SOAPMessagev2/RESTMessagev2 from a script.

These solutions are used to **resolve the issue short term**. To avoid the issue repeating in the future, ServiceNow tech support need to record more details in order to understand what caused the keys to become out of sync in the first place. This includes:

-   Was the instance upgraded recently (from/to versions)? Was the issue seen before the upgrade too?
-   The MID Server version, and host OS and OS version
-   Is this consistently reproducible, even after applying the temporary workaround?
-   Collect the full set of logs for the MID server (zip up and attach the whole agent\\logs folder). If possible, have had the mid.log.level=debug parameter set on the MID Server, during starting, and while running the soap/rest probes.
-   The "keypairs.mid\_id" value in agent\\config.xml, associated with the keystore file. Ideally save the whole config.xml file elsewhere before applying the workaround, and after.
-   The agent\_keystore file found in the security or keystore directory, both before and after trying the workaround.
-   Save the ecc\_agent xml record, before and after the workaround. This record has a relevant public\_key field value, and other field to help understand the setup, such as validated status, custom certificate flag, FIPS mode, mTLS enabled, java versions etc.
