---
title: "Why does an Adobe Creative Cloud reclamation candidate show Justifciation as \"Low Usage\" instead of \"Consolidated subscriptions\"?"
aliases:
  - KB3014800
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3014800
kb_number: KB3014800
last_modified: 2026-05-29
---

## Why does an Adobe Creative Cloud reclamation candidate show Justifciation as "Low Usage" instead of "Consolidated subscriptions"?

  

### Issue

A reclamation candidate is created for an Adobe Creative Cloud All Apps subscription.

The Description may state that the user is not using three or more products included in the Adobe Creative Cloud All Apps subscription and that the subscription will be replaced with subscriptions to the products currently being used.

Example:

> Based on your usage, it is determined that you are not using 3 or more products included in your Adobe Creative Cloud All Apps subscription. As a result, your subscription will be replaced with subscriptions to the products that you are currently using.

However, the Justification field shows:

> Low Usage

Users may expect the justification to show:

> Consolidated subscriptions

### Symptoms

Adobe Creative Cloud reclamation candidates may show Justification = Low Usage even when the candidate description states that the user’s Adobe Creative Cloud All Apps subscription will be replaced with one or more specific Adobe product subscriptions.

### Facts

The Adobe optimization logic uses different candidate creation paths depending on the user’s subscription and usage pattern.

When the user has an All Apps subscription and the product usage count is below the configured threshold, the logic creates an All Apps low-usage reclamation candidate. In that flow, the candidate justification is explicitly set to `low_usage`, which is displayed as Low Usage in the UI.

The `consolidate_subscription` justification is used in a separate flow where multiple single-app subscriptions qualify to be consolidated into an All Apps subscription

### Release

NA

### Cause

This behavior is expected and is based on how Adobe Creative Cloud optimization candidates are generated.

There are two different optimization scenarios:

### Scenario 1: All Apps subscription is replaced with specific used products

This occurs when a user has an Adobe Creative Cloud All Apps subscription but is using fewer products than the threshold configured in the reclamation rule.

For example:

-   User has Adobe Creative Cloud All Apps.
-   The subscribed products threshold is set to 3.
-   User is only using Illustrator.
-   The system recommends replacing All Apps with Illustrator.

In this scenario, the candidate is considered an All Apps low-usage candidate. Therefore, the Justification field is set to Low Usage.

This is why the description may reference subscription replacement, while the justification still shows Low Usage. The replacement recommendation is driven by the fact that the All Apps subscription is underused.

### Scenario 2: Multiple single-app subscriptions are consolidated into All Apps

This occurs when a user has multiple Adobe single-app subscriptions and the system determines that it is better to consolidate them into an Adobe Creative Cloud All Apps subscription.

For example:

-   User has Photoshop, Illustrator, and Acrobat single-app subscriptions.
-   The subscribed products threshold is set to 3.
-   The user is actively using enough Adobe products to meet the configured threshold.
-   The system recommends consolidating those single-app subscriptions into All Apps.

In this scenario, the Justification field is set to Consolidated subscriptions.

## Expected behavior

For a candidate where the user has Adobe Creative Cloud All Apps and the recommendation is to replace it with only the products currently being used, the expected justification is:

> Low Usage

For a candidate where multiple single-app subscriptions are being consolidated into an All Apps subscription, the expected justification is:

> Consolidated subscriptions

### Resolution

No action is required. The behavior is working as designed.

The description provides the recommendation details, while the Justification field reflects the reason the candidate was created.

## Additional validation steps : 

To confirm the behavior, review the related Creative Cloud reclamation rule and affected candidate:

1.  Open the affected Adobe Creative Cloud reclamation candidate.
2.  Confirm the user has an Adobe Creative Cloud All Apps subscription.
3.  Review the candidate description and assigned replacement subscriptions.
4.  Open the related Creative Cloud reclamation rule.
5.  Confirm the Subscribed Products Threshold value.
6.  Confirm the user is using fewer products than the configured threshold.

If the user has All Apps and usage is below the threshold, Low Usage is expected.
