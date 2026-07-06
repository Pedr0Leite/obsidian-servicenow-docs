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
