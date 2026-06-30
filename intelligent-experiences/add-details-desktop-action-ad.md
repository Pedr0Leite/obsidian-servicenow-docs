---
title: Add details to desktop actions in AI Desktop Actions
description: Add desktop action details, such as name, description, and associated applications, and review inputs and outputs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/add-details-desktop-action-ad.html
release: australia
topic_type: task
last_updated: "2026-05-25"
reading_time_minutes: 2
breadcrumb: [Design defined-path desktop actions, AI Desktop Actions, Enable AI experiences]
---

# Add details to desktop actions in AI Desktop Actions

Add desktop action details, such as name, description, and associated applications, and review inputs and outputs.

## Before you begin

-   Capture your automation steps. For more information, see [[auto-create-desktop-action-ad|Automate repetitive tasks by auto-capturing steps in AI Desktop Actions]] or [[manual-create-desktop-action-ad|Extend a desktop action by manually capturing steps in AI Desktop Actions]].
-   Configure the properties for screens, anchors, and steps. For more information, see [[screen-anchor-and-action-properties-ad|Screen, anchor, and step properties in AI Desktop Actions]].

Role required: sn\_aia.admin

## Procedure

1.  In the Design workspace, select the Details tab.

    \[Omitted image "details-tab-ad.png"\] Alt text: [[agentic-desktop-landing-page|AI Desktop Actions]] details tab displaying name, description, application, and many other fields, along with inputs and outputs.

2.  In the Desktop action details section, edit the name of the desktop action.

    The description in the **Action description** field is auto-filled when you select the **Record with AI** option and an AI badge appears.

3.  In the **Application** list, select the applications you want to automate.

    The list displays the applications available on the ServiceNow instance. If an application isn't listed, you can add it by selecting the **Add** icon \[Omitted image "ad-add-app-icon.png"\] Alt text:.

4.  In the Input and output parameters section, review the parameters related to steps for each screen.

5.  Select **Save**.

    You can save the desktop action after all the required fields are configured.


## What to do next

Test and activate the desktop action so that it’s available as a tool in the [[ai-agent-studio|AI Agent Studio]]. You can add this tool to the AI agents that execute desktop actions in your desktop environment. For more information, see [[test-activate-desktop-action-ad|Test and activate a desktop action in AI Desktop Actions]].

## Related

- [[auto-create-desktop-action-ad|Automate repetitive tasks by auto-capturing steps in AI Desktop Actions]]
- [[manual-create-desktop-action-ad|Extend a desktop action by manually capturing steps in AI Desktop Actions]]
- [[screen-anchor-and-action-properties-ad|Screen, anchor, and step properties in AI Desktop Actions]]
- [[test-activate-desktop-action-ad|Test and activate a desktop action in AI Desktop Actions]]
- [[agentic-desktop-landing-page|AI Desktop Actions]]
- [[ai-agent-studio|AI Agent Studio]]
