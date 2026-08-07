---
title: "SAM Activity Job fails with InvalidPathException when iterating on data stream"
aliases:
  - KB1647999
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1647999
kb_number: KB1647999
last_modified: 2025-12-30
---

## SAM Activity Job fails with InvalidPathException when iterating on data stream

  

### Issue

The SAM Activity Job fails with the following error: "Failed to iterate on data stream: com.glide.transform.transformer.exceptions.InvalidPathException: Could not find path in stream: $.results"

The system logs show a related Flow Designer error for the Confluence Cloud Update User Activity operation:

"Flow Designer: Operation failed with error: com.snc.process\_flow.exception.OpException: Call block 'Confluence Cloud Update User Activity...' failed. Detail: Failed to iterate on data stream: com.glide.transform.transformer.exceptions.InvalidPathException: Could not find path in stream: $.results"

### Release

All supported releases

### Cause

The OAuth token for the Confluence Cloud integration is no longer valid because the configured credentials failed to authenticate.

### Resolution

1.  Validate the credentials configured for the Confluence Cloud integration in SAM.
2.  If the password has changed, update the credentials in the instance.
3.  Generate a new OAuth token.
4.  Run the SAM Activity Job again to verify the issue is resolved.
