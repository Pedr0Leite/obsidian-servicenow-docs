---
aliases:
  - "Theming for Now Assist in Virtual Agent enhanced c"
tags:
  - now-assist
  - virtual-agent
  - theming
  - css
  - service-portal
---

# Theming for Now Assist in Virtual Agent enhanced chat

You can customize the look and feel of the Now Assist in Virtual Agent enhanced chat experience in your ServiceNow portal by updating the relevant Cascading Style Sheet (CSS) variables.

As a Virtual Agent admin or admin, you can customize the default enhanced chat theming variables. Information on how to customize theming can be found in [Create a portal theme](https://www.servicenow.com/docs/access?context=c_CustomCSS&version=zurich&pubname=zurich-platform-user-interface&ft:locale=en-US). Edit these variables in the following table within the CSS variables field (sp_theme) record. You can also configure these variables with a CSS Include associated with a portal's theme.

**Note:**

For the variables, nass refers to enhanced chat.

For more information about enhanced chat, see [Enhanced chat](https://www.servicenow.com/docs/r/Xh633tLbz1TiB0XwDksy6A/H3QzdqbJSCqzscf0Vxj~lg).

| **Variable** | **Description** | **Default Values** |
| --- | --- | --- |
| $now-sp-nass-agent-bubble-font-color | Agent text message font color. | $text-color |
| $now-sp-nass-chat-user-message-bubble-bg-color | User text message bubble background color. | $brand-primary-lightest |
| $now-sp-nass-user-bubble-font-color | User text message font color. | $text-color |
| $now-sp-nass-timestamp-color | Timestamp text color. | $text-muted |
| $now-sp-nass-secondary-text-color | Secondary text color for example for Active. | $gray-dark |
| $now-sp-nass-system-msg-text-color | System message text color. | $text-muted |
| $now-sp-nass-base-input-field-placeholder-and-highlight-text-color | Input text color and with .45 opacity for placeholder. | $text-color |
| $now-sp-nass-base-link-color | Link color. | $brand-primary |
| $now-sp-nass-color-secondary_2 | Now Design System secondary-2 color. | $brand-primary-darker |
| $now-sp-nass-modeless-dialog-header-bg-color | Background color for primary Now Assist header bar. | #ffffff |
| $now-sp-nass-modeless-dialog-header-text-color | Text color for primary Now Assist header. | $text-color |
| $now-sp-nass-base-toolbar-labels-and-icons-color | Left-panel tool bar icons. | $gray-light |
| $now-sp-nass-toolbar-icons-color--hover | Left-panel tool bar icons in hover state. | $gray-dark |
| $now-sp-nass-toolbar-icons-color--active | Left-panel tool bar icons in active state. | $text-color |
| $now-sp-nass-toolbar-icons-fullscreen-mode-color | Left-panel tool bar icons in full-screen mode. | darken ($brand-primary-darker, 15%) |
| $now-sp-nass-toolbar-icons-fullscreen-mode-color--active | Left-panel tool bar icons in full-screen mode for active state. | $brand-primary-darker |
| $now-sp-nass-window-control-icons-color | Window controls icons. | $text-muted |
| $now-sp-nass-window-control-icons-color--hover | Window controls icons in hover state. | $text-color |
| $now-sp-nass-window-control-icons-color--active | Window controls icons in active state. | $text-color |
| $now-sp-nass-feedback-and-search-result-panel-color | Feedback panel and search result icon. | $text-muted |
| $now-sp-nass-feedback-and-search-result-panel-selected-color | Selected icon in feedback panel. | $text-muted |
| $now-sp-nass-action-and-kb-citation-color | Action and Knowledge Base link color | $link-color |
| $now-sp-nass-color-primary-0 | Primary-0 for pills/primary buttons. | $brand-primary-lightest |
| $now-sp-nass-color-primary-2 | Primary-2 for pills/primary buttons in active state. | $brand-primary-darker |
| $now-sp-nass-button-primary-bg-color | Submit button in choice picker control. | $btn-primary-bg |
| $now-sp-nass-button-primary-bg-active-color | Button primary active background color. | $btn-primary-bg |
| $now-sp-nass-button-selection-text-color | Now Design System secondary-1 color | $brand-primary |
| $now-sp-nass-tooltip-bg-color | Tooltip background color for input field icons. | $tooltip-bg |
| $now-sp-nass-tooltip-text-color | Tooltip text color for input field icons. | $tooltip-color |
| $now-sp-nass-alert-critical-color | Unread indicator color. | $brand-danger |
| $now-sp-nass-input-field-icon-color | Icon and attachment icon in the input field | $text-muted |
| $now-sp-nass-color-alert-moderate-3 | Animated loading icon color. | #4345a6 |
| $now-sp-nass-body-bg | Body primary background color. | #ffffff |
| $now-sp-nass-base-highlight-color | Background-color of matched text when searching emojis. | lighten ($warning, 35%) |
| $now-sp-nass-color-primary-3 | Bare buttons color in active state. | darken ($brand-primary-darker, 15%) |
| $now-sp-nass-color-background-primary | Content background color. | #ffffff |
| $now-sp-nass-header-panel-bg-color | Header panel background color. | #ffffff |
| $now-sp-nass-button-bg-action-color | Image picker select button background color. | $brand-primary |
| $now-sp-nass-primary-button-action-text-color | Image picker select button color. | $sp-btn-text-color |
| $now-sp-nass-base-separator-color | Separator. | $border-tertiary |
| $now-sp-nass-chat-agent-message-bubble-bg-color | Agent message bubble background color. | $gray-light |
| $now-sp-nass-citation-badge-color | Citation badge color. | $gray-lighter |
| $now-sp-nass-divider-and-border-tertiary-color | Divider and border color of mid-topic switch in search results. | $border-tertiary |
| $now-sp-nass-highlight-value-tertiary-info-bg-color | Highlighted info value in the mid-topic card. | $state-info-bg |
| $now-sp-nass-FAB-icon | Icon imagery that appears on the floating action button. | ai-sparkle-icon |
| $now-sp-nass-FAB-gradient-color-1 | First color of background gradient for chat floating action button icon. | $brand-primary-lighter |
| $now-sp-nass-FAB-gradient-color-2 | Second color of background gradient for chat floating action button icon. | $brand-info |
| $now-sp-nass-FAB-gradient-hover-color-1 | First color of background gradient for chat floating action button icon in hover state. | $brand-primary-darker |
| $now-sp-nass-FAB-gradient-hover-color-2 | Second color of background gradient for chat floating action button icon in hover state. | darken ($brand-info, 10%) |
| $now-sp-nass-FAB-gradient-active-color-1 | First color of background gradient for chat floating action button icon in active state. | $brand-primary |
| $now-sp-nass-FAB-gradient-active-color-2 | Second color of background gradient for chat floating action button icon in active state. | $brand-info |

## Related

- [[Now Assist]]
- [[VA - Basic Arch and ACLs]]
- [[Now Assist Panel (NAP) Troubleshooting Guide Commo]]
- [[ServiceNow – Service Portal]]