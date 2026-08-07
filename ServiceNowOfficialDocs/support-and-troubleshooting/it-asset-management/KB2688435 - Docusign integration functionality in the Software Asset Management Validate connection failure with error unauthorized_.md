---
title: "Docusign integration functionality in the Software Asset Management Validate connection failure with error \"unauthorized_client\"
aliases:
  - KB2688435
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688435
kb_number: KB2688435
last_modified: 2025-12-18
---

## Docusign integration functionality in the Software Asset Management Validate connection failure with error "unauthorized\_client"

  

### Issue

\=> Observed below errors on Get OAuth operation failure in the outbound logs  
  
{"error":"invalid\_grant","error\_description":"unauthorized\_client"}  
  
The error message "invalid\_grant" with the description "unauthorized\_client" typically occurs during the OAuth 2.0 authorization process, indicating that there is an issue with the client credentials or permissions.

### Release

N/A

### Resolution

\=> Incorrect values of Verify Client ID , Technical account Id, client secret. These would be the root cause of the issue.
