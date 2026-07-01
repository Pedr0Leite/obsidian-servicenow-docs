---
title: Install Vault plugins
description: Learn how to review and install the necessary plugins for ServiceNow Vault.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/install-vault-plugins.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring ServiceNow Vault, ServiceNow Vault]
tags:
  - platform-security
  - type-task
---

# Install Vault plugins

Learn how to review and install the necessary plugins for [[servicenow-vault-landing|ServiceNow Vault]].

## Before you begin

Role required: Elevate to sn\_vault\_console.vault\_console\_admin role.

ServiceNow Vault is best used with other ServiceNow security products. Make the most of your tools and [[ca-metrics|metrics]] by installing and configuring the plugins listed in step 3.

## Procedure

1.  Navigate to **All** &gt; **Vault** &gt; **Vault Console**.

2.  Review the status of your tools.

    |Status|Description|
    |------|-----------|
    |\[Omitted image "vault-tool-status-1.png"\] Alt text: Limited access|Tool has a limited access license. Reported metrics may be affected or unavailable.|
    |\[Omitted image "vault-tool-status-2.png"\] Alt text: Included with platform|Tool is included by default with the platform|
    |\[Omitted image "vault-tool-status-3.png"\] Alt text: Needs license|Tool has no license. Reported metrics may be affected or unavailable.|
    |\[Omitted image "vault-tool-status-4.png"\] Alt text: Premium license|Tool has full access.|

3.  If a status is either limited or needs a license, review its respective installation page.

<table id="table_bf1_qhb_1gc"><thead><tr><th>

Tool

</th><th>

Installation page

</th></tr></thead><tbody><tr><td>

[Data Discovery](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-discovery/data-discovery-landing.md)

</td><td>

[Activating Data Discovery](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-discovery/activate-data-discovery.md)

</td></tr><tr><td>

[Data Classification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-classification/data-classification.md)

</td><td>

Included with the platform.

</td></tr><tr><td>

[Data anonymization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-privacy-classic/dps-data-anonymization.md)

</td><td>

[Activate data privacy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-privacy-classic/dps-activate-data-privacy.md)**Note:** [[dps-data-anonymization|Data anonymization]] is installed as part of [Data privacy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-privacy-classic/dps-data-privacy.md).

</td></tr><tr><td>

[Cloud Encryption with Key Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/cloud-encryption/dare-overview.md)

</td><td>

[Requesting Cloud [[encryption-landing|Encryption]] for instances with Now Support Service Catalog \[KB1117369\]](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1117369) article in the Now Support Knowledge Base

</td></tr><tr><td>

[[field-encryption|Field Encryption]]

</td><td>

[[activate-platform-encryption|Activate Field Encryption]]

</td></tr><tr><td>

-   [[session-access|Zero Trust Access \(ZTA\)]]
-   [[ca-homepage|Continuous Authentication \(CA\)]]


</td><td>

-   [[activate-session-access|Activating Zero Trust Access]]
-   [[activate-continuous-authentication|Activating Continuous Authentication]]


</td></tr></tbody>
</table>

## Related

- [[field-encryption|Field Encryption]]
- [[activate-platform-encryption|Activate Field Encryption]]
- [[session-access|Zero Trust Access \(ZTA\)]]
- [[ca-homepage|Continuous Authentication \(CA\)]]
- [[activate-session-access|Activating Zero Trust Access]]
- [[activate-continuous-authentication|Activating Continuous Authentication]]
- [[servicenow-vault-landing|ServiceNow Vault]]
- [[ca-metrics|Metrics]]
- [[dps-data-anonymization|Data anonymization]]
- [[encryption-landing|Encryption]]
