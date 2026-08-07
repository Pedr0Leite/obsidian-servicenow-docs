---
title: "SAM suite inference links unrelated software models through Microsoft downgrade rights chain"
aliases:
  - KB3035098
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3035098
kb_number: KB3035098
last_modified: 2026-05-21
---

## SAM suite inference links unrelated software models through Microsoft downgrade rights chain

  

## Issue

The SAM suite inference engine may infer software models (e.g. Microsoft Windows 10) into suites they do not directly belong to (e.g. Microsoft Visual Studio with GitHub Professional) due to the downgrade rights chain from the Enterprise edition.

## Symptoms

-   Software models appear under unexpected suites in reconciliation results
-   Microsoft Windows 10 installations counted under Visual Studio Enterprise entitlement
-   Suite inference results include products with no direct suite child relationship
-   Reconciliation shows unexpected license consumption for suites

## Cause

The **SAMSuiteEngine** runs two stages:

1.  Build suite structure from **cmdb\_m2m\_suite\_model** and entitlements
2.  Infer best suite via ranking rules

Rule 4 (tiebreaker) prefers the suite with the lower downgrade-rights count. The downgrade rights chain spans three tables:

-   **samp\_dmap\_downgrade\_model** (source from content service)
-   **samp\_sw\_downgrade\_model** (consolidated)
-   Entitlements

The scheduled job **SAM - Create downgrades/upgrades for a software entitlement** walks the downgrade map. Suite children edges (**cmdb\_m2m\_suite\_model**) and downgrade edges (**samp\_sw\_downgrade\_model**) are separate tables, but the inference ranking algorithm uses downgrade-rights depth as a tiebreaker. This causes the downgrade traversal to pull Windows 10 under Visual Studio Enterprise via the downgrade chain during ranking, even though Windows 10 is not a direct suite child.

## Resolution

1.  This is expected behavior based on the downgrade rights model in the content library.
2.  To control which installations get counted under a specific suite, use **Product Install Conditions** (**samp\_sw\_product\_install\_condition**) to filter which installations are eligible for suite membership.
3.  Review the downgrade rights chain for the affected suite: navigate to **samp\_sw\_downgrade\_model** and trace the path from the Enterprise edition to the base product.
4.  If the inference is producing incorrect results for your licensing compliance, contact your SAM administrator to adjust the Product Install Conditions for the affected suite.
