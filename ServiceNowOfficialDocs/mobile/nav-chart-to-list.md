---
title: Configure a navigation from a chart to a list screen
description: Configure a navigation to allow your users to navigate to a list of records from your chart screen.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/nav-chart-to-list.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Chart screen, Mobile screen types, Mobile screens, Mobile app components, Building mobile apps, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-concept
---

# Configure a navigation from a chart to a list screen

Configure a navigation to allow your users to navigate to a list of records from your [[chart-screen|chart screen]].

To create your navigation, you need to create the following components:

-   Configure a parametrized list and [[form-screen|record screen]].
-   Configure a navigation function to navigate from your chart to your parametrized list and form.
-   Associate your navigation function to your chart screen.

These steps assume you have an existing chart screen you want to configure. If you have not yet created a chart screen, you can find details on creating charts at [[config-single-score-applet|Create a chart screen for a data visualization]].

-   **[[nav-chart-to-list-1|Create a parameterized list for your chart]]**  
Create the list that users see when they tap on your chart screen.
-   **[[nav-chart-to-list-2|Create a navigation function for your chart screen]]**  
[[sg-launcher-nav-example-1|Create a navigation function]] to direct your users from the chart screen to a parametrized list.
-   **[[nav-chart-to-list-3|Assign the navigation function to the chart screen]]**  
Assign your navigation function to your chart screen so that your users can tap the chart to access the list of records.

## Related

- [[config-single-score-applet|Create a chart screen for a data visualization]]
- [[nav-chart-to-list-1|Create a parameterized list for your chart]]
- [[nav-chart-to-list-2|Create a navigation function for your chart screen]]
- [[nav-chart-to-list-3|Assign the navigation function to the chart screen]]
- [[chart-screen|Chart screen]]
- [[form-screen|Record screen]]
- [[sg-launcher-nav-example-1|Create a navigation function]]
