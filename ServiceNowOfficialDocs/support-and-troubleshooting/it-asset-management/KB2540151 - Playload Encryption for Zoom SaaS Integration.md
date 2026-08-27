---
title: "Playload Encryption for Zoom SaaS Integration"
aliases:
  - KB2540151
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2540151
kb_number: KB2540151
last_modified: 2025-10-22
---

## Playload Encryption for Zoom SaaS Integration

  

Will Zoom SaaS Integration uses OAuth2 with Payload Encryption — specifically whether will it uses bearer tokens with public/private key encryption?  
  
  
The Zoom SaaS Integration in ServiceNow uses OAuth 2.0 with bearer tokens for authentication. All traffic is secured via TLS 1.2, which provides end-to-end encryption of payloads in transit. The integration does not use public/private key encryption for bearer tokens; instead, it relies on TLS for security.
