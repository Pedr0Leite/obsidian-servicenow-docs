---
title: "Login transactions taking a long time with LDAP authentication"
aliases:
  - KB0549747
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549747
kb_number: KB0549747
last_modified: 2024-04-07
---

## Login transactions taking a long time with LDAP authentication

  

### Issue

Login latency seen with LDAP Authentication 

Problem

* * *

Users notice a latency at login when they are authenticated using LDAP.   

Symptoms

* * *

If you review the stack trace for the login, you will see the following, indicating we are stuck executing the call **getHostByAddr**:  
  
main,Default-thread-14,5,attrs=(session\_id=B67EF8A2B06739C031D014FC588414CF)   
java.net.Inet6AddressImpl.getHostByAddr(Native Method)   
java.net.InetAddress$1.getHostByAddr(InetAddress.java:880)   
java.net.InetAddress.getHostFromNameService(InetAddress.java:559)   
java.net.InetAddress.getHostName(InetAddress.java:502)   
java.net.InetAddress.getHostName(InetAddress.java:474)   
com.sun.net.ssl.internal.ssl.SSLSocketImpl.getHost(SSLSocketImpl.java:1956)   
com.sun.net.ssl.internal.ssl.Handshaker.getHostSE(Handshaker.java:257)   
com.sun.net.ssl.internal.ssl.ClientHandshaker.getKickstartMessage(ClientHandshaker.java:1023)   
com.sun.net.ssl.internal.ssl.Handshaker.kickstart(Handshaker.java:620)   
com.sun.net.ssl.internal.ssl.SSLSocketImpl.kickstartHandshake(SSLSocketImpl.java:1290)   
com.sun.net.ssl.internal.ssl.SSLSocketImpl.performInitialHandshake(SSLSocketImpl.java:1187)   
com.sun.net.ssl.internal.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1215)   
com.sun.net.ssl.internal.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:1199)   
com.sun.jndi.ldap.Connection.createSocket(Connection.java:364)   
com.sun.jndi.ldap.Connection.(Connection.java:186)   
com.sun.jndi.ldap.LdapClient.(LdapClient.java:116) 

Cause

* * *

LDAP authentication requires reverse DNS to be set up. If there is no externally accessible reverse DNS lookup, a delay is seen in authenticating the user.

Resolution

* * *

Reverse DNS lookup needs to be set up on the LDAP server and should be externally accessible.
