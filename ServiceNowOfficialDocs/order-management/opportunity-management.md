---
title: Opportunity Management
description: The ServiceNow Opportunity Management application enables your sales agents and account executives to analyze customer needs and generate product recommendations for potential customers.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/opportunity-management.html
release: australia
topic_type: concept
last_updated: "2026-06-10"
reading_time_minutes: 4
breadcrumb: [Lead and opportunity management, Explore, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-concept
---

# Opportunity Management

The ServiceNow® Opportunity Management application enables your sales agents and account executives to analyze customer needs and generate product recommendations for potential customers.

An opportunity in [[order-mgt-overview|Sales Customer Relationship Management]] provides complete information about a product or service based on the needs of a customer \(called a qualified lead\). A lead for a product is the minimal information that a sales agent uses to advance the conversation with a potential customer and [[create-new-opportunity|create an opportunity]].

\[Omitted image "l2c-quote-workflow.png"\] Alt text: Sales CRM workflow that shows the opportunity, quote, and order creation steps.

## Opportunity Management interface

The Opportunity Management application is integrated with the Product Catalog and product configurator to help sales agents access product offerings to build opportunities. The Opportunity Management interface contains the following tabs:

<table id="table_enp_xnv_c1c"><thead><tr><th>

Tab

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[opportunity-management-details-tab|Details]]

</td><td>

Add basic information for the opportunity.

</td></tr><tr><td>

Catalog tab

</td><td>

Search for and add product offerings to your opportunity.

</td></tr><tr><td>

[[opp-mgmt-use-needs-analysis|Needs]]

</td><td>

Lists the need templates that provide product recommendations for the opportunity.

</td></tr><tr><td>

[[opportunity-management-line-items-tab|Line Items]]

</td><td>

Add different line items to an opportunity.

</td></tr><tr><td>

[[manage-allocations|Allocations]]

</td><td>

Distribute sales credit across multiple contributors on a single opportunity.

</td></tr><tr><td>

[[opportunity-management-competitors-tab|Competitors]]

</td><td>

Record competitor information.

</td></tr><tr><td>

[[opportunity-management-tasks-tab|Tasks]]

</td><td>

Create opportunity tasks.

</td></tr><tr><td>

[[create-new-opportunity-team-member|Team]]

</td><td>

Create opportunity team members.

</td></tr><tr><td>

[[add-opportunity-associated-contact|Contacts]]

</td><td>

Create opportunity associated contacts.

</td></tr><tr><td>

[[opportunity-management-emails-tab|Emails]]

</td><td>

Create emails to send to the required stakeholders.

</td></tr><tr><td>

[[opportunity-management-create-quote|Quotes]]

</td><td>

Create quotes directly from opportunities.

</td></tr><tr><td>

Related Channel Partners

</td><td>

Add authorized service organizations or partner entities \(for example, referral or influencer partners\) linked to a customer opportunity. Related channel partners can be:

-   Authorized organization: Full permissions to access, view, edit, or [[Modify|modify]] opportunity details
-   Listed organization: Only for tracking purposes. No permissions to view, access, edit, or delete opportunity details

</td></tr></tbody>
</table>## Opportunity snapshot

Opportunity Snapshot is an AI-enabled widget that appears on an opportunity record. It is a distinct panel provides sales agents and managers with an AI-generated summary and insights about the opportunity without reviewing all activity, contacts, and deal data on the record.

The widget has two sections:

1.  **Summary**: An at-a-glance summary of key deal information, including:

    -   Deal size and scope \(number of users, contract value\)
    -   Most recent meeting with the Champion \(title and recency\)
    -   Most recent activity \(for example, a check-in email\) and when it occurred
    This provides a brief summary of the deal status, drawn from opportunity [[fields|fields]], related activities, and contact data.

2.  **Insights**: This section combines automated scoring with AI-generated deal intelligence:

    -   Probability Score — A numerical score \(0–100\) representing the likelihood the opportunity will close. In the screenshot, the score is 64.
    -   Numbered insight cards — Contextual, plain-language observations derived from opportunity signals, such as:
        -   Competitor activity detected in recent meetings
        -   Champion engagement patterns \(for example, being unresponsive, canceling demos\)
        -   Benchmarks against similar deals \(for example, "Opportunities with similar stall patterns have 35% lower close rate at this stage"\)

## Integrating pricing in Opportunity Management

Opportunity Management integrates with the pricing engine to consume the default price list and displays the total price and unit price of product offerings in your opportunity.

Based on the prices of product offerings \(POs\) that are added to the opportunity, the total price values are auto-calculated. For more information, see [Add and view the details of an opportunity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/opportunity-management-details-tab.md) and [Add line items to an opportunity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/opportunity-management-line-items-tab.md).

Pricing in Opportunity Management provides the following benefits:

-   Revenue forecasting: The pricing engine helps agents evaluate an opportunity's total worth by computing the combined prices of each offering included, which in turn helps teams to strategize resource or budget allocation for deals.
-   Deal prioritization: By analyzing the potential revenue of each opportunity, your sales team can focus on the deals based on their financial impact. For example, teams can focus on deals with higher potential revenue and higher margins.
-   Negotiation enhancement: The pricing engine gives your sales team real-time pricing insights, which enhances the negotiation process by enabling your sales team to tailor offers that meet customer needs while maintaining profitability.

To learn more about pricing, see [[pricing-management|Pricing Management]].

## What to explore next

To learn about setting up Opportunity Management, see [[configure-opportunity-mgmt|Install and configure Opportunity Management]].

## Related

- [[opportunity-management-details-tab|Add and view the details of an opportunity]]
- [[opp-mgmt-use-needs-analysis|Get product recommendations for opportunities using needs analysis]]
- [[opportunity-management-line-items-tab|Add line items to an opportunity]]
- [[manage-allocations|Manage allocations]]
- [[opportunity-management-competitors-tab|Add competitors to an opportunity]]
- [[opportunity-management-tasks-tab|Add opportunity tasks]]
- [[create-new-opportunity-team-member|Add a new opportunity team member]]
- [[add-opportunity-associated-contact|Add an opportunity associated contact]]
- [[opportunity-management-emails-tab|Compose emails]]
- [[opportunity-management-create-quote|Create a quote from an opportunity]]
- [[pricing-management|Pricing Management]]
- [[configure-opportunity-mgmt|Install and configure Opportunity Management]]
- [[order-mgt-overview|Sales Customer Relationship Management]]
- [[create-new-opportunity|Create an opportunity]]
- [[Modify|Modify]]
- [[fields|Fields]]
