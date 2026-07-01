---
aliases:
  - "Integrate your self-configured bot with single Mic"
tags:
  - teams-integration
  - virtual-agent
  - integrations
  - azure
  - single-tenant
---

# Integrate your self-configured bot with single Microsoft Teams tenant

## Useful links

[https://www.servicenow.com/docs/r/conversational-interfaces/virtual-agent/teams-install-custom-app.html](https://www.servicenow.com/docs/r/conversational-interfaces/virtual-agent/teams-install-custom-app.html)

[Create and download the manifest file for self-configured apps • Yokohama Employee Service Management • Docs | ServiceNow](https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/download-manifest-file-st.html?section=download-manifest-file-st)

[https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/setup-sn-ms-teams.html](https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/setup-sn-ms-teams.html)

[https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/setup-tenants.html](https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/setup-tenants.html)

[https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/setup-sn-ms-teams-ms365.html](https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/setup-sn-ms-teams-ms365.html)

[https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/c_ServiceNowForMSTeams.html](https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/c_ServiceNowForMSTeams.html)

[https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/teams-conv-integration.html](https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/teams-conv-integration.html)

[https://www.servicenow.com/docs/r/zurich/employee-service-management/employee-experience-foundation/c_ServiceNowForMSTeams.html](https://www.servicenow.com/docs/r/zurich/employee-service-management/employee-experience-foundation/c_ServiceNowForMSTeams.html)

[https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/addtional-plugins-msteams.html](https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/addtional-plugins-msteams.html)

[https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/va-integ-single-teams.html](https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/va-integ-single-teams.html)

[https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/addtional-plugins-msteams.html](https://www.servicenow.com/docs/r/yokohama/conversational-interfaces/virtual-agent/addtional-plugins-msteams.html)

[https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/c_ServiceNowForMSTeams.html](https://www.servicenow.com/docs/r/yokohama/employee-service-management/employee-experience-foundation/c_ServiceNowForMSTeams.html)

[https://www.servicenow.com/docs/r/zurich/employee-service-management/employee-experience-foundation/mw-setup-botid-d62283e81467.html](https://www.servicenow.com/docs/r/zurich/employee-service-management/employee-experience-foundation/mw-setup-botid-d62283e81467.html)

## **Supported Scenarios between ServiceNow Instance and MS Teams (Both Single Tenant and Multi Tenant )**

Summary

![image.png](Integrate%20your%20self-configured%20bot%20with%20single%20Mic/image.png)

A) Single MS Teams Tenant - Single SN Instance

Configuration:  Integrating Virtual Agent with Microsoft Teams

Scenario I (Not-Supported): Connection will get Override, leaving Bot for Instance 1 non-functional (No Automated Reply to Messages, as Authentication will fail on instance 1 )

Scenario II (Not Supported): The bot created last will take the connection, leaving earlier bots non-functional.

Scenario III ( Supported ): Additional Tenant Configuration on the MS side is needed in order to create more than one Bot as shown in Scenario III, so that multiple bots can be supported using different tenants.

B) Single MS Tenant - Multiple SN Instances

Scenario IV : (Support Starts from San Diego Version)

Configuration: Integrating multiple ServiceNow instances with a single Microsoft Teams tenant

Confirm the MS tenant entry shows up under  "Integrate multiple ServiceNow instances" like below

![image.png](Integrate%20your%20self-configured%20bot%20with%20single%20Mic/image%201.png)

Understanding Pre-published apps vs Self-Configured apps

Pre-published apps:This flavor of setup is recommended where you can consume an Azure Enterprise application that is maintained by ServiceNow. This application is pre-configured with all required configurations & permissions, and one merely needs to authorize it for usage. This flavor is relatively easier to set up with less manual steps that can be error prone.This Application uses Proxy to enable communication between Microsoft Azure tenant and ServiceNow instance, however, the mapping has a limitation that it can hold only unique Azure tenant ID in the table. Hence the limitation of 1 ServiceNow instance to 1 Microsoft Azure Tenant (1:1 mapping) applies in this setup mode and ServiceNow recommends that you procure 2 Azure tenants to reserve one for testing for lower environments and one earmarked for Production.

Self-Configured app:This flavor of setup involves more manual steps but is preferred by some as this offers more granular control and visibility on the app creation process. This setup involves manually created/maintained App/Bot and adding each permission on Azure. This process is relatively error prone.However, when a customer has multiple ServiceNow instances (one or more lower and Production) and has only one Microsoft Azure tenant to work with, Self Configured gives the flexibility to create multiple azure applications per instance.

Related Links
A. Installation Checklist

B. MS Teams Setup Cleanup Script on SN Instance

C. End-to-End Integration

D. Demo step-by-step Integration video

E. Deployment recommendations on Teams App side

## Related

- [[Teams Integration]]
- [[Conversational integration with Microsoft Teams -]]
- [[Creating Custom MS Teams Cards]]