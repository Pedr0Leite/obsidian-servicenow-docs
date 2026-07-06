---
title: "Some users are unable to login via Multi-Provider SSO 'Logout successful and could not validate SAML response'"
aliases:
  - KB0793472
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793472
kb_number: KB0793472
last_modified: 2026-04-29
---

## Some users are unable to login via Multi-Provider SSO 'Logout successful and could not validate SAML response'

  

### Issue

Some users are unable to login via Multi-Provider SSO 'Logout successful and could not validate SAML response'  
Error: SAML2: Failed to validate signature profile. 

### Cause

SAML Response from the IdP ( Identity Provider) contains attribute with new line (\\n).  
Example below shows Address Attribute in new line(\\n)

<saml2:AttributeStatement>  
<saml2:Attribute Name="streetAddress">  
<saml2:AttributeValue><AttributeValue>9999 S. IH9999  
3rd Floor NW-XXX</AttributeValue>  
</saml2:AttributeValue>  
</saml2:Attribute>  
</saml2:AttributeStatement>

### Resolution

Remove the attribute mapping which contains new line (\\n) in the IdP (Identity Provider). Once removed the SAML Response no longer contains the attribute with new line (\\n).

OR

Make sure the attribute value is in a single line. 

### Related Links

Address is the only field in ADFS, that allows Multi line text to be defined. (Active Directory Federation Services (**ADFS**) is a Single Sign-On (SSO) solution)
