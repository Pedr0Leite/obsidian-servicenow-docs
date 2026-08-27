---
title: Client API reference
description: Use client-side JavaScript APIs to control aspects of how ServiceNow AI Platform is displayed and functions within the web browser. This reference lists available classes and methods along with parameters, descriptions, and examples to help control the end-user experience.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/api-reference/api-client.html
release: australia
product: API Reference
classification: api-reference
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [API reference, API implementation and reference]
tags:
  - api-reference
  - type-concept
---

# Client API reference

Use client-side JavaScript APIs to control aspects of how ServiceNow AI Platform is displayed and functions within the web browser. This reference lists available classes and methods along with parameters, descriptions, and examples to help control the end-user experience.

-   **[[StandaloneClientMethods|StandaloneClientMethods]]**  
Standalone client methods are methods that you can use within your client JavaScripts, such as reflistOpen, but aren't a part of any class or API.
-   **[[DynamicTranslationClientAPI|DynamicTranslation - Client]]**  
The DynamicTranslation API provides methods that translate text, in real time, into multiple languages using translation service providers. This API is available for both standard clients and Angular-based Service Portal clients.
-   **[[g_service_catalogClientAPI|g\_service\_catalog - Client]]**  
The g\_service\_catalog API provides methods to access data in a multi-row variable set \(MRVS\) when a model is open.
-   **[[GlideAgentWorkspaceAPI|GlideAgentWorkspace \(g\_aw\) - Client]]**  
The g\_aw API provides methods that enable a UI action or client script to open a specified record in an Agent Workspace tab.
-   **[[c_GlideAjaxAPI|GlideAjax - Client]]**  
The GlideAjax class enables a client script to call server-side code in a script include.
-   **[[c_GlideDialogWindowAPI|GlideDialogWindow - Client \(deprecated\)]]**  
The GlideDialogWindow API provides methods for displaying a dialog in the current window and frame.
-   **[[c_GlideDocumentV3API|GlideDocument - Client]]**  
The GlideDocument API provides methods to search a Document Object Model \(DOM\) element, a document, or a JQuery element.
-   **[[GlideFlowAPI|GlideFlow - Client]]**  
The GlideFlow API provides methods for client-side interactions with actions, flows, and subflows.
-   **[[c_GlideFormAPI|GlideForm \(g\_form\) - Client]]**  
The GlideForm API provides methods to customize forms.
-   **[[c_MobileGlideForm_API|Mobile GlideForm \(g\_form\) - Client]]**  
The Mobile GlideForm \(g\_form\) API provides methods to work with forms on the mobile platform.
-   **[[c_GlideGuidV3API|GlideGuid - Client]]**  
The GlideGuid API provides methods to create a globally unique identifier.
-   **[[c_GlideList2API|GlideList2 \(g\_list\) - Client]]**  
The GlideList2 API provides methods to customize \(v2\) lists.
-   **[[c_GlideListV3API|GlideListV3 \(g\_list\) - Client \(deprecated\)]]**  
The GlideListV3 API provides methods to manipulate lists.
-   **[[c_GlideMenuAPI|GlideMenu \(g\_menu and g\_item\) - Client]]**  
The GlideMenu API provides methods that can be used in UI context menus and in `onShow` scripts to customize UI context menu items.
-   **[[c_GlideModalFormV3API|GlideModalForm - Client]]**  
The GlideModalForm API provides methods to display a form in a GlideModal.
-   **[[c_GlideModalV3API|GlideModal - Client]]**  
The GlideModal API provides methods for displaying a content overlay, known as a modal. Modals are interactive windows that appear above a page and close when a user takes an action. You can use a modal to display information, ask questions, or perform actions.
-   **[[c_GlideNavigationV3API|GlideNavigation - Client]]**  
The GlideNavigation API provides methods to control and refresh the navigator and main frame.
-   **[[c_GlideNotificationV3API|GlideNotification - Client]]**  
The GlideNotification API provides methods that display messages over the page content.
-   **[[c_GlideRecordClientSideAPI|GlideRecord - Client]]**  
The GlideRecord API provides methods that perform database operations. This API enables the use of some GlideRecord functionality in client-side scripts, such as [[client-scripts|client scripts]] and UI policy scripts.
-   **[[c_GlideURLV3API|GlideURLV3 - Client]]**  
The GlideURLV3 API provides methods for manipulating a URI.
-   **[[c_GlideUserAPI|GlideUser - Client]]**  
The GlideUser API provides methods that access information about the current user and current user roles. Using this API avoids the need to use the slower GlideRecord queries to get user information.
-   **[[GUIScriptsAPI|GlideUIScripts - Client]]**  
The GlideUIScripts API provides methods to access [[c_UIScripts|UI scripts]] from within client-side code.
-   **[[guided_toursAPI|Guided Tours - Client]]**  
The Guided Tours API provides methods for launching and stopping guided tours.
-   **[[c_i18NV3API|i18N - Client]]**  
The i18N API provides methods to get and format translated messages.
-   **[[c_openFrameAPI|openFrameAPI - Client]]**  
The openFrameAPI provides methods that interact with OpenFrame. OpenFrame is an omni-present frame that communication partners can use to integrate their systems into the ServiceNow platform.
-   **[[c_Notify2WebRTCClient|NotifyClient - Client]]**  
The NotifyClient API provides methods that enable you to use Notify telephony functionality, such as making and receiving calls from a web browser.
-   **[[NotifyOnTaskClient|NotifyOnTaskClient - Client]]**  
The NotifyOnTaskClient API provides methods for sending SMS messages or starting/managing a conference call for various telephony service providers, such as Zoom and Webex.
-   **[[ScopedSessionDomainAPI|ScopedSessionDomain - Client]]**  
The ScopedSessionDomain script include that contains client-side methods that provide functionality related to the current session domain.
-   **[[c_ScriptLoaderAPI|ScriptLoader - Client]]**  
The ScriptLoader API provides methods to load scripts asynchronously.
-   **[[SNAnalyticsClientAPI|SNAnalytics - Client]]**  
The SNAnalytics API provides methods to push custom analytics data \(events, pages, and user properties\) to the Usage Insights for Service Portal dashboard.
-   **[[spAriaUtil-API|spAriaUtil - Client]]**  
The spAriaUtil API provides methods to show messages on a screen reader.
-   **[[spContextManagerAPI|spContextManager - Client]]**  
Makes data from a Service Portal widget available to other applications and services in a Service Portal page. For example, pass widget data to Agent Chat when it opens in a Service Portal page.
-   **[[SPModal-API|spModal - Client]]**  
Shows alerts, prompts, and confirmation dialogs in Service Portal widgets. The spModal class is available in Service Portal client scripts.
-   **[[spUtilAPI|spUtil - Client]]**  
The spUtil API provides utility methods to perform common functions in a Service Portal widget client script.
-   **[[c_StopWatchAPI|StopWatch - Client]]**  
The StopWatch API provides methods to measure the duration of operations.

