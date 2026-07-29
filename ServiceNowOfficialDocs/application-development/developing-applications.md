---
title: Developing your application
description: Build a custom application to meet the business needs of your organization. Choose a builder for the type of user experience or workflow that you want to create.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/developing-applications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Building applications]
tags:
  - application-development
  - type-concept
---

# Developing your application

Build a custom application to meet the business needs of your organization. Choose a builder for the type of user experience or workflow that you want to create.

<table id="table_y5t_rg5_gbc" class="nav-card"><tbody><tr><td>

[Vibe coding and AI app development \[Omitted image "bus-ai-sparkle.svg"\] Alt text: Expedite app development, enhance custom applications with AI, and vibe code using the generative and agentic AI capabilities available on the ServiceNow AI Platform.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/use-ai-capabilities-in-custom-apps.md)

</td><td>

[Build no-code applications with [[creator-studio-landing|Creator Studio]]\[Omitted image "bus-automated-testing-framework.svg"\] Alt text: Create and manage custom applications in a simple, no-code environment.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/building-no-code-applications.md)

</td><td>

[Build low-code applications with App Engine \[Omitted image "bus-low-code-dev-tools.svg"\] Alt text: Accelerate innovation with more creators and less complexity. Empower developers of all skill levels to build applications at scale.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/building-low-code-applications-with-app-engine.md)

</td></tr><tr><td>

[Build applications with [[servicenow-studio-landing|ServiceNow Studio]] \[Omitted image "bus-application-development.svg"\] Alt text: Empower developers with a modern, unified environment for building on the ServiceNow AI Platform using integrated builders and tools.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/servicenow-studio-landing.md)

</td><td>

[Build pro-code applications \[Omitted image "bus-application-development.svg"\] Alt text: Extend or maintain existing applications and user experiences. Connect applications and data across the enterprise.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/building-pro-code-applications.md)

</td><td>

[Builder library \[Omitted image "bus-agent-workspace-1.svg"\] Alt text: Choose a builder tool to quickly develop an application.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/builder-library-table.md)

</td></tr></tbody>
</table>## Which app builder should I use?

Use the following table to choose the app building experience that matches your role and technical background.

<table id="app-builders-table"><thead><tr><th>

Tool

</th><th>

Users

</th><th>

Features

</th></tr></thead><tbody><tr><td>

Creator Studio: Build an app without code.

</td><td>

Process owners, line of business owners

</td><td>

Build request-fulfillment apps without writing code. For example, create an application to request office supplies: a user fills out a form, and an approver accepts or denies the request. For more information, see [Exploring Creator Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/creator-studio/exploring-creator-studio.md).

</td></tr><tr><td>

App Engine Studio: Build a range of apps using low-code tools.

</td><td>

Citizen developers

</td><td>

Build a broader range of apps than Creator Studio without writing code.For more information, see [Exploring App Engine Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/app-engine-studio/exploring-aes.md).

</td></tr><tr><td>

ServiceNow Studio: Build and deliver apps in a unified environment.

</td><td>

Citizen developers, Platform developers

</td><td>

Build apps in a unified development environment.ServiceNow Studio provides streamlined navigation, integrated low-code tools, and built-in tracking and packaging so you can develop and ship apps faster. [[use-build-agent|Use Build Agent]] in ServiceNow Studio to create and update apps with a conversational interaction.

For more information, see [Exploring ServiceNow Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/exploring-servicenow-studio.md)and [Build Agent in ServiceNow Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/build-agent-in-servicenow-studio.md).

</td></tr><tr><td>

[[servicenow-ide-landing|ServiceNow IDE]] and [[servicenow-sdk-landing|ServiceNow SDK]]: Build apps in source code.

</td><td>

Source code developers

</td><td>

Develop applications in source code with [[servicenow-fluent|ServiceNow Fluent]], create JavaScript modules, and use third-party libraries. ServiceNow Fluent is a domain-specific programming language for creating application metadata in code. Use Build Agent in ServiceNow IDE to create and update apps in source code with a conversational interaction.The ServiceNow IDE runs Visual Studio Code for the Web on the ServiceNow AI Platform. The ServiceNow SDK runs Visual Studio Code Desktop locally. For more information, see [[building-applications-source-code|Building applications in source code]].

</td></tr></tbody>
</table>## [[dev-get-start-vibe-coding|Vibe coding]] and AI app development on the ServiceNow AI Platform

-   **[[build-agent|Vibe code full-stack applications with Build Agent]]**

    Vibe code on the ServiceNow AI Platform with Build Agent, an autonomous AI agent available with [[now-assist-for-creator-landing|Now Assist for Creator]]. Describe what you need through back and forth conversations with Build Agent, and Build Agent automatically builds the application, including audit trails, security, and compliance.

