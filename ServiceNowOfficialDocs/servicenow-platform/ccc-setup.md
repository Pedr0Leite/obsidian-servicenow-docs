---
title: Setting up ServiceNow Voice
description: Enable ServiceNow Voice and integrate it with a third-party phone system such as Amazon Connect.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/ccc-setup.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [ServiceNow Voice, Manage people and work capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Setting up ServiceNow Voice

Enable ServiceNow Voice and integrate it with a third-party phone system such as Amazon [[c_Connect|Connect]].

When you set up a third-party phone system and integrate it with the ServiceNow instance, an agent can accept an incoming call or make an outbound call from the ServiceNow instance using the integrated softphone. This experience is based on the configurations made within the third-party phone system.

## Get started with Voice

1.  Procure a license for a ServiceNow application, such as ITSM or CSM, which includes ServiceNow Voice.
2.  Install the ServiceNow Voice applications in ServiceNow® Store. For information about this installation, see [[install-ccc-apps|Install ServiceNow Voice applications]].
3.  Sign up and create an account with a third-party phone system. By default, Amazon Connect is supported. For information about creating an Amazon Web Services \(AWS\) account, see the Amazon [documentation](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).
4.  Configure the framework for the third-party phone system within the ServiceNow instance. By default, the framework is supported for Amazon Connect. For information about this configuration, see [[integrate-ccc-amazonconnect|Integrate ServiceNow Voice with Amazon Connect]].

-   **[Install ServiceNow Voice applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/install-ccc-apps.md)**  
You can install the ServiceNow Voice applications if you have the admin role. The application includes demo data and installs related ServiceNow® Store applications and plugins if they are not already installed.
-   **[[domain-separation-voice|Domain separation and ServiceNow Voice]]**  
 [[domain-separation-relationship-formatter-editor|Domain separation]] is supported for ServiceNow Voice. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
-   **[[set-pin-ccc|Configuring a phone PIN]]**  
You can set up or reset a phone PIN that can be used for caller authentication during a call with an agent.
-   **[[configure-e614-consumer|Configure the E.164 format for a consumer phone number]]**  
Ensure that all the necessary information for a phone number is included and properly formatted to successfully route an international call over a territory's public telephone network. Provide the E.164-compliant formatting and validation for phone number.
-   **[[config-cti-comp-log|Configuring CTI component logging]]**  
Configure CTI component logging to enable component logging to the system logs.
-   **[[configure-rtt-sn-voice|Configure Real Time Transcription for ServiceNow Voice Customer Service Management]]**  
Configure settings in your Amazon Connect instance, and in your ServiceNow instance to allow agents to see a real time transcription of voice calls with customers.
-   **[[configure-rtt-sn-voice-itsm|Configure Real Time Transcription for ServiceNow Voice for IT Service Management]]**  
Configure settings in your Amazon Connect instance, and in your ServiceNow instance to allow agents to see a real time transcription of voice calls with customers.
-   **[[cloud-call-center-api|Scripting for operation handlers]]**  
You can use the APIs in the ServiceNow Voice framework to create a seamless voice call experience for your callers and agents.

**Parent Topic:**[[cloud-call-center-overview|ServiceNow Voice]]

## Related

- [[install-ccc-apps|Install ServiceNow Voice applications]]
- [[integrate-ccc-amazonconnect|Integrate ServiceNow Voice with Amazon Connect]]
- [[domain-separation-voice|Domain separation and ServiceNow Voice]]
- [[set-pin-ccc|Configuring a phone PIN]]
- [[configure-e614-consumer|Configure the E.164 format for a consumer phone number]]
- [[config-cti-comp-log|Configuring CTI component logging]]
- [[configure-rtt-sn-voice|Configure Real Time Transcription for ServiceNow Voice Customer Service Management]]
- [[configure-rtt-sn-voice-itsm|Configure Real Time Transcription for ServiceNow Voice for IT Service Management]]
- [[cloud-call-center-api|Scripting for operation handlers]]
- [[cloud-call-center-overview|ServiceNow Voice]]
- [[c_Connect|Connect]]
- [[domain-separation-relationship-formatter-editor|Domain separation]]
