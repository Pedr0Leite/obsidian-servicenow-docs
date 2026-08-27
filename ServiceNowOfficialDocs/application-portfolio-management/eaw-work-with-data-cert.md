---
title: Working with data certification
description: In the Enterprise Architecture Workspace, enterprise architects can manage certifications alongside requests, assessments, and portfolio health insights without switching to separate modules. You can define rules for validating data \(for example, application lifecycle, technology standards\), automate recurring checks \(daily, monthly, quarterly\), assign certifiers to review and approve data. You can highlight overdue certifications and compliance gaps.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-work-with-data-cert.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-concept
---

# Working with data certification

In the [[ea-workspace|Enterprise Architecture Workspace]], enterprise architects can manage certifications alongside requests, assessments, and portfolio health insights without switching to separate modules. You can define rules for validating data \(for example, application lifecycle, technology standards\), automate recurring checks \(daily, monthly, quarterly\), assign certifiers to review and approve data. You can highlight overdue certifications and compliance gaps.

\[Omitted image "eaw-data-cert-intro.png"\] Alt text: Getting started with data certification

## Action and required role mapping for certification policies in the Enterprise Architecture Workspace

|Action|cmdb admin + sn\_apm.apm\_analyst|sn\_apm.apm\_analyst|
|------|---------------------------------|--------------------|
|View list of policies|Yes|Yes|
|View track progress|Yes|Yes|
|View policy by clicking a link to the policy|Yes|No|
|Create policy|Yes|No|
|Edit policy|Yes|No|
|Delete policy|Yes|Yes|
|Activate policy|Yes|Yes|
|Deactivate policy|Yes|Yes|
|Run certification|Yes|Yes|
|Complete certification through Track progress page|Yes|No|

-   **[[eaw-create-policy|Create a certification policy]]**  
Creating a data certification policy serves as a governance mechanism to ensure that the data used in [[application-portfolio-management-landing-page|enterprise architecture]] models and visualizations is accurate, complete, and trustworthy.
-   **[[eaw-data-cert-edit-policy|Edit a certification policy]]**  
Update an existing certification policy details.
-   **[[eaw-data-cert-view-policy|View certification policy]]**  
View details of a published policy.
-   **[[eaw-data-cert-publish-policy|Publish a certification policy]]**  
Publish a draft policy to activate it and enable certifications to be issued under that policy.
-   **[[eaw-data-cert-run-certification|Run certification for a policy]]**  
Run certification for published policies to generate a new certification instance for an active policy.
-   **[[eaw-data-cert-notification|Data certification task notifications]]**  
When a data certification policy runs in the Enterprise Architecture Workspace, the system automatically sends email notifications to task assignees as due dates approach. This notification behavior is provided by the CMDB Data Manager and does not require additional configuration in the Enterprise Architecture Workspace.
-   **[[eaw-data-cert-track-progress|Track progress of a certification policy]]**  
Monitor and review the certification policy status to track completion progress and view details such as total tasks, completed tasks, open tasks, and unassigned tasks.
-   **[[eaw-approve-data-cert-tasks|Review and certify data certification tasks]]**  
You can review and complete data certification tasks to confirm that records meet the standards defined in a certification policy. Certification tasks are generated when a policy is run and are assigned based on the policy's assignment configuration.
-   **[[eaw-data-cert-activate|Activate a certification policy]]**  
Activate a certification policy to add it to the active certification runs. This process ensures that the policy is active and can be used for certifications.
-   **[[eaw-data-cert-deactivate|Deactivate a certification policy]]**  
Deactivate a published policy to remove it from active certification runs. This process ensures that the policy is no longer active and can't be used for certifications.
-   **[[eaw-delete-data-cert|Delete a certification policy]]**  
Delete an unwanted certification policy permanently.

**Parent Topic:**[[eaw-managing-ea-workspace|Managing Enterprise Architecture Workspace]]

## Related

- [[eaw-create-policy|Create a certification policy]]
- [[eaw-data-cert-edit-policy|Edit a certification policy]]
- [[eaw-data-cert-view-policy|View certification policy]]
- [[eaw-data-cert-publish-policy|Publish a certification policy]]
- [[eaw-data-cert-run-certification|Run certification for a policy]]
- [[eaw-data-cert-notification|Data certification task notifications]]
- [[eaw-data-cert-track-progress|Track progress of a certification policy]]
- [[eaw-approve-data-cert-tasks|Review and certify data certification tasks]]
- [[eaw-data-cert-activate|Activate a certification policy]]
- [[eaw-data-cert-deactivate|Deactivate a certification policy]]
- [[eaw-delete-data-cert|Delete a certification policy]]
- [[eaw-managing-ea-workspace|Managing Enterprise Architecture Workspace]]
- [[ea-workspace|Enterprise Architecture Workspace]]
- [[application-portfolio-management-landing-page|Enterprise Architecture]]
