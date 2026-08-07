---
title: Supported integration interfaces
description: ServiceNow provides a number of interfaces to be able to directly integrate with the platform. These interfaces are considered part of the platform and are provided at no additional charge.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/r\_SupportedIntegrationInterfaces.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Integration options, Integration with third-party applications and data sources, Integrations, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-reference
---

# Supported integration interfaces

ServiceNow provides a number of interfaces to be able to directly integrate with the platform. These interfaces are considered part of the platform and are provided at no additional charge.

|Interface|
|---------|
|[[c_InboundEmailActions|Email]]|
|[[t_JDBCProbe|JDBC]]|
|[JSONv2 Web Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/c_JSONv2WebService.md)|
|[LDAP integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_LDAPIntegration.md)|
|[SOAP web service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/c_SOAPWebService.md)|
|[REST API](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/c_RESTAPI.md)|
|[SAML](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_SAML2.0WebBrowserSSOProfile.md)|
|[Digest token authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_DigestTokenAuthentication.md)|
|[ODBC driver](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/c_ODBCDriver.md)|
|[Data Export](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/table-administration-and-data-management/c_ExportData.md)|
|[[r_ComputerTelephonyIntegration|CTI]]|
|[[r_SyslogProbe|Syslog probe]]|

-   **[Computer Telephony Integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_ComputerTelephonyIntegration.md)**  
Computer Telephony Integration \(CTI\) is accomplished by the CTI client on the user machine sending a URL to the instance.
-   **[[c_IntegratServiceNowIntranet|Integrating ServiceNow with your Intranet]]**  
You can add a ServiceNow login link to your intranet.
-   **[JDBCProbe](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_JDBCProbe.md)**  
A JDBC probe runs on the MID Server to query an external database via JDBC and returns [[hs-results|results]] to ServiceNow.
-   **[Syslog probe](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_SyslogProbe.md)**  
The ServiceNow Syslog probe uses the MID Server to deliver log messages from a ServiceNow instance to another machine, such as a dedicated log server, using the syslog protocol over an IP network.

**Parent Topic:**[[c_IntegrationOptions|Integration options]]

## Related

- [[c_InboundEmailActions|Inbound email actions]]
- [[t_JDBCProbe|JDBCProbe]]
- [[r_ComputerTelephonyIntegration|Computer Telephony Integration]]
- [[r_SyslogProbe|Syslog probe]]
- [[c_IntegratServiceNowIntranet|Integrating ServiceNow with your Intranet]]
- [[c_IntegrationOptions|Integration options]]
- [[hs-results|Results]]
