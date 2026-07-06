---
title: "Notify inbound responses fail to get added to the ServiceNow notify message table after cloning"
aliases:
  - KB0792623
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792623
kb_number: KB0792623
last_modified: 2026-05-06
---

## Notify inbound responses fail to get added to the ServiceNow notify message table after cloning

  

### Issue

The end user acknowledgement to any of the notify event is not added to the servicenow notify message table. The response is stored in Twilio, but fails to add into the instance due to the below error caused by the read-only script include "Twilio Helper":  
{     "error": {         "message": "Cannot read property \\"length\\" from null",         "detail": "TypeError: Cannot read property \\"length\\" from null (sys\_script\_include.e8fcbb3c87d21300b18a046787cb0b88.script; line 374)"     },     "status": "failure" } 

Twilio also responds with an error:  
The requested resource /Services/MGc508198b3234b307e1ae8de30b0a577b/ShortCodes was not found (20404).

### Release

All releases

### Cause

For instance upgrades, administrators do not need to reconfigure Twilio. However for clones this is necessary, as credentials do not get cloned:

[Ensure that each instance on which you configure Notify uses a different Twilio account. Each account specifies a unique account SID, authentication token, telephone numbers, and endpoint. Using the same account across multiple instances may cause your Twilio service configuration to be overwritten.](https://docs.servicenow.com/csh?topicname=t_ConfigureNotifyWithTwilio.html&version=latest)

### Resolution

If the account is already associated with an instance, the system displays an error message. In order to connect to this account:

-   [Disconnect Twilio account from the instance](https://docs.servicenow.com/csh?topicname=t_disconnect-from-Twilio-account.html&version=latest "Disconnect Twilio account from the instance").
-   Delete the TwiML apps in the Twilio account.

**NOTE**: If you buy or release numbers on the Twilio account, open the configuration page again to refresh the list of numbers. Numbers removed from the Twilio service remain as Notify Number records, but with the Active field set to false. Use only active phone numbers for inbound or outbound communication.

Enable audit on the \[sn\_twilio\_direct\_basic\_auth\] table to know who/when details are modified, as the history of changes is not known.  
  
[Tables and Business Rules installed by Twiliio](https://docs.servicenow.com/csh?topicname=installed-with-twilio.html&version=latest "Tables and Business Rules installed by Twiliio")

### Related Links

Instructions to delete the TwiML apps in the Twilio account:

1) Side Menu within Twilio.  
2) Select Programmable voice.  
3) Click Twiml.  
4) Select sub menu of Twiml apps.  
5) Select the app and then use the link that states Delete.  
6) Go back to the Twilio configuration in Servicenow and then try to reconnect. Once reconnected the Twiml app should be rebuilt in Twilio.  
7) Ensure the phone numbers are correctly setup in the Notify Phone numbers section of ServiceNow.
