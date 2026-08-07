---
title: "InCommon Federation Registration for integration with the Shibboleth Identity Provider (IdP)"
aliases:
  - KB0596131
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596131
kb_number: KB0596131
last_modified: 2024-04-07
---

## Issue

InCommon requires domains to be registered in order to complete the integration of the Shibboleth Identity Provider (IdP). When trying to register the ServiceNow instance domain, an error occurs because you do not own the “service-now.com” domain. The information below provides a way for you to complete the registration process. 

  

## Resolution

Steps to register a ServiceNow instance using InCommon and Shibboleth: 

1.  Generate the metadata and register with InCommon. In the metadata, specify the entityID as your domain (for example: company.com). The issue is the Service Provider’s domain (service-now.com) is trying to be registered. InCommon blocks this request because the service-now.com domain is not registered to your company. However, if you put your own domain in the entityID and then generate the metadata, InCommon approves the request.  
      
    The domain registered with InCommon is added to the Identity Provider record in the **Entity ID / Issuer** field.  
      
    The InCommon Domain Registration URL is [https://www.incommon.org/certificates/domainreg.html](https://www.incommon.org/certificates/domainreg.html "https://www.incommon.org/certificates/domainreg.html").

2.  Create the Canonical Name record (CNAME) on the DNS.  
    This is a type of resource record in the Domain Name System (DNS) used to specify that a domain name is an alias for another domain (the "canonical" domain). All information (subdomains, IP addresses, etc.) are defined by the canonical domain.  
      
    
3.  Use CNAME in local company DNS (servicenow.company.com) for registration of metadata with InCommon.  
    Use a CNAME in company DNS name space for the configuration of the ServiceNow Service Provider. This ensures that accurate metadata will contain values that you can easily register in the InCommon metadata with no need for any exceptions.
