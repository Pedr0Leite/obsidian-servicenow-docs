---
title: "MID Server support for AES 256 encryption"
aliases:
  - KB0594703
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0594703
kb_number: KB0594703
last_modified: 2025-01-03
---

## Issue

MID Server uses OpenSSL while connecting to the Instance. Although, OpenSSL supports AES 256 encryption, MID Server does not use it while communicating to the Instance.

This article documents the steps to force the MID server to use AES 256 encryption while communicating to the Instance.

## Resolution

Use the following steps to force the MID Server to support AES 256 Encryption. This is done by disabling weaker algorithms, thereby forcing it to use at least AES256.

![](/Info_25x.pngx "Information") These changes need to be performed individually on each MID Server where AES 256 support is required.

1.  Stop the MID Server
2.  Browse to <Install folder>\\**agent\\jre\\lib\\security** on Windows or <Install folder>/agent /jre/lib/security on Linux.
3.  Open the file **java.security** in a text editor
4.  Change the below entry:

  

_**Pre-Orlando**_

from

jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 768

to

jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 768, AES\_128\_CBC, AES\_128\_GCM, 3DES\_EDE\_CBC  
  

_**Post-Orlando**_

from

jdk.tls.disabledAlgorithms=SSLv3, RC4, DES, MD5withRSA, DH keySize < 1024, \\  
    EC keySize < 224, 3DES\_EDE\_CBC, anon, NULL

to

jdk.tls.disabledAlgorithms=SSLv3, RC4, DES, MD5withRSA, DH keySize < 1024, \\  
    EC keySize < 224, 3DES\_EDE\_CBC, anon, NULL, AES\_128\_CBC, AES\_128\_GCM  
  

5.  Save the File
6.  Start the MID Server.

![](/important_25x.pngx "Important")**Important**: These changes are to be repeated every time a MID Server is upgraded. See below.

  

## Additional Information

On a MID Server upgrade (to be exact a JRE update), java.security will be overwritten. If you make it read-only to prevent overwriting, the update will fail. Hence the only option is to repeat these changes after every upgrade.

The success of the changes can be observed by running a network traffic monitoring tool like _wireshark_ or _ssldump_.

Below is an example using wireshark:

![](/sys_attachment.do?sys_id=df0f81f4db0834d0fec4fb24399619a5)

The following example uses _ssldump_ 0.9b3.

The ClientHello message is the client's proposals, and ServerHello message shows the server's selection. Both of these packets are sent in plain text, so you don't have to worry about decryption keys like you would with most SSL/TLS traffic.

This is how a successful AES 256 handshake looks in _ssldump_:

_$_ ssldump -i en0  
New TCP connection #1: <IP\_Address>(55282) <->_<instance\_name>_.service-now.com(443)  
1 1 0.0733 (0.0733) C>S Handshake  
ClientHello  
Version 3.3   
cipher suites  
TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384  
TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384  
TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256  
TLS\_ECDH\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384  
TLS\_ECDH\_RSA\_WITH\_AES\_256\_CBC\_SHA384  
TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA256  
TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA256  
TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA  
TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA  
TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA  
TLS\_ECDH\_ECDSA\_WITH\_AES\_256\_CBC\_SHA  
TLS\_ECDH\_RSA\_WITH\_AES\_256\_CBC\_SHA  
TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA  
TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA  
TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_ECDH\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_ECDH\_RSA\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_DHE\_DSS\_WITH\_AES\_256\_GCM\_SHA384  
TLS\_EMPTY\_RENEGOTIATION\_INFO\_SCSV  
compression methods  
NULL  
1 2 0.1346 (0.0612) S>C Handshake  
ServerHello  
Version 3.3   
session\_id\[32\]=  
a3 27 5a c5 d3 e1 25 94 88 9a 82 02 8f f2 de a6   
3a 63 8a e9 03 10 b9 64 a4 23 75 1b 17 8a de c0   
cipherSuite TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA  
compressionMethod NULL
