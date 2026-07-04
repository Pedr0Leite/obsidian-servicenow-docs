---
title: "Does Edge Proxy Support SAN Certificates for the SSL Certificate (Multi-Domain (SAN) Certificates - Using Subject Alternative Names )?"
aliases:
  - KB0623890
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623890
kb_number: KB0623890
last_modified: 2026-01-13
---

## Does Edge Proxy Support SAN Certificates for the SSL Certificate (Multi-Domain (SAN) Certificates - Using Subject Alternative Names )?

  

### Issue

Does Edge Proxy Support SAN Certificates for the SSL Certificate? |  (Multi-Domain (SAN) Certificates - Using Subject Alternative Names )

  
  

# Use Case:

* * *

This concerns the SSL cert that resides on the Edge Proxy, inside the Java Keystore. The example use case is a configuration of four proxies (ServerA, ServerB, ServerC, ServerD) connected to one instance. This SSL cert is issued by an Enterprise CA, is not self-signed. SAN certificates use Subject Alternate Names and could potentially contain all four server names, the four Edge Proxies, in a single certificate, and is lower-cost to maintain long-term: [https://www.digicert.com/subject-alternative-name.htm](https://www.digicert.com/subject-alternative-name.htm) 

Generate a single SAN certificate that has CN=ServerA, SAN names: ServerB, ServerC, ServerD. Is this supported by Edge Encryption?

# Answer:

* * *

Edge Proxy is using standard Java SSL libraries and API, which do support this feature, including Java keytool.   If the certificate was generated with alternative names, with corresponding CSR,, it can be imported into proxy keystore, and should work.
