---
title: Use Build Agent
description: Build Agent is an autonomous AI agent native to ServiceNow that translates plain language instructions into ready-to-deploy applications and metadata, using the platform’s domain language and guardrails. It's purpose-built for full-stack creation and editing across tables, flows, UI, and scripts, and it operates as the core engine for vibe coding and AI-assisted development on the ServiceNow AI Platform.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/use-build-agent.html
release: australia
topic_type: concept
last_updated: "2026-04-02"
reading_time_minutes: 3
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Build Agent, Agentic development on the ServiceNow AI Platform, Building applications]
---

# Use Build Agent

Build Agent is an autonomous AI agent native to ServiceNow that translates plain language instructions into ready-to-deploy applications and metadata, using the platform’s domain language and guardrails. It's purpose-built for full-stack creation and editing across tables, flows, UI, and scripts, and it operates as the core engine for [[dev-get-start-vibe-coding|vibe coding]] and AI-assisted development on the ServiceNow AI Platform.

Available in the [[servicenow-ide-landing|ServiceNow IDE]] and [[servicenow-studio-landing|ServiceNow Studio]], Build Agent appears as a chat panel with a multi-turn conversation interface. Build Agent processes natural language prompts, autonomously generates full-stack applications, manages the entire build process, and responds to feedback. The agent generates all necessary code, organizes files clearly, and manages both the core logic and user interface components of applications.

Build Agent supports the following development tasks:

-   Generate and edit enterprise-grade applications: Create full-stack ServiceNow applications from natural language prompts with enterprise-grade governance.
-   Accelerate development workflows: Support flow design, catalog item creation, and [[atf-landing-page|Automated Test Framework \(ATF\)]] test creation.
-   Enhance understanding: Explain how to best perform tasks on the ServiceNow AI Platform.
-   Perform diverse code tasks: Refactor tables, explain and document code, validate and enhance existing applications, fix errors, run queries, and more.
-   Support governance: Work inside platform scopes, roles, and testing workflows rather than as a detached external bot.
-   Enable developer learning: Answer ServiceNow development questions, summarize documents, and provide practical examples.

-   **[[access-build-agent|Accessing Build Agent in ServiceNow Studio and the ServiceNow IDE]]**  
Build Agent is available in ServiceNow Studio \(UI-first, declarative workflows\) and the ServiceNow IDE \(code-first, autonomous full-stack development\).
-   **[[create-a-new-application-using-build-agent|Create an application using Build Agent]]**  
Build custom ServiceNow applications by describing your requirements in plain language to Build Agent. The AI agent generates and builds the application code automatically.
-   **[[edit-an-existing-application-using-build-agent|Edit an existing application using Build Agent]]**  
Modify existing ServiceNow applications using natural language prompts with Build Agent.
-   **[[creating-or-updating-an-app-file|Creating or updating an app file with Build Agent]]**  
Use Build Agent to add new files or modify existing files in ServiceNow applications to assist with ongoing metadata and app development and maintenance.
-   **[[ba-about-creating-in-app-agents|Agentic workflows, agents, and skills]]**  
Build Agent can generate agentic workflows, agents, and skills scoped to your custom app. Turn business requirements into configured AI artifacts without building from scratch.
-   **[[create-custom-ai-agent|Create agentic workflows, agents, and skills]]**  
Build custom agentic workflows, AI agents, and skills for your applications using automated generation tools with Build Agent. You can streamline development by creating the necessary instructions, tools, and access controls based on your requirements.
-   **[[revert-app-changes-using-build-agent|Revert app changes with Build Agent]]**  
Restore your development to a previous state when you want to undo recent changes. Use checkpoints created during Build Agent conversations to revert both code and chat history.
-   **[[build-agent-testing|Testing what you built]]**  
[[test-agent-landing-page|Test Agent]] generates test coverage for code created by Build Agent, executes [[tests-module|tests]], and performs root cause analysis on failures. Prompt Test Agent to complete build-to-test workflows in a single development session without manual test authoring or failure investigation.
-   **[[ba-document-an-app|Document an application using Build Agent]]**  
Generate documentation for an application's structure, tables, and UI components. Build Agent reads the codebase and creates a README file describing the application architecture.
-   **[[ba-conversational-change-log|Build Agent conversation change log]]**  
After Build Agent completes the changes you request, you can find information about the updates in the change log that automatically appears in an integrated tab in ServiceNow Studio.
-   **[[ba-update-sets|Update sets and Build Agent]]**  
When you work with Build Agent, your changes are automatically tracked in update sets so you can review, revert, and deploy them without leaving ServiceNow Studio.
-   **[[build-agent-deployment|Deploying what you built with Build Agent]]**  
Learn about [[get-started-deployment|deployment]] methods and workflows for moving applications created with Build Agent from development to production environments. Choose the right deployment approach based on your application complexity and organizational requirements.
-   **[[build-agent-troubleshooting|Common issues and solutions in Build Agent]]**  
Identify and resolve common issues in Build Agent. Use this reference alongside the general debugging approach to identify and fix problems.

**Parent Topic:**[[build-agent|Build Agent]]

## Related

- [[access-build-agent|Accessing Build Agent in ServiceNow Studio and the ServiceNow IDE]]
- [[create-a-new-application-using-build-agent|Create an application using Build Agent]]
- [[edit-an-existing-application-using-build-agent|Edit an existing application using Build Agent]]
- [[creating-or-updating-an-app-file|Creating or updating an app file with Build Agent]]
- [[ba-about-creating-in-app-agents|Agentic workflows, agents, and skills]]
- [[create-custom-ai-agent|Create agentic workflows, agents, and skills]]
- [[revert-app-changes-using-build-agent|Revert app changes with Build Agent]]
- [[build-agent-testing|Testing what you built]]
- [[ba-document-an-app|Document an application using Build Agent]]
- [[ba-conversational-change-log|Build Agent conversation change log]]
- [[ba-update-sets|Update sets and Build Agent]]
- [[build-agent-deployment|Deploying what you built with Build Agent]]
- [[build-agent-troubleshooting|Common issues and solutions in Build Agent]]
- [[build-agent|Build Agent]]
- [[dev-get-start-vibe-coding|Vibe coding]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[atf-landing-page|Automated Test Framework \(ATF\)]]
- [[test-agent-landing-page|Test Agent]]
- [[tests-module|Tests]]
- [[get-started-deployment|Deployment]]
