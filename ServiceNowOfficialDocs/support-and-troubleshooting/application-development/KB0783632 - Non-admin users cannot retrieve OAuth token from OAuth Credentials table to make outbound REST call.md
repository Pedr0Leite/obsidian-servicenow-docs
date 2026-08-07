---
title: "Non-admin users cannot retrieve OAuth token from OAuth Credentials table to make outbound REST call"
aliases:
  - KB0783632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783632
kb_number: KB0783632
last_modified: 2026-03-27
---

## Non-admin users cannot retrieve OAuth token from OAuth Credentials table to make outbound REST call

  

### Issue

Non-admin users cannot retrieve OAuth token from OAuth Credentials table to make outbound REST call.

### Release

All releases

### Cause

This is because of ACLs on OAuth Credentials table which mandate that the user should have been the one who initially created the token or should be an admin user to read the token.

### Resolution

To fix the issue you will need to create 2 new ACLs and make sure non-admin users pass these ACLs. 

1.  Table level"read" ACL on oauth\_credential
2.  Field level "read" ACL on "oauth\_credential.token\_received"
