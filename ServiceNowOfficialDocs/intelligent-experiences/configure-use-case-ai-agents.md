---
title: Create an agentic workflow
description: Create an agentic workflow in AI Agent Studio so that AI agents can coordinate to solve complex problems.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/configure-use-case-ai-agents.html
release: australia
topic_type: task
last_updated: "2025-11-23"
reading_time_minutes: 1
breadcrumb: [Now Assist AI agents, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-task
---

# Create an agentic workflow

Create an agentic workflow in [[ai-agent-studio|AI Agent Studio]] so that AI agents can coordinate to solve complex problems.

## Before you begin

Role required: sn\_aia.admin

## About this task

Agentic workflows solve business problems by automating processes with agentic AI. In AI Agent Studio, you must define an agentic workflow and connect it with an AI agent to execute complex goals. These goals can involve variable data or other factors that traditional automation can struggle with.

## Procedure

1.  Navigate to **All** &gt; **AI Agent Studio** &gt; **Create and manage** &gt; **Agentic workflows** and select **New**.

2.  [[define-key-requirements|Define your key requirements]].

3.  [[define-sec-controls-aw|Define the agentic workflow security controls]].

4.  [[add-trigger-aw|Add a trigger to automatically invoke your agentic workflow if a specified event occurs.]].

    If you want your agentic workflow to be used only in chats, you don’t need to add a trigger.

5.  [[channels-access-aw|Determine the channels to invoke your agentic workflow.]].


## Result

An agentic workflow is created and can be seen in the agentic workflow list in the Create and manage page.

## What to do next

-   Move to the **Testing** playground to [[test-aia-use-case|test your new agentic workflow]] using example utterances.
-   Review the [[platform-use-cases|Platform agentic workflows]].

## Related

- [[define-key-requirements|Define key requirements for an agentic workflow]]
- [[define-sec-controls-aw|Define security controls for an agentic workflow]]
- [[add-trigger-aw|Add a trigger to an agentic workflow]]
- [[channels-access-aw|Select channels and access for an agentic workflow]]
- [[test-aia-use-case|Manually test the execution of an agentic workflow]]
- [[platform-use-cases|Platform agentic workflows]]
- [[ai-agent-studio|AI Agent Studio]]
