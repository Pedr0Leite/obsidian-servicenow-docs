---
title: Activate a supported Microsoft SCCM plugin
description: The SCCM plugins can be activated by an administrator and requires the Integration - JDBC and CI Identification plugins. These dependent plugins are activated automatically with SCCM activation.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/activate-microsoft-sccm-plugin.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Microsoft SCCM integration, ServiceNow provided integrations, Integration options, Integration with third-party applications and data sources, Integrations, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Activate a supported Microsoft SCCM plugin

The SCCM plugins can be activated by an administrator and requires the Integration - JDBC and CI Identification plugins. These dependent plugins are activated automatically with SCCM activation.

## Before you begin

For a complete listing of the plugins that need to be activated, see [[activate-ai-scheduled-imports|Activate SCCM Asset Intelligence scheduled imports]].

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the plugin using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [[find-components|Find components installed with an application]].


**Parent Topic:**[[c_MicrosoftSCCMIntegration|Microsoft SCCM integration]]

## Related

- [[activate-ai-scheduled-imports|Activate SCCM Asset Intelligence scheduled imports]]
- [[find-components|Find components installed with an application]]
- [[c_MicrosoftSCCMIntegration|Microsoft SCCM integration]]
