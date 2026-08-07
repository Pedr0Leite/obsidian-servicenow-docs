---
title: "Resolve a failed email account connection when using SSL on a self-hosted instance"
aliases:
  - KB0748183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748183
kb_number: KB0748183
last_modified: 2025-06-20
---

## Resolve a failed email account connection when using SSL on a self-hosted instance

  

### Issue

On a self-hosted instance configured to use SSL, the connection fails when testing the email account.

### Release

Applies to any release on a self-hosted instance

### Cause

When the SSL handshake fails, verify the issue by doing the following:

1\. Create the system property based on the email account type that fails to connect:

For POP3:

Name = glide.pop3.debug   
Type = true|false  
Value = true

For IMAP:

Name = glide.imap.debug   
Type = true|false  
Value = true

For SMTP:

Name = glide.smtp.debug   
Type = true|false  
Value = true

2\. On the instance nodes, modify the wrapper.conf file to add the java start property: \-Djavax.net.debug=all - /glide/nodes/<instance\_info>/conf/wrapper.conf: 

**Note:** This spacer is for custom, per-instance expansion: wrapper.java.additional.9=-Djavax.net.debug=all 

3\. Restart the instance nodes.   
  
4\. Check the wrapper\_<date>.log. You should see the following. In this example **glide.pop3.debug** is set to **true**: 

INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG: setDebug: JavaMail version 1.5.6   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG: getProvider() returning javax.mail.Provider\[STORE,pop3,com.sun.mail.pop3.POP3Store,Oracle\]   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.rsetbeforequit: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.disabletop: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.forgettopheaders: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.cachewriteto: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.filecache.enable: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.keepmessagecontent: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.starttls.enable: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.starttls.required: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.finalizecleanclose: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.apop.enable: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: mail.pop3.disablecapa: false   
INFO | jvm 4 | 2018/03/12 07:53:57.901 | DEBUG POP3: connecting to host "popmail.intel.com", port 995, isSSL true   
INFO | jvm 4 | 2018/03/12 07:55:18.303 | \[Fatal Error\] :1:1: Content is not allowed in prolog.   
INFO | jvm 4 | 2018/03/12 07:55:28.516 | - I/O exception (java.net.ConnectException) caught when processing request: Connection refused (Connection refused)   
INFO | jvm 4 | 2018/03/12 07:55:28.516 | - Retrying request   
INFO | jvm 4 | 2018/03/12 07:55:28.717 | - I/O exception (java.net.ConnectException) caught when processing request: Connection refused (Connection refused)   
INFO | jvm 4 | 2018/03/12 07:55:28.717 | - Retrying request   
INFO | jvm 4 | 2018/03/12 07:55:29.017 | - I/O exception (java.net.ConnectException) caught when processing request: Connection refused (Connection refused)   
INFO | jvm 4 | 2018/03/12 07:55:29.017 | - Retrying request   
INFO | jvm 4 | 2018/03/12 07:56:38.907 | DEBUG: setDebug: JavaMail version 1.5.6 

Also the additional SSL debug shows the following: 

INFO | jvm 2 | 2018/03/12 09:08:03.014 | \*\*\*   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | %% Invalidated: \[Session-3, TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA\]   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | glide.scheduler.worker.1, SEND TLSv1 ALERT: fatal, description = certificate\_unknown   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | glide.scheduler.worker.1, WRITE: TLSv1 Alert, length = 2   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | \[Raw write\]: length = 7   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | 0000: 15 03 01 00 02 02 2E .......   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | glide.scheduler.worker.1, called closeSocket()   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | glide.scheduler.worker.1, handling exception: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | adding as trusted cert:   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | Subject: CN=eBusiness C-1, O=Secure Inc., C=US   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | Issuer: CN=eBusiness C-1, O=Secure Inc., C=US   
INFO | jvm 2 | 2018/03/12 09:08:03.014 | Algorithm: RSA; Serial number: 0xc2134  
INFO | jvm 2 | 2018/03/12 09:08:03.014 | Valid from Sun Jun 20 21:00:00 PDT 1999 until Sun Jun 21 21:00:00 PDT 2020 

The following shows an SSL handshake error: 

INFO | jvm 2 | 2018/03/12 09:08:03.014 | glide.scheduler.worker.1, handling exception: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target 

### Resolution

There are two possible solutions:

1\. From the command line on one of the instance nodes, run the following, and then add the appropriate X.509 SSL certificate to the instance:

openssl s\_client -connect <email account hostname>:<SSL port> -showcerts

For example:

openssl s\_client -connect mymail.sn.com:995 -showcerts

You should see an X.509 cert that looks something like this in the output:

\-----BEGIN CERTIFICATE-----  
MIIFPTCCBCWgAwIBAgIQYPiq3h8HUIMAAAAAUN/oujANBgkqhkiG9w0BAQsFADCB  
.......  
liGTZg98uJJfH/PQMfGzX20sG5QerWom+0VkvF4xDWZ+VDZFHNNCOQnb1U+/GIDT  
5Q==  
\-----END CERTIFICATE-----

Take that and on the instance go to System Definition -> Certificates -> select New:

Name = <name of your choice>  
In the "PEM Certificate" field copy and paste everything including the -----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- and of course all of the base-64 encoding between

Save that and try the connection again

2\. This option avoids the need to supply the X.509 SSL certificate in the instance from the first solution above. Modify or create these two system properties as follows: 

Name = com.glide.communications.trustmanager\_trust\_all  
Type = true|false  
Value = true

and

Name = com.glide.communications.httpclient.verify\_hostname   
Type = true|false  
Value = false
