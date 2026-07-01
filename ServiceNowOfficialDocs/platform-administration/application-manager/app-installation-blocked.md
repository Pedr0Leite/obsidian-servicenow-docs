---
title: App installation blocked when installing or updating Now Assist Suite
description: Unlicensed applications can block the installation or update of Now Assist Suites.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/application-manager/app-installation-blocked.html
release: australia
product: Application Manager
classification: application-manager
topic_type: topic
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Application Manager, Administering applications, Get started, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - app-manager
  - plugins
  - activation
  - governance
  - type-topic
---

# App installation blocked when installing or updating Now Assist Suite

Unlicensed applications can block the installation or update of Now Assist Suites.

## Symptom

When attempting to update or install a Now Assist application, another application that is part of the same Now Assist Suite displays an "Installation blocked" indicator in the [[installation-details|installation details]]. The update or installation can't be completed.

\[Omitted image "app-mgr-installation-blocked.png"\] Alt text: The installation details for Now Assist for Customer Service Management show "Installation blocked" next to Flow Generation version 28.2.5. The option to Continue installing Now Assist for Customer Service Management is inactive.

## Cause

The application version that displays "Installation blocked" isn't licensed.

## Resolution: License the required application version

## Procedure

1.  If your organization uses the application, license the version required for the Now Assist Suite installation.

    To license the necessary application version, contact your account executive or request the license through the [[servicenow-store|ServiceNow Store]]. For more information about licensing applications through the ServiceNow Store, see [[buy-servicenow-app|Buy a ServiceNow application]].


## Resolution: Uninstall the application

## Procedure

1.  If your organization doesn't use the application that blocks installation, uninstall it through the [[application-manager|Application Manager]].

    For more information about [[uninstalling-apps-app-manager|uninstalling applications]], see [Uninstall an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/application-manager/uninstall-application-app-mgr.md).


**Parent Topic:**[Application Manager reference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/application-manager/app-mgr-reference.md)

## Related

- [[buy-servicenow-app|Buy a ServiceNow application]]
- [[installation-details|Installation details]]
- [[servicenow-store|ServiceNow Store]]
- [[application-manager|Application Manager]]
- [[uninstalling-apps-app-manager|Uninstalling applications]]
