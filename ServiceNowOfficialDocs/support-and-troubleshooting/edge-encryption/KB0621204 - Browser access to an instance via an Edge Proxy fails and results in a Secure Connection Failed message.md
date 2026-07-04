---
title: "Browser access to an instance via an Edge Proxy fails and results in a Secure Connection Failed message"
aliases:
  - KB0621204
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621204
kb_number: KB0621204
last_modified: 2024-04-07
---

## Browser access to an instance via an Edge Proxy fails and results in a Secure Connection Failed message

  

### Issue

Browser access to an instance via an Edge Proxy fails and results in a "Secure Connection Failed" message

Problem

* * *

In a browser, attempts to reach an instance via an Edge Proxy fail with a "Secure Connection Failed" error. The following illustration shows the error in Firefox.

![](sys_attachment.do?sys_id=71f8ec6edb02b450e515c22305961945) 

Symptoms

* * *

-   There is no apparent network connection issue detected in your environment between the Edge Encryption proxy and the instance. From the Edge Proxy machine, you can reach the instance by telnet and traceroute:
    
    $ **telnet <instance\_name>.service-now.com 443**  
    Trying 149.96.32.10...  
    Connected to <instance\_name>.service-now.com.  
    Escape character is '^\]'.
    
    $ **traceroute** <instance\_name>**.service-now.com**  
    traceroute to <instance\_name>.service-now.com (149.96.32.10), 64 hops max, 52 byte packets  
    1  irbu21.bor-001a.iad100.service-now.com (10.250.26.50)  30.273 ms  30.656 ms  30.082 ms
    
    2  10.250.26.179 (10.250.26.179)  31.913 ms  31.895 ms  32.076 ms
    
    3  xe-1-2-7u19.bor-001a.sjc0.service-now.com (10.250.4.26)  104.168 ms  104.056 ms  105.594 ms
    
    4  10.250.4.171 (10.250.4.171)  104.277 ms  103.973 ms  104.266 ms
    
    5  vip-149-96-32-10.cust.service-now.com (149.96.32.10)  104.163 ms  103.944 ms  104.252 ms
    
-   Log files:
    
    The Edge Encryption log files show the following:
    
    edgeencryption.log
    wrapper\_<date>.log
    jetty.log
    
-   The <proxy-install-location>/logs log files do not show any indication that there is a problem when the browser connection is attempted and may log nothing when the connection attempt is made.
    
    Execution of an OpenSSL connection from the proxy machine to the instance results in output like the following example.
    
    $ **openssl s\_client -connect 10.0.2.15:8082**
    CONNECTED(00000003)
    140656798164808:error:140790E5:SSL routines:SSL23\_WRITE:ssl handshake failure:s23\_lib.c:184:
    ---
    no peer certificate available
    ---
    No client certificate CA names sent
    ---
    SSL handshake has read 0 bytes and written 249 bytes
    ---
    New, (NONE), Cipher is (NONE)
    Secure Renegotiation IS NOT supported
    Compression: NONE
    Expansion: NONE
    ---
    
-   After adding the Java SSL debug property on the proxy by adding the wrapper.conf file at <proxy-install-location>/conf and adding the following line and restarting the proxy, errors occur in the log file.
    
    wrapper.java.additional.<next number in sequence> = -Djavax.net.debug=all
    
    For example:
    
    wrapper.java.additional.6 = -Djavax.net.debug=all shows the following errors in the log file at <proxy-install-location/logs/wrapper\_<date>.log:  
      
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Compression Methods:  { 0 }  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Extension renegotiation\_info, renegotiated\_connection: <empty>  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Extension elliptic\_curves, curve names: {secp256r1, secp384r1, secp521r1}  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Extension ec\_point\_formats, formats: \[uncompressed\]  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Unsupported extension type\_35, data:  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Unsupported extension type\_13172, data:  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Unsupported extension type\_16, data: 00:27:05:68:32:2d:31:36:05:68:32:2d:31:35:05:68:32:2d:31:34:02:68:32:08:73:70:64:79:2f:33:2e:31:08:68:74:74:70:2f:31:2e:31  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Unsupported extension status\_request, data: 01:00:00:00:00  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | Extension signature\_algorithms, signature\_algorithms: SHA256withRSA, SHA384withRSA, SHA512withRSA, SHA1withRSA, SHA256withECDSA, SHA384withECDSA, SHA512withECDSA, SHA1withECDSA, Unknown (hash:0x4, signature:0x2), SHA1withDSA  
    ...  
    ...  
    ...  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | %% Initialized:  \[Session-2, SSL\_NULL\_WITH\_NULL\_NULL\]  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | matching alias: rsa  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | qtp1601427063-34, fatal error: 40: no cipher suites in common  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | javax.net.ssl.SSLHandshakeException: no cipher suites in common  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | %% Invalidated:  \[Session-2, SSL\_NULL\_WITH\_NULL\_NULL\]  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | qtp1601427063-34, SEND TLSv1.2 ALERT:  fatal, description = handshake\_failure  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | qtp1601427063-34, WRITE: TLSv1.2 Alert, length = 2  
    INFO   | jvm 1    | 2017/02/01 14:30:43.738 | qtp1601427063-34, fatal: engine already closed.  Rethrowing javax.net.ssl.SSLHandshakeException: no cipher suites in common  
     
