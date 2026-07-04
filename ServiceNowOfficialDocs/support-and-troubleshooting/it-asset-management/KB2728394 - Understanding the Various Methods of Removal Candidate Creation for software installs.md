---
title: "Understanding the Various Methods of Removal Candidate Creation for software installs"
aliases:
  - KB2728394
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2728394
kb_number: KB2728394
last_modified: 2026-05-11
---

## Issue

How Removal candidates for software installs are created

## Resolution

Removal candidates for software installs are created in two different ways :

#### 1\. Reclamation Rule (Low‑Usage) Based Removal

-   When removal candidates are created through reclamation rules (e.g., low‑usage or last‑used logic), entitlements or allocations are not required.
-   Creation is based only on:
    -   Software installation records
    -   Usage records
    -   “Last used before” date
-   This behavior is described in [KB1178718](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1178718).

#### 2\. Compliance Remediation (Unallocated / Unlicensed)

In compliance scenarios, entitlements and allocations directly influence the creation of removal candidates.

-   Unallocated Installs: These are installations that could be covered by available entitlement rights but are not allocated. ServiceNow treats them as unauthorized, and the Remove Unallocated Installs remediation action automatically generates removal candidates.
-   Unlicensed Installs: These installations exceed available entitlement rights, resulting in non‑compliance. Using the Remove Unlicensed Installs remediation option automatically creates removal candidates to address the licensing deficit.

Both remediation paths ensure non‑compliant installations are identified and processed for removal outside of low‑usage reclamation rules.
