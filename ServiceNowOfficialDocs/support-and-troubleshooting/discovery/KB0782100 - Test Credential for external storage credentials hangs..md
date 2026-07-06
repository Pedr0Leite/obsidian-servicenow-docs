---
title: "Test Credential for external storage credentials hangs."
aliases:
  - KB0782100
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782100
kb_number: KB0782100
last_modified: 2024-04-08
---

## Test Credential for external storage credentials hangs.

  

### Issue

Test Credential for external storage credentials hangs.

### Release

All currently supported releases.

### Cause

MID server config.xml does not have all the necessary parameters configured.

By setting the MID server parameter mid.log.level = debug, and reproducing the issue, we see the following in the MID server logs:  
  
**Worker-Interactive:CommandPipeline-61a071d1dbe00450be7d51d7f496192a SEVERE \*\*\* ERROR \*\*\* Problem with client's CredentialResolver:**   
**java.lang.ClassNotFoundException: com.snc.discovery.CredentialResolver**  
**at java.net.URLClassLoader.findClass(URLClassLoader.java:381)**  
**at java.lang.ClassLoader.loadClass(ClassLoader.java:424)**  
**at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:349)**  
**at java.lang.ClassLoader.loadClass(ClassLoader.java:357)**  
**at java.lang.Class.forName0(Native Method)**  
**at java.lang.Class.forName(Class.java:264)**  
**at com.service\_now.mid.services.CredentialResolverProxy.initWithLegacy(CredentialResolverProxy.java:125)**

### Resolution

1.  Search our documentation for "**CyberArk integration configuration**", make sure to filter by your instance version.
2.  Ensure all steps were properly followed.
3.  MID parameter "ext.cred.use\_cyberark" needs to be true in order to connect to CyberArk and get the credentials.

### Related Links

-   [CyberArk integration configuration](https://docs.servicenow.com/csh?topicname=c_CyberArkIntegrationConfiguration.html&version=latest "CyberArk integration configuration")
-   [CyberArk credential storage integration](https://docs.servicenow.com/csh?topicname=c_CyberArkIntegrationConfiguration.html&version=latest "CyberArk credential storage integration")
