---
title: "User unable to get an OAuth 2.0 access token"
aliases:
  - KB0783404
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783404
kb_number: KB0783404
last_modified: 2024-04-08
---

## User unable to get an OAuth 2.0 access token

  

### Issue

After creating an application registry record, a user is not able to get the OAuth 2.0 access token.

When attempting to get the access token, this error may be returned:

No\_Oauth\_Token: server\_error access\_denied

### Release

All releases.

### Cause

The user may have the snc\_read\_only role and therefore isn't able to write to the oauth\_credential table during token creation.

### Resolution

You can keep the snc\_read\_only role for the user but allow an exception where they can write to the oauth\_credential table.

Please verify this on a subprod instance first:  
1\. Create a new system property.  
Name: glide.security.snc\_read\_only\_role.tables.exempt\_create  
Type: string  
Value: sys\_user\_session, sysevent, syslog, syslog\_transaction, sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth, oauth\_credential

You're retaining the default (back-end) value as documented here: [Read-only role](https://docs.servicenow.com/csh?topicname=c_ReadOnlyRole.html&version=latest "Read-only role")  
and adding only the necessary oauth\_credential table.

2\. Click Submit.

Verify that this user is able to get an OAuth 2.0 access token through a third-party tool such as Postman.
