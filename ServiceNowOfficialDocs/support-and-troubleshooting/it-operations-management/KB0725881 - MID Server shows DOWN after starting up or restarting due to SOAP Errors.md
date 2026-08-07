---
title: "MID Server shows DOWN after starting up or restarting due to SOAP Errors "
aliases:
  - KB0725881
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725881
kb_number: KB0725881
last_modified: 2025-02-14
---

## Issue

When starting or restarting a MID Server, you might see SOAP errors in the MID Server agent.log. For example:

02/06/19 19:30:12 (059) StartupSequencer SEVERE \*\*\* ERROR \*\*\* test failure   
java.lang.IllegalStateException: Unable to connect to instance.   
at com.service\_now.mid.services.StartupSequencer.runTests(StartupSequencer.java:328)   
at com.service\_now.mid.services.StartupSequencer$Starter.run(StartupSequencer.java:291)   
  
02/06/19 19:31:22 (062) StartupSequencer WARNING \*\*\* WARNING \*\*\* java.net.SocketTimeoutException: connect timed out when posting to [https://YOUR\_INSTANCE.service-now.com/InstanceInfo.do?SOAP](https://YOUR_INSTANCE.service-now.com/InstanceInfo.do?SOAP)   
02/06/19 19:31:22 (062) StartupSequencer SEVERE \*\*\* ERROR \*\*\* SOAP Request: <SOAP-ENV:Envelope xmlns:xsd="[http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema)" xmlns:SOAP-ENC="[http://schemas.xmlsoap.org/soap/encoding/](http://schemas.xmlsoap.org/soap/encoding/)" xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance](http://www.w3.org/2001/XMLSchema-instance)" xmlns:tns="[http://www.service-now.com/GetMIDInfo](http://www.service-now.com/GetMIDInfo)" xmlns:m="[http://www.service-now.com](http://www.service-now.com)" xmlns:SOAP-ENV="[http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/)" SOAP-ENV:encodingStyle="[http://schemas.xmlsoap.org/soap/encoding/](http://schemas.xmlsoap.org/soap/encoding/)"><SOAP-ENV:Body><m:execute></m:execute></SOAP-ENV:Body></SOAP-ENV:Envelope>   
02/06/19 19:31:22 (062) StartupSequencer SEVERE \*\*\* ERROR \*\*\* SOAP Response: Status code=0, Response body=null   
02/06/19 19:31:22 (062) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Problem invoking InstanceInfo on [https://YOUR\_INSTANCE.service-now.com/](https://YOUR_INSTANCE.service-now.com/): Please check that the InstanceInfo page exists in the sys\_public table and active="true".   
02/06/19 19:31:22 (062) StartupSequencer SEVERE \*\*\* ERROR \*\*\* java.net.SocketTimeoutException: connect timed out when posting to [https://YOUR\_INSTANCE.service-now.com/InstanceInfo.do?SOAP](https://YOUR_INSTANCE.service-now.com/InstanceInfo.do?SOAP)   
(Network Configuration issue) Please check that the MID server can ping the instance: [https://YOUR\_INSTANCE.service-now.com/](https://YOUR_INSTANCE.service-now.com/)   
You may also need to configure the network that the MID server uses to allow traffic over TCP port 443. 

## Resolution

1.  Check the firewall access setup for the instance.
2.  Turn on debugging and observe SNMP traffic in [Wireshark](https://docs.servicenow.com/csh?topicname=request-type.html&version=latest "Wireshark").
3.  Telnet from the MID Server to the instance on port 443, i.e.: "telnet YOUR\_INSTANCE.service-now.com 443".
