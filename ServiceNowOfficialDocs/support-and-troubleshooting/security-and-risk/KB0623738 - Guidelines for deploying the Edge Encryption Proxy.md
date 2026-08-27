---
title: "Guidelines for deploying the Edge Encryption Proxy"
aliases:
  - KB0623738
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623738
kb_number: KB0623738
last_modified: 2024-04-24
---

## Issue

# Edge Encryption Proxy Deployment Guidelines

Things you can do to smooth deployment of an Edge Encryption Proxy

You may be considering investing in greater data security by deploying ServiceNow's Edge Encryption Proxy.  If you have already purchased Edge Proxy, then perhaps you have some questions prior to full deployment.  This article is intended to assist you as you prepare to leverage this powerful data security tool.

There are aspects to any Edge Proxy deployment which must be taken into account beforehand.  Such things as networking, certificates, proxy configuration, and the token database must be considered.  Let's take a closer look at these factors.

**Networking: Know your network.**

It is imperative to understand your network environment as well as where the Edge Proxy would be deployed.  It is not a replacement for a simple pass-through proxy.  Neither is it a caching and web acceleration tool.  It is an [SSL forward proxy](http://www.juniper.net/techpubs/en_US/junos-space15.2/topics/concept/junos-space-ssl-forward-proxy-overview.html).  The client initiates a secure session with the Edge Proxy which is then terminated.  The Edge Proxy initiates a session with your ServiceNow instance on behalf of the client.  The client does not interact directly with the instance, and the reverse is also true.  The proxy, therefore, manages two sessions at once.  This is an important networking consideration.  Please note that Edge Proxy is a Java application.  Java manages HTTP sessions but offloads networking to the host OS.  The host OS' TCP stack, therefore, must be tuned for optimum performance.  Below are some informative links.

-   [https://technet.microsoft.com/en-us/library/2007.01.cableguy.aspx](https://technet.microsoft.com/en-us/library/2007.01.cableguy.aspx)
-   [https://blogs.technet.microsoft.com/networking/2016/08/11/an-update-on-windows-tcp-autotuninglevel/](https://blogs.technet.microsoft.com/networking/2016/08/11/an-update-on-windows-tcp-autotuninglevel/)
-   [https://kb.vmware.com/selfservice/microsites/search.do?language=en\_US&cmd=displayKC&externalId=2129176](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2129176)
-   [http://pubs.vmware.com/vsphere-60/index.jsp?topic=/com.vmware.vsphere.networking.doc/GUID-D80AEC2F-E0DA-4172-BFFD-B721BF36C2E8.html](http://pubs.vmware.com/vsphere-60/index.jsp?topic=/com.vmware.vsphere.networking.doc/GUID-D80AEC2F-E0DA-4172-BFFD-B721BF36C2E8.html)
-   [https://www.ibm.com/support/knowledgecenter/SS7JFU\_8.5.5/com.ibm.websphere.express.doc/ae/tprf\_tunewindows.html](https://www.ibm.com/support/knowledgecenter/SS7JFU_8.5.5/com.ibm.websphere.express.doc/ae/tprf_tunewindows.html)

 [](https://www.ibm.com/support/knowledgecenter/SS7JFU_8.5.5/com.ibm.websphere.express.doc/ae/tprf_tunewindows.html)

## **Sizing recommendations**

ServiceNow recommends that customers deploy at least two Edge Encryption Proxies.  This not only provides for good performance, but also allows for service resiliency in the case of failure of a single host. A recent performance enhancement allows the proxy to make a much greater number of connections to a single host than was previously possible.  This update is available beginning with the following releases: Helsinki Patch 4 Hotfix 5, Helsinki Patch 10, Istanbul Patch 5 and Patch 6, Jakarta. 

At minimum each Edge Proxy should have 4GB of available RAM to use.  Six GB of RAM is recommended.  This implies a hardware requirement of at least an additional 1GB of RAM for the operating system. The following property is commented out by default but should be enabled if hardware requirements are met: [wrapper.java.initmemory](https://docs.servicenow.com/csh?topicname=increase-memory.html&version=latest)\=4096.  If six GB of RAM are available, then the value would be 6144.  The file to edit is <install dir>/conf/wrapper.conf.

While we do not typically set an upper bound for memory utilization it may be something for you to consider setting if the system will be hosting more than one service.  Java will consume nearly all remaining system memory if an upper bound is not set.  In order to set the upper bound, please use the following parameter in wrapper.conf: [wrapper.java.maxmemory](https://wrapper.tanukisoftware.com/doc/english/prop-java-maxmemory.html)\=XX.  The numerical value is expressed in megabytes and must be equal to or larger than that set in wrapper.java.initmemory.

**Load balancer considerations**

With several Edge proxies in a load balancer pool and the load balancer doing SSL termination, clients will need the load balancer to present a certificate valid for the FQDN of the virtual host.  As long as that certificate is trusted by the clients, there should be no issue.  It would then be a choice on your part whether the load balancer uses HTTPS to talk to the Edge proxies, or simple HTTP.  The latter could be used if that leg of the network is secure and you want to avoid SSL overhead.  The Edge proxies will always use HTTPS when connecting to your ServiceNow instance.

Another key factor when using load balancers is that client sessions must be persistent.  This means that if a client connects to the proxy using pool member A, then all subsequent traffic between the proxy and the client must go through pool member A.  How this is accomplished depends on the specific load balancer.  One strategy is to use session ID headers, but it is not the only approach.  Here is information for F5 load balancers.

-   [https://support.f5.com/kb/en-us/products/lc\_9\_x/manuals/product/lc\_config\_guide\_10\_1/lc\_persist\_profiles.html](https://support.f5.com/kb/en-us/products/lc_9_x/manuals/product/lc_config_guide_10_1/lc_persist_profiles.html)

**Certificates and keystores: Involve your security team**

Your security team is an essential part of your deployment process.  They are typically in charge of creating the certificates needed by your Edge Proxy.  The proxy or proxies need certificates which your clients will trust.  As such they will have to be signed by a trusted Certificate Authority (CA).  This certificate will have to be placed into the Edge Proxy's keystore since it will present this certificate to your clients when they attempt to connect.  If you use a load balancer and terminate SSL as mentioned above, then the certificate will be presented by the load balancer.  Again, clients would have to trust the certificate.

-   [Some PKI basics](https://nwrickert.wordpress.com/2011/10/07/certificates-for-dummies/)
-   [What's the difference between a keystore and a truststore?](http://java67.blogspot.com/2012/12/truststore-vs-keystore-in-java-ssl.html)

**Mind your keystores**

The Edge Encryption Proxy is able to use Java keystores as well as SafeNet KeySecure keystores out of the box.  In its default configuration the Edge Proxy will rely on a Java keystore: keystore.jceks.  Note that this is not a JKS file.  [JCEKS](http://pyjks.readthedocs.io/en/latest/jks.html)  (**J**ava **C**ryptography **E**xtension **K**ey**S**tore) files, in general, offer better protection than JKS.  Keystore.jceks is where the proxy stores the certificates it will present as a client.  It also stores your encryption key(s) and its digital signature for signing changes to the encryption properties and configuration files.

-   [https://docs.servicenow.com/csh?topicname=t\_SetUpAKeyPair.html&version=latest](https://docs.servicenow.com/csh?topicname=t_SetUpAKeyPair.html&version=latest)
-   [https://docs.servicenow.com/csh?topicname=t\_CreateEncryptionKeys.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CreateEncryptionKeys.html&version=latest)

Keystore.jceks has a copy of the ServiceNow public key.  This key must be a part of the keystore so that the proxy can trust out of box rules and configurations.  It is possible for you to build your own keystore, but this key must be part of it. When you modify this file, please remember not to set a different password for items inside the keystore.  While it is possible to do so, we are unable to open items inside the keystore which have a different password than the file itself at this time.  Here is a sample command for [importing a certificate into a JCEKS keystore](https://www.ibm.com/support/knowledgecenter/en/SSB2KG_1.0.0/com.ibm.tivoli.isklm.doc_11/top_EKMipug_example_1.html): keytool -import -keystore my\_keystore.jceks -file new\_cert.pem -alias my\_client\_cert -storepass "SOME\_PASSWORD" -storetype JCEKS.

-   [https://docs.servicenow.com/csh?topicname=t\_SetUpSecureSSLConnection.html&version=latest](https://docs.servicenow.com/csh?topicname=t_SetUpSecureSSLConnection.html&version=latest)

If you have multiple proxies connecting to the same instance they should either have a copy of the same keystore file, or should read the keystore from a shared network location.  Either of these \[MW12\] could be difficult to manage.  For this reason, Edge Encryption Proxies can also use SafeNet KeySecure keystores.  This allows for full lifecycle management, automated operations and many other benefits.  Configuration information is found below.

-   [https://docs.servicenow.com/csh?topicname=t\_SetUpNAEKeyStore.html&version=latest](https://docs.servicenow.com/csh?topicname=t_SetUpNAEKeyStore.html&version=latest)

**Know your properties**

The edgeencryption.properties file is the primary configuration document for your Edge Encryption Proxy.  These properties are discussed in the online documentation, but we should take a moment to review some in more detail.

-   [https://docs.servicenow.com/](https://docs.servicenow.com/)

One key property is [edgeencryption.proxy.host](https://docs.servicenow.com/csh?topicname=c_InstallEdgeEncryptionProxy.html&version=latest "edgeencryption.proxy.host").  The documentation is clear: "Server name, IP address, or fully qualified domain name of the computer running the proxy. Along with the port, this property defines the URL used by the client to access the proxy server." The value is important for two reasons.  First, this is the IP or FQDN (Fully Qualified Domain Name) of the host running the Edge Proxy service, not just a host name.  This means having foo.bar.com (FQDN) and not simply foo (server name).  This value is important because it is the host name which the Edge proxy presents to clients upon connection.  Client browsers understand this as the host where resources may be found.  Second, since this will typically be a secure connection, a client will review the certificate presented by the proxy and test whether the DNS record for foo.bar.com resolves to the IP of the host presenting that certificate.  If not, the SSL/TLS session is aborted.  This has further implications for more advanced configurations.  For example, the name of the load balancer can be used in this parameter.  This device will then take care of routing traffic to the appropriate proxy behind it.  Finally, it should be noted that this parameter should never use the loopback address (127.0.0.1) or localhost.  As mentioned before, the proxy provides that address when presenting resources: https://127.0.0.1:8082/navpage.do for example.  The browser would understand that "navpage.do" is found at its localhost address, which is false, and the browser would throw an error.

Let us say that you have decided that multiple Edge proxies are needed to make efficient use of resources.  Each host will still have to have its FQDN in edgeencryption.proxy.host.  In case that the load balancer terminates SSL/TLS, the clients will not communicate directly with the Edge proxies.  Therefore, the proxies will only communicate with the load balancer before them and the instance on the other side.  It is possible for the load balancer not to communicate with the proxies using SSL/TLS to reduce overhead.  This should only be considered if the network is known secured and trusted.  In case that the load balancer simply passes the connections to the proxy pool and sticks sessions to specific proxies, it is still recommended that the value remain the local FQDN.  However, it is in this configuration that certificate validation can become a more complex issue.  Let's say that the client attempts to connect to edge.mydomain.com.  It will expect a certificate issued to edge.mydomain.com, but the proxies may respond with a certificate where the Subject field has a value of proxy\_X.mydomain.com.  If there is nothing further in the Subject Alternative Name field, this connection will fail.  The client would not be able to validate that proxy\_X.mydomain.com is a valid holder of the edge.mydomain.com certificate.  However, if the [Subject Alternative Name](https://en.wikipedia.org/wiki/Subject_Alternative_Name) field includes proxy\_X.mydomain.com and FQDNs of the other pool members, the connection will succeed regardless of which member responds.  [Here](https://technet.microsoft.com/en-us/library/ff625722%28v=ws.10%29.aspx) is how to set the field value on Windows.

Two other properties are important if you decide to run multiple proxies: edgeencryption.customer.assigned.known.cleartext and edgeencryption.encrypter.static.iv.  These properties must have the same values on all your proxies.  The first is an encrypted text which is used to determine that all the proxies are using the same keys.  The second is the salt value which is used for equality preserving and order preserving encryption types.  Note that this salt property must be exactly 16 bytes.  In Linux the following command may be used to generate this random string: tr -dc "\[:graph:\]" < /dev/urandom | head -c 16.

-   [https://docs.servicenow.com/](https://docs.servicenow.com/)

**_Understanding Encryption Tokens_**

The Edge Encryption Proxy allows you to create tokens which replace matching text.  If you create a pattern for matching text "foo" a replacement token will be created and stored in the instance.  The token will be the same size as the text it is replacing and will substitute it whenever matched.  When you search the instance for "foo", the query sent is for the token value.  When the results are returned, the token value is replaced by "foo".  This means  that the original data never leaves your network. It is stored in the same database catalog used for order preserving encryption.

Here are some tips:

-   You can use out of box patterns or make your own.  Basic patterns simply use a specific sequence of characters.  Advanced patterns use Java's powerful [RegEx engine.](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)
-   A pattern of all alpha characters is not allowed
-   The minimum pattern size is 5 characters but this is modifiable via the [glide.edge.pattern.min.size property](https://docs.servicenow.com/)
-   The following characters are illegal in patterns: (\*) and (+)

**Logs are your friend**

There are four logs which the Edge Encryption Proxy generates: edgeencryption.log, jetty.log, wrapper.log and edgenetwork.log.  The edgeencryption.log is the primary application log.  It contains information regarding operations like startup and shutdown.  It also includes transaction information, errors and warnings.  The wrapper.log is the default logging facility when debugging parameters are set.  The Jetty log contains output from the Jetty servlet.  Jetty debugging can be enabled by editing the <install dir>/conf/log4j.properties.  More information about the logging facility may be found here: [http://www.eclipse.org/jetty/documentation/9.0.6.v20130930/configuring-logging.html](http://www.eclipse.org/jetty/documentation/9.0.6.v20130930/configuring-logging.html).

The edgenetwork.log is available beginning on releases Helsinki Patch 10, Istanbul Patch 6 and Jakarta.  It is not enabled by default but can be turned on dynamically by adding a property to the <install dir>/conf/log4j.properties file.  There is no need to restart the proxy.  In a few minutes the file will appear within the logs folder.  The relevant properties are below.

#log4j.logger.com.snc.edgeencryption.metrics.EdgeEncryptionTimingMetricCache=info, TimingLog

#log4j.appender.TimingLog=org.apache.log4j.RollingFileAppender

#log4j.appender.TimingLog.File=../logs/edgenetwork.log

#log4j.appender.TimingLog.MaxFileSize=500MB

#log4j.appender.TimingLog.MaxBackupIndex=4

#log4j.appender.TimingLog.layout=org.apache.log4j.PatternLayout

#log4j.appender.TimingLog.layout.ConversionPattern=%d %-5p %m%n

You may set the logging level to warn, info or debug.  Warn level records requests which require more than ten seconds.  This includes request processing time including rules execution, round trip to instance, and response processing.  Info level records requests which take more than five seconds.  Debug records all requests.

If you encounter an issue with your Edge Proxy it is recommended that you provide a copy of all proxy logs when you open an incident.  This will allow the Technical Support Engineer to immediately begin diagnosing the problem.

**Timing is everything**

There are times when proxy logs are not enough.  Here is an example of a difficult issue.  When connecting through the Edge Proxy the browser recorded HTTP response code 504, Gateway Timeout.  It also recorded Cross-Origin frame errors.  Compounding the issue is the fact that we were dealing with two clients.  One was the browser mentioned above.  The other was a .NET application.  The .NET application was unable to POST content via the Edge proxy.  Browsers were able to navigate the instance but received the 504 and CORS errors at seemingly random intervals.  Below is a sample of what was seen by the customer's browser.

jquery2\_includes.jsx?v=10-\*\*-2016\_1358:17 Uncaught DOMException: Blocked a frame with origin "https://edge.mydomain.com" from accessing a cross-origin frame.

…

js\_includes\_ngCommon.jsx?v=10-\*\*-2016\_1358&lp=Tue\_Dec\_06\_16\_00\_22\_PST\_2016&c=13\_283:11625 snPresence response time 750ms

js\_includes\_amb.jsx?v=10-\*\*-2016\_1358&lp=Tue\_Dec\_06\_16\_00\_22\_PST\_2016&c=13\_283:6POST https://edge.mydomain.com/amb/connect 504 (Gateway Timeout)

At first glance these would seem to be networking issues.  This is because browsers block content originating from a different domain when initiated by scripts.  It is an important security measure and part of the larger HTTP access control known as [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS).  The HTTP response code 504 is specific to proxies.  It is defined by [W3.org](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) as: "The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server specified by the URI (e.g. HTTP, FTP, LDAP) or some other auxiliary server (e.g. DNS) it needed to access in attempting to complete the request."  Taken together these seemed to point to a network issue since the customer's network environment is complex.  In this case, these errors were deceiving.

There was further confusion due to what was recorded in the proxy's wrapper.log.

INFO   | jvm 1    | 2017/01/\*\* 13:04:47.501 | CloudEdgeProxy-175dfe4a-43, WRITE: TLSv1.2 Handshake, length = 40

INFO   | jvm 1    | 2017/01/\*\* 13:04:47.501 | CloudEdgeProxy-175dfe4a-38, WRITE: TLSv1.2 Application Data, length = 2888

INFO   | jvm 1    | 2017/01/\*\* 13:04:47.501 | HttpClient@1970620526-scheduler, called closeOutbound()

INFO   | jvm 1    | 2017/01/\*\* 13:04:47.501 | HttpClient@1970620526-scheduler, closeOutboundInternal()

INFO   | jvm 1    | 2017/01/\*\* 13:04:47.501 | HttpClient@1970620526-scheduler, SEND TLSv1.2 ALERT:  warning, description = close\_notify

The above pointed us to an issue with the client as it connected to the proxy.  An important clue was found in the browser log.  The HTTP 504 error indicated that the verb in use was POST.  When a .NET application carries out a POST it will default to set the Expect header to "100-Continue".  This is fine in most cases.  However, because the underlying Jetty servlet did not handle Expect headers properly, the Edge Proxy could not process the POST request.  The workaround was to prevent the .NET application from setting the Expect header altogether.  After this, the application was able to POST without issue.  The Jetty issue has since been resolved and this behavior is no longer an issue.

We still had the CORS issue, however.  Client browsers still saw HTTP 504 from time to time.  The CORS issue had not disappeared and it would not be practical to configure customer browsers to not send an Expect header when communicating with ServiceNow.  During in depth discussions we considered the possibility that sessions were being timed out.  Again this was a clue we found in the browser logs.

js\_includes\_ngCommon.jsx?v=10-\*\*-2016\_1358&lp=Tue\_Dec\_06\_16\_00\_22\_PST\_2016&c=13\_283:11625 snPresence response time 750ms

js\_includes\_amb.jsx?v=10-\*\*-2016\_1358&lp=Tue\_Dec\_06\_16\_00\_22\_PST\_2016&c=13\_283:6POST https://edge.mydomain.com/amb/connect 504 (Gateway Timeout)

The above revealed that a "presence" check with the instance was unable to complete.  The timeout for this process is 30 seconds.  However, the session timeout for the Edge proxy was set out of box to the same 30 seconds.  We had a timeout collision and there was no way to prevent it.

Some quick thinking and great work by our Edge Development Team produced a property which allows editing the session timeout.  Property edgeencryption.proxy.idle.timeout available in Helsinki Patch 4 Hot Fix 4.  Once this was applied and the timeout value set to a non-multiple of 30, the customer's browser did not record any more CORS or HTTP 504 errors.

**In closing**

The Edge Encryption Proxy is a powerful tool to secure your data.  It is important to understand the networking environment it will reside in.  As a security tool, it does not perform traditional proxy duties like caching or content filtering.  Instead it is an SSL forward proxy.  This means it cannot simply be a drop in replacement for some other proxy type.  Please take time to consider the factors discussed above to ensure the smoothest possible deployment of your Edge Encryption Proxy.
