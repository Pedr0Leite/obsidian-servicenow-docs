---
title: Components installed with Employee Profile
description: Several types of components are installed with activation of the Employee Profile \[sn\_employee\_profile\] plugin, including tables, user roles, and scheduled jobs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/hr-service-delivery/installed-with-employee-profile.html
release: australia
product: HR Service Delivery
classification: hr-service-delivery
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Employee Profile, Employee Profile table, HR Administration, Configure, Case and Knowledge Management, HR Service Delivery, Employee Service Management]
tags:
  - employee-service-management
  - hrsd
  - hr
  - cases
  - service-catalog
  - type-reference
---

# Components installed with Employee Profile

Several types of components are installed with activation of the [[emp-slate-employee-profile|Employee Profile]] \[sn\_employee\_profile\] plugin, including tables, user roles, and scheduled jobs.

**Note:** The Application Files table lists the components that are installed with this application. For instructions on how to access this table, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Roles installed

<table id="table_u1t_gb1_wdb"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains roles

</th></tr></thead><tbody><tr><td>

Employee Profile admin\[sn\_employee.admin\]

</td><td>

Grants access to create, read, update, and delete for the [[employee-profile|Employee Profile table]].

</td><td>

None

</td></tr></tbody>
</table>## Scheduled jobs installed

<table id="table_dx3_gb1_wdb"><thead><tr><th>

Scheduled job

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Sync employee profile from [[c_HRProfileRecords|HR profile]]

</td><td>

[[hr-service-delivery|HR Service Delivery]] only: One-time scheduled job that pulls all users with their corresponding employment\_start\_date and employment\_end\_date values from the HR Profile \(sn\_hr\_core\_profile\) table.

</td></tr></tbody>
</table>## Tables installed

<table id="table_fbz_45z_vdb"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Employee Profile\[sn\_employee\_profile\]

</td><td>

Employee Profile table.

</td></tr></tbody>
</table>**Parent Topic:**[Activate Employee Profile](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/activate-employee-profile.md)

## Related

- [[emp-slate-employee-profile|Employee profile]]
- [[employee-profile|Employee Profile table]]
- [[c_HRProfileRecords|HR Profile]]
- [[hr-service-delivery|HR Service Delivery]]
