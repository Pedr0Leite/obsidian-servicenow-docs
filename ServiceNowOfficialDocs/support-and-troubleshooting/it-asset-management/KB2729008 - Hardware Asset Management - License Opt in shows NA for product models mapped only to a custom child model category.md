---
title: "Hardware Asset Management - \"License Opt in\" shows NA for product models mapped only to a custom child model category"
aliases:
  - KB2729008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2729008
kb_number: KB2729008
last_modified: 2026-01-21
---

## Hardware Asset Management - "License Opt in" shows NA for product models mapped only to a custom child model category

  

## Table of Contents

-   [Issue](#mcetoc_1jfg2fb8c3e)
-   [Symptoms](#mcetoc_1jfg2fb8c3f)
-   [Cause](#mcetoc_1jfg2fb8c3g)
-   [How the field is evaluated (OOB logic)](#mcetoc_1jfg2fb8c3h)
-   [Why custom child categories without a OOB parent category show NA](#mcetoc_1jfg2fb8c3i)
-   [Common misconceptions (and clarifications)](#mcetoc_1jfg2fb8c3j)
    -   ["NA means the model is not eligible for HAM."](#mcetoc_1jfg2fb8c3k)
    -   ["Normalization won’t work when the field shows NA."](#mcetoc_1jfg2fb8c3l)
-   [Resolution](#mcetoc_1jfg2fb8c3m)
-   [Related links](#mcetoc_1jfg2fb8c3n)

## Issue

When a hardware product model is mapped only to a custom model category that is a child of an opted‑in OOB parent model category, the License Opt in field (norm\_license\_opt\_in) on the product model shows NA instead of Yes.

Removing the OOB parent category from the product model and leaving only its custom child category causes norm\_license\_opt\_in to change from Y to NA.

Even though license opt in displays NA for the custom model category, HAM licensing and normalization features continue to include models whose effective eligibility comes via the opted‑in OOB parent category. 

## Symptoms

Map a product model only to a custom child category that lacks resource\_category, save, and observe norm\_license\_opt\_in → NA.  
Add the opted‑in parent category and save again → Y.

## Cause

This is **working as designed**. The License Opt in field on the product model reflects **only the direct resource‑category association of the mapped model categories**.

It does **not inherit from parent categories**. If the mapped custom model category itself does not have a resource\_category populated, the product model’s norm\_license\_opt\_in evaluates to NA, even when the parent model category is opted in.

## How the field is evaluated (OOB logic)

The logic is performed by the following script include: HAMUtils

Single model category mapped  
If the product model has one model category, the platform fetches that category and returns:

`Y if the category’s resource_category.opt_in == true`  
`N if the category’s resource_category.opt_in == false`  
`NA if the category has no resource_category set.` 

Multiple model categories mapped

`Y if any mapped category has resource_category.opt_in == true`  
`NA if any mapped category has no resource_category`  
`N if any mapped category has resource_category.opt_in == false`  
`Default NA`

A custom child category without resource\_category therefore forces NA unless another mapped category explicitly returns Y or N first. 

## Why custom child categories without a OOB parent category show NA

Custom child categories typically do not have resource\_category populated OOB. When a product model is mapped only to such a custom child category, the logic above evaluates to NA. This does not negate the effective eligibility via the opted‑in parent; it only reflects that the direct association is missing on the child. 

## Common misconceptions (and clarifications)

### "NA means the model is not eligible for HAM."

-   Eligibility via hierarchy (opted‑in parent) still applies even when the field shows NA.

### "Normalization won’t work when the field shows NA."

-   Normalization and HAM workflows consider effective licensing through parent categories; the field’s NA does not, by itself, block those flows.

## Resolution

**Keep the opted‑in parent OOB model category mapped to the product model.**

If you would like the License Opt in field to **display Y for operational/reporting purposes, keep (or add back) the parent OOB category alongside the custom child category** so that the logic discussed above sees a category with resource\_category.opt\_in == true.

## Related links

[Hardware Asset Management licensing](https://www.servicenow.com/docs/csh?topicname=ham-licensing.html&version=latest)

[Opt-in or opt-out of HAM license resource categories](https://www.servicenow.com/docs/csh?topicname=optin-optout-ham-license-resource-categories.html&version=latest)
