---
title: "How are potential savings in a Removal Candidate calculated?"
aliases:
  - KB1931828
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1931828
kb_number: KB1931828
last_modified: 2025-10-08
---

## How are potential savings in a Removal Candidate calculated?

  

## Query

Removal candidates have the **“Potential savings”** field populated with a currency value, **how is this cost calculated?**

* * *

### Answer

The **“Potential savings”** associated with a reclamation candidate is derived from the `avg_price` value found in the related **License Metric Result (LMR)**.

The current LMR can be found on the related software install/subscription record in the **"License Metric Result"** field.

### Calculation Formula

The `avg_price` is calculated as:

**Average Price = (Sum of Total Cost for all ‘In Use’ entitlements) ÷ (Sum of Purchased Rights for all 'In Use' entitlements)**

* * *

### Notes

-   This calculation ensures that the cost reflects actual usage and entitlement distribution.
-   The `avg_price` is a dynamic metric and may vary based on entitlement status and cost updates.
