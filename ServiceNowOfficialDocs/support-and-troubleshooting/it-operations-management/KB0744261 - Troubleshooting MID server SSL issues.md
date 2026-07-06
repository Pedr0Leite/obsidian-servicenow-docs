---
title: "Troubleshooting MID server SSL issues"
aliases:
  - KB0744261
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744261
kb_number: KB0744261
last_modified: 2025-07-01
---

## Troubleshooting MID server SSL issues

  

### Issue

This document provides information on properties and steps to follow when troubleshooting MID server created HTTPS connections.

### Release

All

### Resolution

### Table of Contents

-   [Security Checks](#security_checks "Security Checks")
-   [Bootstrap Parameters](#bootstrap_parameters "Bootstrap Parameters")
-   [Common Errors](#common_errors "Common Errors")
-   [Troubleshooting](#troubleshooting "Troubleshooting")  
    -   [Set ssl debug](#set_ssl_debug "Set ssl debug")
-   [Example troubleshooting](#example_troubleshooting "Example troubleshooting")  
    -   [Certificate Chain Error](#certificate_chain_error "Certificate Chain Error")
    -   [OCSP Error](#ocsp_error "OCSP Error")

### Security Checks

The MID server runs security checks before encrypting a connection to a target. The MID server performs the following checks:

-   Hostname Check  
    -   Hostname verification is a part of HTTPS that involves a server identity check to ensure that the client is talking to the correct server. This check prevents sending information to a server after being redirected by a man in the middle attack. The check involves verifying that the `dnsName` of the certificate sent by the server matches the URL used to make the request.
-   Revocation Check  
    -   An OCSP responder (a server typically run by the certificate issuer) returns a signed response that the certificate is 'good', 'revoked', or 'unknown'. If it cannot process the request, it may return an error code.
-   Certificate Chain Check  
    -   Whether the certificates in the certificate chain are found in the mid server cacerts

Configuration on what checks to run for a target address can be seen on table mid\_cert\_check\_policy. For more information regarding MID Server certificate check policies see:

-   [MID Server certificate check policies](https://docs.servicenow.com/search?q=MID+Server+certificate+check+policies "MID Server certificate check policies")

More information on MID server and certificates:

-   [MID Servers and Certificates](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863673 "MID Servers and Certificates")
-   [MID Server TLS/SSL certificate check policy Quebec upgrade information](KB0867397 "MID Server TLS/SSL certificate check policy Quebec upgrade information")
-   [MID server OCSP requirement details](https://hi.service-now.com/kb_view.do?sysparm_article=KB0854165 "MID server OCSP requirement details")
-   [MID Server shows certificate chain errors with self-signed cert](https://hi.service-now.com/kb_view.do?sysparm_article=KB0864241 "MID Server shows certificate chain errors with self-signed cert")

### Bootstrap Parameters

The MID server loads the following parameters at startup with the following default values, unless explicitly set:

<parameter name="mid.ssl.bootstrap.default.target\_endpoint" value="\*.service-now.com"/>  
<parameter name="mid.ssl.bootstrap.default.check\_cert\_chain" value="true"/>  
<parameter name="mid.ssl.bootstrap.default.check\_cert\_revocation" value="true"/>  
<parameter name="mid.ssl.bootstrap.default.check\_cert\_hostname" value="true"/>

The parameters above are for the initial connection between the MID server and the instance. Once the MID server connects to the instance the MID server runs checks as configured in the mid\_cert\_check\_policy. The above bootstrap parameters can be adjusted if the MID server is down due to certificate errors when connecting to the instance. For self hosted instances, or MID servers connecting to urls not ending in ".service-now.com", the target\_endpoint will need to be updated to match the target url.

**Note:** mid.security.validation.endpoints and com.glide.communications.httpclient.verify\_revoked\_certificate are used in Orlando and Paris. Quebec+ makes full use of the mid\_cert\_check\_policy.

### Common Errors

-   PKIX path building failed
-   Unable to find certificate chain
-   No issuer certificate for certificate in certification path found
-   Peer not authenticated
-   certificate\_unknown
-   Session contains no certificates - Untrusted
-   OCSP revoke check
-   Certificates do not conform to algorithm constraints
-   failed certificate revocation verification
-   OCSP certificate revocation check was not processed
-   No Certificate Policies were returned from the instance

**Note:** When troubleshooting certificate issues, if you see the error "No Certificate Policies were returned from the instance" this error indicates there may be customizations to the file listed below. If this file is customized, please revert it to OOB:

-   sys\_web\_service.do?sys\_id=9d5754c5ff7200006857361332f49d5c

### Troubleshooting

#### Set ssl debug:

1.  Stop the MID server
2.  Open file \\agent\\conf\\wrapper-override.conf
3.  Add either parameter:  
    -   **\-Djavax.net.debug=ssl,handshake**
    -   **\-Djavax.net.debug=all** (fine-grained and highly verbose)
4.  For example:  
    
    wrapper.java.additional.3=-Djavax.net.debug=ssl,handshake
    
5.  Open file \\agent\\config.xml and add parameter
    
    <parameter name="mid.log.level" value="debug"/>
    
6.  Start the MID server
7.  Reproduce the issue
8.  Review file  
    1.  agent\\log\\wrapper log.

**Note:** In Quebec+ with parameter mid.log.level = debug you will also additional debug messages for the security policies. For example:

08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: MIDSecPolicy: calculating security Policy to be applied on instance.service-now.com   
08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: MIDSecPolicy: returning a security policy from the fast cache!  
08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: MIDSecPolicy: hostname verification for host\[instance.service-now.com\] is true  
08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: MIDSecPolicy: calculating security Policy to be applied on instance.service-now.com   
08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: MIDSecPolicy: returning a security policy from the fast cache!  
08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: MIDSecPolicy: Certificate revocation check for host\[instance.service-now.com\] is true  
08/23/21 13:46:49 (168) ECCQueueMonitor.1 DEBUG: Server certificate chain: 

#### Additional properties

To also turn on glide http log, will debug http calls but may not be necessary for SSL issues:

1.  Stop the MID server
2.  Open \\agent\\properties\\glide.properties
3.  Add property  
    1.  glide.http.log\_debug=true
4.  Start the MID server

OR

1.  Stop the MID Server
2.  Open the agent\\config.xml
3.  Add parameter glide.http.log\_debug
    
    <parameter name="glide.http.log\_debug" value="true"/>
    
4.  Start the MID server

### Example Troubleshooting

#### Certificate Chain Error

**Troubleshooting Steps:**

1.  1.  Set debug level
    2.  Determine missing certificate
    3.  Import missing certificate to the MID server

With the ssl debug enabled, we reproduce the issue. In the agent log we see error:

08/23/21 06:50:40 (816) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Request not sent to uri= https://instancename.service-now.com/InstanceInfo.do?SOAP : javax.net.ssl.SSLHandshakeException: PKIX path building failed: java.security.cert.CertPathBuilderException: No issuer certificate for certificate in certification path found.

On the wrapper log we see:

1.  Client Hello
    
    Produced ClientHello handshake message (  
    "ClientHello": {
    
2.  Server Hello
    
    Consuming ServerHello handshake message (  
    "ServerHello": {
    
3.  Certificate Chain
    
    Consuming server Certificate handshake message (  
    "Certificates": \[
    
4.  Error
    
    2021/08/23 06:52:41 | javax.net.ssl|ERROR|52|StartupSequencer|2021-08-23 06:52:41.890 PDT|TransportContext.java:318|Fatal (CERTIFICATE\_UNKNOWN): PKIX path building failed: java.security.cert.CertPathBuilderException: No issuer certificate for certificate in certification path found. (  
    2021/08/23 06:52:41 | "throwable" : {  
    2021/08/23 06:52:41 |   sun.security.validator.ValidatorException: PKIX path building failed: java.security.cert.CertPathBuilderException: No issuer certificate for certificate in certification path found.  
    2021/08/23 06:52:41 |    at java.base/sun.security.validator.PKIXValidator.doBuild(PKIXValidator.java:439)
    

Above steps are standard for a SSL handshake. However, the Certificate Chain step fails and the connection is not established. In the Certificate Chain step we can see the certificates sent back to the MID server before the error:

![](sys_attachment.do?sys_id=2ba504a087aaae9457288519dabb3584)

**Analyze certificate**

**Windows**

From the MID server host, and using the same proxy configured in the mid (if any), we open up the target url and analyze the certificate:

![](sys_attachment.do?sys_id=eba584a087aaae9457288519dabb352d)

![](sys_attachment.do?sys_id=aba584a087aaae9457288519dabb3534)

**Linux**

On Linux MID Servers the OpenSSL command line tool can be used to view certificate. Below is an example (replace INSTANCENAME and ensure port number is accurate).

openssl s\_client -showcerts -servername INSTANCENAME.service-now.com -connect INSTANCENAME.service-now.com:443 2>/dev/null </dev/null

The example below shows how to output ALL certificates to a file:

openssl s\_client -showcerts -servername INSTANCENAME.service-now.com -connect INSTANCENAME.service-now.com:443 2>/dev/null </dev/null |  sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > all.crts

At this point, we see the same certificate in the browser, or output from openssl, and in the MID server wrapper logs. Next we list the certificates in the MID server cacerts file. If using the OOB JRE, the cacerts would be \\agent\\jre\\lib\\security\\cacerts. Using the keytool we can list the certificates. For example:

![](sys_attachment.do?sys_id=23a584a087aaae9457288519dabb3530)

In the above command we used the keytool to send the certificates to a text file. The default password for the keytool is "changeit".

keytool -list -v -keystore "..\\lib\\security\\cacerts" > C:\\temp\\certificates.txt

By comparing the certificate to what we have in the cacerts we see indeed that the intermediate certificate is not present in the cacerts. Because the certificate is indeed not present the connection is terminated, this is for security purposes. A quick workaround for such cases would be to create a policy for this target and set the option "Certificate Chain Check" to false, for creating a MID server certificate check policy see [MID Server certificate check policies](https://docs.servicenow.com/search?q=MID+Server+certificate+check+policies "MID Server certificate check policies"). Also, if the connection failing is the initial connection between the MID server and the instance you could add following parameter to the MID server config.xml:

<parameter name="mid.ssl.bootstrap.default.check\_cert\_chain" value="true"/>

However, a better solution would be to:

1.  Confirm with your team this certificate is valid/safe
2.  Add the certificate to the MID server cacerts

Once you are provided the certificate, you could also get the certificate by following steps of [KB0816002 How to obtain SSL certificate from the browser](https://hi.service-now.com/kb_view.do?sysparm_article=KB0816002 "KB0816002 How to obtain SSL certificate from the browser"), add the certificate to the cacerts with following example command:

keytool -import -alias <certificate alias> -file "<path to certificate>" -keystore "<path to the JRE>\\lib\\security\\cacerts"

For example, you might enter: 

keytool -import -alias MyCA -file "C:\\myca.cer" -keystore "C:\\Program Files\\Java\\jre1.8.0\_161\\lib\\security\\cacerts"

After the certificate is added, we no longer see errors and the connection is successful.

**Note:** Only root and intermediary certs should be added to Trust Certificate Trust List. Never add Leaf (end-entity) certificates to Certificate Trust Lists.

#### OCSP Error

**Troubleshooting Steps:**

1.  1.  Review MID server logs
    2.  Determine the OCSPCheck authority
    3.  Allow communications between MID server and OCSPCheck authority
    4.  Confirm OCSPCheck authority replies with a certStatus "good"

With ssl debug enabled, we reproduce the issue and see in the MID server agent logs errors like so, example errors:

08/23/21 08:38:29 (563) StartupSequencer WARNING \*\*\* WARNING \*\*\* OCSPCheck authority: http://ocsp.entrust.net, error: java.net.ConnectException: Connection timed out: connect  
08/23/21 08:38:29 (563) StartupSequencer WARNING \*\*\* WARNING \*\*\* Request not sent to uri= https://instance.service-now.com/InstanceInfo.do?SOAP : org.apache.commons.httpclient.HttpException: Connection timed out: connect \*.service-now.com

ECCQueueMonitor.1 WARNING \*\*\* WARNING \*\*\* OCSP revoke check IOException for \*.service-now.com   
ECCQueueMonitor.1 WARNING \*\*\* WARNING \*\*\* org.apache.commons.httpclient.HttpException: OCSP communication error 403 Method failed: (/) with code: 403 - Forbidden username/password combo

File sync worker: ecc\_agent\_jar WARNING \*\*\* WARNING \*\*\* Socket error  
File sync worker: ecc\_agent\_jar WARNING \*\*\* WARNING \*\*\* OCSP revoke check IOException for \*.service-now.com  
File sync worker: ecc\_agent\_jar WARNING \*\*\* WARNING \*\*\* org.apache.commons.httpclient.HttpException: Connection reset

Note: In the examples above the OCSPCheck authority is https://ocsp.entrust.net/. This information comes from the certificate and thus could be a different address.

In the wrapper logs we see we see the handshake was successful. However, from the errors above the MID server could not confirm if the certificate was revoked. In the "Certificates" step of the handshake we see in the wrapper log the "AuthorityInfoAccess", which is the address of the endpoint the MID server contact to confirm the certificate is not revoked.

![](sys_attachment.do?sys_id=67a584a087aaae9457288519dabb3532)

If the MID server cannot reach the accessLocation URIName the revocation test will not pass.

To resolve the issue:

-   Review communication between MID server and OCSP server, and review certStatus result:  
    1.  Confirm the MID server can communicate to the OCSP server, may need to involve your network team if communication is being blocked
    2.  Review the traffic and confirm the server replied with a certStatus good. In the following example using wireshark we see the MID server can reach the OCSP server and he certStatus is good  
        ![](sys_attachment.do?sys_id=93a504a087aaae9457288519dabb3582)
-   Or create a policy for the target uri so that the OCSP check is not performed, this is not the suggested workaround

**Note:** Your security team would need to determine what they consider the safest solution out of the two above.

If the MID server is down due to OCSP errors, you could also set following mid server parameter on the config.xml as a temporary workaround:

<parameter name="mid.ssl.bootstrap.default.check\_cert\_revocation" value="true"/>
