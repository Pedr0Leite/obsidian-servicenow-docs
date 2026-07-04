---
title: "Determining if the properties from the source were copied over a target"
aliases:
  - KB0538768
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538768
kb_number: KB0538768
last_modified: 2025-10-21
---

## Issue

Troubleshooting: Determining if the properties from the source are copied over a target

This issue is related to properties that are not preserved during system cloning.

## Resolution

To solve the issue:

1.  Make sure that this happens _after_ the clone.
2.  Log in to the system using an administrator account.
3.  Go to **SAML properties** page. 
4.  Open a new browser tab. For a single SAML SSO, enter **https://host:port/system\_properties\_ui.do?sysparm\_category=SAML%202%20Single%20Sign-on,SAML2%20idp,SAML2%20sp,SAML2%20advanced,SAML2%20eSignature**.
5.  For a multiple provider SSO, enter **http://host:port/sso\_properties\_list.do?sysparm\_userpref\_module=b77f2b131b121100227e5581be071381" then find the right SAML SSO configuration**.  
    
6.  Check if the SAML properties (**IdP Authnrequest** URL or **Audience** URL) have been changed. Check if they are the same as the source instance's properties value by comparing the source instance and the target instance.  
    
7.  Restore the target instance's properties value and certificate. Check with the IdP administrator to determine the correct values for the **IdP Authnrequest** URL, **IdP provider** URL, **SinglelogoutRequest** URL, and the **SAML signing certificate**.  
    
8.  Once the properties and certificate are corrected, ask users to try to log in again.
