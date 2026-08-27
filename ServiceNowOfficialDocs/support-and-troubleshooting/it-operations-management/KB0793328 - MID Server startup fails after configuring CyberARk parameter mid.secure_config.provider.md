---
title: "MID Server startup fails after configuring CyberARk parameter mid.secure_config.provider"
aliases:
  - KB0793328
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793328
kb_number: KB0793328
last_modified: 2024-04-08
---

## MID Server startup fails after configuring CyberARk parameter mid.secure\_config.provider

  

### Issue

MID Server startup fails after configuring CyberARk parameter mid.secure\_config.provider. In the MID server agent logs, the following errors are observed:

MIDServer SEVERE \*\*\* ERROR \*\*\* Unable to secure the config parameter mid.instance.password, leaving it unsecured  
java.lang.IllegalArgumentException: Invalid parameter value "encrypted:w/66o2jKI0vjrWvevajPrA==": must have the format of "cyberark::id=xxxxx,type=yyyyy"  
at com.service\_now.mid.services.config.CyberArkSecuredConfigProvider.secureParameterValue(CyberArkSecuredConfigProvider.java:51)  
at com.service\_now.mid.services.Config.secureParameters(Config.java:418)  
at com.service\_now.mid.services.Config.init(Config.java:194)  
...  
MIDServer SEVERE \*\*\* ERROR \*\*\* Unexpected exception, terminating the MID server  
java.lang.RuntimeException: Unable to unsecure parameter mid.instance.password: Invalid parameter value "encrypted:w/66o2jKI0vjrWvevajPrA==": must have the format of "cyberark::id=xxxxx,type=yyyyy"  
at com.service\_now.mid.services.Config.getProperty(Config.java:520)  
at com.service\_now.mid.services.Config.getProperty(Config.java:546)  
at com.service\_now.mid.services.Config$InstanceConnectionConfig.getUserPassword(Config.java:863)  
at com.service\_now.mid.Instance.getUserPassword(Instance.java:941)  
at com.service\_now.mid.Instance.setupFactory(Instance.java:890)

### Release

All currently supported environments.

### Cause

The MID server parameter mid.secure\_config.provider determines what class will secure the parameters in the MID server configuration file. Any encrypted/secured parameters need to be updated to comply with the format expected by the class which is set in the mid.secure\_config.provider.

See the following document on how to configure it for class com.service\_now.mid.services.config.CyberArkSecuredConfigProvider:

-   [Use CyberArk as a secure configuration provider](https://docs.servicenow.com/csh?topicname=use-cyberark-secure-config-provider.html&version=latest "Use CyberArk as a secure configuration provider")

### Resolution

Either remove the parameter mid.secure\_config.provider from the MID server configuration, or update encrypted/secured parameters as expected by the class handling such.
