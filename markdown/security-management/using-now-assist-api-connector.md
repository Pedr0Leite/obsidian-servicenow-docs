---
title: Creating an API connector with generative ai
description: Use the SPC Setup Connector generative AI skill in USEM to help your developers quickly and automatically create an API connector that you can publish and use in the Security Posture Control workspace. This skill automatically selects an API template, populates request and header parameters, and maps sample response attributes to SPC attributes based on API documentation you provide.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/using-now-assist-api-connector.html
release: australia
topic_type: concept
last_updated: "2026-05-26"
reading_time_minutes: 2
breadcrumb: [Use, Unified Security Exposure Management, Security Operations]
---

# Creating an API connector with generative ai

Use the SPC Setup Connector generative AI skill in USEM to help your developers quickly and automatically create an API connector that you can publish and use in the [[spc-landing|Security Posture Control]] workspace. This skill automatically selects an API template, populates request and header parameters, and maps sample response attributes to SPC attributes based on API documentation you provide.

**Note:** Depending on your license, you will have access to certain application features, generative AI skills, agentic workflows, and AI agents. For more information, see [ServiceNow product tiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-native-sku-overview.md).

You must have Zurich Patch 4 of [[now-assist-for-vulnerability-response-landing|Now Assist for Vulnerability Response]] to view the SPC Setup Connector skill.

**Important:** This Now Assist skill is turned on by default. The skill will be automatically available to appropriate role users for the application. For more information, see [Now Assist skills, agents, and agentic workflows on by default](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/now-assist-skills-on-by-default.md).

You have the option to use Now Assist to help you automatically complete the following steps in the Connector builder in the Security Posture Control workspace.

-   [[spc-sgc-template-stepper-3|Select template]] \(Step 3\)- A template is selected to support your API's structure based on vendor documentation that you provide.
-   [[spc-sgc-template-stepper-4|Provide inputs]] \(Step 4\)- Input parameters are provided, the connection is tested, and a sample response is generated based on the vendor documentation that you provide.
-   [[spc-sgc-stepper-5|Map response]] \(Step 5\)- [[mapping-logrhythm|Mapping]] the sample response parameters to SPC attributes and policies is provided.

You must complete steps 1-2 manually to enter connector metadata and credentials in the Connector builder in the Security Posture Control workspace before you can invoke the SPC Setup Connector Now Assist skill for steps 3-5.

See [[spc-creating-sgc-template|Creating your own API connectors in Security Posture Control]] for more information about completing the first two steps manually in the Connector builder.

See [[select-api-template|Create an API connector with generative AI]] for the steps in the Connector builder that use Now Assist for Vulnerability Response.

-   **[Create an API connector with generative AI](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/select-api-template.md)**  
Use the SPC Setup Connector skill to help you automatically complete configuration steps 3-5 in the Connector builder in the Security Posture Control Workspace.

**Parent Topic:**[[using-unified-security-exposure-management|Using Unified Security Exposure Management]]

## Related

- [[spc-sgc-template-stepper-3|Select a connector template]]
- [[spc-sgc-template-stepper-4|Provide input values for your API connector]]
- [[spc-sgc-stepper-5|Map API response to SPC attributes]]
- [[spc-creating-sgc-template|Creating your own API connectors in Security Posture Control]]
- [[select-api-template|Create an API connector with generative AI]]
- [[using-unified-security-exposure-management|Using Unified Security Exposure Management]]
- [[spc-landing|Security Posture Control]]
- [[now-assist-for-vulnerability-response-landing|Now Assist for Vulnerability Response]]
- [[mapping-logrhythm|Mapping]]
