---
title: Configure AI Desktop Actions
description: You can enable the AI Desktop Actions application if you have the admin role.If the application does NOT include demo data or it does NOT install related applications and plugins, delete or revise the following sentence:
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/configure-agentic-desktop.html
release: australia
topic_type: task
last_updated: "2025-11-02"
reading_time_minutes: 1
breadcrumb: [AI Desktop Actions, Enable AI experiences]
---

# Configure AI Desktop Actions

You can enable the [[agentic-desktop-landing-page|AI Desktop Actions]] application if you have the admin role.

## Before you begin

To get started with AI Desktop Actions, you must have:

-   A ServiceNow Pro Plus or Enterprise Plus license.
-   An instance on Zurich Patch 4+.
-   A .NET 9.0 runtime v9.0.10 and .NET 9 Desktop Runtime v9.0.10 is installed.

Role required: administrator

## About this task

AI Desktop Actions isn’t a standalone application that you can install directly. To enable AI Desktop Actions on your instance, you must install other [[platform-now-assist-landing|Now Assist]] applications, such as Now Assist for IT Service Management \(ITSM\) or Now Assist for Customer Service Management \(CSM\).

-   Review the [AI Desktop Actions](https://store.servicenow.com/store/app/dc9057f4873932d0221e8409dabb35a5) application listing in ServiceNow Store for information on dependencies, licensing or subscription requirements, and release compatibility.
-   Perform these steps in your ServiceNow instance.

For more information about the components installed, see [[components-installed-with-agentic-desktop|Components installed with AI Desktop Actions]].

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Plugins**.

2.  Search for and select a Now Assist application, such as Now Assist for IT Service Management \(ITSM\) or Now Assist for Platform.

3.  Select **Install**.


## What to do next

-   **Defined desktop action**

    Download and install the AI Desktop Actions installer on your system to automate repetitive tasks that involve fixed steps in your desktop and web environment. For more information, see [[download-agentic-desktop-installer|Download AI Desktop Actions installer]].

-   **Adaptive desktop action**

    Install the Chrome browser extension and configure allowed websites to automate repetitive tasks that involve adaptive steps for web applications. For more information, see [[na-ai-wa-install-browser-extension|Install the Google Chrome extension for adaptive desktop actions]] and [[na-ai-wa-configure-allowed-websites|Configure allowed websites for adaptive desktop actions]].

## Related

- [[components-installed-with-agentic-desktop|Components installed with AI Desktop Actions]]
- [[download-agentic-desktop-installer|Download AI Desktop Actions installer]]
- [[na-ai-wa-install-browser-extension|Install the Google Chrome extension for adaptive desktop actions]]
- [[na-ai-wa-configure-allowed-websites|Configure allowed websites for adaptive desktop actions]]
- [[agentic-desktop-landing-page|AI Desktop Actions]]
- [[platform-now-assist-landing|Now Assist]]
