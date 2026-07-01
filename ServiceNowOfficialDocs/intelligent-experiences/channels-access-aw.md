---
title: Select channels and access for an agentic workflow
description: In the guided setup for an agentic workflow, activate the agentic workflow to use in the Now Assist panel or UI actions in the Core UI and workspaces.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/channels-access-aw.html
release: australia
topic_type: task
last_updated: "2025-11-23"
reading_time_minutes: 2
breadcrumb: [Create an agentic workflow, Now Assist AI agents, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-task
---

# Select channels and access for an agentic workflow

In the guided setup for an agentic workflow, activate the agentic workflow to use in the [[now-assist-center-now-assist-panel|Now Assist panel]] or UI actions in the Core UI and workspaces.

## Before you begin

Role required: sn\_aia.admin

## About this task

The final step of the agentic workflow guided setup includes options for where a user can invoke the agentic workflow. The Now Assist panel is available to users with the correct role. You can specify the exact conditions when a UI action is available to users on a table.

## Procedure

1.  Select whether you want users to use the Now Assist panel to invoke the agentic workflow.

2.  Add a UI action to your agentic workflow.

    1.  Select **Add UI action**.

    2.  Enter the UI action label.

        The UI action label is the text that the user sees in the button on the table.

    3.  Select a table where the UI action can be used.

        Users who are accessing a record on the selected table can view the UI action in the Core UI and workspaces. See [[in-product-agentic-ai|In-product agentic AI]] for more information about the AI Workflows panel.

    4.  Specify conditions for the UI action to appear and select **Add**.

        For example, you could only show a UI action for a Generate resolution plan agentic workflow if the record state is Active.

        **Note:** The display for a new UI action is turned on by default.

    \[Omitted image "channels-access-aw.png"\] Alt text: Select channels and access page

3.  Select **Save and test**.


## Result

You have completed the guided setup for creating an agentic workflow. Your new agentic workflow can be edited at any time using [[ai-agent-studio|AI Agent Studio]].

If you added a UI action for your agentic workflow in this guided setup, but the UI action is not appearing on forms, ensure that the property **com.glide.agentic\_processes\_view.enabled** is set to `true`.

## What to do next

Move to the **Testing** playground to [[test-aia-use-case|test an agentic workflow execution]] using example utterances or to [[test-aw-access|test user access]].

## Related

- [[in-product-agentic-ai|In-product experience for agentic workflows]]
- [[test-aia-use-case|Manually test the execution of an agentic workflow]]
- [[test-aw-access|Test user access to an agentic workflow]]
- [[now-assist-center-now-assist-panel|Now Assist panel]]
- [[ai-agent-studio|AI Agent Studio]]
