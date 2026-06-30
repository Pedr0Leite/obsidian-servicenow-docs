---
title: Configuring client accessible secrets
description: Learn how to configure your instance to use client accessible secrets.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/client-access-secret-landing.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Secrets Management, Platform Security]
---

# Configuring client accessible secrets

Learn how to configure your instance to use client accessible secrets.

Use this example implementation to configure Secrets Management without using proxies, or giving ServiceNow access to your decrypted data.

For more detail on using client-side Secrets Management to manage access to passwords and groups, see [[understand-sec-man|About client-side Secrets Management]].

These instructions assume you have a MID Server configured on your local network. For information on this process see [MID Server](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server-landing.md).

## Process overview

-   **1. [[client-access-example-1|Create encryption keys and certificate]]**

    Create [[encryption-landing|encryption]] keys and a certificate using terminal commands on your local environment.

-   **2. [[client-access-example-2|Add your certificate to the ServiceNow Trusted Key Store]]**

    Upload your key and certificate to the ServiceNow Trusted Key Store.

-   **3. [[client-access-example-3|Create a secret group with criteria]]**

    Create a group for your secrets. Secret groups are used to organize your secrets into groups. Using these groups enables you to apply access [[ca-policies|policies]] to those secrets at a group level. Then associate your secrets group to an [[identity-landing|identity]] group and add your MID Server to that identity group.

-   **4. [[client-access-example-5|Upload the public/private keypair to the MID Server]]**

    Upload your public/private keypair to your MID Server. This keypair enables the MID Server to handle [[c_Authentication|authentication]] requests from your instance.

-   **5. [[client-access-example-4|Create credentials and test credential encryption]]**

    Create a credential to authenticate into a third-party system and test that ServiceNow can't access the credential.

-   **6. [[client-access-example-6|Configure Flow Designer to manage the integration]]**

    On your instance, use Workflow Studio to manage an integration between your local network and your instance.

-   **7. [[client-access-example-7|Test the end-to-end client-side encrypted secrets integration]]**

    Test your integration, and review the execution details to confirm your [[sc-configuration|configuration]] is working.


-   **[Create encryption keys and certificate](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-1.md)**  
Create encryption keys and a certificate using terminal commands on your local environment.
-   **[Add your certificate to the ServiceNow Trusted Key Store](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-2.md)**  
Upload your key and certificate to the ServiceNow Trusted Key Store.
-   **[Create a secret group with criteria](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-3.md)**  
Secret groups organize secrets and apply access policies at the group level. Associate a secret group with an identity group to control MID Server access.
-   **[Upload the public/private keypair to the MID Server](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-5.md)**  
Upload your public/private keypair to your MID Server. This keypair enables the MID Server to handle authentication requests from your instance.
-   **[Create credentials and test credential encryption](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-4.md)**  
Create a credential to authenticate into a third-party system.
-   **[Configure Flow Designer to manage the integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-6.md)**  
On your instance, use Workflow Studio to manage an integration between your local network and your instance.
-   **[Test the end-to-end client-side encrypted secrets integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/client-access-example-7.md)**  
Test your integration, and review the execution details to confirm your configuration is working.
-   **[[client-access-example-8|Test a Windows Management Instrumentation credential encrypted with Secrets Management]]**  
Verify that your Windows Management Instrumentation \(WMI\) credential is encrypted with Secrets Management and use an Integration Hub workflow to complete end-to-end testing.
-   **[[cloning-and-secrets-mgmt|Cloning and Secrets Management]]**  
Learn how to reconfigure secrets groups and client secrets groups after a clone.

**Parent Topic:**[[secrets-management|Secrets Management]]

## Related

- [[understand-sec-man|About client-side Secrets Management]]
- [[client-access-example-1|Create encryption keys and certificate]]
- [[client-access-example-2|Add your certificate to the ServiceNow Trusted Key Store]]
- [[client-access-example-3|Create a secret group with criteria]]
- [[client-access-example-5|Upload the public/private keypair to the MID Server]]
- [[client-access-example-4|Create credentials and test credential encryption]]
- [[client-access-example-6|Configure Flow Designer to manage the integration]]
- [[client-access-example-7|Test the end-to-end client-side encrypted secrets integration]]
- [[client-access-example-8|Test a Windows Management Instrumentation credential encrypted with Secrets Management]]
- [[cloning-and-secrets-mgmt|Cloning and Secrets Management]]
- [[secrets-management|Secrets Management]]
- [[encryption-landing|Encryption]]
- [[ca-policies|Policies]]
- [[identity-landing|Identity]]
- [[c_Authentication|Authentication]]
- [[sc-configuration|Configuration]]
