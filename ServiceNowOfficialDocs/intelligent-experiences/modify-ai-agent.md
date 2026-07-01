---
title: Modify an AI agent
description: Modify an AI agent in AI Agent Studio to suit your changing business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/modify-ai-agent.html
release: australia
topic_type: task
last_updated: "2025-11-18"
reading_time_minutes: 3
breadcrumb: [Create an AI agent, Now Assist AI agents, Enable AI experiences]
---

# Modify an AI agent

Modify an AI agent in [[ai-agent-studio|AI Agent Studio]] to suit your changing business needs.

## Before you begin

Role required: sns\_aia.admin

## Procedure

1.  Navigate to **All** &gt; **AI Agent Studio** &gt; **Create and manage** &gt; **AI agents**

2.  Select the AI agent that you want to modify.

3.  Modify the fields of the different sections of the Guided Setup, making changes to the fields for your requirements.

    The guided setup is the same as the one for creating an AI agent:

    -   [[define-specialty|Define the AI agent's specialty]].
    -   [[define-sec-controls-aia|Define the AI agent security controls]].
    -   [[add-trigger-aia|\(Optional\) Add a trigger to automatically invoke your AI agent if a specified event occurs.]].
    -   [[channels-access-aia|Determine whether you want to use the Now Assist in Virtual Agent chat assistants and/or as UI action, set the processing messages, and activate your AI agent.]].
    **Note:** Some fields aren't editable if the agent is associated with a [[platform-now-assist-landing|Now Assist]] application. If you want to make more modifications, [[clone-aia-usecase|duplicate the agentic workflow]] and make changes to the duplicate.

    -   For the **List of steps** field in the **Define specialty** step, you can create multiple versions of the same AI agent without losing previous versions. Creating versions enables you to test different instructions to evaluate performance. See [[version-control|Version control for AI agents and agentic workflows]] for more information.
    -   For more guidance on creating effective instructions, see the [[gg-creating-aia|general guidelines for creating AI agents and agentic workflows]].
    -   For the access control lists \(ACLs\), you can edit the security fields and define who can access the AI agent and edit the entity to run the AI agent as a dynamic user or an AI user. For more information, see [[aia-security-implementation|Implement access control in Now Assist AI agents]].
    You can navigate through the steps of the Guided Setup with the **Continue** and **Back** buttons.

4.  Navigate to the last step and select **Test** to save your changes and begin testing your modified agent.


## Result

Your agent is modified and ready to test.

## What to do next

You can [[test-ai-agent|test an execution of your AI agent manually]] or [[test-aia-access|test the user access]]. Once you've determined that the AI agent has the basic functionality you expect, you can [[execute-aia-eval|evaluate the AI agent using automated tests]].

## Related

- [[define-specialty|Define the specialty of an AI agent]]
- [[define-sec-controls-aia|Define security controls for an AI agent]]
- [[add-trigger-aia|Add a trigger to an AI agent]]
- [[channels-access-aia|Select channels and status for an AI agent]]
- [[clone-aia-usecase|Duplicate an agentic workflow]]
- [[version-control|Version control for AI agents and agentic workflows]]
- [[gg-creating-aia|General guidelines for creating AI agents and agentic workflows]]
- [[aia-security-implementation|Implement access control in Now Assist AI agents]]
- [[test-ai-agent|Manually test the execution of an AI agent]]
- [[test-aia-access|Test user access to an AI agent]]
- [[execute-aia-eval|Execute an agentic evaluation run]]
- [[ai-agent-studio|AI Agent Studio]]
- [[platform-now-assist-landing|Now Assist]]
