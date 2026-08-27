---
title: "New AD users cannot login to Servicenow instance with SSO: ERROR *** *** Script: User: [Username] not found"
aliases:
  - KB0788105
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788105
kb_number: KB0788105
last_modified: 2024-04-08
---

## New AD users cannot login to Servicenow instance with SSO: ERROR \*\*\* \*\*\* Script: User: \[Username\] not found

  

### Issue

-   Newly provisioned SSO Users fail to logon to Servicenow and they are immediately redirected to the    external\_logout\_complete.do page
-   The following error is observed in the System log "ERROR \*\*\* \*\*\* Script: User: \[Username\] not found"
-   In the node logs the error "SAMLRequestIDGenerator: can’t get request id from session." was observed

### Cause

Once a user is successfully authenticated, the last step in the authentication process is to validate the user is to identify the user in the sys\_user table based on the value in the 'User field' configured in the advanced section of the Identity Provider record. In this occasion it was trying to validate a valid name against an email address. As the email address did not match the name, the user was not found. It is important to validate the name against the 'user\_name' or validate the email against the email address so the values can match

### Resolution

From the logs it was identified that subjectUserName was a user name but the user\_field was 'email' which is not a valid match

To resolve the issue it was necessary to navigate to the advanced section of the Identity provider record and update the 'User Field' column with 'user\_name' instead of 'email'
