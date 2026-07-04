---
title: "Direct Integration Connectivity Requirements: Public IP and Certificate Validation"
aliases:
  - KB2692403
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2692403
kb_number: KB2692403
last_modified: 2025-12-23
---

## Issue

A customer is unable to establish a direct integration from their ServiceNow instance to an on-premises endpoint configured with a private IP address.

## Resolution

To resolve this issue, the customer must update the integration configuration as follows:

1.  Expose the integration endpoint publicly  
    \-- Configure the endpoint to resolve to a public IP address or publicly accessible DNS name.  
    \-- Ensure the endpoint is reachable from the ServiceNow instance over the internet.  
      
    
2.  Update the SSL certificate configuration

\-- The certificate Common Name (CN) and/or Subject Alternative Name (SAN) must match the publicly accessible hostname.

\-- The certificate must be issued by a trusted Certificate Authority and be valid for external access.  
  

1.  Revalidate the integration

\-- Once the endpoint and certificate are updated, retest the integration to confirm successful connectivity.
