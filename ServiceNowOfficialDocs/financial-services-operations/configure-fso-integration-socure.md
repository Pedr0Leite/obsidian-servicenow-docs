---
title: Configure Financial Services Operations Integration with Socure
description: Configure the Financial Services Operations Integration with Socure application to verify a customer's identity and improve the customer's risk determination.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/configure-fso-integration-socure.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Socure, Integrate, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - type-task
---

# Configure Financial Services Operations Integration with Socure

Configure the [[integrating-socure-service|Financial Services Operations Integration with Socure]] application to verify a customer's identity and improve the customer's risk determination.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Process Automation** &gt; **Flow Designer**.

2.  In the Search field, search for **Sync Reason Codes Flow**.

3.  To set the conditions and frequency for the flow, select the **Trigger** field.

4.  Locate the flow you want to activate from the list of saved flows and open it.

5.  Click **Activate**.

    **Note:** When you are using the Financial Services Operations Integration with Socure for the first time, you must activate the scheduled flow and set the desired frequency.

6.  Configure the KYC service definitions, Socure - CDD - Customer and Socure - CDD - Contact.

    For information on configuring flows and service definitions, see [[configure-flow-designer-flows-fso-apps|Configure flows]] and [[configure-service-definitions|Configure service definitions for Financial Services Operations applications]].

## Related

- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-service-definitions|Configure service definitions]]
- [[integrating-socure-service|Financial Services Operations integration with Socure]]
