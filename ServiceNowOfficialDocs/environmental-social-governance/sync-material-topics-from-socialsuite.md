---
title: Sync material topics from Socialsuite
description: Sync material topics from Socialsuite to import materiality assessment results into the Operational Sustainability Management application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/environmental-social-governance/sync-material-topics-from-socialsuite.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Integrating Operational Sustainability Management with Socialsuite, Integrating Operational Sustainability Management \(formerly ESG\) with other applications, Operational Sustainability Management \(formerly Environmental, Social, and Governance\)]
tags:
  - environmental-social-governance
  - esg
  - sustainability
  - reporting
  - carbon
  - type-task
---

# Sync material topics from Socialsuite

Sync material topics from Socialsuite to import materiality assessment results into the Operational Sustainability Management application.

## Before you begin

Role required: sn\_esg.program\_manager

## About this task

When you sync material topics, the system imports assessment data from Socialsuite for the selected reporting period. Each reporting period may contain different topics based on organizational priorities and external landscape.

## Procedure

1.  Navigate to **All** &gt; **Operational Sustainability Workspace**.

2.  Select **List**.

3.  Under **Program setup**, select **Material topics**.

4.  Select **Sync Topics**.

    The **Sync Topics** button is available in the list view only when the Operational Sustainability Integration with Socialsuite plugin is installed and the Material topic selection system property is set to Socialsuite.

5.  In the Sync from SocialSuite dialog box, select a reporting period from the **Reporting period** field.

6.  Select **Import**.


## Result

Material topics from the selected reporting period are imported from Socialsuite. The imported topics display **Socialsuite** in the Material topic source column and appear in workflow states based on their status in Socialsuite. For more information about how Socialsuite states map to your ServiceNow instance states, see [[material-topic-workflow-and-states|Material topic workflow and states]].

**Parent Topic:**[[integrate-operational-sustainability-with-SocialSuite|Integrating Operational Sustainability Management with Socialsuite]]

**Related topics**  


[[socialsuite-material-topic-fields|Socialsuite material topic fields]]

[[socialsuite-import-log|Socialsuite import log]]

## Related

- [[material-topic-workflow-and-states|Material topic workflow and states]]
- [[integrate-operational-sustainability-with-SocialSuite|Integrating Operational Sustainability Management with Socialsuite]]
- [[socialsuite-material-topic-fields|Socialsuite material topic fields]]
- [[socialsuite-import-log|Socialsuite import log]]
