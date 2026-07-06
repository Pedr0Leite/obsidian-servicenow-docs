---
title: "MID Server Will Not Start Due To Severe Error - \"An error occurred while decrypting automation encryption keys\" "
aliases:
  - KB0745466
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745466
kb_number: KB0745466
last_modified: 2025-04-02
---

## MID Server Will Not Start Due To Severe Error - "An error occurred while decrypting automation encryption keys"

  

### Issue

When starting your MID Server, it is still showing a "Down" status on your instance. When viewing the agent log you will see after starting the MID Server:

03/28/19 10:27:09 (774) StartupSequencer SEVERE \*\*\* ERROR \*\*\* An error occurred while decrypting automation encryption keys.   
com.snc.automation\_common.integration.exceptions.AutomationIOException: No key pair found for DefaultSecurityKeyPairHandle   
at com.service\_now.mid.keypairs.provider.standard.StandardKeyPairsProvider.decrypt(StandardKeyPairsProvider.java:340)   
at com.glide.util.MIDServerInfoPayloadDecrypter.decryptPayload(MIDServerInfoPayloadDecrypter.java:30)   
at com.service\_now.mid.services.AutomationEncryptionKeys.load(AutomationEncryptionKeys.java:98)   
at com.service\_now.mid.services.AutomationEncryptionKeys.onMIDServerEvent(AutomationEncryptionKeys.java:42)   
at com.service\_now.mid.services.Events.internalFire(Events.java:102)   
at com.service\_now.mid.services.Events.fire(Events.java:34)   
at com.service\_now.mid.services.StartupSequencer.startServices(StartupSequencer.java:218)   
at com.service\_now.mid.services.StartupSequencer.testsSucceeded(StartupSequencer.java:114)   
at com.service\_now.mid.services.StartupSequencer.access$200(StartupSequencer.java:64)   
at com.service\_now.mid.services.StartupSequencer$Starter.run(StartupSequencer.java:363) 

### Release

All releases

### Cause

Invalid keystore or MID Server cannot be validated

### Resolution

1\. Delete the /agent/keystore folder and restart the MID Server service. In linux-based installation the agent\_keystore file is located under the agent/security folder. Stop the agent, delete that file and start the agent.

2\. If the solution above doesn't work, check for any customizations made to the MID Server related scripted web services below:

https://<instance>.service-now.com/sys\_web\_service\_list.do?sysparm\_query=sys\_package%3De70d4bc61bd20010cf0bda09dc4bcbeb&sysparm\_view=

### Related Links

There is a similar error with a different cause explained in [KB0748823/PRB1342894 An error occurred while decrypting credentials from instance - Creating OAuth 2.0 credential results in no credentials being retrieved by the MID server, and Probes will no longer be able to use them](https://support.servicenow.com/kb_view.do?sysparm_article=KB0748823)
