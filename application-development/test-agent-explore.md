---
title: Exploring Test Agent
description: Test Agent autonomously manages end‑to‑end test authoring, execution, and troubleshooting from a single prompt.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/test-agent-explore.html
release: australia
topic_type: concept
last_updated: "2026-04-21"
reading_time_minutes: 1
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Test Agent, Agentic development on the ServiceNow AI Platform, Building applications]
---

# Exploring Test Agent

[[test-agent-landing-page|Test Agent]] autonomously manages end‑to‑end test authoring, execution, and troubleshooting from a single prompt.

## Test Agent overview

By extending [[build-agent|Build Agent]], Test Agent uses the same prompt and code context to generate unit and functional ATF [[tests-module|tests]], run the tests, and automatically triage failures.

\[Omitted image "test-agent-new.gif"\] Alt text: Gif showing test agent

Test Agent delivers the following measurable outcomes:

-   Build and test together: Author code and generate tests sequentially in a single Build Agent session.
-   Faster failure resolution: Automated root cause analysis and recommended fixes reduce test failure investigation time. When a test fails, Test Agent performs root cause analysis and either automatically applies safe fixes or provides actionable guidance in the chat panel, enabling issue resolution without leaving the [[servicenow-ide-landing|ServiceNow IDE]].
-   Greater release confidence: Automated tests enforce quality gates and validate code health before promoting to production.
-   Seamless test reuse and execution: All generated ATF tests are stored in the standard sys\_atf\_tests table within the target [[c_ApplicationScope|application scope]] and can be reused to schedule and run regression tests, just like manually authored ATF tests.

## Test Agent users

AI agents use [role masking](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/aia-role-masking.md) to determine which users can access them. Ones installed with Now Assist applications have specific roles that come included with the application. If you select **Users with specific roles** for user access, you must configure the security controls to include these roles. For the instructions to change the security controls, see [Define security controls for an AI agent](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/define-sec-controls-aia.md).

Test Agent has the following users.

|Users|Description|
|-----|-----------|
|admin|This role is required to access Test Agent and its capabilities.|

## Test Agent benefits

|Benefit|Feature|Users|
|-------|-------|-----|
|One-stop shop experience|[[test-agent-use|Author, execute, and troubleshoot tests with Test Agent]]|admin|

## What to explore next

To learn more about configuring and using Test Agent, see:

-   [[test-agent-access|Test Agent access]]
-   [Author, execute, and troubleshoot tests with Test Agent](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/test-agent-use.md)
-   [[test-agent-exceptions|Test Agent guidelines]]

## Related

- [[test-agent-use|Author, execute, and troubleshoot tests with Test Agent]]
- [[test-agent-access|Test Agent access]]
- [[test-agent-exceptions|Test Agent guidelines]]
- [[test-agent-landing-page|Test Agent]]
- [[build-agent|Build Agent]]
- [[tests-module|Tests]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[c_ApplicationScope|Application scope]]
