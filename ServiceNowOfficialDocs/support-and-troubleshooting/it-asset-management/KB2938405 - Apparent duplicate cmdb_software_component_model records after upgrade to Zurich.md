---
title: "Apparent duplicate cmdb_software_component_model records after upgrade to Zurich"
aliases:
  - KB2938405
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2938405
kb_number: KB2938405
last_modified: 2026-04-06
---

## Apparent duplicate cmdb\_software\_component\_model records after upgrade to Zurich

  

 

## Issue

Following an upgrade from Yokohama Patch 11 to Zurich, a large number of `cmdb_software_component_model` records appear to have been created in duplicate, with each Software Component Model entry appearing twice.

## Symptoms

-   After upgrading to Zurich, `cmdb_software_component_model` records appear doubled — approximately two records exist for each Software Install entry.
-   In each apparent pair, one record has the `build` field empty and the other has it populated with the normalized full version string.

## Facts

-   The affected table is `cmdb_software_component_model`.
-   The records are created by the `SamComponentModelGenerator` Script Include.
-   The behavior is controlled by the system property `com.snc.sam.software_component.choice.version_level`.
-   If this property is not explicitly defined on the instance, it defaults to `both`.
-   Under the `both` setting, two `cmdb_software_component_model` records are intentionally created per Software Discovery Model entry — one tracking the major version only and one tracking the full normalized version.
-   These are not duplicate records; they represent the same software tracked at two different version granularities simultaneously.

## Release

Zurich

## Cause

The system property `com.snc.sam.software_component.choice.version_level` was not explicitly set on the instance, causing it to operate on its default value of `both`. Under this setting, the `SamComponentModelGenerator` Script Include deliberately creates two `cmdb_software_component_model` records per Software Discovery Model entry:

-   **Record 1** — `version` field set to the normalized major version; `build` field left empty.
-   **Record 2** — `version` field set to the normalized major version; `build` field set to the normalized full version.

This is expected behavior by design. The records that appear to be duplicates are, in fact, the same software being tracked at two different version granularities simultaneously.

## Resolution

No corrective action is required if dual version-granularity tracking is acceptable. The behavior of this feature is fully configurable via the system property `com.snc.sam.software_component.choice.version_level`. The available values and their effect are as follows:

| Property Value | Records Created per Install | version Field | build Field |
| --- | --- | --- | --- |
| `both` (default) | 2 | Normalized major version | Empty on one record; normalized full version on the other |
| `major` | 1 | Normalized major version | Empty |
| `full` | 1 | Normalized major version | Normalized full version |
| `none` | 0 | — | — |

To set or update this property:

1.  Navigate to **System Properties** and search for `com.snc.sam.software_component.choice.version_level`.
2.  If the property does not exist on the instance, create it with the desired value.
3.  Set the value to `major`, `full`, or `none` based on the preferred version tracking granularity.

**Important:** Changing this property to `major`, `full`, or `none` affects only newly created records going forward. Records already created under the `both` default will remain and must be manually reviewed and cleaned up if desired. Confirm the preferred version tracking granularity before making any changes.

## Related Links

[Software Component Model table](https://www.servicenow.com/docs/r/it-asset-management/now-assist-for-software-asset-management-sam/software-component-model-table.html)
