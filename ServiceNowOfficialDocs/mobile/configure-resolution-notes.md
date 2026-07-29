---
title: Configure mobile resolution notes generation
description: Generate the resolution notes that summarize work orders for mobile.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/configure-resolution-notes.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring Now Assist, Now Assist for Mobile, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Configure mobile resolution notes generation

Generate the resolution notes that summarize work orders for mobile.

## Before you begin

Role required: admin

Make sure that Now Assist is enabled in the instance. For more information, see [Now Assist](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/platform-now-assist-landing.md).

## Procedure

1.  Navigate to **All** &gt; **System Mobile** &gt; **[[mab-concept|Mobile App Builder]]**.

    The Mobile App Builder opens in a new browser tab and displays the application scope selection screen.

2.  Search for the application scope you are working in and then select the name of the application scope.

    The [[mab-menu-screen|Mobile App Builder categories home screen]] displays.

3.  Select the **Screens** category, and then choose the [[parameter-input-screen|input form screen]] you wish to add resolution notes generation to, or select **New**.

    **Note:** The input form screen must have at least one **String** type input as this is where the summary text will be generated.

4.  [[param-screen-config-actions|Create a parameter action]].

5.  [[create-mobile-ui-rule|Create a mobile UI rule]] with the **onUserAction** trigger type.

    This action is what will show up on the keyboard when a user clicks into an input field.

    **Note:** Parameter actions will only support triggering record summarization and will only appear when the input field is empty.

6.  [[create-mobile-ui-rule-action|Create a mobile UI rule action]] with the **Record Summarization** operation type.

7.  Add a delete action using the **ShowDeleteAll** input attribute.

    For more information, see [[parameter-screen-var-attr|Input form screen attributes for inputs]].

8.  Select **Save**.


**Parent Topic:**[[configuring-now-assist-mobile|Configuring Now Assist for Mobile]]

## Related

- [[param-screen-config-actions|Configure input sources in an input form screen]]
- [[create-mobile-ui-rule|Create a mobile UI rule]]
- [[create-mobile-ui-rule-action|Create a mobile UI rule action]]
- [[parameter-screen-var-attr|Input form screen attributes for inputs]]
- [[configuring-now-assist-mobile|Configuring Now Assist for Mobile]]
- [[mab-concept|Mobile App Builder]]
- [[mab-menu-screen|Mobile App Builder categories home screen]]
- [[parameter-input-screen|Input form screen]]
