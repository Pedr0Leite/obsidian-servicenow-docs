---
title: "OAuth Token Generation Fails for Adobe Cloud Integration Profile — Invalid Null Response"
aliases:
  - KB2829960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2829960
kb_number: KB2829960
last_modified: 2026-03-10
---

## OAuth Token Generation Fails for Adobe Cloud Integration Profile — Invalid Null Response

  

### Issue

The Adobe Cloud direct integration profile for Software Asset Management (SAM) fails to generate an OAuth token. Clicking "Get OAuth Token" on the integration profile returns the error:

_OAuth flow failed. Verify the configurations and try again. Error detail: Invalid null response._

### Release

Not release specific

### Cause

The Connection URL configured in the Adobe Cloud integration profile is incorrect or does not match the actual URL from the Adobe Developer Console, resulting in a null response during the OAuth handshake.

### Resolution

Log in to the Adobe Developer Console.

Navigate to the project credentials used for the ServiceNow integration.

In the Generate access token section, select View cURL command.

Copy the correct Connection URL from the cURL command.

In ServiceNow, create a new Adobe Cloud integration profile — simply updating the Connection URL on the existing profile will not resolve the issue.

While creating the new profile, paste the correct Connection URL obtained from step 4.

Click Get OAuth Token to confirm the OAuth flow completes successfully.

Note: Editing the Connection URL on an existing integration profile does not fix the issue. The profile must be recreated with the correct Connection URL.