-   Checking the content of the keystore.jceks file at <proxy-install-location>/keystore using the keystore tool (the $JAVA\_Location/bin PATH must be added) may show that there is no cert alias to handle the proxy/instance connection.
    
       
    $ **keytool -list -keystore keystore.jceks -storetype jceks -v**  
    Enter keystore password:   
       
    Keystore type: JCEKS  
    Keystore provider: SunJCE  
       
    Your keystore contains 3 entries  
       
    Alias name: servicenow  
    Creation date: Jul 13, 2015  
    Entry type: trustedCertEntry  
       
    Owner: CN=Unknown, OU=Platform Development, O=ServiceNow Inc., L=San Diego, ST=CA, C=US  
    Issuer: CN=Unknown, OU=Platform Development, O=ServiceNow Inc., L=San Diego, ST=CA, C=US  
    Serial number: b6b15d5  
    Valid from: Mon Jul 13 17:54:15 PDT 2015 until: Sun Oct 11 17:54:15 PDT 2015  
    Certificate fingerprints:  
                 MD5:  90:CD:AC:1D:FB:DC:32:98:51:26:69:4C:56:1E:1C:40  
                 SHA1: 6B:46:C7:A6:67:6D:8E:BC:22:08:B6:47:F8:3E:3D:A7:91:30:AE:C7  
                 SHA256: 95:50:4C:25:C6:01:D1:DC:5B:19:2E:54:64:9C:1A:02:22:23:68:AC:33:87:D7:D0:04:48:FD:BD:00:8F:65:D1  
                 Signature algorithm name: SHA256withRSA  
                 Version: 3  
       
    Extensions:  
       
    #1: ObjectId: 2.5.29.14 Criticality=false  
    SubjectKeyIdentifier \[  
    KeyIdentifier \[  
    0000: 3B 73 BE C8 E6 05 A5 06   97 A4 D6 FC 86 A6 A3 0D  ;s..............  
    0010: 98 42 43 9E                                        .BC.  
    \]  
    \]  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    Alias name: aes128  
    Creation date: Sep 29, 2016  
    Entry type: SecretKeyEntry  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    Alias name: rsa  
    Creation date: Sep 29, 2016  
    Entry type: PrivateKeyEntry  
    Certificate chain length: 1  
    Certificate\[1\]:  
    Owner: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown  
    Issuer: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown  
    Serial number: 54e78389  
    Valid from: Thu Sep 29 09:15:36 PDT 2016 until: Wed Dec 28 08:15:36 PST 2016  
    Certificate fingerprints:  
                 MD5:  91:28:F4:FD:D0:EE:36:37:B0:66:B0:8C:14:C7:C6:2F  
                 SHA1: 7D:69:02:1B:B7:45:9E:03:FB:9F:D0:96:94:E5:63:FC:D2:F2:DD:9F  
                 SHA256: CE:93:BF:2B:02:41:0A:55:FE:B3:6C:C7:B0:0E:35:CA:1D:AE:14:90:BA:93:F9:5F:EC:FF:77:CE:79:D8:D5:7E  
                 Signature algorithm name: SHA256withRSA  
                 Version: 3  
       
    Extensions:  
       
    #1: ObjectId: 2.5.29.14 Criticality=false  
    SubjectKeyIdentifier \[  
    KeyIdentifier \[  
    0000: E8 A6 B0 A8 86 A7 0B 1B   D7 97 2A 3A EB 45 2A 60  ..........\*:.E\*\`  
    0010: 45 CD 53 3A                                        E.S:  
    \]  
    \]  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
       
    where in a good case you see the Alias name: cert as in the following example.  
      
    $ **keytool -list -keystore keystore.jceks -storetype jceks -v**  
    Enter keystore password:   
       
    Keystore type: JCEKS  
    Keystore provider: SunJCE  
       
    Your keystore contains 4 entries  
    Alias name: servicenow  
    Creation date: Jul 13, 2015  
    Entry type: trustedCertEntry  
       
    Owner: CN=Unknown, OU=Platform Development, O=ServiceNow Inc., L=San Diego, ST=CA, C=US  
    Issuer: CN=Unknown, OU=Platform Development, O=ServiceNow Inc., L=San Diego, ST=CA, C=US  
    Serial number: b6b15d5  
    Valid from: Mon Jul 13 17:54:15 PDT 2015 until: Sun Oct 11 17:54:15 PDT 2015  
    Certificate fingerprints:  
                 MD5:  90:CD:AC:1D:FB:DC:32:98:51:26:69:4C:56:1E:1C:40  
                 SHA1: 6B:46:C7:A6:67:6D:8E:BC:22:08:B6:47:F8:3E:3D:A7:91:30:AE:C7  
                 SHA256: 95:50:4C:25:C6:01:D1:DC:5B:19:2E:54:64:9C:1A:02:22:23:68:AC:33:87:D7:D0:04:48:FD:BD:00:8F:65:D1  
                 Signature algorithm name: SHA256withRSA  
                 Version: 3  
       
    Extensions:  
    #1: ObjectId: 2.5.29.14 Criticality=false  
    SubjectKeyIdentifier \[  
    KeyIdentifier \[  
    0000: 3B 73 BE C8 E6 05 A5 06   97 A4 D6 FC 86 A6 A3 0D  ;s..............  
    0010: 98 42 43 9E                                        .BC.  
    \]  
    \]  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
     Alias name: aes128  
    Creation date: Sep 29, 2016  
    Entry type: SecretKeyEntry  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   
    Alias name: cert  
    Creation date: Sep 29, 2016  
    Entry type: PrivateKeyEntry  
    Certificate chain length: 1  
    Certificate\[1\]:  
    Owner: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown  
    Issuer: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown  
    Serial number: 5754eb47  
    Valid from: Thu Sep 29 09:13:28 PDT 2016 until: Wed Dec 28 08:13:28 PST 2016  
    Certificate fingerprints:  
                 MD5:  B3:D0:B5:22:F3:9F:50:38:5D:16:E8:F1:E8:B7:43:73  
                 SHA1: F2:90:80:FE:AB:A7:11:72:D1:BA:36:48:A6:EF:A7:54:5C:68:15:DD  
                 SHA256: 00:98:FC:1C:E7:1F:F2:00:D8:93:DB:DB:E1:E4:5A:55:66:6D:B4:03:31:03:B6:5A:97:3F:86:C0:23:BF:42:12  
                 Signature algorithm name: SHA256withRSA  
                 Version: 3  
       
    Extensions:  
    #1: ObjectId: 2.5.29.14 Criticality=false  
    SubjectKeyIdentifier \[  
    KeyIdentifier \[  
    0000: AB 0B 96 17 F0 56 83 D6   E9 79 1A 3A EF C5 AE 3E  .....V...y.:...>  
    0010: FC 6D 60 F9                                        .m\`.  
    \]  
    \]  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
     Alias name: rsa  
    Creation date: Sep 29, 2016  
    Entry type: PrivateKeyEntry  
    Certificate chain length: 1  
    Certificate\[1\]:  
    Owner: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown  
    Issuer: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown  
    Serial number: 54e78389  
    Valid from: Thu Sep 29 09:15:36 PDT 2016 until: Wed Dec 28 08:15:36 PST 2016  
    Certificate fingerprints:  
                 MD5:  91:28:F4:FD:D0:EE:36:37:B0:66:B0:8C:14:C7:C6:2F  
                 SHA1: 7D:69:02:1B:B7:45:9E:03:FB:9F:D0:96:94:E5:63:FC:D2:F2:DD:9F  
                 SHA256: CE:93:BF:2B:02:41:0A:55:FE:B3:6C:C7:B0:0E:35:CA:1D:AE:14:90:BA:93:F9:5F:EC:FF:77:CE:79:D8:D5:7E  
                 Signature algorithm name: SHA256withRSA  
                 Version: 3  
       
    Extensions:  
       
    #1: ObjectId: 2.5.29.14 Criticality=false  
    SubjectKeyIdentifier \[  
    KeyIdentifier \[  
    0000: E8 A6 B0 A8 86 A7 0B 1B   D7 97 2A 3A EB 45 2A 60  ..........\*:.E\*\`  
    0010: 45 CD 53 3A                                        E.S:  
    \]  
    \]  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
      
    
    In this example, the certs should have been added to keystore.jcek using self-signing in the following example commands:
    
    keytool -genkey -alias cert -keyalg rsa -keystore keystore.jceks -storetype jceks
    keytool -genkey -alias rsa -keyalg rsa -keystore keystore.jceks -storetype jceks
    keytool -genseckey -alias aes128 -keyalg aes -keystore keystore.jceks -storetype jceks -keysize 128
    
    The certificate that manages the https connection between the proxy and the instance is the one with \-alias cert in the command line.
    

# Causes

* * *

The connection is failing due to two possible causes:

-   A misconfiguration of the keystore.jceks file for the https certificate between the proxy and instance.  The certificate between the proxy and instance is the one with the "cert" alias as shown previously, that is:
    
    Alias name: cert
    Creation date: Sep 29, 2016
    Entry type: PrivateKeyEntry
    Certificate chain length: 1
    Certificate\[1\]:
    Owner: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
    Issuer: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
    Serial number: 5754eb47
    Valid from: Thu Sep 29 09:13:28 PDT 2016 until: Wed Dec 28 08:13:28 PST 2016
    Certificate fingerprints:
                 MD5:  B3:D0:B5:22:F3:9F:50:38:5D:16:E8:F1:E8:B7:43:73
                 SHA1: F2:90:80:FE:AB:A7:11:72:D1:BA:36:48:A6:EF:A7:54:5C:68:15:DD
                 SHA256: 00:98:FC:1C:E7:1F:F2:00:D8:93:DB:DB:E1:E4:5A:55:66:6D:B4:03:31:03:B6:5A:97:3F:86:C0:23:BF:42:12
                 Signature algorithm name: SHA256withRSA
                 Version: 3
     
    Extensions:
     
    #1: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier \[
    KeyIdentifier \[
    0000: AB 0B 96 17 F0 56 83 D6   E9 79 1A 3A EF C5 AE 3E  .....V...y.:...>
    0010: FC 6D 60 F9                                        .m\`.
    \]
    \] Alias name: cert
    Creation date: Sep 29, 2016
    Entry type: PrivateKeyEntry
    Certificate chain length: 1
    Certificate\[1\]:
    Owner: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
    Issuer: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
    Serial number: 5754eb47
    Valid from: Thu Sep 29 09:13:28 PDT 2016 until: Wed Dec 28 08:13:28 PST 2016
    Certificate fingerprints:
                 MD5:  B3:D0:B5:22:F3:9F:50:38:5D:16:E8:F1:E8:B7:43:73
                 SHA1: F2:90:80:FE:AB:A7:11:72:D1:BA:36:48:A6:EF:A7:54:5C:68:15:DD
                 SHA256: 00:98:FC:1C:E7:1F:F2:00:D8:93:DB:DB:E1:E4:5A:55:66:6D:B4:03:31:03:B6:5A:97:3F:86:C0:23:BF:42:12
                 Signature algorithm name: SHA256withRSA
                 Version: 3
     
    Extensions:
     
    #1: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier \[
    KeyIdentifier \[
    0000: AB 0B 96 17 F0 56 83 D6   E9 79 1A 3A EF C5 AE 3E  .....V...y.:...>
    0010: FC 6D 60 F9                                        .m\`.
    \]
    \]
    
-   This "cert" alias may be misconfigured or missing from the keystore.jceks file.
    

# Resolution

* * *

There are a couple of resolutions for this issue.

-   If the "cert" does not exist in the keystore.jceks file after execution of:
    
     keytool -list -keystore keystore.jceks -storetype jceks -v
    
    As mentioned in the Symptoms section, it can be added using keytool, as in the following self-signed certificate example.
    
    keytool -genkey -alias cert -keyalg rsa -keystore keystore.jceks -storetype jceks
    
-   If the execution of:
    
    keytool -list -keystore keystore.jceks -storetype jceks -v
    
    shows an https certificate between the proxy and instance, there might be a problem with how it was initially entered.  To resolve this issue, you may want to delete the current "cert" alias entry as follows:
    
    keytool -delete -keystore keystore.jceks -alias cert -storetype jceks
    
    And add it again making sure that the properties are correct as in this example:
    
    keytool -genkey -alias cert -keyalg rsa -keystore keystore.jceks -storetype jceks
    
    After changes are made to keystore.jceks, the Edge Proxy will need to be restarted and the browser access retried.
