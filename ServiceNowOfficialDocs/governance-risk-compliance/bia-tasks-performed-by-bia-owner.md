---
title: Structured workflows for BIAs
description: Perform the tasks that are outlined in this section to create a business impact analysis in Business Continuity Workspace \(also known as BCM Configurable Workspace\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/bia-tasks-performed-by-bia-owner.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Manage, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Structured workflows for BIAs

Perform the tasks that are outlined in this section to create a business impact analysis in Business Continuity Workspace \(also known as [[bcm-workspace|BCM Configurable Workspace]]\).

Business impact analysis \(BIA\) owner performs these tasks:

-   Create a business impact analysis. For more information, see [[create-bia-in-uib-ws|Create a business impact analysis]].
-   Assess the impact categories and submit the analysis for a review and approval. For more information, see [[assess-impact-categories-bia-in-uib-ws|Assess impact categories and dependencies]].
-   As the BCM lead, approve the BIA. For more information, see [[approve-bia-in-uib-ws|Approve the business impact analysis]].
-   Generate and save the PDF of the analysis for reference.

## BIA updates

Beginning with the Xanadu and later releases, the reliability of business impact analysis is enhanced through the implementation of following updates.

-   Access the latest BIAs of the dependent items and their recovery objectives such as Recovery Time Objectives \(RTOs\), Recovery Point Objectives \(RPOs\), and Recovery Tiers.
-   Configure the columns in the dependency assessment of a BIA.
-   Schedule automated updates for the dependencies from the CMDB.
-   Configure the updates to be done after a manual review.

**Note:** If an approval record is created for a BIA, the **Approve** or **Reject** button is not displayed on the BIA form. For a user to view the **Approve** or **Reject** button, these conditions must be fulfilled:

-   The user should have the sn\_bia.bia\_manager role.
-   The BIA should be in the **Pending approval** state.
-   The BIA should not have any approval records created.

## Additional information on Business Impact Analysis

-   For more information on the **Business impact analysis** tab in the Home page, see [[home-page-uib-ws|Home page view]].
-   For more information on business impact analysis, see [[bia-uib|Business impact analysis]].
-   For more information on the administrative tasks in business impact analysis, see [[bcm-admin-tasks|Setup for a business impact analysis]].

-   **[[bia-impact-categories|Impact categories and ratings]]**  
Impact categories are the types of an impact that you can assess during a business impact analysis. The BCM administrator of an organization is responsible for defining the impact categories and the timeframe during which an organization may experience a downtime. This information is used to determine the recovery time objective and recovery point objective of the assets.
-   **[[rto-rpo-recovery-tiers|RTO, RPO, and recovery tiers]]**  
Due to unforeseen disruptive events, the business processes in your organization can face a downtime. It is important to classify your business processes in the recovery tiers and calculate the amount of time and amount of data loss that your organization can handle without significant effect on the operations.
-   **[[rto-rpo-calculation|Calculating RTO and RPO]]**  
The BCM application provides an assessment questionnaire for calculating the recovery time objective \(RTO\) and recovery point objective \(RPO\) in the business impact analysis \(BIA\). As a pre-requisite to the BIA, BCM administrator defines the impact ratings and sets up the assessment questions. After receiving the responses to the assessment, the BCM application calculates the RTO and RPO.
-   **[[states-ui-actions-bia|BIA states and UI actions]]**  
When you create a business impact analysis \(BIA\), certain UI actions are associated with each state.
-   **[[bcm-enhanced-bia-logic|Configuring dictionary, UI policy, and element variables]]**  
Starting with Release 6.1.x, administrators have the capability to configure different aspects of a dependency. This includes the Dictionary, UI policy, element variables, and UI view. These configurations play a crucial role in determining specific columns, required fields, and overall display in the [[list-view-uib-ws|list view]] and form view of a dependency within the dependency assessment of a BIA.
-   **[[using-smart-asmt-template|Using latest assessment template for conducting BIAs]]**  
Beginning with the Yokohama release, you can use the latest assessment template for conducting a Business Impact Analysis \(BIA\). The BIA template is now integrated with the [[smart-asmnt-engine-landing-page|Smart Assessment Engine]], enabling you to use the Smart Assessment along with the legacy assessment.
-   **[Create a business impact analysis](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/create-bia-in-uib-ws.md)**  
Create a business impact analysis in BCM UI Builder Workspace to get the necessary information for a plan.
-   **[[update-impactanalysis-dep-based-on-cmdb-changes|Scheduling an auto-update of dependencies]]**  
You can schedule an auto-update of the dependencies in the business impact analysis based on the source data and relationships in the CMDB. You can receive an email notification with details of the BIA dependency updates from the BCM application.
-   **[Assess impact categories and dependencies](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/assess-impact-categories-bia-in-uib-ws.md)**  
Assess the impact categories and dependencies in BCM UIB Workspace to get the necessary information for a plan. Use the business impact analysis to identify the recovery time objective for an item and prioritize the assets that have the least and most critical dependencies. Use the information to establish their recovery strategies during the planning phase.
-   **[Approve the business impact analysis](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/approve-bia-in-uib-ws.md)**  
Approve the business impact analysis in BCM UI Builder Workspace in the BCM application. If you’re the business impact analysis owner or the BCM lead for the business impact analysis, you can approve the business impact analysis.
-   **[[update-dependency-details-of-BIA-in-self-service-as-contributor|Update dependencies of BIAs in Self-Service]]**  
Use the contributor role to update the impact category result, RPO Impact analysis responses, state of the impact dependency group, and the work notes in the **Activity** section in the BCM application.
-   **[[visualize-360-degree-view-for-bia|Visualize 360° relationships for BIAs]]**  
Visualize the 360° relationships for a business impact analysis and its associated entities in BCM UIB Workspace. You can access the 360° view at any time while creating a business impact analysis.
-   **[[generate-pdf-for-bia|Generate BIA reports in PDF or Microsoft Word formats]]**  
Generate a PDF or Microsoft Word copy of a business impact analysis in the BCM Configurable Workspace and save it for a future reference.

**Parent Topic:**[[manage-bcm-with-uib-workspace|Managing BCM workflow tasks]]

## Related

- [[create-bia-in-uib-ws|Create a business impact analysis]]
- [[assess-impact-categories-bia-in-uib-ws|Assess impact categories and dependencies]]
- [[approve-bia-in-uib-ws|Approve the business impact analysis]]
- [[home-page-uib-ws|Home page view]]
- [[bia-uib|Business impact analysis]]
- [[bcm-admin-tasks|Setup for a business impact analysis]]
- [[bia-impact-categories|Impact categories and ratings]]
- [[rto-rpo-recovery-tiers|RTO, RPO, and recovery tiers]]
- [[rto-rpo-calculation|Calculating RTO and RPO]]
- [[states-ui-actions-bia|BIA states and UI actions]]
- [[bcm-enhanced-bia-logic|Configuring dictionary, UI policy, and element variables]]
- [[using-smart-asmt-template|Using latest assessment template for conducting BIAs]]
- [[update-impactanalysis-dep-based-on-cmdb-changes|Scheduling an auto-update of dependencies]]
- [[update-dependency-details-of-BIA-in-self-service-as-contributor|Update dependencies of BIAs in Self-Service]]
- [[visualize-360-degree-view-for-bia|Visualize 360° relationships for BIAs]]
- [[generate-pdf-for-bia|Generate BIA reports in PDF or Microsoft Word formats]]
- [[manage-bcm-with-uib-workspace|Managing BCM workflow tasks]]
- [[bcm-workspace|BCM Configurable Workspace]]
- [[list-view-uib-ws|List view]]
- [[smart-asmnt-engine-landing-page|Smart Assessment Engine]]
