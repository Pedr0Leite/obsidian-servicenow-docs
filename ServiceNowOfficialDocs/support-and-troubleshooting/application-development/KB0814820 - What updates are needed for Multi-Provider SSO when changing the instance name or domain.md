---
title: "What updates are needed for Multi-Provider SSO when changing the instance name or domain"
aliases:
  - KB0814820
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814820
kb_number: KB0814820
last_modified: 2024-04-08
---

## What updates are needed for Multi-Provider SSO when changing the instance name or domain

  

### Issue

When an instance is moved into servicenowservices.com from service-now.com or when a custom URL is implemented for the first time, the Service Provider information for Single-Sign-On has to be updated accordingly.

### Cause

The Identity Provider record in Multi-Provider SSO defines not only the IDP information, but also the Service Provider (ServiceNow) information. If this information changes due to an instance move to a different domain (not datacenter) or implementation of a custom url, the updates have to be performed on both sides - ServiceNow and the IDP, or users will be unable to log in via SSO.

### Resolution

In the Identity Provider record, the items to change are:

ServiceNow Homepage  
Entity ID / Issuer  
Audience URI

and if e-Signature is used, also the URL containing consumer.do

The change will be to replace any occurrence of service-now.com with servicenowservices.com, or the old instance URL with the new custom URL.

After the record is saved, Test Connection if prompted.

The IDP record does not have to be deactivated for the domain name change.

In case something goes wrong, you can do these steps:

With debugging turned on, if you go within the same browser tab that failed your login and go to "Node Log File Browser" in your module list and search for message=SAML (case sensitive) for the timeframe of the failed login, you will find the exact error message and can address the root cause.
