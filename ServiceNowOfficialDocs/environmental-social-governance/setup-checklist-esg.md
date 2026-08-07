---
title: Setup checklist for the Operational Sustainability Management \(formerly ESG Management\) application
description: This checklist includes the set up tasks that you're required to complete in your ServiceNow AI Platform instance. When you have completed these tasks, the base system is ready for operation.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/environmental-social-governance/setup-checklist-esg.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Operational Sustainability Management \(formerly ESG Management\) implementation, Configure, Operational Sustainability Management \(formerly Environmental, Social, and Governance\)]
tags:
  - environmental-social-governance
  - esg
  - sustainability
  - reporting
  - carbon
  - type-task
---

# Setup checklist for the Operational Sustainability Management \(formerly ESG Management\) application

This checklist includes the set up tasks that you're required to complete in your ServiceNow AI Platform® instance. When you have completed these tasks, the base system is ready for operation.

## Before you begin

Role required: none

Consider creating and printing a PDF of this checklist topic. You can then check off tasks as you complete them. To generate a PDF, click the **Save As PDF** \[Omitted image "save-as-pdf.png"\] Alt text: Save as PDF iconicon and at the top of the topic and click **Selected topic**.

<table id="table_rzz_z21_xmb"><thead><tr><th>

Item

</th><th>

Checklist

</th></tr></thead><tbody><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

A user with the sn\_esg.program\_manager role, can download and install the Operational Sustainability Management application. For details, see [[install-esg|Install Operational Sustainability Management \(formerly ESG Management\)]].

</td></tr><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

A user with the sn\_esg.program\_manager role performs the following tasks:-   [[create-material-topics|Creates material topics]]
-   [[create-esg-goal|Creates goals]]
-   [[create-esg-target|Creates targets]]
-   [[create-an-emission-activity|Creates an emission activity]]
-   [[create-an-emission-factor|Creates an emission factor]]

</td></tr><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

A user with the sn\_esg.program\_manager role also manages entities and performs the following tasks:-   [[create-entity|Creates an entity]]
-   [[create-entity-type|Creates an entity type]]
-   [[create-entity-class|Creates an entity class]]

</td></tr><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

A user with the sn\_esg.metrics\_manager role defines the various [[types-of-metric-definitions|types of metric definitions]] and metrics. This user performs the following tasks:-   [[update-automated-metric-definition|Creates an automated metric definition]]
-   [[create-manual-metric-definition|Creates a manual metric]]
-   [[create-composite-metric-definition|Creates a composite metric definition]]
-   [[create-a-metric|Create a metric]]

</td></tr><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

A user with the sn\_esg.data\_owner role can provide data for the manual metrics data tasks and a user with the sn\_esg.program\_manager can override the data that is provided. For more information, see [[provide-data-for-metric-data-task|Provide data for a metric data task]]

</td></tr><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

A user with the sn\_esg.reporting\_disclosure\_manager, sn\_esg.program\_manager roles can create disclosure. Disclosures enable the investors to make informed decisions about the companies, their risk posture, sustainability standards, and Operational Sustainability Management compliance.

</td></tr><tr><td>

\[Omitted image "checkbox.png"\] Alt text: checkbox

</td><td>

Optionally, users of the [Install Operational Sustainability Management \(formerly ESG Management\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/environmental-social-governance/install-esg.md) application can integrate with other applications such as Project Portfolio Management and Integrated Risk Management. These integrations provide more features and capabilities. For more information, see [[integrate-esg|Integrating Operational Sustainability Management \(formerly ESG\) with other applications]]

</td></tr></tbody>
</table>**Parent Topic:**[[esg-implementation|Operational Sustainability Management \(formerly ESG Management\) implementation]]

## Related

- [[install-esg|Install Operational Sustainability Management \(formerly ESG Management\)]]
- [[create-material-topics|Create a material topic]]
- [[create-esg-goal|Create an Operational Sustainability Management \(formerly ESG Management\) goal]]
- [[create-esg-target|Create an Operational Sustainability Management \(formerly ESG Management\) target]]
- [[create-an-emission-activity|Create a new emission activity]]
- [[create-an-emission-factor|Create an emission factor]]
- [[create-entity|Create an entity]]
- [[create-entity-type|Create an entity type]]
- [[create-entity-class|Create an entity class]]
- [[update-automated-metric-definition|Update a metric definition]]
- [[create-manual-metric-definition|Create a manual metric definition]]
- [[create-composite-metric-definition|Create a calculated metric definition]]
- [[create-a-metric|Create a metric]]
- [[provide-data-for-metric-data-task|Provide data for a metric data task]]
- [[integrate-esg|Integrating Operational Sustainability Management \(formerly ESG\) with other applications]]
- [[esg-implementation|Operational Sustainability Management \(formerly ESG Management\) implementation]]
- [[types-of-metric-definitions|Types of metric definitions]]
