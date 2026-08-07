---
title: "Page not found when logging in through side_door.do"
aliases:
  - KB0715664
tags:
  - servicenow
  - support-kb
  - side_door
  - authentication
  - external-authentication
  - login
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715664
kb_number: KB0715664
last_modified: 2024-01-28
---

## Page not found when logging in through side\_door.do

  

### Issue

# Symptoms

* * *

When logging in from 'https://<instance\_name>.service-now.com/side\_door.do', The page you are looking for could not be found is appearing.

# Release

* * *

All

# Cause

* * *

A logged in user cannot access the side\_door.do page. If a user attempts to access the page while logged in, it will produce 'page not found' error

# Resolution

* * *

When a user doesn't log out of the instance and just close the browser. Logout from the instance properly to access the side\_door.do page.

# Additional Information

* * *

Here is the doc about it: [side\_door.do page not found](https://docs.servicenow.com/csh?topicname=t_EnablingExternalAuthentication.html&version=latest "side_door.do page not found")

## Related

- [[KB0745590 - session_timeout page is displayed when navigating to instance URL using side_door]]
- [[KB0746067 - Disable local login on the instance by disabling login.do page]]
- [[t_EnablingExternalAuthentication]] - official docs on enabling external authentication / side_door.do

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728437 - User unable to login to Servicenow after administrator has updated user's password in ServiceNow instance|User unable to login to Servicenow after administrator has updated user's password in ServiceNow instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0744254 - After user's password has been updated on user record, user is unable to login to instance|After user's password has been updated on user record, user is unable to login to instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
