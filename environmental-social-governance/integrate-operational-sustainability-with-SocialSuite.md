---
title: Integrating Operational Sustainability Management with Socialsuite
description: Socialsuite is a platform for conducting materiality assessments. You can import material topics from Socialsuite into your ServiceNow instance and manage them in the Operational Sustainability Management application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/environmental-social-governance/integrate-operational-sustainability-with-SocialSuite.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Integrating Operational Sustainability Management \(formerly ESG\) with other applications, Operational Sustainability Management \(formerly Environmental, Social, and Governance\)]
---

# Integrating Operational Sustainability Management with Socialsuite

Socialsuite is a platform for conducting materiality assessments. You can import material topics from Socialsuite into your ServiceNow instance and manage them in the Operational Sustainability Management application.

The integration supports both double materiality and single materiality assessments. Double materiality assesses both impact and financial materiality. Single materiality assesses either impact or financial materiality. Assessments comply with the Corporate Sustainability Reporting Directive \(CSRD\), European Sustainability Reporting Standards \(ESRS\), Global Reporting Initiative \(GRI\), and International Financial Reporting Standards \(IFRS\).

## Assessment data

The integration imports the following data from Socialsuite:

-   Material topics
-   Impact materiality scores
-   Financial materiality scores

## Integration workflow

1.  Conduct materiality assessments in Socialsuite.
2.  Sync the assessment results to your ServiceNow instance.

    For more information, see [[sync-material-topics-from-socialsuite|Sync material topics from Socialsuite]].

    The imported material topics appear in your ServiceNow instance in workflow states based on their status in Socialsuite. For details about how Socialsuite states map to the ServiceNow instance states, see [[material-topic-workflow-and-states|Material topic workflow and states]].

3.  Associate the material topics with goals and targets.

-   **[[activate-operational-sustainability-integration-with-socialsuite|Activate Operational Sustainability Integration with Socialsuite]]**  
You can activate the Operational Sustainability Integration with Socialsuite plugin \(sn\_osm\_ma\) for Operational Sustainability Management if you have the admin role. The plugin enables you to import materiality assessment results from Socialsuite for reporting and compliance.
-   **[[set-material-topic-selection-system-property|Set Material topic selection system property]]**  
Set the Material topic selection system property to enable the Socialsuite integration features.
-   **[[create-a-socialsuite-connection|Create a Socialsuite connection]]**  
Create a Socialsuite connection to sync material topics and materiality assessment results from Socialsuite into your ServiceNow instance.
-   **[Sync material topics from Socialsuite](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/environmental-social-governance/sync-material-topics-from-socialsuite.md)**  
Sync material topics from Socialsuite to import materiality assessment results into the Operational Sustainability Management application.

**Parent Topic:**[[integrate-esg|Integrating Operational Sustainability Management \(formerly ESG\) with other applications]]

**Related topics**  


[[socialsuite-material-topic-fields|Socialsuite material topic fields]]

[[socialsuite-import-log|Socialsuite import log]]

## Related

- [[sync-material-topics-from-socialsuite|Sync material topics from Socialsuite]]
- [[material-topic-workflow-and-states|Material topic workflow and states]]
- [[activate-operational-sustainability-integration-with-socialsuite|activate operational sustainability integration with socialsuite]]
- [[set-material-topic-selection-system-property|Set Material topic selection system property]]
- [[create-a-socialsuite-connection|Create a Socialsuite connection]]
- [[integrate-esg|Integrating Operational Sustainability Management \(formerly ESG\) with other applications]]
- [[socialsuite-material-topic-fields|Socialsuite material topic fields]]
- [[socialsuite-import-log|Socialsuite import log]]
