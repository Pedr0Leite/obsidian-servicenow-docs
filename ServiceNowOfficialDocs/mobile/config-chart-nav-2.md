---
title: Add a navigation function to an analytics preview
description: Configure your analytics preview to use a navigation function. This function directs your users to your chart screen from the analytics preview on your screen launcher.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/config-chart-nav-2.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Create a navigation function to a chart screen, Chart screen, Mobile screen types, Mobile screens, Mobile app components, Building mobile apps, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Add a navigation function to an analytics preview

Configure your analytics preview to use a navigation function. This function directs your users to your [[chart-screen|chart screen]] from the analytics preview on your screen launcher.

## Before you begin

Role required: admin

These steps detail instructions for adding your navigation function to an existing chart analytics preview. To utlize the navigation function, you must have configured a screen launcher with an analytics preview and a navigation to a chart screen. For details on that process, see [[sg-mobile-dashboard-preview|Create a mobile analytics preview]] and [[config-chart-nav|Create a navigation function to a chart screen]].

## Procedure

1.  Navigate to **All** &gt; **System Mobile** &gt; **[[mab-concept|Mobile App Builder]]**.

    The Mobile App Builder opens in a new browser tab and displays the application scope selection screen.

2.  Search for the application scope you're working in and then select the name of the application scope.

    The [[mab-menu-screen|Mobile App Builder categories home screen]] displays.

3.  Select **All mobile records** from the menu.

4.  From the **Record type** field, select Analytics preview **\[sys\_sg\_chart\]**, and then select the analytics preview record you created in the topic [Create a mobile analytics preview](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/sg-mobile-dashboard-preview.md).

5.  Navigate to the Destination screen navigation section and select the navigation function you created in the topic, [Create a navigation function to a chart screen](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/config-chart-nav.md).

6.  Select **Save**.


## Result

With this procedure, you’ve created the infrastructure of a mobile analytics preview and a navigation to a data visualization.

## What to do next

The final process involves adding the analytics preview to the launcher screen UI section. For more information, see, [[sg-ui-section-config-reports|Configure an analytics UI section]].

An additional configuration is available, where users view a list of records when they tap the data visualization. For more information, see [[nav-chart-to-list-1|Create a parameterized list for your chart]].

**Parent Topic:**[Create a navigation function to a chart screen](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/config-chart-nav.md)

## Related

- [[sg-mobile-dashboard-preview|Create a mobile analytics preview]]
- [[config-chart-nav|Create a navigation function to a chart screen]]
- [[sg-ui-section-config-reports|Configure an analytics UI section]]
- [[nav-chart-to-list-1|Create a parameterized list for your chart]]
- [[chart-screen|Chart screen]]
- [[mab-concept|Mobile App Builder]]
- [[mab-menu-screen|Mobile App Builder categories home screen]]
