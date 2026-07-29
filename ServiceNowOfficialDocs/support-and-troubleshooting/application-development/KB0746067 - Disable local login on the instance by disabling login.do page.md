---
title: "Disable local login on the instance by disabling login.do page"
aliases:
  - KB0746067
  - Disable local login on the instance by disabling login.do page
tags:
  - servicenow
  - support-kb
  - sso
  - saml
  - login
  - login-do
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746067
kb_number: KB0746067
last_modified: 2025-11-05
---

## Issue

Disable local login on the instance by ensuring INSTANCE.service-now.com/login.do redirects to Single Sign On.

## Resolution

Please follow below steps to disable local login:

1.  Navigate to sys\_properties.list from filter navigator and look for the property glide.authentication.external.disable\_local\_login and set the value to true.  
2.  Ensure system property glide.authenticate.external is set to false in sys\_properties table.
3.  Navigate to sys\_public.list from filter navigator and look for page 'login' and ensure 'active' field is set to 'false'.
4.  This would redirect INSTANCE.service-now.com/login.do to Single Sign on.

## Related

- [[KB0745590 - session_timeout page is displayed when navigating to instance URL using side_door]]
- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]]
- [[KB0691974 - How to customize login.do page]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745590 - session_timeout page is displayed when navigating to instance URL using side_door|session_timeout page is displayed when navigating to instance URL using side_door]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538770 - Determining if the SAML issue is the result of a user being locked out| Determining if the SAML issue is the result of a user being locked out]]
