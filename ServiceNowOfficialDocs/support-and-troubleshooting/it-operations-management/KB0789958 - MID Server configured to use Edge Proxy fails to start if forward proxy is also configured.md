---
title: "MID Server configured to use Edge Proxy fails to start if forward proxy is also configured"
aliases:
  - KB0789958
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789958
kb_number: KB0789958
last_modified: 2024-04-08
---

## MID Server configured to use Edge Proxy fails to start if forward proxy is also configured

  

### Issue

MID Server fails to startup after config.xml is updated to use the Edge proxy url

See [Edge Encryption MID Server integration](https://docs.servicenow.com/csh?topicname=edge-mid-pass-through.html&version=latest "Edge Encryption MID Server integration") for details on how to configure MID Server to use Edge Proxy  
  
Error in the MID server logs:

12/12/19 21:19:59 (287) StartupSequencer SEVERE **\* ERROR **_ SOAP  
Response: Status code=503, Response body=  
12/12/19 21:19:59 (288) StartupSequencer SEVERE _** ERROR **_ Problem  
invoking InstanceInfo on [https://atyourservice.xxxx.com/:](https://atyourservice.verizon.com/:) Please check  
that the InstanceInfo page exists in the sys\_public table and active="true".  
12/12/19 21:19:59 (288) StartupSequencer SEVERE _** ERROR **_ (Network  
Configuration issue) Please check that the MID server can ping the  
instance: [https://atyourservice.xxxx.com/](https://atyourservice.verizon.com/)  
You may also need to configure the network that the MID server uses to  
allow traffic over TCP port 443.  
12/12/19 21:19:59 (290) StartupSequencer SEVERE _** ERROR \*** test failure  
java.lang.IllegalStateException: `Unable to connect to instance`.  
at com.service\_now.mid.services.StartupSequencer.runTests(  
StartupSequencer.java:405)  
at com.service\_now.mid.services.StartupSequencer$Starter.run(  
StartupSequencer.java:367)

### Cause

The MID Server was also configured to use a Forward Proxy. So the communication path was MID Server --> Forward Proxy --> Edge Proxy --> Forward Proxy --> Instance  
which was breaking.  
  

The following parameters in the config.xml indicate a forward proxy is used:

```
<parameter name="mid.proxy.use_proxy" value="true"/><parameter name="mid.proxy.host" value="xxxx.xxxx.xxx"/><parameter name="mid.proxy.port" value="xxxx"/>
```

### Resolution

Update the MID Server config.xml file and remove the Forward proxy configuration.  
Stop and Start the MID Server  
The MID Server started successfully.
