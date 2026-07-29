---
title: "How to resolve MID Server user credential issues"
aliases:
  - KB0597570
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597570
kb_number: KB0597570
last_modified: 2025-04-07
---

## How to resolve MID Server user credential issues

  

### Issue

 Table of Contents

1.  [MID Server user is locked out](#lockedOut)
2.  [Changing MID Server user password](#changePassword)
3.  [Error 404 error: User is unable to authenticate reported in the agent log](#404)
4.  [Keystore corrupted](#keystore)

  

Symptoms

-   Agent logs report an Error 404 error that user is unable to authenticate
-   MID Server upgrade process is hung
-   Cannot restart MID Server
-   MID Server keeps going down
-   All MID Servers are down
-   ECC Queue is backed up

Along with a clear communication path to the instance, the MID Server requires a valid user to authenticate. The inability for the MID Server to successfully authenticate with the instance will affect the MID's ability to install, upgrade, and execute services for the instance. [Most authentication issues](/kb_view.do?sysparm_article=KB0597574 "Most authentication issues") are reported either in the MID Server's agent log or wrapper log. Read more about [credential and authentication requirements of the MID Server](https://docs.servicenow.com/search?q=credentials "credential and authentication requirements of the MID server"). 

  

Authentication issues between MID Server and instance

-   **MID Server user is locked out**
-   **Changing MID Server user password**
-   **Error 404 error: User is unable to authenticate**

The password associated with your MID User ID is locked out. This is caused by a delta between what is in the **config.xml** of one of the MID Servers that the MID Server user is authenticating for, and the password in the user record. For example, a newly installed MID Server might have a typo in the config.xml file. A recent clone of the instance that has MID Servers running against an instance attempts to log in several times and fail. This could cause the user to be auto-set to locked out. System administrators may also proactively set the user to locked out manually.

**SOLUTION:** **Reset MID User Password -** In order to reset the password, all MID servers authenticating with that User ID must be stopped.

1.  Navigate to **MID Server > Servers**.
2.  In the list view, locate the **Logged in User** column.
3.  Filter on **Show Matching** for the MID Server user that is locked out
4.  For each MID Server remaining in the list:  
    1.  Log on to the host machine.
    2.  In the /agent directory, execute the stop command to shut down the MID Server.
5.  On the instance, in the User record for the MID Server user, enter a new password, clear the locked out box, and save the record.
6.  For each MID Server in step 4:  
    1.  Log back onto the host machine of the MID Server.
    2.  Edit the config.xml, setting the property **mid.instance.password** to the new password. (current password value may look like: encrypted:pBMG7zSYCLkGD2fJ6oXEPg==, replace the whole value including the encrypted: part, with your new password).
    3.  Save the config.xml file.
    4.  Restart the service using the start execution file (.bat or .sh).
7.  On the instance, open the list of MID Servers filtered. The MID Servers should start showing as **UP**.

  

-   **Keystore Corrupted**

_(Only on existing MID Servers and not on new MID Server installations)_

The MID Server has a keystore on the host machine of the MID Server. The keystore is a repository of security certificates and private keys that have been established as part of the trust management between the MID Server and either the instance itself or the host machines the MID Server is configured to communicate with during a discovery or integration task. When this keystore becomes corrupted, either the communication with the instance itself is compromised or part of the services supported by the MID Server are corrupted. 

The keystore is located under the /agent directory of the MID Server. When you validate the MID Server from the instance, you contribute to the keystore.

When a MID Server has been reinstalled, or if a MID Server crashes unexpectedly, the keystore can become corrupted. Once it does, the MID Server will act unpredictably.

You can see if the keystore is the source of MID Server issues by looking in the agent log and searching for the phrase _SEVERE \*\*\* ERROR \*\*\* Unable to load keystore:._ If the MID Server is attempting to start or restart, this will prevent the MID from starting successfully.

**SOLUTION****: Recreate the keystore directory -** There is no way to mend the keystore once corrupted. The only thing you can do is delete the keystore directory from the /agent directory of the affected MID Server. 

1.  If the MID Server is running, go to the /agent directory and execute the stop script (.bat or .sh).
2.  Delete the keystore directory.
3.  Restart the MID Server using the start script (.bat or .sh).
4.  On the instance, open the **MID Server > Servers** list.
5.  Open the record for the restarted MID Server.
6.  Select the **Validate UI**. The MID Server will clear the cache, restart, and regenerate the keystore. The MID Server record will report that it is **Validated**. 

  

[\[Back to top\]](#toc)
