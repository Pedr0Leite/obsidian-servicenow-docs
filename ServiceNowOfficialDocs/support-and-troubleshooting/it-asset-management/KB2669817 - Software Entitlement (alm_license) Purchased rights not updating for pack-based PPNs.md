---
title: "Software Entitlement (alm_license): Purchased rights not updating for pack-based PPNs"
aliases:
  - KB2669817
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2669817
kb_number: KB2669817
last_modified: 2025-12-08
---

## Issue

Purchased rights do not populate when creating a Software Entitlement for certain Product Part Numbers (PPNs). Users cannot proceed because the expected calculation does not occur on the entitlement form.

## Resolution

1.Restore the two OOB fields to the form layout

\- Open any Software Entitlement record (table alm\_license).

\- Form header → Configure → Form Layout.

\- Move Rights per license pack and Number of packs to the Selected column and Save.

2\. Create or edit the entitlement

\- Select the relevant PPN.

\- Ensure Rights per license pack is visible (read-only or prefilled as designed).

\- Enter Number of packs.

\- Confirm Purchased rights is automatically calculated able to save the record
