---
title: "Resolving issues when downloading a WSDL from an external web service to ServiceNow"
aliases:
  - KB0546191
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546191
kb_number: KB0546191
last_modified: 2024-04-30
---

## Resolving issues when downloading a WSDL from an external web service to ServiceNow

  

### Issue

Resolving issues when downloading a WSDL from an external web service to ServiceNow 

Problem

* * *

The ServiceNow instance may encounter issues when attempting to download a WSDL from a web service provider.  

Symptoms

* * *

When clicking the **Generate sample SOAP messages** button in your ServiceNow instance you are unable to download the WSDL.  

Cause

* * *

The behavior may be caused by one of these issues:

-   An UnknownHost exception occurs.
-   The ServiceNow instance is prevented from reaching the web service provider by a firewall.
-   The web service provider requires mutual authentication.
-   The web service provider requires authentication other than BasicAuth.  
      
      
    

Resolution - UnknownHost exception

* * *

This error occurs when the WSDL URL is invalid or unreachable, or if any imports or includes defined in the WSDL are unreachable. Open the WSDL using a different SOAP client, such as SOAP-UI or a web browser to confirm the URL is accessible.  
  

Resolution - Firewall

* * *

This error occurs when some imports defined in the WSDL are hosted behind a firewall that the ServiceNow instance cannot reach. If possible, configure the firewall to allow traffic from the ServiceNow instance IP address. If this is not possible, manually copy the WSDL and import it to the ServiceNow instance.

Resolution - Mutual authentication

* * *

This error occurs when the web service provider requires mutual (two-way) authentication to download the WSDL. Refer to the [Mutual Authentication product documentation](https://docs.servicenow.com/csh?topicname=c_MutualAuthentication.html&version=latest "Mutual Authentication product documentation") for instructions on setting up mutual authentication. 

Resolution - Authentication other than BasicAuth

* * *

ServiceNow supports only BasicAuth. If the web service provider requires a different authentication system, manually copy the WSDL from the web service provider and import it to the ServiceNow instance.
