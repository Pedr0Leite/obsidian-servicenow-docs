---
title: List view of application rationalization
description: As an Enterprise Architect, you can view the list of all business applications. The List view enables you to see high-level information on all your business applications and all the indicator scores that are attached to them.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-list-view.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Rationalization of business applications, Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# List view of application rationalization

As an Enterprise Architect, you can view the list of all business applications. The List view enables you to see high-level information on all your business applications and all the indicator scores that are attached to them.

\[Omitted image "eaw-list-view.png"\] Alt text: List view in the Application Rationalization page.

## Overview of the list view

The list view of application rationalization enables you to view all available applications based on your scoring profile, in your [[application-portfolio-management-landing-page|enterprise architecture]] landscape. For details, see [[eaw-setup-scroring-prof|Configure scoring profiles]].

You can perform side-by-side comparison of application scores and indicators across multiple dimensions.

You can also create your own application indicators to analyze business applications in the List view. For information on how to create custom application indicators, see [[eaw-create-indicator|Add or edit an application indicator]]. The new custom indicators appear as new columns in the list view.

**Note:**

-   The created indicator must also be attached to the default application profile. For information on how to attach new profile indicators with a scoring profile, see [[eaw-attach-profile-indicators-with-application-scoring-profiles|Attach a profile indicator with an application scoring profile]].
-   If the created indicator isn’t displayed in the list, verify that the indicator is active. For information on how to activate an indicator, see [[eaw-enable-or-disable-an-application-indicator|Activate or turn off an application or capability indicator]].

All the indicator scores are displayed according to the latest fiscal period, by default. You can also select a different fiscal period from the Scores for fiscal period list. Your fiscal period preferences are saved and applied the next time you visit the page.

\[Omitted image "fiscal-period-dropdown.png"\] Alt text: Scores for fiscal period list highlighted on the Application rationalization list view page.

The latest fiscal period is derived from the apm\_app\_indicator\_score list. The duration of a fiscal period is derived from the system property **com.glide.fiscal\_calendar.fiscal\_unit**.

You can select the name of a business application to open it and view its associated details. Also, you can select the expand row icon \(\[Omitted image "ExpandIcon.png"\] Alt text: Expand row icon.\) to see the demands and projects associated with that business application. On selecting a demand or a project, its details are displayed. You can modify business application details and its associated demand and project details, as required.

Business applications marked as **Retired** or in **End of Life** lifecycle stage aren’t displayed on the Application Rationalization List view page. However, you can view those business applications by updating the **sn\_apm\_ws.business\_application\_default\_filter** system property. Contact your ServiceNow® account service manager to update the system property.

You can also generate insights into business applications using Now Assist. For information, see [[generate-insights-into-ba|Generate insights into business applications]].

## View and compare actual and normalized indicator scores

You can view the actual indicator scores for a business application on the list view page and compare them with the normalized scores. Actual scores refer to the raw value of the indicator as captured from its source. These values aren’t scaled and can vary widely across applications, depending on the underlying data.

The normalized score refers to the scaled value of an indicator, derived from the actual score using a normalization formula. This enables all indicator scores to fit into a common range. Normalized scores ensure comparability across different indicators with varying units and ranges.

To view the actual scores of indicators, select the data visibility icon \(\[Omitted image "list-view-display-visibility-icon.png"\] Alt text: Data visibility icon.\) and then enable the **Show actual score data** toggle.

\[Omitted image "list-view-actual-score-toggle.png"\] Alt text: List view page with the data visibility icon and Show actual score data toggle highlighted.

The actual indicator scores and their normalized values for business applications are displayed. For example, the actual column for the Number of Incidents indicator displays the actual number of incidents associated with the business application during the selected fiscal period.

\[Omitted image "list-view-scores-highlighted.png"\] Alt text: List view page with the actual and normalized score columns highlighted for the Number of Incidents indicator.

**Note:** The Portfolio TCO indicator displays currency values in the format specified in the **glide.currency2.default\_reference\_currency** property. If this property isn’t configured, the currency values are displayed in US dollar \(USD\) format by default.

Your display preferences are saved and applied the next time you visit the page.

## Actions available on the list view page

You can perform the following from the list view page:

-   Edit business application details. For more information, see [[eaw-edit-business-application-details|Edit business application details in list view]].
-   Create a demand for a business application. For more information, see [[eaw-create-a-demand-using-the-list-view|Create a demand using the list view]].
-   Set the planned disposition of a business application. For more information, see [[eaw-set-planned-disposition-of-a-business-application-listview|Set the planned disposition of a business application]].
-   Add the business application lifecycle data. For more information, see [[eaw-add-business-application-lifecycle-data-listview|Add business application lifecycle data using the list view]].
-   You can add or hide the displayed columns according to your requirement by selecting the Personalize icon \(\[Omitted image "icon-bubblechart-settings.png"\] Alt text: Personalize icon.\). Your display preferences are saved and applied the next time you visit the page.
-   Export the list view data to Microsoft Excel or CSV. For more information, see [[eaw-export-app-rat-list-data|Export application rationalization data to Excel or CSV]].

**Note:** You can zoom on this page to 200% or 400% through your browser settings without the loss of content or functionality. Page layouts are transformed into a vertical, stacked view automatically.

**Parent Topic:**[[eaw-rationalize-business-applications|Rationalization of business applications]]

**Related topics**  


[[eaw-edit-a-demand-associated-with-a-business-application|Edit a demand associated with a business application]]

[[eaw-edit-a-project-associated-with-a-business-application|Edit a project associated with a business application]]

[Export application rationalization data to Excel or CSV](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-export-app-rat-list-data.md)

[[eaw-apply-filters-app-rat|Apply filters on the Application Rationalization page]]

[Generate insights into business applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/generate-insights-into-ba.md)

## Related

- [[eaw-setup-scroring-prof|Configure scoring profiles]]
- [[eaw-create-indicator|Add or edit an application indicator]]
- [[eaw-attach-profile-indicators-with-application-scoring-profiles|Attach a profile indicator with an application scoring profile]]
- [[eaw-enable-or-disable-an-application-indicator|Activate or turn off an application or capability indicator]]
- [[generate-insights-into-ba|Generate insights into business applications]]
- [[eaw-edit-business-application-details|Edit business application details in list view]]
- [[eaw-create-a-demand-using-the-list-view|Create a demand using the list view]]
- [[eaw-set-planned-disposition-of-a-business-application-listview|Set the planned disposition of a business application]]
- [[eaw-add-business-application-lifecycle-data-listview|Add business application lifecycle data using the list view]]
- [[eaw-export-app-rat-list-data|Export application rationalization data to Excel or CSV]]
- [[eaw-rationalize-business-applications|Rationalization of business applications]]
- [[eaw-edit-a-demand-associated-with-a-business-application|Edit a demand associated with a business application]]
- [[eaw-edit-a-project-associated-with-a-business-application|Edit a project associated with a business application]]
- [[eaw-apply-filters-app-rat|Apply filters on the Application Rationalization page]]
- [[application-portfolio-management-landing-page|Enterprise Architecture]]
