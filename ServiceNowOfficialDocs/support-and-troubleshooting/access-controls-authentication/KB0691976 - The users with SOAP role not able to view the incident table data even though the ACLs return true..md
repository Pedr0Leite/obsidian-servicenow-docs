---
title: "The users with SOAP role not able to view the incident table data even though the ACLs return true."
aliases:
  - KB0691976
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - business-rules
  - soap
  - non-interactive-session
  - incident-management
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691976
kb_number: KB0691976
last_modified: 2024-01-28
---

## The users with SOAP role not able to view the incident table data even though the ACLs return true.

  

### Issue

# Symptoms

* * *

 The Access Control Lists(ACL) return true.But the users with SOAP role are not able to view the records of the incident table and there is no security constraint message.

# Cause

* * *

The business rule - "incident query" checks if the user is interactive under Advanced tab's script. If the user has SOAP roles,  "incident query" Business rule will consider the user as non-interactive session.

# Resolution

* * *

Manually switch a non-interactive user to an interactive user.

Procedure:

1)Navigate to User Administration  --> Users

2)Search for the user you want to update. For ex: System Administrator.

3)Clear the Web Service Access Only check box.

4)Click Update

# Additional Information

* * *

Please refer the following doc for more information about Non-interactive sessions.

[https://docs.servicenow.com/csh?topicname=c\_NonInteractiveSessions.html&version=latest](https://docs.servicenow.com/csh?topicname=c_NonInteractiveSessions.html&version=latest)

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]]
- [[KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)]] - business rules and interactive-session checks
- [[c_BusinessRules]] - official docs on business rules
