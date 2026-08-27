---
title: Rationalization of business applications
description: As an Enterprise Architect, you can use application rationalization to evaluate your business applications.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-rationalize-business-applications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-concept
---

# Rationalization of business applications

As an Enterprise Architect, you can use application rationalization to evaluate your business applications.

## Application rationalization overview

Rationalize all business applications in a category and decide whether to invest, sustain, migrate, or retire an application.

Select the application rationalization icon \(\[Omitted image "icon-app-rationalization.png"\] Alt text: Application rationalization icon.\) to navigate to the Application Rationalization page.

You can perform the following using application rationalization:

-   Analyze business applications based on multiple scores.
-   Create a demand for a business application.
-   [[eaw-set-planned-disposition-of-a-business-application-listview|Set the planned disposition of a business application]].
-   Add life-cycle details to an existing business application.

You can view all the business applications in a bubble chart view or in a list view. However, business applications marked as **Retired** or in **End of Life** lifecycle stage aren’t displayed on the Application Rationalization bubble chart or list view pages. However, you can view those business applications by updating the **sn\_apm\_ws.business\_application\_default\_filter** system property. Contact your ServiceNow® account service manager to update the system property.

You can also generate insights into business applications using Now Assist. For information, see [[generate-insights-into-ba|Generate insights into business applications]].

\[Omitted image "bubble-chart-view.png"\] Alt text: Bubble chart view in the Application Rationalization page.

\[Omitted image "eaw-list-view.png"\] Alt text: List view in the Application Rationalization page.

## Application rationalization insights on the Enterprise Architecture Workspace home page

The application rationalization feature of Application Portfolio Management also provides insights for your business applications. To see the insight cards, navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]** and select the Insights section. The insights cards display information based on scores derived from application rationalization. The following insight cards are available:

-   **Candidate business applications for retirement**-business applications that might fit for retirement based on their indicator scores.
-   **Candidate business applications for migration**-business applications that might fit for migration based on their indicator scores.
-   **Candidate business applications for investment**-business applications that might fit for investment based on their indicator scores.
-   **Candidate business applications with mismatch planned disposition**-business application with mismatch between their planned disposition and their indicator scores.

\[Omitted image "app-rat-card-homepage.png"\] Alt text: Application rationalization cards highlighted on the Home page of EA Workspace.

On selecting a particular card, the Application Rationalization page appears to display the relevant business application data, based on your selection.

**Note:** To return to the main Application Rationalization page, select **Go to Application Rationalization**.

\[Omitted image "app-rat-back-button.png"\] Alt text: Go to Application Rationalization button highlighted on the application rationalization list view page.

## Indicator scores based on fiscal period

All the indicator scores are displayed according to the latest fiscal period, by default. You can also select a different fiscal period from the Scores for fiscal period list. Your fiscal period preferences are saved and applied the next time you visit the page.

\[Omitted image "fiscal-period-dropdown.png"\] Alt text: Scores for fiscal period list highlighted on the Application rationalization list view page.

The latest fiscal period is derived from the apm\_app\_indicator\_score list. The fiscal period type \(month, quarter, or year\) is derived from the system property **com.glide.fiscal\_calendar.fiscal\_unit**.

**Note:** You can zoom on this page to 200% or 400% through your browser settings without the loss of content or functionality. Page layouts are transformed into a vertical, stacked view automatically.

-   **[[eaw-bubble-chart-view|Bubble chart view of application rationalization]]**  
Bubble charts are interactive graphs that position applications in different quadrants, based on their indicator scores. Based on the position of the business application in the quadrants, enterprise architects can take decisions to invest in, sustain, migrate, or retire the business applications.
-   **[[eaw-list-view|List view of application rationalization]]**  
As an Enterprise Architect, you can view the list of all business applications. The List view enables you to see high-level information on all your business applications and all the indicator scores that are attached to them.
-   **[[eaw-application-indicator-score-calculation|Application indicator score calculation in Enterprise Architecture Workspace]]**  
Enterprise Architecture Workspace calculates a composite score for each business application and business capability by running data from configured indicators through a multi-step pipeline that normalizes raw values, applies weighted contributions, and aggregates the results into a final score per fiscal period.
-   **[[trm-tech-debt-indicator-for-app-rat|Tech debt indicator score for application rationalization]]**  
The Technology Reference Model \(TRM\) Technical Debt indicator is a customizable application metric that evaluates the technical debt score for each Business Application. This score reflects the number of associated technologies that don’t comply with established TRM standards. It offers a clear and measurable value that can be leveraged across the Enterprise Architecture workspace for scoring, analysis, and visualization.
-   **[[eaw-trm-technology-lifecycle-risk-score|Technology lifecycle risk score in Enterprise Architecture Workspace]]**  
The Technology Portfolio Management \(TPM\) lifecycle risk score is a numeric value that quantifies how close a technology is to its end-of-support or end-of-life milestone. Risk scores roll up from individual technologies through application services to business applications, and serve as an indicator in scoring profiles to surface lifecycle exposure across the portfolio.

**Parent Topic:**[[explore-eaw|Exploring Enterprise Architecture Workspace]]

**Related topics**  


[[eaw-work-with-app-rat|Working with application rationalization]]

[Generate insights into business applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/generate-insights-into-ba.md)

## Related

- [[generate-insights-into-ba|Generate insights into business applications]]
- [[eaw-bubble-chart-view|Bubble chart view of application rationalization]]
- [[eaw-list-view|List view of application rationalization]]
- [[eaw-application-indicator-score-calculation|Application indicator score calculation in Enterprise Architecture Workspace]]
- [[trm-tech-debt-indicator-for-app-rat|Tech debt indicator score for application rationalization]]
- [[eaw-trm-technology-lifecycle-risk-score|Technology lifecycle risk score in Enterprise Architecture Workspace]]
- [[explore-eaw|Exploring Enterprise Architecture Workspace]]
- [[eaw-work-with-app-rat|Working with application rationalization]]
- [[eaw-set-planned-disposition-of-a-business-application-listview|Set the planned disposition of a business application]]
- [[ea-workspace|Enterprise Architecture Workspace]]
