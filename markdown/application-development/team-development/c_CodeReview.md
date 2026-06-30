---
title: Code reviews
description: Team Development administrators can require that pushes undergo code review before accepting pushes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/team-development/c\_CodeReview.html
release: australia
product: Team Development
classification: team-development
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Administer, Team Development, Planning your application, Building applications]
---

# Code reviews

[[team-development-landing|Team Development]] administrators can require that pushes undergo code review before accepting pushes.

When code review is enabled, pushing a change to the parent instance triggers the [[c_CodeReviewWorkflow|code review workflow]]. By default, users with the teamdev\_code\_reviewer role receive [[notifications|notifications]] to review changes and can approve or reject changes. The Team Development Code Reviewers has the teamdev\_code\_reviewer role.

For each change, reviewers can see the following information.

-   Which [remote instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/team-development/t_DefineARemoteInstance.md) the pushed change comes from.
-   Who pushed the change to the parent.
-   What the change is called.
-   When the change was created.
-   Which [[c_Versions|versions]] the change includes.

Reviewers must [[t_ApproveOrRejectAPush|approve or reject a push]] from the Team Development application.

While changes are being reviewed on the parent instance, a child instance cannot do the following activities involving the parent instance:

-   Push changes to the parent instance.
-   Pull changes from the parent instance.
-   [[t_Reconcile|Reconcile changes]] with the parent instance.
-   [[t_ChangeTheParentInstance|Change the parent instance]] to another instance.
-   Delete the remote instance record for the parent instance.

## Related

- [[team-development-landing|Team Development]]
- [[c_CodeReviewWorkflow|Code review workflow]]
- [[notifications|Notifications]]
- [[c_Versions|Versions]]
- [[t_ApproveOrRejectAPush|Approve or reject a push]]
- [[t_Reconcile|Reconcile changes]]
- [[t_ChangeTheParentInstance|Change the parent instance]]
