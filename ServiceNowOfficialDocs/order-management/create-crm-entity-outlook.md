---
title: Create a CRM record from Microsoft Outlook
description: Create a new lead or contact record and associate an email with it directly from Microsoft Outlook, enabling you to capture new prospects without having to leave your email inbox.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/create-crm-entity-outlook.html
release: australia
topic_type: task
last_updated: "2026-06-08"
reading_time_minutes: 2
keywords: [ServiceNow CRM for Outlook, create lead, create contact, create and associate]
breadcrumb: [Activity Management, Lead and opportunity apps, Use, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-task
---

# Create a CRM record from Microsoft Outlook

Create a new lead or contact record and associate an email with it directly from Microsoft Outlook, enabling you to capture new prospects without having to leave your email inbox.

## Before you begin

Write permission on the underlying CRM entity table is required to view the corresponding tab in the ServiceNow CRM for Outlook Add-in and to create or associate records on that tab. For example, to associate an email with a LEAD record, you must have write permission on the Lead \[sn\_lead\_mgmt\_core\_lead\] table.

Your admin can grant you this write permission in either of these ways: directly through table ACLs, or through the responsibility framework. The responsibility framework grants you access to specific records based on your role and your membership. For more information, see [Create a responsibility definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/t_CreateAResponsibilityDefinition.md).

Role required: sn\_crm\_outlook.crm\_outlook\_user

## Procedure

1.  Open an email in Microsoft Outlook.

2.  Load the Microsoft Outlook add-in by selecting **ServiceNow CRM for Outlook** from the Microsoft Outlook ribbon.

3.  If a sign-in form appears, enter your credentials and select **Log in**.

4.  Select a record type from the **Create new** drop-down menu.

    |Record type|Description|
    |-----------|-----------|
    |**Lead**|New lead record for a potential customer who has shown interest but is not yet qualified. For a description of the field values, see [[lead-fields-outlook|Lead form in the ServiceNow CRM for Outlook add-in]].|
    |**Contact**|New contact record for an individual associated with an existing or new account. For a description of the field values, see [[contact-fields-outlook|Contact form in the ServiceNow CRM for Outlook add-in]].|

    When you [[create-new-lead|create a Lead]] or Contact from a sent email, the form populates with the first recipient's first name, last name, and domain. For received emails, the form is populated with the sender’s details.

5.  Complete the required [[fields|fields]] and any optional fields relevant to your workflow.

6.  Select **Create and associate**.


## Result

The CRM record is created and the email association is logged, enabling you to continue engagement tracking from either Microsoft Outlook or CSM/FSM Configurable Workspace.

## What to do next

You can view the associated emails from the respective entity record's Emails tab. For more information, see [[view-associated-emails-crm|Track emails linked from Microsoft Outlook]].

**Parent Topic:**[[using-activity-management|Using Activity Management]]

**Related topics**  


[[configuring-activity-management|Configuring Activity Management]]

[[explore-activity-management|Activity Management]]

## Related

- [[lead-fields-outlook|Lead form in the ServiceNow CRM for Outlook add-in]]
- [[contact-fields-outlook|Contact form in the ServiceNow CRM for Outlook add-in]]
- [[view-associated-emails-crm|Track emails linked from Microsoft Outlook]]
- [[using-activity-management|Using Activity Management]]
- [[configuring-activity-management|Configuring Activity Management]]
- [[explore-activity-management|Activity Management]]
- [[create-new-lead|Create a lead]]
- [[fields|Fields]]
