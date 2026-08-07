---
title: Install Health and Safety Testing
description: You can install Health and Safety Testing if you have the admin role.Several types of components are installed with Health and Safety Testing, including user roles and tables.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/health-and-safety-testing/install-health-testing.html
release: australia
product: Health and Safety Testing
classification: health-and-safety-testing
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Health and Safety Testing, Safe Workplace, Health and Safety, Employee Service Management]
tags:
  - employee-service-management
  - testing
  - certification
  - training
  - ehs
  - type-task
---

# Install Health and Safety Testing

You can install Health and Safety Testing if you have the admin role.

## Before you begin

[[health-safety-testing|Health and Safety Testing]] requires the ServiceNow® [[employee-readiness-core|Employee Readiness Core]] application.

The ServiceNow® [[contact-tracing|Contact Tracing]] application can optionally be installed to send an email notification to employees who are potentially exposed individuals in a contact tracing case. The notification informs the employee of the potential exposure and provides them with a link to request testing.

The ServiceNow® [[emergency-response-management|Emergency Response Management]] for Now Mobile application can optionally be installed to add a **Health** tab to the [[mobile-employee-experience|Now Mobile app]] where employees can request testing or report a test result.

Role required: admin

<table id="table_kxr_yz3_blb"><thead><tr><th>

Type

</th><th>

Instructions

</th></tr></thead><tbody><tr><td>

Commercial on-premise

</td><td>

Visit the ServiceNow® Store to download and install the application.

</td></tr><tr><td>

Federal hosted

</td><td>

See the [Federal downloads for the Emergency Response Management and [[safe-workplace|Safe Workplace]] suite apps \[KB0030260\]](https://store.servicenow.com/$appstore.do#!/store/help?article=KB0030260) article in the Store Help Center for more information.

</td></tr><tr><td>

Federal on-premise

</td><td>

If you are a federal on-premise customer and you would like to install this application, reach out to your sales representative or open a Now Support or HIWAVE ticket. In the ticket, request to be routed to the SHOT team.

 See the [Federal downloads for the Emergency Response Management and Safe Workplace suite apps \[KB0030260\]](https://store.servicenow.com/$appstore.do#!/store/help?article=KB0030260) article in the Store Help Center for more information.

</td></tr><tr><td>

On-premise

</td><td>

See the [Commercial downloads for the Emergency Response Management and Safe Workplace suite apps \[KB0030258\]](https://store.servicenow.com/$appstore.do#!/store/help?article=KB0030258) article in the Store Help Center for more information.

</td></tr></tbody>
</table>If you've subscribed to the Safe Workplace suite and you already have some of the apps installed, refer to the following order of installation for the remaining apps.

-   [[emergency-outreach|Emergency Outreach]] \(sn\_imt\_checkin\)
-   [[employee-health-screening|Employee Health Screening]] \(sn\_imt\_monitoring\)
-   [[ppe-inventory-management|Workplace PPE Inventory Management]] \(sn\_imt\_ppe\)
-   [[employee-readiness-surveys|Employee Readiness Surveys]] \(sn\_imt\_readiness\)
-   COVID-19 Global Health Data Set \(sn\_imt\_c19datafeed\)
-   Contact Tracing \(sn\_imt\_tracing\)
-   [[emergency-self-report|Emergency Self Report]] \(sn\_imt\_quarantine\)
-   [[workplace-safety-mgmt-hr|Workplace Core]] \(sn\_wsd\_core\)
-   [[safe-workplace-dashboard|Safe Workplace Dashboard]] \(sn\_imt\_dashboard\)
-   Emergency Response Management for Now Mobile \(sn\_imt\_mobile\)
-   [[employee-travel-safety|Employee Travel Safety]] \(sn\_imt\_travel\)
-   Health and Safety Testing \(sn\_imt\_health\_test\)
-   [[vaccination-status|Vaccination Status]] \(sn\_imt\_vaccine\)

## Procedure

1.  Navigate to **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Search for `Health and Safety Testing`.

3.  Click **Install**.

    The Application installation dialog box opens.

4.  Click **Activate**.


**Parent Topic:**[Health and Safety Testing](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/health-and-safety-testing/health-safety-testing.md)

## Components installed with Health and Safety Testing

Several types of components are installed with Health and Safety Testing, including user roles and tables.

**Note:** The Application Files table lists the components that are installed with this application. For instructions on how to access this table, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

### Roles installed

<table id="table_u1t_gb1_wdb"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains roles

</th></tr></thead><tbody><tr><td>

Health and Safety Testing admin\[sn\_imt\_health\_test.admin\]

</td><td>

Application-specific admin for Health and Safety Testing.**Important:** By default, the System Administrator \[admin\] role contains the sn\_imt\_health\_test.admin role. The sn\_imt\_health\_test.admin role should be reassigned to another user and then removed from the admin. This process protects sensitive application data by restricting access to the application.

</td><td>

sn\_imt\_health\_test.testing\_admin

</td></tr><tr><td>

Health testing manager\[sn\_imt\_health\_test.testing\_admin\]

</td><td>

Can view and manage health testing requests, results, providers, and test types.

</td><td>

None

</td></tr></tbody>
</table>### Tables installed

<table id="table_udb_2hn_2mb"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Provider\[sn\_imt\_health\_test\_provider\]

</td><td>

Health providers that your organization uses for COVID-19 diagnostic testing.

</td></tr><tr><td>

Test Request\[sn\_imt\_health\_test\_request\]

</td><td>

Test requests submitted by users.Users can review their test requests in **My test requests**.

</td></tr><tr><td>

Test Result\[sn\_imt\_health\_test\_result\]

</td><td>

Test results submitted by users.Users can review their test results in **My test results**. Managers can review the test results of their direct reports in **My Employee's Test Results** if enabled by their organization.

 For more information, see [Configure Health and Safety Testing](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/health-and-safety-testing/configure-health-safety-testing.md).

</td></tr><tr><td>

Test Type\[sn\_imt\_health\_test\_type\]

</td><td>

Types of testing offered by providers. The options are **At a facility** and **Self-administered**. You can create additional test types if necessary.

</td></tr></tbody>
</table>

## Related

- [[health-safety-testing|Health and Safety Testing]]
- [[employee-readiness-core|Employee Readiness Core]]
- [[contact-tracing|Contact Tracing]]
- [[emergency-response-management|Emergency Response Management]]
- [[mobile-employee-experience|Now Mobile app]]
- [[safe-workplace|Safe Workplace]]
- [[emergency-outreach|Emergency Outreach]]
- [[employee-health-screening|Employee Health Screening]]
- [[ppe-inventory-management|Workplace PPE Inventory Management]]
- [[employee-readiness-surveys|Employee Readiness Surveys]]
- [[emergency-self-report|Emergency Self Report]]
- [[workplace-safety-mgmt-hr|Workplace Core]]
- [[safe-workplace-dashboard|Safe Workplace Dashboard]]
- [[employee-travel-safety|Employee Travel Safety]]
- [[vaccination-status|Vaccination Status]]
