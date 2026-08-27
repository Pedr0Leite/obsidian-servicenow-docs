---
title: "MID Server Service Starts but MID Server Status shows as Down - Unable to unsecure parameter mid.instance.password: Problem while decrypting"
aliases:
  - KB0745202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745202
kb_number: KB0745202
last_modified: 2024-04-07
---

## MID Server Service Starts but MID Server Status shows as Down - Unable to unsecure parameter mid.instance.password: Problem while decrypting

  

### Issue

MID Server Service Starts but MID Server Status shows as Down. When starting your MID Server you see the following in the agent log:

03/28/19 08:20:53 (707) MIDServer SEVERE \*\*\* ERROR \*\*\* Unexpected exception, terminating the MID server java.lang.RuntimeException: Unable to unsecure parameter mid.instance.password:  
Problem while decrypting at com.service\_now.mid.services.Config.getProperty(Config.java:509)  
at com.service\_now.mid.services.Config.getProperty(Config.java:535)  
at com.service\_now.mid.services.Config$InstanceConnectionConfig.getUserPassword(Config.java:843)  
at com.service\_now.mid.Instance.getUserPassword(Instance.java:537)  
at com.service\_now.mid.Instance.setupFactory(Instance.java:486)  
at com.service\_now.mid.Instance.init(Instance.java:74)  
...  
at org.tanukisoftware.wrapper.WrapperStartStopApp.run(WrapperStartStopApp.java:405)  
at java.lang.Thread.run(Thread.java:748)  
Caused by: java.lang.IllegalStateException: Problem while decrypting  
at com.glide.util.AESCodec.decrypt(AESCodec.java:227)  
at com.service\_now.mid.services.config.DefaultMidServerEncrypter.decrypt(DefaultMidServerEncrypter.java:63)  
at com.service\_now.mid.services.config.DefaultMidServerEncrypter.decrypt(DefaultMidServerEncrypter.java:45)  
at com.service\_now.mid.services.config.DefaultSecuredConfigProvider.unsecuredParameterValue(DefaultSecuredConfigProvider.java:54) at com.service\_now.mid.services.Config.getProperty(Config.java:506) ... 31 more

### Release

All currently supported environments.

### Cause

There is a problem with the password in the config.xml file.

### Resolution

1.  Open the config.xml file
2.  2\. Re enter the user's password. (By default, this will be encrypted after you restart the service)  
    ![](sys_attachment.do?sys_id=84eca022db82b450e515c223059619f0)
3.  Start or Restart the MID Server service.

If you get the same error message after following the above steps, and you are sure the password is correct:  

1.  Stop the service
2.  Run agent/bin/UninstallMID-NT.bat
3.  Run agent/bin/InstallMID-NT.bat
4.  Start service

  

What you should be seeing from a normal startup without this issue is as follows:

03/26/19 11:37:40 (297) MIDServer Creating injector...  
03/26/19 11:37:40 (815) MIDServer Using configuration: C:\\ServiceNowTemp\\agent\\config.xml  
03/26/19 11:37:40 (925) MIDServer Logger config: root=INFO  
03/26/19 11:37:40 (925) MIDServer Refreshing LoggerFactory cache  
03/26/19 11:37:41 (018) MIDServer Loaded credentials provider: com.service\_now.mid.keypairs.provider.standard.StandardKeyPairsProvider  
03/26/19 11:37:41 (034) MIDServer ThreadPool-Interactive started with corePoolSize: 10, maxPoolSize: 10, maximumQueueSize: 40  
03/26/19 11:37:41 (034) MIDServer ThreadPool-Expedited started with corePoolSize: 20, maxPoolSize: 20, maximumQueueSize: 400  
03/26/19 11:37:41 (034) MIDServer ThreadPool-Standard started with corePoolSize: 25, maxPoolSize: 25, maximumQueueSize: 500  
03/26/19 11:37:41 (034) MIDServer ExtensionContainer ThreadPool started with corePoolSize: 25, maximumPoolSize: 25, maximumQueueSize: 500  
03/26/19 11:37:44 (837) MIDServer Setting basic authentication with user admin  
03/26/19 11:37:45 (134) MIDServer MIDCredentialsConfigProvider initialized with com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider  
03/26/19 11:37:45 (244) MIDServer MID Server starting  
03/26/19 11:37:45 (275) MIDServer Agent home path: C:\\ServiceNowTemp\\agent  
03/26/19 11:37:45 (478) MIDServer MID Server started
