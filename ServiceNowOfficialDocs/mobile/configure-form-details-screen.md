---
title: Configure a details screen for a record screen
description: Create a details screen to display record fields on your screen.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/configure-form-details-screen.html
release: australia
topic_type: task
last_updated: "2026-03-25"
reading_time_minutes: 3
breadcrumb: [Record screen, Mobile screen types, Mobile screens, Mobile app components, Building mobile apps, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Configure a details screen for a record screen

Create a details screen to display record fields on your screen.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Mobile** &gt; **[[mab-concept|Mobile App Builder]]**.

    The Mobile App Builder opens in a new browser tab and displays the application scope selection screen.

2.  Search for the application scope you are working in and then select the name of the application scope.

    The [[mab-menu-screen|Mobile App Builder categories home screen]] displays.

3.  Select the **Screens** category, and then select the [[form-screen|record screen]] for which you want to configure a details screen.

4.  In the Record Screen form, scroll down to the **Record screen segments** area, and then select **New**.

5.  In the **Create a record screen segment** dialog box, select **Record screen segment**, and then select **Continue**.

6.  In the Record Screen Segment form, scroll down to the **Embedded screen** area, and then select **New**.

7.  In the **[[sg-studio-configure-applet-screens|Create a screen]]** dialog box, select **Details**, and then select **Continue**.

8.  Complete the following fields as needed.

    **Note:** The available fields that can be configured on a details screen form are determined by your organization's mobile UI rules. For more information, see [[mobile-ui-rules|Mobile UI Rules]].

<table id="table_wrg_24n_lwb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td class="sub-head" colspan="2">

Properties

</td></tr><tr><td>

Name

</td><td>

The screen name. This name is not visible to end users.

</td></tr><tr><td>

Description

</td><td>

Description that is used to identify the details screen.

</td></tr><tr><td class="sub-head" colspan="2">

Settings

</td></tr><tr><td>

Fetch type

</td><td>

Settings that determine when data is loaded in your screens. Select from the following fetch types:

-   **Prefetch**: This option pre-loads record screen data when an end user accesses a list, calendar, or record screen.
-   **Background**: The app makes a background network request to load embedded screens or record screen segments.
-   **Dynamic prefetch**: Screens for the first 10 rows load as described for the **Prefetch** fetch type. After the 10 first rows load, additional rows of screens load with the **On-demand** fetch type.
-   **On-demand**: The app sends a network request to load the app only when end users navigate to it.
 For more information about fetch types, see [[applet-fetch-types|Mobile fetch types]].

</td></tr><tr><td>

Available offline

</td><td>

Whether the details screen is available when the device is offline.**Note:** [[mobile-offline-mode|Offline mode]] is only supported on the Mobile Agent.

</td></tr><tr><td>

Icon

</td><td>

The icon that displays for your details screen. Select **Choose** to use an existing icon, or select **New** to configure one.

</td></tr><tr><td>

Data

</td><td>

The table that is used for the details screen. Select the arrow to display a list of tables you can choose from.

</td></tr><tr><td>

Screen fields

</td><td>

Sets the fields for the details screen. For information about setting these fields, see [[sg-screen-field-enhancements|Screen fields]].

</td></tr><tr><td>

Field function instances

</td><td>

\(Optional\) Sets the functions for your details screen. Select an existing field function instance or select **New** to add one. For information about adding field functions, see [[details-screen-functions|Add functions to your details screens]].

</td></tr><tr><td>

Footer function instances

</td><td>

\(Optional\) Sets the function in the footer region of the mobile app screen. Select an existing footer function instance or select **New** to add one. For more information about adding a footer function instance, see [[sg-studio-button-instances|Associate a function with a location in the app]].

</td></tr><tr><td>

UI parameters

</td><td>

UI parameters are variables that affect how a field or UI element behaves. Use UI parameters to determine how a value can be entered or whether it is automatically populated for the UI element based on the end user's action. Select an existing UI parameter or select **New** to add one. For more information about adding a UI parameter, see [[configure-param-form-applet|Configure a parameterized record screen]].

</td></tr></tbody>
</table>9.  Select **Save**.

## Related

- [[mobile-ui-rules|Mobile UI Rules]]
- [[applet-fetch-types|Mobile fetch types]]
- [[sg-screen-field-enhancements|Screen fields]]
- [[details-screen-functions|Add functions to your details screens]]
- [[sg-studio-button-instances|Associate a function with a location in the app]]
- [[configure-param-form-applet|Configure a parameterized record screen]]
- [[mab-concept|Mobile App Builder]]
- [[mab-menu-screen|Mobile App Builder categories home screen]]
- [[form-screen|Record screen]]
- [[sg-studio-configure-applet-screens|Create a screen]]
- [[mobile-offline-mode|Offline mode]]
