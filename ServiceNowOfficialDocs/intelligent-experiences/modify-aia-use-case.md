---
title: Modify an agentic workflow
description: Make changes to existing agentic workflows in AI Agent Studio to adjust them to suit your business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/modify-aia-use-case.html
release: australia
topic_type: task
last_updated: "2025-11-18"
reading_time_minutes: 3
breadcrumb: [Create an agentic workflow, Now Assist AI agents, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-task
---

# Modify an agentic workflow

Make changes to existing agentic workflows in [[ai-agent-studio|AI Agent Studio]] to adjust them to suit your business needs.

## Before you begin

Role required: sns\_aia.admin

## Procedure

1.  Navigate to **All** &gt; **AI Agent Studio** &gt; **Create and manage** &gt; **Agentic workflows** and open the agentic workflows list on your AI Agent Studio.

2.  Select the agentic workflow that you want to modify.

3.  Modify the fields in the different sections of the guided setup, making changes to the fields for your own requirements.

    The guided setup is the same as the one for creating an agentic workflow:

    -   [[define-key-requirements|Define the AI agent's specialty]].
    -   [[define-sec-controls-aw|Define the AI agent security controls]].
    -   [[add-trigger-aw|\(Optional\) Add a trigger to automatically invoke your AI agent if a specified event occurs.]].
    -   [[channels-access-aw|Determine the channels to invoke your agentic workflow.]].
    **Note:** Some fields aren't editable if the agent is associated with a [[platform-now-assist-landing|Now Assist]] application. If you want to make more modifications, [[clone-aia-usecase|duplicate the agentic workflow]] and make changes to the duplicate.

    -   For the **List of steps** field, you can create multiple versions of the same agentic workflow without losing previous versions. Creating versions enables you to test different instructions to evaluate performance. See [[version-control|Version control for AI agents and agentic workflows]] for more information.
    -   For the access control lists \(ACLs\), you can edit the security fields and define who can access the agentic workflow and edit the entity to run the agentic workflow as a dynamic user or an AI user. For more information, see [[aia-security-implementation|Implement access control in Now Assist AI agents]].
    -   For more guidance on creating effective instructions, see the [[gg-creating-aia|general guidelines for creating AI agents and agentic workflows]].
    You can navigate through the steps of the Guided Setup with the **Continue** and **Back** buttons.

4.  Navigate to the last step and select **Save and test** to save your changes and begin testing your modified agentic workflow.


## Result

Your agentic workflow is modified and ready to test.

## What to do next

You can [[test-aia-use-case|test an execution of your agentic workflow manually]] or [[test-aw-access|test the user access]]. Once you've determined that the agentic workflow has the basic functionality you expect, you can [[execute-aia-eval|evaluate it using automated tests]].

## Related

- [[define-key-requirements|Define key requirements for an agentic workflow]]
- [[define-sec-controls-aw|Define security controls for an agentic workflow]]
- [[add-trigger-aw|Add a trigger to an agentic workflow]]
- [[channels-access-aw|Select channels and access for an agentic workflow]]
- [[clone-aia-usecase|Duplicate an agentic workflow]]
- [[version-control|Version control for AI agents and agentic workflows]]
- [[aia-security-implementation|Implement access control in Now Assist AI agents]]
- [[gg-creating-aia|General guidelines for creating AI agents and agentic workflows]]
- [[test-aia-use-case|Manually test the execution of an agentic workflow]]
- [[test-aw-access|Test user access to an agentic workflow]]
- [[execute-aia-eval|Execute an agentic evaluation run]]
- [[ai-agent-studio|AI Agent Studio]]
- [[platform-now-assist-landing|Now Assist]]
