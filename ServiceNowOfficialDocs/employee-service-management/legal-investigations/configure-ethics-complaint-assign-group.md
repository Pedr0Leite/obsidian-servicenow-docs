---
title: Configure system properties to update ethics complaint assignment group
description: As an admin, configure the sn\_lg\_investigate.ethics\_complaints\_assignment\_group system property to use a different assignment group to assign ethics complaints.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/legal-investigations/configure-ethics-complaint-assign-group.html
release: australia
product: Legal Investigations
classification: legal-investigations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Legal Investigations, Legal Service Delivery Practice Applications, Legal Service Delivery, Legal and Contract Operations, Employee Service Management]
tags:
  - employee-service-management
  - legal
  - investigations
  - cases
  - compliance
  - type-task
---

# Configure system properties to update ethics complaint assignment group

As an admin, configure the `sn_lg_investigate.ethics_complaints_assignment_group` system property to use a different assignment group to assign ethics complaints.

## Before you begin

Role required: sn\_lg\_ops.legal\_admin

## About this task

`sn_lg_investigate.ethics_complaints_assignment_group` is a configurable system property that is used to configure default assignment group for ethics complaints raised using [[emp-center-quick-link-config|quick links]] in [[employee-center-landing-page|Employee Center]]. The sys\_id of any group that is protected with the [[ur-landing-limitedaccess|Universal Request]] sensitive role and has fulfillers who can work on ethics complaints is enabled to configure the system property.

Alternatively, configure the property from [Set up Legal Investigations with HR Service Delivery Employee Relations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-investigations/integrate-lsd-hrsd.md).

## Procedure

1.  In the filter navigator, enter `sys_properties.list`.

2.  In the **Name** column, search for the `sn_lg_investigate.ethics_complaints_assignment_group` property.

3.  Select the property.

4.  If you aren’t able to edit the property in the current application scope, select the word **here** in the message at the top of the page.

5.  Update the **Value** field with the sys\_id of the new assignment group.

6.  Select **Update**.


## Result

You can now use the new assignment group to assign ethics complaints.

## Related

- [[emp-center-quick-link-config|Quick links]]
- [[employee-center-landing-page|Employee Center]]
- [[ur-landing-limitedaccess|Universal Request]]
