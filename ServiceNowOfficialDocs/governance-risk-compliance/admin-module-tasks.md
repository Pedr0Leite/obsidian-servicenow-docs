---
title: Completing general administrative tasks
description: A user with the sn\_oper\_res.admin role can perform the setup tasks in the Operational Resilience application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/admin-module-tasks.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure, Operational Resilience, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Completing general administrative tasks

A user with the sn\_oper\_res.admin role can perform the setup tasks in the [[grc-opres-landing-page|Operational Resilience]] application.

## Admin module in the classic Operational Resilience view

If you have the sn\_oper\_res.admin role, you can configure the Admin module and set up the administrative tasks in the Operational Resilience Workspace as shown in the following example:

\[Omitted image "admin-tasks.png"\] Alt text: Admin module in the classic view.

A user with the sn\_oper\_res.admin role can set up the following entities by using the Admin module:

-   [[entity-type-in-risk-ws|Entity Types]]

    **Note:** Installing the Operational Resilience application inserts seed data to the Entity type \[sn\_grc\_profile\_type\] table. Both entity types and [[what-is-an-entity-filter|entity filters]] are installed as inactive. When you activate them, it could lead to generation of thousands of entity records.

-   Pillars
-   Scenarios
-   Event Groups
-   Events
-   Participant Roles
-   Important Choices
-   Importance and Impact Tolerance Rating Scale
-   Attestation Templates
-   [[airc-assessment-templates|Assessment Templates]]

**Note:** When you log in to the application as a user with the sn\_oper\_res.admin role, you can view the Admin module.

Operational Resilience administrators can create pillars and can also modify the reports on the dashboard.

**Note:** Though you can modify the entity types, their filters, and pillars as a user with the sn\_oper\_res.admin role, you must exercise proper caution while modifying them.

## Administrative setup tasks

As a user with the sn\_oper\_res.admin role, you can complete the following general setup tasks:

-   Create a scenario that represents a risk. For more information, see [[define-scenarios|Create a scenario and link it to an event]].
-   Classify an event by associating it with an event group. For more information, see [[create-event-group|Create an event group for the scenario]].
-   Create an event that you can associate with a scenario. For more information, see [[create-events|Create an event for the scenario]].
-   Add a participant role for your [[scenario-analysis-ov|scenario analysis]]. For more information, see [[add-participant-role|Add a participant role for the scenario analysis]].
-   Update the assessment rating by using the Important choices module. For more information, see [[set-up-important-choices|Update the Important choices module]].
-   Update the importance and impact rating scale. For more information, see [[create-importance-impact-rating-scale|Set up the Importance and Impact Tolerance Rating Scale]].
-   Create an attestation template. For more information, see [[create-new-attestation-template|Create and edit the attestation template]].

## Related

- [[define-scenarios|Create a scenario and link it to an event]]
- [[create-event-group|Create an event group for the scenario]]
- [[create-events|Create an event for the scenario]]
- [[add-participant-role|Add a participant role for the scenario analysis]]
- [[set-up-important-choices|Update the Important choices module]]
- [[create-importance-impact-rating-scale|Set up the Importance and Impact Tolerance Rating Scale]]
- [[create-new-attestation-template|Create and edit the attestation template]]
- [[grc-opres-landing-page|Operational Resilience]]
- [[entity-type-in-risk-ws|Entity types]]
- [[what-is-an-entity-filter|Entity filters]]
- [[airc-assessment-templates|Assessment templates]]
- [[scenario-analysis-ov|Scenario analysis]]
