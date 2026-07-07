---
title: "Unable to get SCOM Event Collector to connect to SCOM server. There is a connection error message as follows  \"The client and server cannot communicate, because they do not possess a common algorithm\"
aliases:
  - KB0694651
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694651
kb_number: KB0694651
last_modified: 2024-04-07
---

## Unable to get SCOM Event Collector to connect to SCOM server. There is a connection error message as follows "The client and server cannot communicate, because they do not possess a common algorithm"

  

### Issue

# Symptoms

* * *

SCOM connector fails with the following error "[System.ComponentModel.Win32Exception](http://System.ComponentModel.Win32Exception): The client and server cannot communicate, because they do not possess a common algorithm"

**Error Message:**

Connection test failed: SCOM Event connector failed. [Microsoft.EnterpriseManagement.Common.UnauthorizedAccessEnterpriseManagementException](http://Microsoft.EnterpriseManagement.Common.UnauthorizedAccessEnterpriseManagementException): The user does not have sufficient permission to perform the operation. ---> System.ServiceModel.Security.SecurityNegotiationException: SOAP security negotiation with 'net.tcp://Ipaddress:port/DispatcherServiceSSL' for target 'net.tcp://ipaddress:port/DispatcherServiceSSL' failed. See inner exception for more details. ---> [System.ComponentModel.Win32Exception](http://System.ComponentModel.Win32Exception): The client and server cannot communicate, because they do not possess a common algorithm

# Release

* * *

All Releases

# Cause

* * *

SCOM client running on the mid server and SCOM manager does not have common TLS algorithm to communicate with each other.

# Resolution

* * *

1.  Navigate to HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\ on both Mid server and Scom server.
2.   In the protocol registry, you will see all TLS cipher suites like TLS 1.0, 1.1 and 1.2. You can enable or disable it for both Client and server. Enabled will have value 1 where as disable will have value 0.
3.  Make sure SCOM server and Scom client have a common cipher suite to communicate.
    
    4.If you would like to specifically communicate on TLS 1.2, you will have to configure the SCOM server.  You can refer the following article.
    
         [https://support.microsoft.com/en-us/help/4055768/tls-1-2-protocol-support-deployment-guide-for-system-center-2012-r2](https://support.microsoft.com/en-us/help/4055768/tls-1-2-protocol-support-deployment-guide-for-system-center-2012-r2%29)
