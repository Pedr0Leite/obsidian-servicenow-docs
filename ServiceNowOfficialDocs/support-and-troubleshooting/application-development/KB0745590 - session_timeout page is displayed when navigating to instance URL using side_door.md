---
title: "session_timeout page is displayed when navigating to instance URL using side_door"
aliases:
  - KB0745590
  - session_timeout page is displayed when navigating to instance URL using side_door
tags:
  - servicenow
  - support-kb
  - sso
  - saml
  - login
  - session-timeout
  - side-door
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745590
kb_number: KB0745590
last_modified: 2025-11-06
---

## session\_timeout page is displayed when navigating to instance URL using side\_door

  

### Issue

Upon navigating to INSTANCE.service-now.com/side\_door redirects to INSTANCE.service-now.com/session\_timeout and 'You are not logged in, or your session has expired. Redirecting to the login page' message is displayed and user cannot log into the instance. 

### Release

ALL

### Cause

glide.authenticate.sso.redirect.idp system property is set in sys\_properties table with value being sys\_id of the identity provider record. However, there is no identity provider record configured on the instance resulting in redirection to session\_timeout page when navigating to INSTANCE.service-now.com/side\_door.do

### Resolution

1\. Navigate to sys\_properties.LIST from filter navigator

2\. Look for name contains glide.authenticate.sso.redirect.idp

3\. Wipe off the value for this system property 

Once this is done INSTANCE.service-now.com/side\_door.do displays ServiceNow homepage and user can login to the instance.

## Related

- [[KB0715664 - Page not found when logging in through side_door.do]]
- [[KB0746067 - Disable local login on the instance by disabling login.do page]]
- [[KB0746907 - Page stuck on "Establishing Session" after login]]
- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]]
