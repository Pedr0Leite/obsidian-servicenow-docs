---
title: "MID Server not able to connect to instance - WS-Security header error"
aliases:
  - KB0549558
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549558
kb_number: KB0549558
last_modified: 2025-08-19
---

## MID Server not able to connect to instance - WS-Security header error

  

### Issue

Mid-server not able to connect to instance - WS-Security header error 

Overview

* * *

ServiceNow offers the capability of [enabling WS-Security header verification](https://docs.servicenow.com/bundle/helsinki-servicenow-platform/page/integrate/inbound-soap/task/t_EnableWS-SecurityVerification.html "Product documentation") for all incoming SOAP requests. It is commonly used by administrators who want to:

-   verify that the sender of a SOAP message is trusted
-   ensure that SOAP messages have not been altered after they are sent

When enabling this system property, it is important to exclude service accounts from the WSS authentication requirement. Due to technical limitations, service accounts responsible for integrations cannot make use of WSS. One very common error that might occur after enabling the security setting is that the MID Server(s) stops working.

When inspecting the log files for the MID Server, you might see errors such as this:

ECCSender.1 WARNING \*\*\* WARNING \*\*\* RemoteGlideRecord failed to send data to https://instancename.service-now.com/ with (An error was discovered processing the WS-Security header)

MIDServer WARNING \*\*\* WARNING \*\*\* Method failed: (https://instancename.service-now.com/ecc\_agent.do?SOAP&displayvalue=all&redirectSupported=true)HTTP/1.1 500 Internal Server Error with code: 500

MIDServer SEVERE \*\*\* ERROR \*\*\* getRecords failed (An error was discovered processing the WS-Security header No certificate(s) found in WS-Security profile)

StartupSequencer WARNING \*\*\* WARNING \*\*\* SOAP server error reported by ServiceNow instance, user 'Your-MID-Account' may be missing the 'soap\_script' role

The MID Server service might show that it is running correctly and you are able to restart the service. However, the instance does not acknowledge the connection and shows a status of **down**. 

Solution

* * *

Administrators might forget that the MID Server user is also considered a service account. Therefore, it must also be excluded from the WSS security settings by making it an [Internal Integration User](https://docs.servicenow.com/bundle/helsinki-servicenow-platform/page/integrate/inbound-soap/task/t_MarkSvcAcctsAsInternalIntegUsers.html "Making service accounts as internal integration users"). To do so, please follow these steps:

1.  Navigate to **User Administration > Users** and locate the MID Server user
2.  Select the MID server user and right click on the header to [personalize the form](https://docs.servicenow.com/bundle/helsinki-servicenow-platform/page/use/using-forms/task/t_PersonalizeAForm.html "Personalize the form").
3.  Add the **Internal Integration User** field from the left slushbucket.
4.  Reload the form.
5.  Select the **Internal Integration User** option.
6.  Update the user record.

Ensure that the MID Server user is configured correctly in compliance with the newly added security setting. The error messages should be resolved.
