---
title: Extension points in Voice
description: Using extension points, you can call the custom scripts to extend the functionality of ServiceNow Voice. While integrating a third-party phone system with ServiceNow Voice, you can invoke extension points using the CTI API to handle events in ServiceNow Voice.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/extension-point-ccc.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Scripting for operation handlers, Setting up ServiceNow Voice, ServiceNow Voice, Manage people and work capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Extension points in Voice

Using extension points, you can call the custom scripts to extend the functionality of [[cloud-call-center-overview|ServiceNow Voice]]. While integrating a third-party phone system with ServiceNow Voice, you can invoke extension points using the CTI API to handle events in ServiceNow Voice.

By using extension points, you can easily integrate customizations without having to alter the base code. You can extend standard base functionality using customized scripts. For more information, see [Using extension points to extend application functionality](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/extension-points.md).

To view the extension points that are available by default, navigate to **System Extension Points** &gt; **Scripted Extension Points** and group by the ServiceNow Voice application.

**Note:** You should install the ServiceNow Voice, ServiceNow Voice for ITSM, ServiceNow Voice for CSM, and ServiceNow Voice with Amazon [[c_Connect|Connect]] applications from the ServiceNow® Store. For information about these installations, see [[install-ccc-apps|Install ServiceNow Voice applications]], [[install-ccc-itsm|Install ServiceNow Voice for ITSM]], and [[install-ccc-csm|Install ServiceNow Voice for CSM]].

|Extension point|Description|
|---------------|-----------|
|sn\_cti\_core.clickToCallContextMap|Enables the copying of application-specific field values to interaction records for ServiceNow Voice outbound calls.|
|sn\_cti\_core.CTICallAnalysisExtractor|Defines how the transcription and the recording data is retrieved for an interaction based on the third-party phone system integrated with ServiceNow Voice.|
|sn\_cti\_core.SoftPhoneEventSink|Defines if the third-party phone system can handle an event. Maps events from the Softphone interface to back-end events.|

**Parent Topic:**[[cloud-call-center-api|Scripting for operation handlers]]

## Related

- [[install-ccc-apps|Install ServiceNow Voice applications]]
- [[install-ccc-itsm|Install ServiceNow Voice for ITSM]]
- [[install-ccc-csm|Install ServiceNow Voice for CSM]]
- [[cloud-call-center-api|Scripting for operation handlers]]
- [[cloud-call-center-overview|ServiceNow Voice]]
- [[c_Connect|Connect]]
