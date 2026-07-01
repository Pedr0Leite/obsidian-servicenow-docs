---
title: Configure Next Experience accessibility preferences
description: Set up Next Experience accessibility preferences to achieve a UI that's most accessible to you.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/next-experience-accessibility-preferences.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
keywords: [accessibility preferences, next experience accessibility]
breadcrumb: [Preferences, Use, Next Experience UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-task
---

# Configure Next Experience accessibility preferences

Set up Next Experience accessibility preferences to achieve a UI that's most accessible to you.

## Before you begin

Next Experience includes a guided tour that introduces the available accessibility preferences and where to find them. The guided tour is available from the [[help-center|Help Center]] \[Omitted image "help-icon-new.png"\] Alt text: Help Center in Unified navigation header. and provides an in-context walkthrough of the preferences and related settings.

Role required: none

## Procedure

1.  Navigate to **User Menu** &gt; **Preferences** &gt; **Accessibility**.

2.  Select the toggle next to each option to turn the preference on or off.

<table id="table_y5b_j2f_jqb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

\[Omitted image "pol-pref-date-time.png"\] Alt text: Show date and time formats.

</td><td>

Displays the date and time format \(yyyy-MM-dd-HH:mm:ss\) next to the [[c_FormFields|form fields]] ensuring the format remains visible even when the field is in focus. For more information, see [[show-date-time-formats-forms|Show date and time formats on forms preference]].

</td></tr><tr><td>

\[Omitted image "pol-pref-colors.png"\] Alt text: Replace colors with patterns in charts and graphs.

</td><td>

Adjusts charts and graphs to display with a pattern such as stripes or dashed lines instead of just a color. For more information, see [[replace-colors-with-patterns|Replace colors with patterns in charts and graphs preference]].

</td></tr><tr><td>

\[Omitted image "pol-pref-shortcuts.png"\] Alt text: Enable special keyboard shortcuts.

</td><td>

Use keyboard shortcuts to quickly perform common actions in the user interface. The keyboard shortcuts that display in the modal are specific to the screen you are viewing. For more information, see [[enable-keyboard-shortcuts-pref|Enable keyboard shortcuts preference]] and [[next-experience-keyboard-shortcuts|Next Experience keyboard shortcuts]]. **Note:** If you’re [[working-in-classic-lists-and-forms|working in the Classic Environment]], see [[r_KeyboardShortcuts|Core UI keyboard shortcuts]].

</td></tr><tr><td>

\[Omitted image "pol-pref-no-hover.png"\] Alt text: Show all buttons without the need to hover

</td><td>

Displays all hidden fields, buttons or other UI elements, eliminating the need to hover over them. For more information, see [[show-all-buttons-pref|Show all buttons without the need to hover preference]].

</td></tr><tr><td>

\[Omitted image "pol-pref-data.png"\] Alt text: Enable data table for charts and graphs.

</td><td>

Shows a table with chart and graph data for easier screen reader access. For more information, see [[enable-data-table-pref|Enable data table for charts and graphs preference]].

</td></tr><tr><td>

\[Omitted image "pol-pref-reduce-motion.png"\] Alt text: Reduce motion.

</td><td>

Reduces the speed of the animations when switching between screens. This reduction pertains mainly to login animations. For more information, see [[reduce-motion-pref|Reduce motion preference]].

</td></tr><tr><td>

\[Omitted image "pol-pref-classic-accessibility.png"\] Alt text: Enable accessibility in classic.

</td><td>

Extends keyboard navigation and enables more tab stops in the classic environment so you can tab to icons and buttons in [[lists-configurable-workspace|lists]], form fields, and cards. This option also presents additional info on [[form-configurable-workspace|forms]]. For more information, see [[enable-accessibility-in-classic-pref|Enable accessibility in Classic preference]].**Note:** The classic environment refers to working in lists of records and on record forms directly. You can work in the classic environment with Next Experience active, or with it inactive, which is referred to as [[c_UI16|Core UI]].

</td></tr><tr><td>

\[Omitted image "pol-pref-truncated-text.png"\] Alt text: Enable keyboard focus on truncated text.

</td><td>

Allows keyboard-only users to access truncated text. Truncated text is text that doesn't fit on the screen and is indicated by an ellipsis \[Omitted image "ellipsis-h-fill.png"\] Alt text: Ellipses icon.. When this preference is enabled, keyboard-only users can access the truncated text as they Tab through the focus order, revealing the full text of each tooltip as they navigate the screen. For more information, see [[enable-keyboard-focus-pref|Enable keyboard focus on text that displays tooltip]].

</td></tr><tr><td>

\[Omitted image "pol-pref-voice-input.png"\] Alt text: Enable voice input for the Now Assist panel.

</td><td>

Voice input is activated automatically when Now Assist panel is activated. As of the Zurich patch 4, voice input is configured in [Additional chat features](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/conversational-interfaces/additional-chat-features.md) and not with this option.

Activates voice-to-text in the Now Assist panel. With this feature, use your voice to access Now Assist skills in the [Now Assist panel](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/now-assist-panel-overview.md) in any supported language. For more information on this preference, see [[enable-voice-input-pref|Enable voice input for the Now Assist panel]].**Note:** This preference appears only if your system administrator has enabled Now Assist voice input for your instance. For more information, see [Enable voice input for Now Assist panel](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/enable-voice-input-for-now-assist-panel.md).

</td></tr><tr><td>

\[Omitted image "pol-pref-auto-dismiss.png"\] Alt text: Do not auto-dismiss page alerts.

</td><td>

Keeps page alerts visible until you acknowledge them. When this preference is turned off, page alerts may disappear after a certain amount of time depending on how the specific page alert is configured. For more information, see [[do-not-auto-dismiss-pref|Do not auto-dismiss page alerts preference]].**Note:** Critical and warning alerts do not disappear. If focus is applied to the alert, the auto-dismiss feature will not apply.

</td></tr><tr><td>

\[Omitted image "pol-pref-auto-focus.png"\] Alt text: Enable auto-focus on page alerts.

</td><td>

Automatically shifts focus to any page alert as soon as it appears.

</td></tr></tbody>
</table>    **Note:** If users have configured operating system-specific settings, such as forced colors or contrast in Windows, those settings are not overridden by Next Experience [[c_UserPreferences|user preferences]] or themes. If those OS-specific settings are inactive, color and theme behaviors will revert to those behaviors defined in the [[next-experience-landing-page|Next Experience UI]].

## Related

- [[show-date-time-formats-forms|Show date and time formats on forms preference]]
- [[replace-colors-with-patterns|Replace colors with patterns in charts and graphs preference]]
- [[enable-keyboard-shortcuts-pref|Enable keyboard shortcuts preference]]
- [[next-experience-keyboard-shortcuts|Next Experience keyboard shortcuts]]
- [[r_KeyboardShortcuts|Core UI keyboard shortcuts]]
- [[show-all-buttons-pref|Show all buttons without the need to hover preference]]
- [[enable-data-table-pref|Enable data table for charts and graphs preference]]
- [[reduce-motion-pref|Reduce motion preference]]
- [[enable-accessibility-in-classic-pref|Enable accessibility in Classic preference]]
- [[enable-keyboard-focus-pref|Enable keyboard focus on text that displays tooltip]]
- [[enable-voice-input-pref|Enable voice input for the Now Assist panel]]
- [[do-not-auto-dismiss-pref|Do not auto-dismiss page alerts preference]]
- [[help-center|Help Center]]
- [[c_FormFields|Form fields]]
- [[working-in-classic-lists-and-forms|Working in the classic environment]]
- [[lists-configurable-workspace|Lists]]
- [[form-configurable-workspace|Forms]]
- [[c_UI16|Core UI]]
- [[c_UserPreferences|User preferences]]
- [[next-experience-landing-page|Next Experience UI]]
