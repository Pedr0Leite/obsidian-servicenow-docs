---
title: "How the \"SAM — Discovery Model to Software Model Matching\" scheduled job works"
aliases:
  - KB3023382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3023382
kb_number: KB3023382
last_modified: 2026-05-15
---

## How the "SAM — Discovery Model to Software Model Matching" scheduled job works

  

### Issue

#### Overview

The scheduled job "SAM — Discovery Model to Software Model Matching" assigns a software model reference to each discovery model record in the system. It runs as a parallelized background process, working through every publisher and product combination that has unassigned discovery models, and associates each one with the most appropriate software model available.

Important: The software model field populated on the discovery model record by this job is not used by the SAM reconciliation engine to calculate the compliance.

### Release

ALL

### Resolution

#### Resetting auto-matched records

Before any matching logic runs, the job performs a full reset of all previously auto-matched discovery model records. Any discovery model that was assigned by a prior run of this job — identified by having the auto-matched flag set to `true` — has its software model reference cleared and its auto-matched flag reset to `false`.

This ensures the job always re-evaluates the current state of the software model catalog on every run, picking up newly created or modified software models. Discovery models that were matched manually by a SAM administrator — identified by having the auto-matched flag set to `false` — are never affected by this reset. Manual matches are always preserved.  
  

#### Execution flow

##### Step 1 — Identify publishers with unassigned discovery models

The job queries the discovery model table to find every distinct publisher that has at least one discovery model where both the normalized publisher and normalized product fields are populated, and the software model reference is empty. Each publisher found becomes an independent parallel task. This allows the job to process large catalogs efficiently.

##### Step 2 — Identify products per publisher

Within each publisher task, the job queries the discovery model table again to find every distinct normalized product associated with that publisher where the software model reference is still empty. The job then processes each publisher and product combination individually.

##### Step 3 — Retrieve candidate software models

For each publisher and product combination, the job queries the software model table to retrieve all software models that match that publisher and product. These are the candidates evaluated in the following steps.

##### Step 4 — Build the software model tree

The retrieved candidate software models are passed into the Software Model Tree engine. This engine analyzes the relationships between all candidates and orders them from the most generic to the most specific, based on their version, edition, platform, and language operator definitions.

A software model is considered more specific when its field operators constrain to a narrower set of values — for example, a model scoped to a particular version and edition is more specific than a model scoped to any version and any edition. The tree represents these containment relationships, and the ordering it produces ensures that the most specific applicable software model is always evaluated and applied before a more general one.

##### Step 5 — Match and assign discovery models (most specific first)

The job iterates through the ordered software models, starting from the most specific. For each software model, it determines which discovery models are compatible with it. This compatibility check considers the normalized publisher, normalized product, version, edition, platform, and language fields on the discovery model against the operator-based definitions on the software model.

If the software model carries a software install condition, that condition is also included as an additional criterion when identifying compatible discovery models.

For each compatible discovery model found, the job checks whether a software model reference is already set on that record. If the field is empty, the job assigns the current software model to it and marks the record as auto-matched. If a software model reference is already present — whether from a previous iteration in the same run or from a manual match — the record is skipped. It is never overwritten.

This ordering and protection mechanism means that if a discovery model is compatible with both a specific software model and a general software model, it always receives the most specific one. The general software model cannot overwrite what the specific one already assigned.  
  

#### Key behaviors

-   Auto-matched records are always re-evaluated on every run. The reset at the start of each run clears all previously auto-matched assignments. The job re-evaluates the full catalog each time, so improvements to the software model catalog are automatically reflected on the next run.
-   Manual matches are always preserved. Any discovery model that a SAM administrator has explicitly matched — where the auto-matched flag is `false` — is never affected by the reset or by any assignment pass.
-   More specific software models always take precedence. The tree ordering ensures that a discovery model receives the narrowest applicable software model. Once assigned, it cannot be overwritten by a more general model within the same run.
-   Install conditions narrow the compatible discovery model set when present. When a software model carries an install condition, that condition is included as an additional filter when determining compatible discovery models.