**Parent Topic:**[[api-reference|API reference]]

## Related

- [[StandaloneClientMethods|StandaloneClientMethods]]
- [[DynamicTranslationClientAPI|DynamicTranslation - Client]]
- [[g_service_catalogClientAPI|g\_service\_catalog - Client]]
- [[GlideAgentWorkspaceAPI|GlideAgentWorkspace \(g\_aw\) - Client]]
- [[c_GlideAjaxAPI|GlideAjax - Client]]
- [[c_GlideDialogWindowAPI|GlideDialogWindow - Client \(deprecated\)]]
- [[c_GlideDocumentV3API|GlideDocument - Client]]
- [[GlideFlowAPI|GlideFlow - Client]]
- [[c_GlideFormAPI|GlideForm \(g\_form\) - Client]]
- [[c_MobileGlideForm_API|Mobile GlideForm \(g\_form\) - Client]]
- [[c_GlideGuidV3API|GlideGuid - Client]]
- [[c_GlideList2API|GlideList2 \(g\_list\) - Client]]
- [[c_GlideListV3API|GlideListV3 \(g\_list\) - Client \(deprecated\)]]
- [[c_GlideMenuAPI|GlideMenu \(g\_menu and g\_item\) - Client]]
- [[c_GlideModalFormV3API|GlideModalForm - Client]]
- [[c_GlideModalV3API|GlideModal - Client]]
- [[c_GlideNavigationV3API|GlideNavigation - Client]]
- [[c_GlideNotificationV3API|GlideNotification - Client]]
- [[c_GlideRecordClientSideAPI|GlideRecord - Client]]
- [[c_GlideURLV3API|GlideURLV3 - Client]]
- [[c_GlideUserAPI|GlideUser - Client]]
- [[GUIScriptsAPI|GlideUIScripts - Client]]
- [[guided_toursAPI|Guided Tours - Client]]
- [[c_i18NV3API|i18N - Client]]
- [[c_openFrameAPI|openFrameAPI - Client]]
- [[c_Notify2WebRTCClient|NotifyClient - Client]]
- [[NotifyOnTaskClient|NotifyOnTaskClient - Client]]
- [[ScopedSessionDomainAPI|ScopedSessionDomain - Client]]
- [[c_ScriptLoaderAPI|ScriptLoader - Client]]
- [[SNAnalyticsClientAPI|SNAnalytics - Client]]
- [[spAriaUtil-API|spAriaUtil - Client]]
- [[spContextManagerAPI|spContextManager - Client]]
- [[SPModal-API|spModal - Client]]
- [[spUtilAPI|spUtil - Client]]
- [[c_StopWatchAPI|StopWatch - Client]]
- [[api-reference|API reference]]
- [[client-scripts|Client scripts]]
- [[c_UIScripts|UI scripts]]
