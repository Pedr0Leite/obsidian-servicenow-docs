---
title: Setup by system administrators
description: If you are the system administrator, you can set up the Business Continuity Management application by performing certain setup tasks.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/set-up-bcm-sys-admin-tasks.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Setup by system administrators

If you are the system administrator, you can set up the [[business-continuity-mangmt-overview|Business Continuity Management]] application by performing certain setup tasks.

Setting up the common administrative tasks requires configuring the pre-requisite data. These configurations are required to set up the business continuity workspace for different users who would be using the workspace:

-   To update the number of the records for a reference field, see [[configure-referencefield-system-property|Update number of records for reference fields]].
-   To update the number of the element definitions for dependency assessment, see [[update-ele-def-for-dependency-assessment|Update the number of element definitions]].
-   To set up an approval configuration in the Business Continuity Management \(BCM\) application, see [[bcm-approval-configuration|Approval configuration]].
-   To refer to the BCM application menu options, see [[app-menu-views-bcm-viewers|Application menu options for BCM users]].

-   **[Update number of records for reference fields](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/configure-referencefield-system-property.md)**  
Update the number of the records that are displayed for a reference field in the Business Continuity Management \(BCM\) Workspace. You can configure the **referenceFieldLoadLimit** system property to control the number of the records that are displayed for each reference field on the grid configuration pages.
-   **[Update the number of element definitions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/update-ele-def-for-dependency-assessment.md)**  
Update the number of the element definitions that are displayed on the **Dependency Assessment** tab in the Business Continuity Management \(BCM\) Workspace. You can configure the **dependencyAssessmentElementsLimit** system property to control the number of the element definitions that are used for the dependency assessment in a [[bia-uib|business impact analysis]].
-   **[Application menu options for BCM users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/app-menu-views-bcm-viewers.md)**  
The table lists the application menu options that are available for the main users of the business continuity management application to view and navigate.

**Parent Topic:**[[configuring-business-continuity-management|Configuring Business Continuity Management]]

## Related

- [[configure-referencefield-system-property|Update number of records for reference fields]]
- [[update-ele-def-for-dependency-assessment|Update the number of element definitions]]
- [[bcm-approval-configuration|Approval configuration]]
- [[app-menu-views-bcm-viewers|Application menu options for BCM users]]
- [[configuring-business-continuity-management|Configuring Business Continuity Management]]
- [[business-continuity-mangmt-overview|Business Continuity Management]]
- [[bia-uib|Business impact analysis]]
