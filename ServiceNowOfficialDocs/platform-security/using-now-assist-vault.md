---
title: Use generative AI skills in Now Assist for Vault
description: The Now Assist for Vault application includes the generative AI skills and features that enable you to streamline your administrative workload.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/using-now-assist-vault.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [ServiceNow Vault]
tags:
  - platform-security
  - type-concept
---

# Use generative AI skills in Now Assist for Vault

The [[now-assist-vault-landing|Now Assist for Vault]] application includes the generative AI skills and features that enable you to streamline your administrative workload.

**Note:** Depending on your license, you will have access to certain application features, generative AI skills, agentic workflows, and AI agents. For more information, see [ServiceNow product tiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-native-sku-overview.md).

After you activate skills, they appear in the Ask Now Assist panel in ServiceNow Vault console.

\[Omitted image "vault-dashboard-now-assist.png"\] Alt text: Vault console dashboard with the Ask Now Assist panel highlighted.

By default, all skills exist in the global domain. When you use Now Assist in a domain-separated environment, [[users|users]] are only able to access data in their domain. For example, if a user uses the summarization skill, Now Assist only uses material that exists in the user's domain when generating that summary. Additionally, there is no co-mingling of data for domain-separated instances when using generative AI skills. The data resides only on the instance, and the shared services used for generative AI do not persist any requests \(prompts\) and responses. For more information, see [Domain separation in the Now Assist Admin console](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/domain-separation-in-the-now-assist-admin-console.md). \(Note that global domain is not the same as global scope. For more information, see [Exploring Next Experience pickers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/next-experience-pickers.md).\)

-   **[[generate-custom-data-pattern-now-assist-vault|Generate a custom data pattern by using Now Assist for Vault]]**  
Use the generate custom data pattern skill to create a custom regular expression data pattern from your description and add it as an active data pattern to your instance.
-   **[[check-role-access-now-assist-vault|Check role access for an encrypted column with Now Assist for Vault]]**  
Use the check role access for encrypted column skill to identify user roles that have access to [[encryption-landing|encryption]] and decryption keys in your instance.
-   **[[schedule-data-discovery-job-now-assist-vault|Schedule a Data Discovery job with Now Assist for Vault]]**  
Use the schedule [[data-discovery-landing|data discovery]] job skill to schedule one-time or recurring [[data-discovery-jobs|Data Discovery jobs]] with Now Assist. Data Discovery jobs can detect sensitive data such as PII or PHI provided as input to the Now LLM.

**Parent Topic:**[[servicenow-vault-landing|ServiceNow Vault]]

## Related

- [[generate-custom-data-pattern-now-assist-vault|Generate a custom data pattern by using Now Assist for Vault]]
- [[check-role-access-now-assist-vault|Check role access for an encrypted column with Now Assist for Vault]]
- [[schedule-data-discovery-job-now-assist-vault|Schedule a Data Discovery job with Now Assist for Vault]]
- [[servicenow-vault-landing|ServiceNow Vault]]
- [[now-assist-vault-landing|Now Assist for Vault]]
- [[users|Users]]
- [[encryption-landing|Encryption]]
- [[data-discovery-landing|Data Discovery]]
- [[data-discovery-jobs|Data Discovery jobs]]
