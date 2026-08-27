---
title: Configure an empty state for a list screen
description: Configure an empty state to display on empty list screens, to provide information to further direct users. These features are configured in the web-based UI instead of in the Mobile App Builder.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/empty-state-list-screen.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [List screen, Mobile screen types, Mobile screens, Mobile app components, Building mobile apps, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Configure an empty state for a list screen

Configure an empty state to display on empty list screens, to provide information to further direct users. These features are configured in the web-based UI instead of in the [[mab-concept|Mobile App Builder]].

## Before you begin

You should already have an empty state configured for list screens that do not contain any data. For more information, see [[empty-state-default|Configure an empty state]].

Role required: admin

## Procedure

1.  In the web-based UI, enter `sys_sg_list_screen.list` in the filter navigator.

2.  Select a [[list-screen|list screen]] to display the specific empty state.

3.  In the **Empty State** field, select an empty state to associate with the list screen.

4.  Right-click in the header and select **Save**.

## Related

- [[empty-state-default|Configure an empty state]]
- [[mab-concept|Mobile App Builder]]
- [[list-screen|List screen]]
