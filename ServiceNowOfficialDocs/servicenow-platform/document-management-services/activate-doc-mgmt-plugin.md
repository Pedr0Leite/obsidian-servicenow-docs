---
title: Activate Document Management
description: Activate the Document Management plugin.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/document-management-services/activate-doc-mgmt-plugin.html
release: australia
product: Document Management Services
classification: document-management-services
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Document Management, Document Services, Manage content capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - documents
  - storage
  - dms
  - attachments
  - type-task
---

# Activate Document Management

Activate the [[doc-mgt-plugin|Document Management plugin]].

## Before you begin

Role required: admin

## About this task

The following items are installed with [[doc-management-landing|Document Management]]:

-   Roles
-   Tables

For more information, see[Components installed with Document Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/installed-with-doc-mgmt.md).

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Document Management plugin \(com.snc.platform\_document\_management\) using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When [[domain-separation-relationship-formatter-editor|domain separation]] and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Related

- [[doc-mgt-plugin|Document Management plugin]]
- [[doc-management-landing|Document Management]]
- [[domain-separation-relationship-formatter-editor|Domain separation]]
