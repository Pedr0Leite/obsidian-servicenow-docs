---
title: "IBM license compliance and Architecture Process "
aliases:
  - KB2702183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2702183
kb_number: KB2702183
last_modified: 2026-02-09
---

## Issue

IBM sub-capacity requirements mandate hardware capacity scans to be run every 30-minutes, and we understand that "devices to scan" section under IBM license compliance defaults the scan frequency to 30-minutes for gathering hardware capacity.This KB walks through about how the 30-minute scan configurations and defaults

## Resolution

## Architecture Process Flow Overview

### IBM Authorized SAM Provider (IASP) Integrations

#### Discovery

ServiceNow File-Based Discovery identifies IBM component installations across the environment. However, some required details—such as file names, file maps, and file set content—may not always be fully available within ServiceNow.

IASPs supplement this gap by:Providing enriched file and component details through extension tables, or Manually normalizing entries found in the _Unidentified Filenames_ table.This ensures a more complete and accurate discovery of IBM software components.

### Classification

ServiceNow leverages IASPs to accurately classify IBM component installations.

As part of this process:IASPs retrieve entitlement data, discovered component installations, and prior classification information from the ServiceNow instance.

IASPs then apply updated classification logic and push the new classification results back into ServiceNow.

Data is sent via scripted REST APIs into Import Set tables and transformed into target tables in controlled batches of up to 1,000 records.

This integration ensures consistent and compliant classification of IBM software.

### Synchronization of New Installations

When new IBM component installations are discovered in ServiceNow, corresponding classification records must also be created.

This synchronization is handled automatically through a daily scheduled job, ensuring that all newly discovered installations are included in the classification process without manual intervention.

## IBM Usage Calculation – How It Works

IBM licensing follows a High-Water Mark (HWM) model. This model determines licensing requirements based on the maximum resource usage observed over a defined period—typically 90 days—rather than average or current usage.

### High-Water Mark Licensing

#### Resource Monitoring

IBM tools continuously monitor resource consumption across the infrastructure, including metrics such as:

CPU cores,Virtual cores,Memory,Virtual machines

Infrastructure usage snapshots are typically captured every 30 minutes to ensure accuracy and completeness.

#### Daily Peak Calculation

For each day:The highest resource usage observed for a given IBM product or classification is recorded.

This ensures that even short-duration usage spikes are captured and accounted for.

**Infrastructure Scanning**

IBM requires infrastructure snapshots to be collected every 30 minutes. ServiceNow supports this requirement by using different data collection strategies depending on the infrastructure type, ensuring alignment with IBM compliance expectations.

Ref:[https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/task/specify-vm-managers-anglepoint-integration.html](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/task/specify-vm-managers-anglepoint-integration.html)
