---
title: "REST and SOAP requiring TLS extension Server Name Indication (SNI) could cause socket error, handshake failures, etc "
aliases:
  - KB0621614
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621614
kb_number: KB0621614
last_modified: 2024-04-26
---

## REST and SOAP requiring TLS extension Server Name Indication (SNI) could cause socket error, handshake failures, etc

  

### Issue

REST and SOAP requiring TLS extension Server Name Indication (SNI) could cause socket error, handshake failures, etc  

Problem

* * *

[Server Name Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication "Server Name Indication (SNI)") is an extension to the TLS computer networking protocol by which a client indicates the hostname it is attempting to connect to at the start of the handshaking process. This allows:

-   a server to present multiple certificates on the same IP address and TCP port number
-   multiple secure (HTTPS) websites (or any other Service over TLS) to be served off the same IP address without requiring all those sites to use the same certificate

SNI is the conceptual equivalent to HTTP/1.1 name-based virtual hosting, but for HTTPS. It also resolves the problem of having several sites, for which you want a different certificate set.  
  
ServiceNow does not currently support SNI. There are plans to include SNI support in a future release.  
  
   
Symptoms

* * *

Calls using latest SOAPUI and Postman (with SNI support) work properly. SOAPUI v5.3.0+ has support for SNI. Previous versions do not support SNI. However, when testing on the instance, a socket error, handshake failures, or other problems may occur.  
  
To identify the need for SNI, use openssl to validate. On the command line:  
  

1.  Try to retrieve the certificate using the server name (as expected on SNI):  
      
    \> openssl s\_client -connect <server-name>:443 -servername ' <server-name>'  
    is successful retrieves the certificate for  <server-name>  
      
    No errors  
      
    
2.  Try to retrieve the certificate without using the server name:  
      
    \> openssl s\_client -connect <server-name>:443  
    returns an error or a certificate for a different <server-name>  
      
    The following error is displayed:  
      
    \>> SSL\_connect:SSLv2/v3 write client hello A  
    \>> SSL\_connect:error in SSLv2/v3 read server hello A  
    \>> write:errno=54  
      
    Alternatively, the certificate does not match the one retrieved in step 1.  
      
    

Cause

* * *

ServiceNow does not currently support SNI on instances before Jakarta.  

  
Resolution

* * *

On instances before Jakarta, the best solution is to modify the server so that SNI is not needed. For example, use a dedicated IP and certificate for your integration until ServiceNow supports SNI.

Another option is to define how your server responds to the absence of SNI information by providing the wanted certificates (have two different URLs on the same certificate).  
  

<table class="noteTable" style="text-align: left; border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: Providing the same certificate to two different URLs may look unprofessional</td></tr></tbody></table>

After Jakarta,  Server Name Indication (SNI) support is disabled by default for all outbound HTTP requests.  
  
To enable or disable SNI support for outbound HTTP requests sent directly from the instance, set the system property **glide.outbound.tls\_sni.enabled** to true or false (default).  
  
To enable or disable SNI support for outbound HTTP requests sent through a MID Server, create the property **glide.outbound.tls\_sni.enabled** on the MID Server with a value of true or false (default), then restart the MID Server.  
  
More information here:  
[Server Name Indication for outbound web services](https://docs.servicenow.com/csh?topicname=outbound-sni-support.html&version=latest "Server Name Indication for outbound web services")

<table class="noteTable" style="text-align: left; border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: After you change the property, wait at least 30 seconds before testing a request to ensure that a cached connection is not reused</td></tr></tbody></table>
