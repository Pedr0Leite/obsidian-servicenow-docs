---
title: "Error: \"No issuer certificate for certificate in certification path found.\"  when we to try to discover datacenters for an AWS account"
aliases:
  - KB0716556
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716556
kb_number: KB0716556
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

1) When we perform discovery datacenters on an AWS , we get the below error :

com.amazonaws.AmazonClientException: Unable to execute HTTP request: sun.security.validator.ValidatorException: PKIX path building failed: java.security.cert.CertPathBuilderException: No issuer certificate for certificate in certification path found. 

# Cause

* * *

If the mid server has proxy settings, it might be the case that proxy settings are blocking the handshake between our MID Server Host and the AWS. The proxy server might be intercepting the certificate from AWS.

# Resolution

* * *

1) Add the AWS server certificate and the proxy certificate using the mid server key tool.

2) You can add certificates following the below guide :   
[https://docs.servicenow.com/csh?topicname=add-ssl-certificates.html&version=latest](https://docs.servicenow.com/csh?topicname=add-ssl-certificates.html&version=latest) 

3) Once this is done , you can rerun the datacenter discovery.
