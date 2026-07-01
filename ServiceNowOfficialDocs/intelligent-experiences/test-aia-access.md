---
title: Test user access to an AI agent
description: Run a manual test to verify that only the users you want to access the AI agent can do so.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/test-aia-access.html
release: australia
topic_type: task
last_updated: "2025-11-13"
reading_time_minutes: 3
breadcrumb: [Create an AI agent, Now Assist AI agents, Enable AI experiences]
---

# Test user access to an AI agent

Run a manual test to verify that only the users you want to access the AI agent can do so.

## Before you begin

Role required: sn\_aia.admin and either admin or at least one role required by the ACL of the AI agent being testing and each of the ACLs of its downstream components

## About this task

You can establish the security settings for an AI agent in the guided setup to establish which users can access it. See [[define-sec-controls-aia|Define security controls]] for instructions on how to change the user access settings. When you select **Save and continue** on that step of the guided setup, an ACL is created that establishes limitations on which users can access the AI agent.

Once you have created these ACLs, you can verify that they work as intended by using the **Test access** test type of a manual test of an AI agent.

To see instructions for performing manual tests to evaluate performance, see [[test-ai-agent|Test performance manually]]. For more information about automated tests, see [[execute-aia-eval|Evaluate an AI agent]].

## Procedure

1.  Navigate to **All** &gt; **[[ai-agent-studio|AI Agent Studio]]** &gt; **Testing**.

2.  Select **Start manual test**.

3.  In the **Choose a test type** drop-down menu, select **Test access**.

    If you want to test the basics of how an AI agent works, select **AI agent or worfklow**. The full instructions for that test type can be found in [Test performance manually](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/test-ai-agent.md).

4.  Search for or select the name of the AI agent you want to test.

5.  Select an invoking user.

    The invoking user can be the user that triggers the AI agent or it can be the invoking user of an upstream component, such as an agentic workflow. For more information about how the invoking user works, see [[aia-security-implementation|Security for AI agents]].

    When you select an invoking user, the user roles are populated in the **Invoking user roles** field. The field is read-only. If you want to change a user's roles, you must change the user's User record. See [Assign a role to a user](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_AssignARoleToAUser.md).

6.  Select **Test access**.

    \[Omitted image "aia-test-access-form.png"\] Alt text: Completed test form for a test access test type


## Result

The results of the access test are opened in the Access Analyzer in a new browser tab.

Access Analyzer identifies all the ACL calls made in the execution of the AI agent, including its tools, if any are present. You can see the results of each ACL to verify that each one has the correct user access defined.

## What to do next

If the results are different than what you expect or want, you can [redefine the security controls](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/define-sec-controls-aia.md) of the AI agent.

You can also [[test-ai-agent-mcp|test an AI agent]]'s performance with either a manual test or automated evaluations. See [Test performance manually](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/test-ai-agent.md) or [Evaluate an AI agent](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/execute-aia-eval.md).

## Related

- [[define-sec-controls-aia|Define security controls for an AI agent]]
- [[test-ai-agent|Manually test the execution of an AI agent]]
- [[execute-aia-eval|Execute an agentic evaluation run]]
- [[aia-security-implementation|Implement access control in Now Assist AI agents]]
- [[ai-agent-studio|AI Agent Studio]]
- [[test-ai-agent-mcp|Test an AI agent]]
