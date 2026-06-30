---
title: Agentic development app refinement in ServiceNow Studio
description: ServiceNow Studio connects AI-generated apps to enterprise-grade solutions, where you can review, edit, and enhance your application in a dedicated development environment.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/vc-refine-sns.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [ServiceNow Studio, vibe coding, Build Agent, AI-assisted development, application development, developer tools, code refinement, metadata editing, Automated Test Framework, ATF, application files, access control lists, ACL, record producers, update sets]
audience: developer
breadcrumb: [Build Agent overview, Develop, Agentic development, Agentic development on the ServiceNow AI Platform, Building applications]
---

# Agentic development app refinement in ServiceNow Studio

[[servicenow-studio-landing|ServiceNow Studio]] connects AI-generated apps to enterprise-grade solutions, where you can review, edit, and enhance your application in a dedicated development environment.

After developing an application agentically with [[build-agent|Build Agent]] or [[now-assist-for-creator-landing|Now Assist for Creator]], ServiceNow Studio provides a powerful, developer-friendly environment for reviewing, customizing, and perfecting your app.

If you're a developer who's new to agentic development, ServiceNow Studio provides a more abstracted approach to code refinement compared to [[servicenow-ide-landing|ServiceNow IDE]].

For documentation on using [[build-agent-in-servicenow-studio|Build Agent in ServiceNow Studio]], see [Build Agent in ServiceNow Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/build-agent-in-servicenow-studio.md).

## ServiceNow Studio workflow

To review and refine your app from Build Agent in ServiceNow Studio, follow these steps:

1.  Open your app in ServiceNow Studio.

2.  [[use-build-agent|Use Build Agent]] to create or edit metadata for your application.
3.  Review and edit [[c_ApplicationFiles|application files]].

    -   Use the **Application Files** tab to see all generated elements and metadata—tables, access controls, roles, record producers, and more.
    -   Open any file \(such as a table or ACL\) in a new tab for detailed inspection and editing.
    -   Confirm that generated tables capture the correct data and adjust field [[atf-admin-properties|properties]] as needed.
    -   Edit access control lists \(ACLs\) to confirm that the correct roles and permissions are applied.
    -   Review and modify roles, record producers, and other artifacts for accuracy.
4.  Use developer tools in ServiceNow Studio.

    -   ServiceNow Studio provides a tabbed, IDE-like interface for navigation and editing.
    -   You can refine code, add business logic, and manage metadata across your app's scope.
    -   Use Build Agent for update set management, cross-scope editing, and safe [[get-started-deployment|deployment]].
5.  Iterate with Build Agent.

    -   Use the Build Agent panel to edit metadata for your application.
    -   Toggle the panel as needed to avoid covering important information.
6.  Test and validate the app.

    -   Use Build Agent to create and run [[atf-landing-page|Automated Test Framework \(ATF\)]] [[tests-module|tests]].
    -   Verify that your refined app functions correctly.

## When to choose the ServiceNow IDE or ServiceNow Studio

1.  ServiceNow IDE: Best for file‑centric, code‑heavy edits, rapid iteration, and pairing with the [[servicenow-sdk-landing|ServiceNow SDK]] for local dev/CI. Suitable for developers familiar with the ServiceNow AI Platform.
2.  ServiceNow Studio: Best for metadata‑centric review \(tables, ACLs, roles\) and cross‑scope editing with a visual overview of app artifacts; keeps Now Assist in‑context for conversational adjustments. Suitable for developers with various levels of experience on the ServiceNow AI Platform.

**Parent Topic:**[[vc-build-agent-landing|AI-assisted ServiceNow AI Platform development with Build Agent]]

## Related

- [[vc-build-agent-landing|AI-assisted ServiceNow AI Platform development with Build Agent]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[build-agent|Build Agent]]
- [[now-assist-for-creator-landing|Now Assist for Creator]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[build-agent-in-servicenow-studio|Build Agent in ServiceNow Studio]]
- [[use-build-agent|Use Build Agent]]
- [[c_ApplicationFiles|Application files]]
- [[atf-admin-properties|Properties]]
- [[get-started-deployment|Deployment]]
- [[atf-landing-page|Automated Test Framework \(ATF\)]]
- [[tests-module|Tests]]
- [[servicenow-sdk-landing|ServiceNow SDK]]
