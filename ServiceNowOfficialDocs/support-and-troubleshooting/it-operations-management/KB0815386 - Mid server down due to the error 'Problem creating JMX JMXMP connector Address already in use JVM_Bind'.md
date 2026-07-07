---
title: "Mid server down due to the error 'Problem creating JMX JMXMP connector Address already in use: JVM_Bind"
aliases:
  - KB0815386
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815386
kb_number: KB0815386
last_modified: 2024-04-08
---

## Mid server down due to the error 'Problem creating JMX JMXMP connector Address already in use: JVM\_Bind'

  

### Issue

-   The Mid server is down and the mid server agent logs contain the below error during the mid server startup.

MIDServer SEVERE \*\*\* ERROR \*\*\* Problem creating JMX JMXMP connector  
java.net.BindException: Address already in use: JVM\_Bind  
  

### Release

-   Madrid P\*

### Cause

-   When two or more Mid servers running on the same host, one of the mid servers is restarted, mid server during startup checks for any JMX requests even when it's not configured, when it fails to set it up the error is thrown, the MID still continues with startup process and the mid server would be up and running and the Status in the instance is set to UP if there do not exist any other issues related to the mid server.

### Resolution

-   This error is subtle and this issue is addressed through the PRB1323940 if you do not use JMX server you can set the _**mid.jmx.enabled**_ MID Server property to false to mitigate the error.  
              Refer [Add a MID Server Parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "Add a MID Server Parameter") to configure the mid server parameter.
-   Review the mid server agent logs and wrapper logs for other errors which might cause the mid server to be down.
-   In one of the scenarios, I found the below error in the wrapper logs.

2020/02/25 15:53:19 | - Required proxy credentials not available for BASIC <any realm>@patchproxy.xyz.com:3128  
2020/02/25 15:53:19 | - Preemptive authentication requested but no default proxy credentials available

-   Observed the proxy was configured on the mid server and mid.proxy.username mid server parameter did not contain any value in it.
-   Add the proxy username and proxy password if the proxy server uses credentials for authentication or remove the parameter.
-   Restart the mid server service, the mid server would be up and running.
