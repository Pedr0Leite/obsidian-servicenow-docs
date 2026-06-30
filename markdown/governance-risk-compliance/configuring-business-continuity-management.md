---
title: Configuring Business Continuity Management
description: Configure the Business Continuity Management application to perform the business continuity tasks for your organization.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/configuring-business-continuity-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Business Continuity Management, Governance, Risk, and Compliance]
---

# Configuring Business Continuity Management

Configure the [[business-continuity-mangmt-overview|Business Continuity Management]] application to perform the business continuity tasks for your organization.

## Configuration overview

Configuring Business Continuity Management involves installing the application from ServiceNow® Store and setting it up by the administrators.

**Note:** If you have the BCM role, you can perform the setup tasks that are described in this section.

-   Install the Business Continuity Management application from store. For more information, see [[install-business-continuity-management|Install Business Continuity Management from ServiceNow Store]].

    **Note:** Installing GRC: [[bia-uib|Business Impact Analysis]], GRC: [[bcp-uib|Business Continuity Planning]], or GRC: Crisis Management automatically installs GRC: Business Continuity Management – Core and GRC: Business Continuity Management – Components.

-   Verify that you have assigned users with the required roles. For detailed instructions and a list of roles, see [[installed-with-bcm|Components installed with Business Continuity Management]].
-   Set up the Business Continuity Management application by performing the administrative tasks with the BCM administrator role. For more information, see [[set-up-bcm-bcmadmin-tasks|General administration setup for BCM]].

    **Note:** You can view **[[my-tasks-page-config-module|My tasks page configurations]]** and **Properties** in the **General [[Administration|Administration]]** setup.

-   Complete the setup for a business impact analysis by performing the administrative tasks with the BIA administrator role. For more information, see [[bcm-admin-tasks|Setup for a business impact analysis]].

    **Note:** When you [[create-bia-in-uib-ws|create a business impact analysis]] in BCM UIB Workspace, you can assign a BCM lead to the analysis in the BIA form itself.

-   Complete the setup for a business continuity plan by performing the administrative tasks with the BCP administrator role. For more information, see [[bcp-admin-tasks|Setup for a business continuity plan]].

    **Note:** When you [[create-bcp-plan-in-uib-ws|create a business continuity plan]] in BCM UIB Workspace, you can assign a BCM lead to the plan in the BCP form itself.

-   Format the PDF templates for a business impact analysis, a business continuity plan, or an event. For more information, see [[update-pdf-format-for-bia-bcp-event|Format PDF templates for BIAs, BCPs, and Events]].
-   Configure the 360° relationship registries and views. For more information, see [[configure-relationship-registries-views|Configure 360° relationship registries and views]].
-   Set up the notifications with Everbridge. For more information, see [[setup-steps-for-emergency-notification-uib-ws|Setup for Everbridge notifications]].
-   Set up the Crisis map. For more information, see [[crisis-map-admin-tasks|Setup for Crisis map]].
-   Review the setup tasks that are performed by an administrator. For more information, see [[set-up-bcm-sys-admin-tasks|Setup by system administrators]].
-   Review the setup information for UI Builder. For more information, see [[configuring-bcm-workspace-by-using-ui-builder|Setup for the UI Builder]].

**Note:**

Both BCM classic Workspace and [[bcm-workspace|BCM Configurable Workspace]] use the Workspace view. If you have made any customizations in other UI views, you must apply the same customizations before or after upgrading from a prior release to the Australia release.

For information on the custom components configuration in BCM classic Workspace, see the [KB1442692](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1442692) article.

For information on how to migrate reports and custom changes to BCM Configurable Workspace, see the [KB1444397](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1444397) article.

## Related

- [[install-business-continuity-management|Install Business Continuity Management from ServiceNow Store]]
- [[installed-with-bcm|Components installed with Business Continuity Management]]
- [[set-up-bcm-bcmadmin-tasks|General administration setup for BCM]]
- [[bcm-admin-tasks|Setup for a business impact analysis]]
- [[bcp-admin-tasks|Setup for a business continuity plan]]
- [[update-pdf-format-for-bia-bcp-event|Format PDF templates for BIAs, BCPs, and Events]]
- [[configure-relationship-registries-views|Configure 360° relationship registries and views]]
- [[setup-steps-for-emergency-notification-uib-ws|Setup for Everbridge notifications]]
- [[crisis-map-admin-tasks|Setup for Crisis map]]
- [[set-up-bcm-sys-admin-tasks|Setup by system administrators]]
- [[configuring-bcm-workspace-by-using-ui-builder|Setup for the UI Builder]]
- [[business-continuity-mangmt-overview|Business Continuity Management]]
- [[bia-uib|Business impact analysis]]
- [[bcp-uib|Business continuity planning]]
- [[my-tasks-page-config-module|My tasks page configurations]]
- [[Administration|Administration]]
- [[create-bia-in-uib-ws|Create a business impact analysis]]
- [[create-bcp-plan-in-uib-ws|Create a business continuity plan]]
- [[bcm-workspace|BCM Configurable Workspace]]
