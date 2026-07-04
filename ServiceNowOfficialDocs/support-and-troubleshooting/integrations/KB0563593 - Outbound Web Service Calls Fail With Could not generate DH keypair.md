---
title: "Outbound Web Service Calls Fail With \"Could not generate DH keypair\""
aliases:
  - KB0563593
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563593
kb_number: KB0563593
last_modified: 2024-04-07
---

## Outbound Web Service Calls Fail With "Could not generate DH keypair"

  

### Issue

Web Services are becoming more secure. When TLS 1.1 or 1.2 is required by the web service that is being called, an exception is thrown if ServiceNow is using the default SSLv3 or TLS 1.0. When creating or testing an Outbound SOAP or REST Message, a message indicating that the WSDL is unable to load. 

### Symptoms

Symptoms include:

-   Outbound web service calls fail:
    
    javax.net.ssl.SSLException: java.lang.RuntimeException: Could not generate DH keypair
    
-   Searching for the Java version in the page **/xmlstats.do** will show lines like the following, depending on the instance version:  
    
    <system.java.version type="info">1.6.0\_xx</system.java.version>  
    <system.java.version type="info">1.8.0\_152-snc2</system.java.version>
    

### Cause

The loaded Java version (i.e. 1.6 or 1.8) does not allow for TLS 1.1 or 1.2.

For example, on the latest Jakarta patch the expected Java version should be:

<system.java.version type="info">1.8.0\_161-snc1</system.java.version>

### Resolution

ServiceNow Customer Support can upgrade the Java version of your instance. [Open a case](http://www.servicenow.com/support/contact-support.html "Open an incident") with Technical Support. Include the exact error message you received and your Java version (obtained from xmlstats.do). 

After the case has been received and reviewed, a Change record is created and can be processed at the time of your choice.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Alert" src="/Warning_25x.pngx" alt="Alert icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Warning</strong>: The instance is not taken down to implement the change, however, each node in the instance requires a restart. Any users currently logged into the node must re-authenticate, so it is best to schedule the change during a low use time period.</td></tr></tbody></table>
