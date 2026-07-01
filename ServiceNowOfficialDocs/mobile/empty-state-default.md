---
title: Configure an empty state
description: Configure an empty state to inform users that a page currently does not contain data. Add an image, text, and buttons to customize the empty state and improve the user experience.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/empty-state-default.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Empty state display, Mobile app components, Building mobile apps, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Configure an empty state

Configure an empty state to inform users that a page currently does not contain data. Add an image, text, and buttons to customize the empty state and improve the user experience.

## Before you begin

Whether creating a default or specific empty state, the following items might be required if you plan to display an image or button:

-   An image from the Attachments \[sys\_attachment\] table.
-   Defined button actions from the Function \[sys\_sg\_button\] table. For more information, see [[sg-studio-config-smart-button|Configure a smart button]].

Role required: admin

## About this task

This task explains how to configure a default empty state used in all screens. For information about how to customize empty states for specific screens, see the following topics:

-   [[empty-state-list-screen|Configure an empty state for a list screen]].
-   [[empty-state-form-applet-embedded-list|Configure an empty state for an embedded list in a record screen]].
-   [[empty-state-search-results|Configure an empty state for search results]].

## Procedure

1.  Navigate to **All** &gt; **System Mobile** &gt; **[[mab-concept|Mobile App Builder]]**.

    The Mobile App Builder opens in a new browser tab and displays the application scope selection screen.

2.  Search for the application scope you are working in and then select the name of the application scope.

    The [[mab-menu-screen|Mobile App Builder categories home screen]] displays.

3.  Create an empty state record, then use the bridge to [[mobile-card-builder|Mobile Card Builder]] \(MCB\) to configure the card that is referenced by the empty state record:

    1.  Select **All mobile records** in the menu.

    2.  From the Record type drop-down menu, select **Empty state \[sys\_sg\_empty\_state\]**, and then select **New**.

    3.  In the Empty State form, fill in the fields.

<table id="table_t2b_nm5_znb"><thead><tr><th>

Field

</th><th>

Value

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Title for the record.

</td></tr><tr><td>

Description

</td><td>

Optional description of the record.

</td></tr><tr><td>

Active

</td><td>

Option for enabling the display of the card setup within the empty state. Select the toggle to make the empty state record active.

</td></tr><tr><td>

Card

</td><td>

Select **Choose** to select an existing card that is referenced by the empty state record or select **New** to create a card.

 You are taken to MCB to configure the card.

</td></tr></tbody>
</table>    **Note:**

    Empty states can also be selected or created in the record editing screen in Mobile App Builder \(MAB\) for the following record types:

    -   [[list-screen|List screen]]
    -   [[map-screen|Map screen]]
    -   Custom map screen
    -   Search config
    -   Mobile app config
4.  In MCB, select the card you want to be referenced by the empty state record.

5.  Select **Use this card**.

    You are automatically returned to MAB.

6.  In MAB, select **Save** to save the empty state record.


## Result

An empty state displays in any screen that does not contain data.

## Related

- [[sg-studio-config-smart-button|Configure a smart button]]
- [[empty-state-list-screen|Configure an empty state for a list screen]]
- [[empty-state-form-applet-embedded-list|Configure an empty state for an embedded list in a record screen]]
- [[empty-state-search-results|Configure an empty state for search results]]
- [[mab-concept|Mobile App Builder]]
- [[mab-menu-screen|Mobile App Builder categories home screen]]
- [[mobile-card-builder|Mobile Card Builder]]
- [[list-screen|List screen]]
- [[map-screen|Map screen]]
