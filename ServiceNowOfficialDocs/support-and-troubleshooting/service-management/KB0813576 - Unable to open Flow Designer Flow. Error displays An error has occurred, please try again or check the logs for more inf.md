---
title: "Unable to open Flow Designer Flow. Error displays : An error has occurred, please try again or check the logs for more information."
aliases:
  - KB0813576
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813576
kb_number: KB0813576
last_modified: 2026-05-21
---

## Issue

Unable to open a Flow anymore after modifying the action in the Flow.

Error displays :  
'An error has occurred, please try again or check the logs for more information.'

Steps to reproduce:

Issue is not reproducible out of the box in the base system.

Navigate to Flow Designer > Flows  
Search for the Flow  
An error displays when you will try to open it.  
\-------------  
An error has occurred, please try again or check the logs for more information.  
\---------------------

Investigation:  
Console log:  
\--------------  
designer-bundle.min.js?sysparm\_substitute=false&version=1.4.30:205512 GET 500 (Internal Server Error)  
  
Failed to load resource: the server responded with a status of 500 (Internal Server Error)  
\------------------------------------  
  
Network tab:  
\--------------  
{"result":{"errorCode":500,"integrationsPluginActive":false},"session":{"notifications":\[\]}}  
\-----------

  
System log:  
\-------------  
04/02/2020 14:12:35  
Error null  
Flow Designer  
04/02/2020 14:12:34  
Error Flow Designer: null  
: no thrown error com.glide.ui.ServletErrorListener  
\---------------

Node log:

\----------

..  
05:12:34.987 Error Default-thread-7 FEC2DDC1DB3ACC94EA75FF361D961984 txid=a54d1981db7e SEVERE \*\*\* ERROR \*\*\* Flow Designer: null  
..

\---------------

## Resolution

When this issue occurs, check the following:

Review the Flows inputs/outputs

Review the flow's actions and try to open it.

If that fails to open, check the inputs/outputs for that action

Verify sys\_id field is not being used in the action and remove it

After removing the sys\_id field from the action, the Flow was functioning.

The sys\_id field was not being used in the action so nothing changed functionally with the action.  
  
In the base system, we prevent this from happening in current versions of the code by preventing sys\_id from being put in as a field name as well as other default fields like sys\_created\_on, sys\_updated\_on, sys\_updated\_by etc.
