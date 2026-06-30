---
title: Generate a SHA-1 thumbprint
description: Generate a SHA-1 thumbprint using the JWT provider's sys\_id and JKS certificate's sys\_id and certificate's alias to be added to the GraphCertificateOAuthTemplate script.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/generate-thumbprint.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [OAuth profile to use certificates, Read email using Microsoft Graph, Read or send emails using Microsoft Graph, Advanced email setup, Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Generate a SHA-1 thumbprint

[[generate-sha-1-thumbprint|Generate a SHA-1 thumbprint]] using the JWT provider's sys\_id and JKS certificate's sys\_id and certificate's alias to be added to the GraphCertificateOAuthTemplate script.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Scripts-Background**.

2.  Paste the following script to generate the SHA-1 thumbprint value.

    ```
    var certId = "<sys_id of the certificate record>";​
    
    var certAlias = "<alias name for the certificate>";​
    
    var gce = new GlideCertificateEncryption();​
    
    var thumbprint = gce.getThumbPrintFromKeyStore(certId, certAlias,"SHA-1");​
    
    gs.log(thumbprint);​
    ```

3.  Select **Run script**.


## What to do next

[[oauth-api-script|Create an OAuth API script]]

**Parent Topic:**[[configure-oauth-profile-using-certificates|Configure an OAuth profile to use certificates for authentication with Microsoft Azure]]

## Related

- [[oauth-api-script|Create an OAuth API script]]
- [[configure-oauth-profile-using-certificates|Configure an OAuth profile to use certificates for authentication with Microsoft Azure]]
- [[generate-sha-1-thumbprint|Generate a SHA-1 thumbprint]]
