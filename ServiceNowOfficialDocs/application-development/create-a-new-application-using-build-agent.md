---
title: Create an application using Build Agent
description: Build custom ServiceNow applications by describing your requirements in plain language to Build Agent. The AI agent generates and builds the application code automatically.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/create-a-new-application-using-build-agent.html
release: australia
topic_type: task
last_updated: "2026-06-08"
reading_time_minutes: 5
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Use, Build Agent, Agentic development on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-task
---

# Create an application using Build Agent

Build custom ServiceNow applications by describing your requirements in plain language to [[build-agent|Build Agent]]. The AI agent generates and builds the application code automatically.

## Before you begin

You can watch a short video on how to create an application in Build Agent.

\[Omitted video\] Description: Create an application in Build Agent

Install and enable Build Agent. For more information, see [[install-build-agent|Install Build Agent]].

If you prefer to access in the [[servicenow-ide-landing|ServiceNow IDE]] instead of [[servicenow-studio-landing|ServiceNow Studio]], you must first create a workspace. For more information, see [Create a workspace in the ServiceNow IDE](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-ide-family-release/create-workspace-servicenow-ide.md).

**Note:** Build Agent requires [[servicenow-sdk-landing|ServiceNow SDK]] version 4.0 at a minimum. If you’re using an older version, Build Agent prompts you to upgrade to ServiceNow SDK 4.0.

For some prompting guidelines and ideas, see [[build-agent-example-prompts|Example prompts]].

Role required: admin

## About this task

A ServiceNow app is a package that performs a specific task for a specified group of users. Think of an app as a container with a set of rules around who can access and edit it. For example, ServiceNow apps can include an API, a table, a workspace, a form, a flow, or any combination of those things.

## Procedure

1.  Navigate to **All** &gt; **App Development** &gt; **ServiceNow Studio**.

    You can also open Build Agent in the ServiceNow IDE if you prefer a more code-centric experience.

    The Build Agent chat panel opens by default in new ServiceNow Studio sessions. If the panel isn't open, select **Open Build Agent** from the status bar in the lower corner of your browser. You can also select the Sparkle icon \[Omitted image "ba-sns-ai-sparkle.png"\] Alt text: in the application banner.

    \[Omitted image "sn-studio-access-build-agent.png"\] Alt text: If Build Agent isn't open, open it from the status bar in the corner of your browser.

2.  In the chat panel, describe the application that you want to create in plain language or select a prompt.

<table id="choicetable_qzh_hj2_lgc"><thead><tr><th align="left" id="d247918e233">

Scenario

</th><th align="left" id="d247918e236">

Actions

</th></tr></thead><tbody><tr><td id="d247918e242">

**Describe the app you want to create**

</td><td>

Describe the application that you want to create, and then select the Send icon\[Omitted image "ba-send-icon.png"\] Alt text:. For example:\[Omitted image "build-agent-describe-app.png"\] Alt text: Describe the application in a chat panel

You can also attach images, such as architectural diagrams or UI wireframes, to provide context for prompts.

</td></tr><tr><td id="d247918e263">

**Select a predetermined prompt**

</td><td>

1.  Select **[[app-tutorial-create-an-app|Create an app]]** from the [[c_ApplicationList|Application list]]. \[Omitted image "ba-create-app-1.png"\] Alt text: Welcome to Build Agent message
2.  Describe the application that you want to create, including as much context as possible, and then select the Send icon \[Omitted image "ba-send-icon.png"\]. For example, include roles, data requirements, and success criteria.


</td></tr></tbody>
</table>    After reviewing your requirements, Build Agent requests confirmation to proceed with creating the application.

3.  Instruct Build Agent to start developing the application by selecting **Approve plan**.

    Or, if you're not satisfied with the plan, tell Build Agent what you change, and continue to prompt until you have a plan you like.

    \[Omitted image "ba-create-app-2.png"\] Alt text: Implementation plan for Planner Tracker application

    Build Agent can access ServiceNow knowledge sources and tools, which enable it to learn, analyze, and then create applications.

    After creating the application, Build Agent builds the application.

    **Note:** You can preview the code files before approval. But to see the actual metadata output, you must build and install the application on the instance.

4.  If your application has a user interface, you can preview the app in a tab in ServiceNow Studio to inspect how it looks.

    You can keep prompting to refine the app, its appearance, and functionality. For more information, see [[edit-an-existing-application-using-build-agent|Edit an existing application using Build Agent]].


## Result

Review the application and its metadata in ServiceNow Studio using the change log. For more information, see [[ba-conversational-change-log|Build Agent conversation change log]]. You can also review the application using the File Navigator in ServiceNow Studio. For more information, see [Find an app or app file using the Navigator panel](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/qs-find-app-app-file-using-navigator-panel.md).

For information on deploying your application, see [[build-agent-deployment|Deploying what you built with Build Agent]].

For information on troubleshooting issues, see [[build-agent-troubleshooting|Common issues and solutions in Build Agent]].

After the application is built, Build Agent displays a success message. For example:

\[Omitted image "build-agent-success.png"\] Alt text: Build Agent success message

Build Agent displays the details of your app in the chat panel.

\[Omitted image "ba-create-app-3.png"\] Alt text: Planner Tracker application build summary

You can prompt Build Agent for details on how to access your new app.

\[Omitted image "ba-access-app.png"\] Alt text: Response with multiple methods to access the Planner Tracker app

If you want to view source code, open the ServiceNow IDE and select the **File Explorer** view from the Activity bar. The [[servicenow-fluent|ServiceNow Fluent]] application code and other source code in the `src` directory appears.

\[Omitted image "build-agent-file-explorer.png"\] Alt text: File Explorer showing project structure with folders and configuration files

**Parent Topic:**[[use-build-agent|Use Build Agent]]

## Related

- [[install-build-agent|Install Build Agent]]
- [[build-agent-example-prompts|Example prompts]]
- [[edit-an-existing-application-using-build-agent|Edit an existing application using Build Agent]]
- [[ba-conversational-change-log|Build Agent conversation change log]]
- [[build-agent-deployment|Deploying what you built with Build Agent]]
- [[build-agent-troubleshooting|Common issues and solutions in Build Agent]]
- [[use-build-agent|Use Build Agent]]
- [[build-agent|Build Agent]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[servicenow-sdk-landing|ServiceNow SDK]]
- [[app-tutorial-create-an-app|Create an app]]
- [[c_ApplicationList|Application list]]
- [[servicenow-fluent|ServiceNow Fluent]]
