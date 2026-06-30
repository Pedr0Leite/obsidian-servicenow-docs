---
title: Configuring the Recommended Actions application
description: As an admin, configure the Recommended Actions application to display relevant actions to your agents based on a record context.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configure-recommended-actions.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Recommended Actions configuration, Implement Intelligence, Configure, Customer Service Management]
---

# Configuring the Recommended Actions application

As an admin, configure the [[configure-nba|Recommended Actions]] application to display relevant actions to your agents based on a record context.

## Recommended actions

You can configure recommended actions by following these steps.

<table id="table_jm3_lm4_15b"><thead><tr><th>

Step

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[ra-csm-contexts-create|Create a context]]

</td><td>

A context enables agents to see recommendations for records from a specific table, such as the Case table.

</td></tr><tr><td>

[[ra-csm-create-context-inputs|Create a context input]]

</td><td>

A context input enables you to associate entities beyond just the context table with a context ensuring that recommendations are updated dynamically as the context evolves.**Note:** This step is not mandatory.

</td></tr><tr><td>

[[ra-csm-rules-create|Create a rule for a context]]

</td><td>

A rule is a set of conditions that applies to a context and determines when a recommended action appears.

 When you create a rule:

-   Select conditions that apply to the context table.
-   Select the roles that have access to the recommended actions.

**Note:** New [[gamification-components-rules|rules]] can only be created from within a context.

</td></tr><tr><td>

[[ra-csm-recommendations-create|Create a recommendation for a rule]]

</td><td>

A recommendation is a way to suggest an action to an agent.

 Create a recommendation by selecting one of the recommendation types available on the New Recommendation screen:

-   Guidance
-   Guided decision tree
-   Field recommendation

**Note:** New recommendations can only be created from within a rule.

</td></tr></tbody>
</table>## Action types

With the Recommended Actions application, you can create the following types of actions for agents to take.

<table id="table_nxk_y1t_c5b"><thead><tr><th>

Action type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Guidance

</td><td>

An action that an agent can take or information that they can share. For example, a guidance can recommend that an agent can view and attach a knowledge article to a case or [[create-work-orders|create a work order]].

</td></tr><tr><td>

Guided decision tree

</td><td>

A guided flow to follow. A decision tree is a multi-step process that includes a series of questions and answers and results in guidance.

</td></tr><tr><td>

Field recommendation

</td><td>

A recommended value to use for a field. For example, this type of action can recommend the assignment group based on the text in the case short description.

</td></tr></tbody>
</table>For more information, see [[ra-csm-config-recommendations|Creating guidance and field recommendation in Recommended Actions]].

## Resource generators

Configure resource generators to provide information that you can use as inputs to actions such as guidances and field recommendations. Configuration of decision trees don’t require resource generators. For more information, see [[ra-csm-resource-generators-create|Create a resource generator in Recommended Actions]].

## Arbitration parameters

Configure arbitration parameters to determine the frequency of issues or the priority order of the recommended actions so that agents get the guidance that they must help resolve customer issues. For more information, see [[configure-nba-arbitration-param|Configure the arbitration parameters in Recommended Actions]].

## Related

- [[ra-csm-contexts-create|Create a context in Recommended Actions]]
- [[ra-csm-create-context-inputs|Create a context input in Recommended Actions]]
- [[ra-csm-rules-create|Create a rule in Recommended Actions]]
- [[ra-csm-recommendations-create|Create a recommendation in Recommended Actions]]
- [[ra-csm-config-recommendations|Creating guidance and field recommendation in Recommended Actions]]
- [[ra-csm-resource-generators-create|Create a resource generator in Recommended Actions]]
- [[configure-nba-arbitration-param|Configure the arbitration parameters in Recommended Actions]]
- [[configure-nba|Recommended Actions]]
- [[gamification-components-rules|Rules]]
- [[create-work-orders|Create a work order]]
