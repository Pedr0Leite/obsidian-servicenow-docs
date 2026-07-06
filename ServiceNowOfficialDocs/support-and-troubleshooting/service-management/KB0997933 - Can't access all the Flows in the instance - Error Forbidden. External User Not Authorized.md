---
title: "Can't access all the Flows in the instance - Error \"Forbidden. External User Not Authorized\"
aliases:
  - KB0997933
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997933
kb_number: KB0997933
last_modified: 2025-01-15
---

## Can't access all the Flows in the instance - Error "Forbidden. External User Not Authorized"

  

### Issue

We are not able to access flows from Flow Designer page. It will either just spin on the loading screen or provide the error "Forbidden. External User Not Authorized"

### Release

All Versions

### Cause

Since the "Explicit Roles" plugin is enabled and we have snc\_internal role on the instance, The "snc\_internal" role has to be provided to the users in order for them to view the flows

Console Error  
  
Uncaught (in promise)  
DSError {name: 'DesignerError', code: 403, message: 'Forbidden. External User Not Authorized', data: {…}, response: {…}}  
code: 403  
data: {error: {…}, status: 'failure', session: {…}}  
message: "Forbidden. External User Not Authorized"  
name: "DesignerError"  
response: {data: {…}, status: 403, statusText: 'Forbidden', headers: {…}, config: {…}, …}  
\[\[Prototype\]\]: Error  
  

### Resolution

Provide the users with role "snc\_internal" role to resolve this issue.
