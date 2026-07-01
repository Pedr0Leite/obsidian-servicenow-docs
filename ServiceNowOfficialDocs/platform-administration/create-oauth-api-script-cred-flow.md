---
title: Create an OAuth API script
description: Create and duplicate an OAuth API script for application registry.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/create-oauth-api-script-cred-flow.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [SMTP OAuth2 to use certificates, Send email using client credential flow, Advanced email setup, Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Create an OAuth API script

Create and duplicate an OAuth API script for application registry.

## Before you begin

Generate an SHA-1 thumbprint. For more information, see [[generate-thumbprint|Generate a SHA-1 thumbprint]].

Generate a sys\_id when you configure a JWT provider. For more information, see [[config-jwt-credential-flow|Configure a JWT provider]].

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Script Includes**.

2.  Select and open **EmailCertificateOAuthTemplate**.

3.  Duplicate the script by changing the name in the **Name** field, select **Insert and Stay** from the record menu.

    **Note:** The name must begin with **OAuth** to create an OAuth script.

    The script is copied and created with a different name.

4.  In the copied script, enter the JWT provider sys\_id and SHA-1 thumbprint.

5.  Select **Update**.


## What to do next

[[register-oauth-cred-flow|Register an OAuth provider]].

**Parent Topic:**[[config-credential-flow-certificate|Configure client credential flow for SMTP OAuth2 using certificate-based authentication]]

## Related

- [[generate-thumbprint|Generate a SHA-1 thumbprint]]
- [[config-jwt-credential-flow|Configure a JWT provider]]
- [[register-oauth-cred-flow|Register an OAuth provider]]
- [[config-credential-flow-certificate|Configure client credential flow for SMTP OAuth2 using certificate-based authentication]]