-   **[Generate apps in ServiceNow Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/now-assist-for-creator/sns-app-gen-using-landing.md)**

    Use the [[sns-now-assist-app-gen-landing|app generation]] skill available with Now Assist for Creator to generate an application in ServiceNow Studio. Describe the app that you want to create and continue the conversation to refine and edit the app further.

-   **[Leverage AI assets in custom apps at runtime with Now Assist for App Engine](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/now-assist-for-app-engine/use-now-assist-for-app-engine-enterprise.md)**

    Enhance App Engine applications with AI agents, skill, and agentic workflows that users can leverage at runtime with [[add-ai-to-custom-apps-with-now-assist-for-app-engine-enterprise|Now Assist for App Engine]].

-   **[Generate code with AI-powered code generation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/scripts/generate-scripts-from-text.md)**

    Generate scripts from text, code, or a combination of both with AI-powered code generation.


## Build no-code applications with Creator Studio

-   **[Create applications without coding](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/creator-studio/creator-studio-landing.md)**

    Build request-fulfill applications in a simple environment, without using code, in Creator Studio.


## Build low-code applications with App Engine

Build low-code apps quickly, with more creators and less complexity. Safely scale cross-enterprise experiences that users want.

-   **[Empower creators](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/app-engine-studio/use-app-template.md)**

    Bring creator workflow apps to production quickly for mission-critical tasks. Design with guidance and templates that are all within a holistic low-code dev experience​.

-   **[Scale low-code development](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/app-engine-management-center/manage-collaboration-requests.md)**

    Empower business and IT to collaborate, manage, and govern low-code app development.​  Set development guardrails, apply standards, and check for compliance, all in one place.

-   **[Engage your users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/mab-concept.md)**

    Captivate users with a modern unified experience that’s easy to understand. Build mobile-first experiences using an intuitive, low-code designer.


## Build applications with the new ServiceNow Studio

Build apps smarter and deliver them faster with the new ServiceNow Studio. ServiceNow Studio empowers platform developers with a modern, unified environment for building on the ServiceNow AI Platform. ServiceNow Studio features streamlined navigation to applications and metadata, integrated low-code tools, efficient tracking and packaging of development work that accelerates development processes and enhances productivity.

-   **[ServiceNow Studio quick start](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/servicenow-studio-quick-start.md)**

    Quickly familiarize yourself with new features in ServiceNow Studio.

-   **[Build applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/create-an-application-in-servicenow-studio.md)**

    Admins can easily build custom or global apps using a guided experience and integrated builders.

-   **[Deploy applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/working-with-update-sets-in-servicenow-studio.md)**

    Deploy your applications seamlessly using update sets, pipelines, or the Application Repository.

-   **[ServiceNow Studio Navigator panel taxonomy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/servicenow-studio-file-navigator-taxonomy.md)**

    Learn more about each type of file you can add to [[working-with-apps-in-servicenow-studio|applications in ServiceNow Studio]].


## Build pro-code applications

Build and deploy apps with fine-grained control. Debug code, manage source control, and publish your apps from a central hub.

-   **[[building-pro-code-applications|Build your apps faster]]**

    Get all your work done in one place, accelerating the process from coding to [[get-started-deployment|deployment]].

-   **[Develop applications in source code](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/building-applications-source-code.md)**

    Write code that defines application metadata in an integrated development environment.

-   **[Work as a team](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/team-development/team-development-landing.md)**

    Provide individual developer access to specific application resources for better collaboration.


## Develop in sandbox environments

Use [[sandboxes-landing|Developer Sandboxes]] to create isolated development environments where users can develop on the ServiceNow AI Platform in parallel. Sandboxes help enhance Git-based workflows of the software development life cycle by reducing conflicts and enabling faster time to production.

## Builder library

Each builder fulfills a specific need or produces a specific type of data, such as Decision Builder, [[ui-builder-overview|UI Builder]], and [[workspace-builder-landing|Workspace Builder]]. For a complete list of builders, see [[builder-library-table|Builder Library]].

## Related

- [[building-applications-source-code|Building applications in source code]]
- [[build-agent|Build Agent]]
- [[building-pro-code-applications|Building pro-code applications]]
- [[builder-library-table|Builder library]]
- [[creator-studio-landing|Creator Studio]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[use-build-agent|Use Build Agent]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[servicenow-sdk-landing|ServiceNow SDK]]
- [[servicenow-fluent|ServiceNow Fluent]]
- [[dev-get-start-vibe-coding|Vibe coding]]
- [[now-assist-for-creator-landing|Now Assist for Creator]]
- [[sns-now-assist-app-gen-landing|App generation]]
- [[add-ai-to-custom-apps-with-now-assist-for-app-engine-enterprise|Now Assist for App Engine]]
- [[working-with-apps-in-servicenow-studio|Applications in ServiceNow Studio]]
- [[get-started-deployment|Deployment]]
- [[sandboxes-landing|Developer Sandboxes]]
- [[ui-builder-overview|UI Builder]]
- [[workspace-builder-landing|Workspace Builder]]
