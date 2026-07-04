---
title: "Which License Metrics are supported for Downgrade/Upgrade in Software Asset Management"
aliases:
  - KB0791783
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791783
kb_number: KB0791783
last_modified: 2024-04-08
---

## Which License Metrics are supported for Downgrade/Upgrade in Software Asset Management

  

### Issue

The concept of upgrading and downgrading licenses is built into the Software Asset Management plugin feature.This is helpful when reconciling licenses.

Downgrading a license is the process of purchasing a license, but using an earlier version.

Upgrading a license occurs when a newer version of a license is not purchased, but you are allowed to use the newer version. Downgrading is more common than upgrading.

Not all the License Metrics are supported for "Downgrade/Upgrade".

### Release

All Versions.

### Resolution

Prior to New York release, the only supported downgrades/upgrades rights are:

-   -   Per User
    -   Per Named User
    -   Per Device
    -   Per Named Device

In the New York release, we added downgrade/upgrade support for the following MS license metrics.

-   -   Per Core (New)
    -   Per Core (with CAL)
    -   Server (Per Instance)
    -   Server (Per Server)
    -   Per Processor
