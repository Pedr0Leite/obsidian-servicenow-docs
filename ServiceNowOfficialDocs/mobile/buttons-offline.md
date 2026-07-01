---
title: Display and hide functions in offline mode
description: Define whether to show or hide buttons while users are in offline mode on their Mobile Agent app.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/buttons-offline.html
release: australia
topic_type: task
last_updated: "2026-06-09"
reading_time_minutes: 1
breadcrumb: [Supported functions, Align apps, screens, and functions, Offline mode setup options, Offline mode, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Display and hide functions in offline mode

Define whether to show or hide buttons while users are in [[mobile-offline-mode|offline mode]] on their [[mobile-experience|Mobile Agent app]].

## Before you begin

Role required: mobile\_admin, admin

## Procedure

1.  Navigate to **All** and in the filter enter `sys_sg_button.list`.

2.  Select an existing action function or select **New**.

    The Function screen displays. For more information on how to [[sg-studio-config-action-function|configure an action function]], see [[mobile-actions|Action functions]].

3.  Select the **Offline Properties** tab.

4.  Select the **Offline** check box to display all the fields relevant for an offline function configuration.

5.  Complete the action function offline mode property fields as required, see [[config-offline-properties-action-funct|Configure offline mode properties for action functions]].

6.  From the **Offline Condition Type** field, select whether the condition style is **Declarative** or **Script**.

7.  From the **Table** field, select a table that is the source of the fields used in the **Offline Condition** field, and from where the conditions are evaluated.

8.  Depending on the selection made from the **Offline Condition Type** field, either do one of the following in the **Offline Condition** field:

    -   For **Declarative**, create declarative conditions to be performed in offline mode.
    -   For **Script**, enter a script in the text window that contains query conditions that are evaluated in offline mode.
9.  Select **Submit** to save your display and hide button configurations.

10. Complete the action function offline mode property fields as required, see [[config-offline-property-function-instance|Configure offline mode properties for function instances]].


**Parent Topic:**[[functions-offline|Supported functions for offline mode]]

## Related

- [[mobile-actions|Action functions]]
- [[config-offline-properties-action-funct|Configure offline mode properties for action functions]]
- [[config-offline-property-function-instance|Configure offline mode properties for function instances]]
- [[functions-offline|Supported functions for offline mode]]
- [[mobile-offline-mode|Offline mode]]
- [[mobile-experience|Mobile Agent app]]
- [[sg-studio-config-action-function|Configure an action function]]
