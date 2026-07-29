---
title: "MID server fails to validate after copying the directory from old to new host"
aliases:
  - KB0639100
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639100
kb_number: KB0639100
last_modified: 2025-08-31
---

## MID server fails to validate after copying the directory from old to new host

  

### Issue

When a working MID server directory is copied from another host instead of doing a fresh install, it fails to validate.

### Scenario

MID Server Directory was copied from a working host to a new host to create a new MID server. The config.xml file was edited with the new MID server name. The MID Server record was created in the instance and shows that the MID server is up, but it cannot be validated.

  
The following log entry appears in the Agent.log.0 file.

\----
09/22/17 13:49:34 (983) StartupSequencer Agent record not found, creating new record. Instance: XXXXX213;
09/22/17 13:49:35 (045) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Unable to load keystore: Unexpected IOException loading KeyStore, caused by: Keystore was tampered with, or password was incorrect&#13;
09/22/17 13:49:35 (045) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Keystore and config.xml files out of sync. 1) Delete keystore/agent\_keystore.jks or restore config.xml to its previous state, 2) ensure MID server has write permissions to config.xml and to keystore directory, 3) restart MID server.&#13;
09/22/17 13:49:35 (045) StartupSequencer WARNING \*\*\* WARNING \*\*\* Encountered error: \[Unable to load keystore\] while starting up the service. Retry...&#13;
09/22/17 13:49:35 (154) StartupSequencer WARNING \*\*\* WARNING \*\*\* Unable to get agent record while setting validation status, retry in 5 seconds&#13;
09/22/17 13:49:40 (217) StartupSequencer WARNING \*\*\* WARNING \*\*\* Unable to get agent record while setting validation status, retry in 5 seconds&#13;
09/22/17 13:49:45 (280) StartupSequencer WARNING \*\*\* WARNING \*\*\* Unable to get agent record while setting validation status, retry in 5 seconds&#13;
09/22/17 13:49:50 (280) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Unable to change mid server validation status to validation\_failed&#13;
09/22/17 13:50:50 (639) StartupSequencer Agent record not found, creating new record. Instance: XXXXX213;
09/22/17 13:50:50 (639) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Unable to load keystore: Unexpected IOException loading KeyStore, caused by: Keystore was tampered with, or password was incorrect&#13;
09/22/17 13:50:50 (639) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Keystore and config.xml files out of sync. 1) Delete keystore/agent\_keystore.jks or restore config.xml to its previous state, 2) ensure MID server has write permissions to config.xml and to keystore directory, 3) restart MID server.&#13;
09/22/17 13:50:50 (639) StartupSequencer WARNING \*\*\* WARNING \*\*\* Encountered error: \[Unable to load keystore\] while starting up the service. Retry...&#13;
09/22/17 13:50:50 (718) StartupSequencer WARNING \*\*\* WARNING \*\*\* Unable to get agent record while setting validation status, retry in 5 seconds&#13;
09/22/17 13:51:05 (858) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Unable to change mid server validation status to validation\_failed&#13;
----

### Resolution

1.  Stop the MID server service.  
    <install-directory>\\agent\\stop.bat.
2.  Check to make sure the MID server is not longer running on the instance.
3.  Rename the keystore directory.  
    <Install directory>\\agent\\rename _keystore_ _keystore.old_
4.  Run install.bat from the agent directory and ensure that the instance name, MID username/password are correct.  
    The MID server should now come up in the instance and validation should work.
