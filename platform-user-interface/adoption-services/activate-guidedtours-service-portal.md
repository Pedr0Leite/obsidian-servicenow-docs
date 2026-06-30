---
title: Enable Guided Tours
description: Enable guided tours for Standard platform UI, Workspace, Service Portal pages, and Custom UI.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/adoption-services/activate-guidedtours-service-portal.html
release: australia
product: Adoption Services
classification: adoption-services
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure Guided Tours, Guided Tours, Adoption services, Configure user experiences]
---

# Enable Guided Tours

Enable guided tours for Standard platform UI, Workspace, [[c_ServicePortal|Service Portal]] pages, and Custom UI.

## Before you begin

Role required: admin

## Procedure

1.  In the application navigator, enter `sys_properties.list` and press the Enter key.

2.  From the System Properties list, find the following properties and make sure that their values are set to **True**.

    |Property|Description|
    |--------|-----------|
    |com.snc.guided\_tours.standard\_ui.enable|Enables [[guided-tours|guided tours]] across your instance to run on the Standard platform UI and Workspace.|
    |com.snc.guided\_tours.sp.enable|Enables guided tours across your instance to run on Service Portal pages.|
    |com.snc.guided\_tours.custom\_ui.enable|Enables guided tours across your instance to run on the Custom UI pages.|

3.  If the values of the system properties aren’t set to true, change them to **True**.


## Result

You can create, update, and play guided tours within the ServiceNow® user interface.

**Note:**

-   The [[guided-tours-designer|Guided Tour Designer]] is only available in [[c_UI16|Core UI]]. The designer isn’t compatible with UI15. For information about how to activate the Core UI plugin, see [[t_ActivateUI16|Activate Core UI]].

-   Guided Tours are supported in Next Experience pages, such as Workspace or pages configured in UI Builder using the Next Experience UI Framework.

    Set the value of the system property `com.snc.guided_tours.standard_ui.enable` to **True** to enable Guided Tours under Next Experience. The following scenarios are still supported with Next Experience enabled:

    -   Creating and running new or existing Guided Tours in the Classic Environment \(including [[lists-configurable-workspace|lists]] and [[form-configurable-workspace|forms]]\).
    -   Creating and running new or existing Guided Tours for a Service Portal.
    -   Creating new Guided Tours for Unified Navigation menus \(such as the **All** or **Favorites** menus\).
    For more information, see [[next-experience-landing-page|Next Experience]]


**Parent Topic:**[Configuring Guided Tours](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/adoption-services/configure-guided-tours.md)

## Related

- [[t_ActivateUI16|Activate Core UI]]
- [[next-experience-landing-page|Next Experience UI]]
- [[c_ServicePortal|Service Portal]]
- [[guided-tours|Guided Tours]]
- [[guided-tours-designer|Guided Tour Designer]]
- [[c_UI16|Core UI]]
- [[lists-configurable-workspace|Lists]]
- [[form-configurable-workspace|Forms]]
