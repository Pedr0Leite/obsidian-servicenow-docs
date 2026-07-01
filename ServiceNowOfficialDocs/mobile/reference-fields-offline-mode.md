---
title: Configure reference inputs for input form screens in offline mode
description: Configure reference inputs so that users can see a list of records in offline mode on their Mobile Agent.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/reference-fields-offline-mode.html
release: australia
topic_type: task
last_updated: "2026-06-08"
reading_time_minutes: 1
breadcrumb: [Input forms in offline, Offline mode setup options, Offline mode, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
---

# Configure reference inputs for input form screens in offline mode

Configure reference inputs so that users can see a list of records in [[mobile-offline-mode|offline mode]] on their Mobile Agent.

## Before you begin

Role required: mobile\_admin, admin

## Procedure

1.  Navigate to **All** &gt; **System Mobile** &gt; **[[mab-concept|Mobile App Builder]]**.

    The Mobile App Builder opens in a new browser tab and displays the application scope selection screen.

2.  Search for the application scope you are working in and then select the name of the application scope.

    The [[mab-menu-screen|Mobile App Builder categories home screen]] displays.

3.  Select **All mobile records** from the menu.

4.  From the **Record type** field, select **[[parameter-input-screen|Input form screen]] \[sys\_sg\_parameter\_screen\]** and then either select **New** or an existing record.

5.  If you're creating a new input form screen, enter a name for the input form screen and complete the fields as required.

6.  In the Settings area, select the **Available offline** to true.

7.  In the Inputs area, select **New** and configure the input fields that your users use to enter information.

    For an explanation of the fields, see [[param-screen-config-inputs|Configure input form screen inputs]].

8.  In the Settings area, select the **Input type** for users to use within the input form screen.

9.  In the Input attributes area of the Input form, select **New** to open the Input Attribute form.

10. Select the name and value of the input attributes you want to use in offline mode.

    The options available in these fields correspond to the selection made in the **Input type** field from the Input form.

    **Note:** For a list of the attributes to use in offline mode, see [[reference-fields-offline-attributes|Reference field attributes for input form screens in offline mode]].

11. Select **Save**.


**Parent Topic:**[[offline-input-form|Input forms in offline]]

## Related

- [[param-screen-config-inputs|Configure input form screen inputs]]
- [[reference-fields-offline-attributes|Reference field attributes for input form screens in offline mode]]
- [[offline-input-form|Input forms in offline]]
- [[mobile-offline-mode|Offline mode]]
- [[mab-concept|Mobile App Builder]]
- [[mab-menu-screen|Mobile App Builder categories home screen]]
- [[parameter-input-screen|Input form screen]]
