---
title: "Verify all AWS certificates needed to establish a connection from the MID server to the AWS cloud server"
aliases:
  - KB0787467
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787467
kb_number: KB0787467
last_modified: 2024-04-08
---

## Verify all AWS certificates needed to establish a connection from the MID server to the AWS cloud server

  

### Issue

MID server cannot connect to AWS cloud server for Discovery or other functionality. Will see this error in logs:

**Unable to execute HTTP request: sun.security.validator.ValidatorException: PKIX path building failed: java.security.cert.CertPathBuilderException: No issuer certificate for certificate in certification path found**

### Release

Any

### Cause

All certificates needed for connection to the AWS gateway server being used have not been imported.

### Resolution

We need to see the fingerprint SHA1 certificates the MID server needs to use AWS. Follow these steps and see the fingerprints needed:  
  
1) Go to the host machine for the MID server connecting to the AWS gateway  
2) Open a browser (chrome is preferred)  
3) Go to the URL being used for connection e.g: [https://apigateway.us-east-1.amazonaws.com/](https://apigateway.us-east-1.amazonaws.com/?WSDL)  
4) Once the page loads, click the padlock at the top left next to the URL  
5) Click the certificate section  
6) Once the certificate window opens, go to the certification path tab  
7) On each of the certificates listed click the view certificate button  
8) Click the details tab on this window  
9) Scroll down to view the thumbprint and copy and paste this into a text, along with which certificate it corresponds to

These thumbprints show you which certificates are needed to establish the connection
