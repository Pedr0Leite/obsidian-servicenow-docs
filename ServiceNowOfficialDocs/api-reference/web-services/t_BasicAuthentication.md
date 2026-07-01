---
title: Enable basic authentication for outbound SOAP
description: If the endpoint requires a user name and password, you can provide credentials using basic authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/api-reference/web-services/t\_BasicAuthentication.html
release: australia
product: Web Services
classification: web-services
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Outbound SOAP security, SOAP, Outbound, Web services, API implementation, API implementation and reference]
tags:
  - api-reference
  - soap
  - web-services
  - wsdl
  - integration
  - type-task
---

# Enable basic authentication for outbound SOAP

If the endpoint requires a user name and password, you can provide credentials using basic authentication.

## Before you begin

Role required: web\_service\_admin

## Procedure

1.  Navigate to **All** &gt; **System [[r_AvailableWebServices|Web Services]]** &gt; **Outbound** &gt; **[[c_SOAPMessage|SOAP Message]]**.

2.  Select a SOAP message record.

3.  In the [[c_SOAPMessageFunctions|SOAP Message Functions]] related list, select a function.

4.  Select **Use basic auth**.

5.  Enter a user name in the Basic auth user ID field.

6.  Enter the password for that user in Basic auth user password.

7.  Click **[[r_Update|Update]]**.


**Parent Topic:**[Outbound SOAP security](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/c_OutboundSOAPSecurity.md)

## Related

- [[c_SOAPMessageFunctions|SOAP message functions]]
- [[c_SOAPMessage|SOAP message]]
- [[r_AvailableWebServices|Web services]]
- [[r_Update|update]]
