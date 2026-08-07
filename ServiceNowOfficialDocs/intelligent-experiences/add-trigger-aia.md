---
title: Add a trigger to an AI agent
description: In the guided setup for an AI agent, add triggers to run the AI agent automatically when certain conditions are met.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/add-trigger-aia.html
release: australia
topic_type: task
last_updated: "2025-11-23"
reading_time_minutes: 2
breadcrumb: [Create an AI agent, Now Assist AI agents, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-task
---

# Add a trigger to an AI agent

In the guided setup for an AI agent, add triggers to run the AI agent automatically when certain conditions are met.

## Before you begin

Role required: sn\_aia.admin

## About this task

Adding a trigger is optional. If you want your AI agent to be used only in chats, you don't need to add a trigger. Only add a trigger if you want to invoke the AI agent automatically when some event occurs.

**Note:** Triggers contain instance-specific information. If you are moving AI agents or agentic workflows between instances using Update Sets, you must set the triggers to inactive before adding them to the update sets and then activate them on the new instance.

If you don't want to add a trigger, skip to the final step, [[channels-access-aia|Select channels and access]].

## Procedure

1.  Select **Add trigger**.

2.  On the form, fill in the fields.

    |Fields|Description|
    |------|-----------|
    |Select trigger|List of triggers that are available in the instance.|
    |Name|Name of the trigger.|
    |Trigger objective|Additional user statements or sample utterances that help guide when to trigger this AI agent.|

    \[Omitted image "edit-trigger-1.png"\] Alt text: Edit/create a trigger basic description

<table><thead><tr><th>

Fields

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Table

</td><td>

Name of the applicable table for your AI agent.

</td></tr><tr><td>

Conditions

</td><td>

Conditions that you can add to control the trigger configuration. You must have at least one condition.Select **+ Add condition set** to add conditions to your AI agent trigger.

</td></tr><tr><td>

Active trigger toggle

</td><td>

Only enable the trigger once you’re confident in the execution of your AI agent. Try testing the [[test-ai-agent|AI agent execution]] and [[test-aia-access|user access]]. To review overall trends over many executions, try an [[execute-aia-eval|automated evaluation]].

</td></tr></tbody>
</table>    \[Omitted image "edit-trigger-2.png"\] Alt text: Define when the trigger occurs section

<table><thead><tr><th>

Fields

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Channel

</td><td>

Medium for the AI agent output: [[now-assist-center-now-assist-panel|Now Assist panel]] or Virtual Agent.

 **Note:** To view the output from a triggered AI agent in the Now Assist panel, you need the now\_assist\_panel\_user role.

</td></tr><tr><td>

Show an alert to users

</td><td>

Alerts appear in the selected channel.

</td></tr></tbody>
</table>    \[Omitted image "edit-trigger-3.png"\] Alt text: Log and launch options for a trigger section

    If you choose a scheduled trigger, additional options are available, such as the day of the week and time when you want the trigger to run.

    **Note:** When running a scheduled trigger, not every record is included in the execution. By default, the value is 10. If you want to change this number, you must set the **sn\_aia.max\_scheduled\_trigger\_query** system property to a different value.

    If you choose an email trigger, the target emails must exist on the Reply \[sys\_reply\] table. New emails aren’t available as triggers.

3.  Select **Add**.

4.  Repeat the preceding steps for additional triggers.


## Result

You have added triggers to your AI agent to run it automatically under the specified conditions.

## What to do next

Select **Save and continue** to move to the final step, [Select channels and access](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/channels-access-aia.md).

## Related

- [[channels-access-aia|Select channels and status for an AI agent]]
- [[test-ai-agent|Manually test the execution of an AI agent]]
- [[test-aia-access|Test user access to an AI agent]]
- [[execute-aia-eval|Execute an agentic evaluation run]]
- [[now-assist-center-now-assist-panel|Now Assist panel]]
