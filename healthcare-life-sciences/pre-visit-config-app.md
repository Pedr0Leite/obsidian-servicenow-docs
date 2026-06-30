---
title: Configuring Pre-Visit Management
description: Set up the Pre-Visit Management application to complete pre-visit activities associated with a procedure.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/pre-visit-config-app.html
release: australia
topic_type: concept
last_updated: "2023-08-03"
reading_time_minutes: 3
breadcrumb: [Pre-Visit Management, Healthcare and Life Sciences Service Management, Healthcare and Life Sciences]
---

# Configuring Pre-Visit Management

Set up the [[pre-visit-mgmt-app|Pre-Visit Management]] application to complete pre-visit activities associated with a procedure.

**Important:**

Starting with the Yokohama release, Pre-Visit Management is being prepared for future deprecation. It will be hidden and no longer activated on new instances but will continue to be supported.

For details, see the [Deprecation Process \[KB0867184\]](https://support.servicenow.com/kb_view.do?sysparm_article=KB0867184) article in the Now Support knowledge base.

The following table provides an overview of the configuration tasks required for Pre-Visit Management.

**Note:** The Pre-Visit Management application is based on the [Healthcare and Life Sciences data model](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/healthcare-life-sciences/healthcare-and-life-sciences-service-management-core/hcls-serv-mgmt-core.md) and stores all procedure requests in the Procedure request \[sn\_previsit\_procedure\_request\] table.

<table id="table_ksw_gpr_4nb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[install-pre-visit-mgmt|Install Pre-Visit Management]].

</td><td>

Install the Pre-Visit Management application to work on procedure requests.

</td></tr><tr><td>

[[pre-visit-assign-roles|Assign roles for Pre-Visit Management users]].

</td><td>

Assign roles to control access to features, capabilities, and data in the Pre-Visit Management application.

</td></tr><tr><td>

[[pre-visit-approve-rca|Approve restricted caller access privileges for Pre-Visit Management.]]

</td><td>

Approve restricted caller access \(RCA\) privileges for accessing document templates from the Pre-Visit Management application.

</td></tr><tr><td>

[[pre-visit-proc-scheduler-grp|Determine who can work on the appointment booking task for a procedure]].

</td><td>

Add users who can work on the appointment booking task for a procedure to the Procedure scheduler assignment group.

</td></tr><tr><td>

[[pre-visit-config-proc-consent-time|Configure when to send the procedure consent form to a patient]].

</td><td>

Configure the Pre-Visit Management application to when to send the procedure consent document for review and signature to a patient before the procedure appointment date.

</td></tr><tr><td>

[[pre-visit-config-to-do-items|Specify a to-do item for patients]].

</td><td>

Add a to-do item that patients must complete as part of their pre-visit planning.

</td></tr><tr><td>

[[pre-visit-config-doc-decisions|Configure the auto-generation of documents for a procedure request]].

</td><td>

Define the conditions for auto-generating documents for a procedure request.

</td></tr><tr><td>

[[pre-visit-config-to-do|Configure the patient portal to add a to-dos menu item for procedure request tasks]].

</td><td>

Configure the patient portal to add a menu item that lists all to-do items for patients.

</td></tr><tr><td>

[[pre-visit-config-playbook|Configure a playbook for Pre-Visit Management]].

</td><td>

Configure a playbook to provide step-by-step guidance for resolving procedure request cases.

</td></tr><tr><td>

[[pre-visit-config-emails|Configure a Pre-Visit Management email notification]].

</td><td>

Configure the Pre-Visit Management email notifications sent to patients about pre-visit activities for procedure requests.

</td></tr><tr><td>

[[pre-visit-connector-contributor|Determine additional user profiles]].

</td><td>

Determine who can act as an agent connector or contributor for procedure request cases.

</td></tr><tr><td>

[[pre-visit-case-contributor|Set up the process for contributors to create a procedure request case]].

</td><td>

Set up the process for creating procedure request cases on a service portal.

</td></tr></tbody>
</table>

## Related

- [[install-pre-visit-mgmt|Install Pre-Visit Management]]
- [[pre-visit-assign-roles|Assign roles for Pre-Visit Management users]]
- [[pre-visit-approve-rca|Approving restricted caller access privileges for Pre-Visit Management]]
- [[pre-visit-proc-scheduler-grp|Determine who can work on the appointment booking task for a procedure]]
- [[pre-visit-config-proc-consent-time|Configure when to send the procedure consent form to a patient]]
- [[pre-visit-config-to-do-items|Specifying the to-do items for patients in Pre-Visit Management]]
- [[pre-visit-config-doc-decisions|Configuring the auto-generation of documents for procedure requests]]
- [[pre-visit-config-to-do|Configuring the patient portal to add a to-dos menu item for procedure request tasks]]
- [[pre-visit-config-playbook|Configuring playbooks for Pre-Visit Management]]
- [[pre-visit-config-emails|Configuring the Pre-Visit Management email notifications]]
- [[pre-visit-connector-contributor|Determining additional user profiles in Pre-Visit Management]]
- [[pre-visit-case-contributor|Setting up the process to create procedure request cases as a contributor]]
- [[pre-visit-mgmt-app|Pre-Visit Management]]
