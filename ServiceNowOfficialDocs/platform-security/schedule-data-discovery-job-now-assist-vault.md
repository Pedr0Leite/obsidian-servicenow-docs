---
title: Schedule a Data Discovery job with Now Assist for Vault
description: Use the schedule data discovery job skill to schedule one-time or recurring Data Discovery jobs with Now Assist. Data Discovery jobs can detect sensitive data such as PII or PHI provided as input to the Now LLM.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/schedule-data-discovery-job-now-assist-vault.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use generative AI skills, ServiceNow Vault]
---

# Schedule a Data Discovery job with Now Assist for Vault

Use the schedule [[data-discovery-landing|data discovery]] job skill to schedule one-time or recurring [[data-discovery-jobs|Data Discovery jobs]] with Now Assist. Data Discovery jobs can detect sensitive data such as PII or PHI provided as input to the Now LLM.

## Before you begin

-   [[install-vault|Install ServiceNow Vault]]. For more information, see [[configuring-servicenow-vault|Configuring ServiceNow Vault]].
-   Ensure that the schedule Data Discovery job skill is active. For more information, see [Activate a Now Assist skill](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/configure-a-now-assist-skill.md).

Role required: sn\_vault\_console.vault\_console\_admin

## Procedure

1.  Navigate to **All** &gt; **Vault** &gt; **Vault console**.

2.  In the Ask Now Assist panel, select **Schedule data discovery job** and specify the job details.

    Example prompt: `[[configure-data-discovery-jobs|Configure a data discovery job]] that scans the tables Task and Knowledge, looking for data patterns like Credit Card-Visa and Phone Number in columns such as Description and Text. Schedule a sample scan to occur on August 15th, 2025, with a time window from 10:00 AM to 5:00 PM. Name the job "Credit Card & Phone Number Scan" and describe it as "Scans for credit card and phone number data in Task and Knowledge tables."`

## Related

- [[configuring-servicenow-vault|Configuring ServiceNow Vault]]
- [[data-discovery-landing|Data Discovery]]
- [[data-discovery-jobs|Data Discovery jobs]]
- [[install-vault|Install ServiceNow Vault]]
- [[configure-data-discovery-jobs|Configure a Data Discovery job]]
