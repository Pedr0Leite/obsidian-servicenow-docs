---
title: Activate Field Service Multi-Day Task Scheduling
description: Install the Field Service Multi-Day Task Scheduling application to enable scheduling of work order tasks across multiple days. You can activate the Field Service Multi-Day Task Scheduling plugin \(com.snc.fsm\_multiday\_tasks\) for Field Service if you have the admin role. If the application does NOT include demo data or it does NOT install related applications and plugins, delete or revise the following sentence:
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/field-service-management/field-service-scheduling/install-multi-day-tasks.html
release: australia
product: Field Service Scheduling
classification: field-service-scheduling
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring Multi-day scheduling, Additional scheduling configuration options, Setting up a Field Service scheduling method, Configure, Field Service Management]
tags:
  - field-service-management
  - scheduling
  - territories
  - optimization
  - dispatch
  - type-task
---

# Activate Field Service Multi-Day Task Scheduling

Install the Field Service Multi-Day Task Scheduling application to enable scheduling of work order tasks across multiple days. You can activate the Field Service Multi-Day Task Scheduling plugin \(com.snc.fsm\_multiday\_tasks\) for Field Service if you have the admin role.

## Before you begin

-   Field Service Multi-Day Task Scheduling requires you to install the [[fsm-application-landing-page|Field Service Management]] plugin. For more information about activating Field Service Management, see [[t_ActivateFieldServiceManagement|Activate Field Service Management]].

Role required: admin.

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Field Service Multi-Day Task Scheduling plugin \(com.snc.fsm\_multiday\_tasks\) using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).


## Result

The Field Service Multi-Day Task Scheduling plugin when activated successfully adds the following attributes:

-   The **Assign across the schedule entries** option is added to the work order task form.
-   The **sn\_fsm\_multiday.minDurationForFirstWorkSchedule** property is added to the Field Service [[dynamic-scheduling|Dynamic Scheduling]] Properties page. For more information about enabling a dynamic scheduling property, see [[r_PropInstallWFieldServMgmnt|Properties installed with Field Service Management]].
-   The **sn\_fsm\_disp\_wrkspc.dispatcher\_workspace.enableTwoAndFourWeeks** property is added to the Field Service [[dispatcher-activities|Dispatcher Workspace]] set of properties. For more information about enabling a Workspace Settings property, see [[configure-workspce-settings|Configure settings for Dispatcher Workspace]].

## Related

- [[t_ActivateFieldServiceManagement|Activate Field Service Management]]
- [[r_PropInstallWFieldServMgmnt|Properties installed with Field Service Management]]
- [[configure-workspce-settings|Configure settings for Dispatcher Workspace]]
- [[fsm-application-landing-page|Field Service Management]]
- [[dynamic-scheduling|Dynamic scheduling]]
- [[dispatcher-activities|Dispatcher Workspace]]
