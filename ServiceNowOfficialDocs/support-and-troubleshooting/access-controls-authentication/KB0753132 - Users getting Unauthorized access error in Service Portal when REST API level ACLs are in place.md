---
title: "Users getting \"Unauthorized access\" error in Service Portal when REST API level ACLs are in place "
aliases:
  - KB0753132
tags:
  - servicenow
  - support-kb
  - rest-api
  - acl
  - roles
  - service-portal
  - table-api
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753132
kb_number: KB0753132
last_modified: 2025-01-21
---

## Issue

Users getting "Unauthorized access" error in Service Portal when REST API level ACLs are in place

## Resolution

Add "snc\_platform\_rest\_api\_access" role for the user

## Additional Information

[Rest API Documentation](https://docs.servicenow.com/csh?topicname=c_RESTAPI.html&version=latest "https://docs.servicenow.com/csh?topicname=c_RESTAPI.html&version=latest")

[REST API Roles](https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html#d977123e694)

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — general ACL evaluation background for REST-level ACLs
- [[KB0693899 - On Service Portal the record producer form  does not display all subcategories option  for users with no role]] — another Service Portal ACL/role restriction issue
- [[c_RESTAPI]] — official REST API concept and role reference doc
