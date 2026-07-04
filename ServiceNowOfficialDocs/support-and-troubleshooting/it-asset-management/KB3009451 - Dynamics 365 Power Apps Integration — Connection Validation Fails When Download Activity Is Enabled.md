---
title: "Dynamics 365 / Power Apps Integration — Connection Validation Fails When \"Download Activity\" Is Enabled"
aliases:
  - KB3009451
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3009451
kb_number: KB3009451
last_modified: 2026-05-10
---

## Dynamics 365 / Power Apps Integration — Connection Validation Fails When "Download Activity" Is Enabled

  

### Issue

SAM (Software Asset Management) subscription profile for Dynamics 365 and Power Apps, clicking \*\*Validate Connection\*\* fails with the error:

  

\`\`\`

Connection validation is not successful. Invalid credentials

\`\`\`

  

or

  

\`\`\`

The connection record is not associated with the Connection and credential field. Create the connection to proceed further.

\`\`\`

### Symptoms

\- When the \*\*Download Activity\*\* checkbox is \*\*unchecked\*\* on the same integration profile, the connection validates successfully.

\- The OAuth token is present and valid; an expired token does not cause the issue.

\- Outbound HTTP logs show authentication errors (e.g., \`InvalidAuthenticationToken\` or \`Authorization\_RequestDenied\`) to the Microsoft Graph API endpoint.

### Release

ALL

### Cause

The \*\*Download Activity\*\* flow in the Dynamics 365 / Power Apps integration profile uses a \*\*separate Connection and Credential configuration\*\* from the main subscription sync flow.

When \*\*Download Activity\*\* is enabled, the platform expects a dedicated \*\*HTTP Connection\*\* record to be configured for that flow.

If no HTTP connection has been configured specifically for the Download Activity flow, the OAuth token request for that flow fails — causing the entire \*\*Validate Connection\*\* check to return an error.

  

This is distinct from the main profile credentials, which may be correctly configured. The two flows authenticate independently.

### Resolution

**\*\*Option A — Disable Download Activity (if not required):\*\***

  

1\. Navigate to the affected Subscription Profile record.

2\. Uncheck the \*\*Download Activity\*\* checkbox.

3\. Save and re-run \*\*Validate Connection\*\* — it should succeed.

  

**\*\*Option B — Configure the HTTP Connection for Download Activity:\*\***

  

1\. Navigate to the Subscription Profile for Dynamics 365 / Power Apps.

2\. Locate the \*\*Download Activity\*\* section and find its associated \*\*Connection and Credential\*\* field.

3\. Create or associate a valid HTTP Connection record for the Download Activity flow.

4\. Ensure the OAuth token for this connection is obtained by clicking \*\*Get OAuth Token\*\* (requires Global Administrator permissions in Microsoft Admin Centre).

5\. Save and re-run \*\*Validate Connection\*\*.

  

**\*\*Note:\*\*** 

If further errors remain after Step 4 (such as \`InvalidAuthenticationToken\` or \`Authorization\_RequestDenied\`), verify that the Azure App Registration has the correct \*\*Application Permissions\*\* (not Delegated) assigned in Azure AD, and that \*\*Admin Consent\*\* has been granted. Required permissions typically include: \`Directory.Read.All\`, \`Organisation.Read.All\`, \`Reports.Read.All\`.

  

**\*\*Reference:\*\*** 

For Microsoft 365 integration guidance, see:

https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrating-with-microsoft365.html

  

\---

  

**\### Workaround**

  

Uncheck \*\*Download Activity\*\* on the integration profile to allow the main connection to validate while the Download Activity HTTP connection is being configured.

  

\---
