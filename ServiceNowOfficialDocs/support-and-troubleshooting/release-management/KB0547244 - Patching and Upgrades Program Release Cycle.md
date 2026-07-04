---
title: "Patching and Upgrades Program | Release Cycle"
aliases:
  - KB0547244
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547244
kb_number: KB0547244
last_modified: 2025-04-08
---

## Patching and Upgrades Program | Release Cycle

  

### Issue

The ServiceNow release cycle is designed to provide optimal stability and quality, with the flexibility to quickly address problems and deliver new features.  
Customer customizations are typically preserved throughout all upgrades. ServiceNow uses the concept of a family for a given feature set. For example, Quebec Patch 1 Hotfix 2 is in the Quebec family. A family contains:

-   A feature release that contains new functionality and fixes to existing functionality.
-   Patch releases and hotfixes that provide problem fixes and are released as needed.

Feature release notes are available in the [product documentation](https://docs.servicenow.com/ "product documentation") for all releases.

For information about the ServiceNow upgrade process, see [ServiceNow upgrades](https://docs.servicenow.com/bundle/rome-release-notes/page/release-notes/upgrades/reference/upgrade.html "ServiceNow upgrades").

For information about the ServiceNow Patching Program (SPP), refer to the [Patching Program FAQ](https://support.servicenow.com/kb_view.do?sysparm_article=KB0696901 "Patching Program FAQ").

For information about Early Releases, please see [Early Release Program](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB0718545 "Early Release Program") and [FAQs](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB0635446 "FAQs").

For more information about the general upgrade process, see [How to upgrade a ServiceNow instance and manage scheduled upgrades](/kb_view.do?sysparm_article=KB0541128 "How to update a ServiceNow instance and manage schduled upgrades").

###   
Release terminology

**Release type**  
  
This table defines the types of releases that may be available in a family.

<table class="internalTable" align=""><tbody><tr class="sphr"><td><strong>Type</strong></td><td><strong>Scope</strong></td></tr><tr class="sp"><td><strong>Feature release</strong></td><td><ul><li>Introduces new features, such as complete new solutions that customers can implement to add value to their organization.<br>New features are generally only available as part of a feature release.</li><li>Includes all available fixes to existing functionalities to date.</li><li>Is production-oriented; quality and stability are of the highest priority throughout the life cycle.</li></ul></td></tr><tr class="sp"><td><strong>Patch release</strong></td><td><ul><li>Supports existing functionalities with a collection of all known problem fixes to date.</li><li>Generally does not include new features, unless these are strictly bound to the known problems that have been fixed within the patch.</li></ul></td></tr><tr class="sp"><td><strong>Hotfix</strong></td><td><ul><li>Supports existing functionalities with a targeted and specific problem fix that has been found necessary to release before the next official patch. Problems of such high severity are generally detected during testing, but can be found at early availability release time, or later by customer support cases.</li><li>Generally does not include previous fixes for a given release, unless these are pre-requisites for the specific problem fix target.</li><li>Does not include new features.</li></ul></td></tr></tbody></table>

### Release Distribution Phases

**Feature releases**

Feature releases move through two phases of distribution for customers and partners:

-   Phase 1: Early access
-   Phase 2: On-demand or auto-upgrade scheduled based on available dates

The following table provides a brief summary:

<table class="internalTable" align=""><tbody><tr class="sphr"><td style="text-align: center;"><strong>Phase</strong></td><td><strong>How do I obtain&nbsp;a new feature release?</strong></td><td><strong>Is the feature release visible when&nbsp;</strong><strong>requesting an upgrade on Now Support (HI)?</strong></td><td><strong>Is there a maximum number of&nbsp;</strong><strong>customers that can upgrade per week?</strong></td></tr><tr class="sp"><td style="text-align: center;"><strong>Phase 1</strong></td><td>Register for the early release program to access the latest family</td><td>Yes, for registered customers</td><td>No</td></tr><tr class="sp"><td style="text-align: center;"><strong>Phase 2</strong></td><td>Request and receive the version&nbsp;at any time or be auto-upgraded</td><td>Yes, for all customers</td><td>No</td></tr></tbody></table>

**Patches and hotfixes**

-   Access to patches and public hotfixes are available as soon as they are released
-   Entitlements are provided to specific customers for Hot Fixes released for Controlled Availability
    

### Release cycle examples

Quebec was a feature release, thus the Quebec family includes:

1.  Quebec feature release
2.  Quebec patches
3.  Hotfixes  
    1.  Limited distribution hotfixes
    2.  Public hotfixes

For example:

-   Quebec = New features + a collection of fixes
-   Quebec Patch 1 (IP1) = Quebec + a collection of problem fixes
-   Quebec Patch 1 Hotfix 1 (QP1HF1) = Quebec + QP1 + a fix for a problem in QP1
-   Quebec Patch 1 Hotfix 2 (QP1HF2) = Quebec + QP1 + QP1HF1 + a fix for a different QP1 problem
-   Quebec Patch 2 (IP2) = Quebec + QP1 + a collection of problem fixes that may or may not include QP1HF1-QP1HF2, depending on if these hotfixes have been adopted by the official patch, or discarded with the official patch development.

![](Screen%20Shot%202021-04-06%20at%203.53.01%20PM.pngx)
