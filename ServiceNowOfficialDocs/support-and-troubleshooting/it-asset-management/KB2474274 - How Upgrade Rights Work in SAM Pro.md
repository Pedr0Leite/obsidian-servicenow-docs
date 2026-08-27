---
title: "How Upgrade Rights Work in SAM Pro"
aliases:
  - KB2474274
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2474274
kb_number: KB2474274
last_modified: 2025-08-29
---

## How Upgrade Rights Work in SAM Pro

  

### Summary

Step-by-Step: How Upgrade Rights Work in SAM Pro

-   Understand the Licensing Principle
    -   Upgrade rights allow a customer to use later versions of software without needing a new license, if their license includes upgrade rights.
        -   Example: A license for Autodesk 2023 with upgrade rights may also allow use of 2024 or 2025 versions.
-   Base Software Model Setup
    -   Ensure the base software model (e.g., Autodesk 2023) is created properly:
        -   Publisher: Autodesk
        -   Product: AutoCAD (example)
        -   Version: 2023
        -   Entitlement: Linked to the purchase or subscription 
-   Add Next Version(s) to Software Model
    -   To enable automatic entitlement shifting via upgrade rights, add "Next version" entries:
        -   Go to the Software Model record for 2023.
        -   In the Upgrade rights related list, click "New".
        -   Add 2024 as the next version.
        -   Then go to 2024’s model, and repeat by adding 2025 as next version. This builds a chain of upgrade rights: 2023 → 2024 → 2025
-   Install Records Detected
    -   The Discovery / SCCM integration pulls actual installations:
        -   It sees machines with Autodesk 2024 and 2025 installed.
        -   These installs initially won’t map to the 2023 license unless upgrade rights are configured.
-   Run the Reconciliation Job
    -   After configuring the upgrade chain:
        -   Go to Software Asset > License Workbench or run the reconciliation job manually/scheduled.
        -   The job checks if higher version installs (e.g., 2025) can legally be covered under 2023 entitlements using the upgrade path.
-   Entitlement Adjusts Automatically
    -   Once the job runs, the system evaluates:
        -   Is there an entitlement with upgrade rights?
        -   Does it cover the installed version?
        -   It then maps the install to the latest eligible entitlement in the upgrade path (i.e., 2025 Autodesk license).
        -   This is expected behavior—it’s how SAM ensures the correct entitlement is always applied for compliance.
-   Why Did the Entitlement Change from 2016 to 2019?  
    As in the video:
    -   When upgrade rights are enabled and higher version installs are detected, SAM moves the entitlement association to the newest install version in the upgrade chain.
    -   So if the oldest entitlement is 2016 and you’ve installed 2019, it gets mapped up the chain (2016 → 2017 → … → 2019).
    -   Same logic applies to your 2023 → 2025 Autodesk example.
-   Important Notes
    -   SAM will always map to the highest version possible via upgrade chain.
    -   You don’t lose the original entitlement; it's still valid—it’s just now used to cover a newer install version.
    -   If the install is for a version not in the upgrade chain, it won't match and will show as unlicensed.
