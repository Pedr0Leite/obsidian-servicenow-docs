---
title: "How to integrate Multi-Provider SSO plugin with CASB ( SkyHighNetworks ) for SSO?"
aliases:
  - KB0693308
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693308
kb_number: KB0693308
last_modified: 2025-01-03
---

## How to integrate Multi-Provider SSO plugin with CASB ( SkyHighNetworks ) for SSO?

  

### Issue

  
  

# Description

* * *

CASB is a product sits between user and cloud application.When user access instance with CASB application url, user request will go through CASB and then the request will be redirected to ServiceNow. If user is not authenticated, ServiceNow will issue a SAML request to the configured IDP and then the  SAML response will be returned to the CASB.CASB will then forward the SAML response to ServiceNow for authentication.

This guide explains the steps involved to configure SAML with ServiceNow,IDP & CASB Product.

# Procedure

* * *

SSO Setup involves 3 steps.

1.Configure forward rules in the CASB for instance url.Engage your CASB vendor to complete setup.Note down CASB url for ServiceNow Instance.

ex:If your instance url is https://empabc.service-now.com, then CASB url to access instance would be https://casbabc.net

2.Configure SAML configuration for ServiceNow instance in the IDP.Engage your IDP vendor to complete setup.Your are expected to use CASB url for assertion consumer service and entity ID.

3.Configure SAML configuration in the ServiceNow for IDP.Details about configuring SAML setup is available in the doc site.You are expected to use CASB url for instance homepage, Audience and Entity ID.

   a)Goto [https://docs.servicenow.com/](https://docs.servicenow.com/)

   b)Search "Set up Multi-Provider SSO".

<table style="border-collapse: collapse; width: 403pt;" border="0" width="537" cellspacing="0" cellpadding="0"><colgroup><col style="width: 213pt;" width="284"><col style="width: 190pt;" width="253"></colgroup><tbody><tr style="height: 16.0pt;"><td style="height: 16pt; width: 213pt; font-weight: bold; border: 0.5pt solid windowtext; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 12pt; font-style: normal; text-decoration: none; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;" width="284" height="21">SAML Property</td><td style="border-left: none; width: 190pt; font-weight: bold; border-top: 0.5pt solid windowtext; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 12pt; font-style: normal; text-decoration: none; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;" width="253">Value</td></tr><tr style="height: 16.0pt;"><td style="height: 16pt; border-top: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-left: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 12pt; font-weight: 400; font-style: normal; text-decoration: none; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;" height="21">Assertion Consumer Service URL</td><td style="border-top: none; border-left: none; color: #0563c1; text-decoration: underline; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 12pt; font-weight: 400; font-style: normal; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;"><span style="text-decoration: underline;"><a href="https://casb-provider.com/navpage.do" rel="nofollow">https://&lt;casb_url&gt;/navpage.do</a></span></td></tr><tr style="height: 16.0pt;"><td style="height: 16pt; border-top: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-left: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 12pt; font-weight: 400; font-style: normal; text-decoration: none; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;" height="21">Audience</td><td style="border-top: none; border-left: none; color: #0563c1; text-decoration: underline; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 12pt; font-weight: 400; font-style: normal; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;"><a style="font-family: Calibri, sans-serif; font-size: 16px; white-space: nowrap;" href="https://casb-provider.com/navpage.do" rel="nofollow">https://&lt;casb_url&gt;</a></td></tr><tr style="height: 16.0pt;"><td style="height: 16pt; border-top: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-left: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 12pt; font-weight: 400; font-style: normal; text-decoration: none; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;" height="21">Entity ID / Issuer</td><td style="border-top: none; border-left: none; border-right: 0.5pt solid windowtext; border-bottom: 0.5pt solid windowtext; border-image: initial; padding-top: 1px; padding-right: 1px; padding-left: 1px; color: black; font-size: 12pt; font-weight: 400; font-style: normal; text-decoration: none; font-family: Calibri, sans-serif; vertical-align: bottom; white-space: nowrap;"><a style="font-family: Calibri, sans-serif; font-size: 16px; white-space: nowrap;" href="https://casb-provider.com/navpage.do" rel="nofollow">https://&lt;casb_url&gt;</a></td></tr></tbody></table>

# Applicable Versions

* * *

Jakarta and Higher release.This Integration was tested in the Jakarta Release.

# Additional Information

* * *

1)CASB Integration with ServiceNow

[https://www.skyhighnetworks.com/product/servicenow-security/](https://www.skyhighnetworks.com/product/servicenow-security/)
