---
title: Configuring Patient Support Services
description: Set up the Patient Support Services application to complete enrollment activities associated with a patient service program.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/pss-config-app.html
release: australia
topic_type: concept
last_updated: "2023-08-03"
reading_time_minutes: 4
breadcrumb: [Patient Support Services, Healthcare and Life Sciences Service Management, Healthcare and Life Sciences]
---

# Configuring Patient Support Services

Set up the [[pss-app|Patient Support Services]] application to complete enrollment activities associated with a patient service program.

**Important:**

Starting with the Yokohama release, Patient Support Services is being prepared for future deprecation. It will be hidden and no longer activated on new instances but will continue to be supported.

For details, see the [Deprecation Process \[KB0867184\]](https://support.servicenow.com/kb_view.do?sysparm_article=KB0867184) article in the Now Support knowledge base.

**Note:** The Patient Support Services application is based on the Patient Support Services data model that extends the [Healthcare and Life Sciences data model](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/healthcare-life-sciences/healthcare-and-life-sciences-service-management-core/hcls-serv-mgmt-core.md) and stores all enrollment requests in the Enrollment case \[sn\_patientservice\_enroll\_case\] table.

The following table provides an overview of the configuration tasks required for Patient Support Services.

<table id="table_ksw_gpr_4nb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[pss-install-app|Install Patient Support Services]].

</td><td>

Install the Patient Support Services application to work on patient support services.

</td></tr><tr><td>

[[pss-assign-roles|Assign roles for Patient Support Services users]].

</td><td>

Assign roles to control access to features, capabilities, and data in the Patient Support Services application.

</td></tr><tr><td>

[[pss-data-model|Use the Patient Support Services data model]].

</td><td>

Use Patient Support Services tables to store the data related to enrollment requests.

</td></tr><tr><td>

[[pss-approve-rca|Approve restricted caller access privileges for Patient Support Services.]]

</td><td>

Approve restricted caller access \(RCA\) privileges for accessing document templates from the Patient Support Services application.

</td></tr><tr><td>

[[pss-enroll-form-config|Configure an enrollment request form]].

</td><td>

Configure an enrollment request form to enable patients or practitioners enroll into Patient Support Services programs offered by a healthcare organization.

</td></tr><tr><td>

[[pss-ext-point-enrollment-form|Configure the submission flow of the enrollment request form]].

</td><td>

Use scripted extension points to decide what records are created or updated after an enrollment request form is submitted.

</td></tr><tr><td>

[[pss-nurse-ts-group|Determine who can conduct training tasks]].

</td><td>

Add users who can conduct the trainings for Patient Support Services to the Nurse Training Support assignment group.

</td></tr><tr><td>

[[pss-appt-booking-setup|Configure an appointment booking setting]].

</td><td>

Enable patients to book an appointment for the training tasks conducted within the Patient Support Services application

</td></tr><tr><td>

[[pss-program-services-setup|Configure a program]].

</td><td>

Enable your patients to enroll to a program in the Patient Support Services application.

</td></tr><tr><td>

[[pss-config-checklist|Configure a checklist for a program.]]

</td><td>

Configure a checklist for a Patient Support Services program as an informal list of questions or tasks used as a reminder for the completion of an enrollment request.

</td></tr><tr><td>

[[pss-config-doc-decisions|Configure the auto-generation of documents]].

</td><td>

Define the conditions for auto-generating documents for an enrollment request.

</td></tr><tr><td>

[[pss-config-to-do|Add a to-dos menu item to patient portal]].

</td><td>

Configure the patient portal to add a menu item that lists all to-do items for enrollment request tasks.

</td></tr><tr><td>

[[pss-config-playbook|Configure a playbook for Patient Support Services]].

</td><td>

Configure a playbook to provide step-by-step guidance for resolving enrollment cases.

</td></tr><tr><td>

[[pss-config-emails|Configure a Patient Support Services email notification]].

</td><td>

Configure the email notifications sent to patients about Patient Support Services programs.

</td></tr><tr><td>

[[pss-connector-contributor|Determine additional user profiles]].

</td><td>

Determine who can act as an agent connector or contributor for enrollment cases in the Patient Support Services application.

</td></tr><tr><td>

[[pss-case-contributor|Set up the process for contributors to create an enrollment case]].

</td><td>

Set up the process for creating enrollment cases on a service portal.

</td></tr></tbody>
</table>

## Related

- [[pss-install-app|Install Patient Support Services]]
- [[pss-assign-roles|Assign roles for Patient Support Services users]]
- [[pss-data-model|Patient Support Services data model]]
- [[pss-approve-rca|Approving restricted caller access privileges for Patient Support Services]]
- [[pss-enroll-form-config|Configuring the enrollment request form]]
- [[pss-ext-point-enrollment-form|Configure the submission flow of the enrollment request form]]
- [[pss-nurse-ts-group|Determine who can conduct a training for Patient Support Services]]
- [[pss-appt-booking-setup|Configuring an appointment booking setting for Patient Support Services]]
- [[pss-program-services-setup|Configuring a program for Patient Support Services]]
- [[pss-config-checklist|Configure a checklist for Patient Support Services]]
- [[pss-config-doc-decisions|Configuring the auto-generation of documents for enrollment requests]]
- [[pss-config-to-do|Configuring the patient portal to add a to-dos menu item for enrollment request tasks]]
- [[pss-config-playbook|Configuring playbooks for Patient Support Services]]
- [[pss-config-emails|Configuring the Patient Support Services email notifications]]
- [[pss-connector-contributor|Determining additional user profiles in Patient Support Services]]
- [[pss-case-contributor|Setting up the process to create enrollment cases as a contributor]]
- [[pss-app|Patient Support Services]]
