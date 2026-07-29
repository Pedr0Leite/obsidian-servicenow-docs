---
title: "Discovery Models, Lifecycle Data and Current Phase - FAQs "
aliases:
  - KB2516073
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2516073
kb_number: KB2516073
last_modified: 2025-09-17
---

## Discovery Models, Lifecycle Data and Current Phase - FAQs

  

### Summary

### Factors That Calculate the "Current Phase"

The Current Phase is determined based on lifecycle phase records defined for the corresponding software model. The calculation depends on:

-   Lifecycle phase entries (e.g., General Availability, End of Support, End of Life) stored in the software lifecycle table
-   Valid start dates for each phase
-   The current date in relation to these phase start dates
-   Phase precedence if date ranges overlap (e.g., End of Life takes priority over General Availability)
-   Data sources such as Publisher Pack content or manually entered lifecycle data
-   Successful execution of the _Generate Software Lifecycle Report_ job to refresh calculations
-   If no lifecycle phase entry exists, or dates are missing or misaligned, the Current Phase will remain empty.

### Why Can Normalized Software Models Have an Empty Current Phase?

Software model normalization ensures correct product name, publisher, version, and categorization but does not automatically populate lifecycle data. Lifecycle enrichment requires either:

-   Matching lifecycle data from a Publisher Pack, or
-   Manual addition of lifecycle phase records with valid start dates
-   Without lifecycle data, even fully normalized models will show an empty Current Phase.

### Why Lifecycle Reports May Show Rows with Empty Current Phase

The lifecycle report includes all software models in scope, regardless of whether lifecycle data exists. If no matching lifecycle phase record is found for a model, it will still appear in the report with a blank Current Phase.

### Why Don’t Fully Normalized Discovery Models Show Lifecycle Data?

Normalization ≠ Lifecycle Coverage.  
Normalization maps a Discovery Model to a Software Model with clean metadata (publisher/product/version), but it does not guarantee lifecycle content exists for that exact model.

-   For lifecycle data to appear, the following must be true:
-   The Discovery Model is mapped to a Software Model (normalization result).
-   That Software Model has at least one active lifecycle phase record (e.g., GA, End-of-Sale, End-of-Support, End-of-Life) with a valid start date.
-   The lifecycle record’s keys match the model’s identity at the expected level (usually publisher + product + version, sometimes edition/variant).
-   The lifecycle record is active, not expired-only, and has coherent, non-overlapping phase dates.

Why gaps occur even when “in sync with Content library”:

-   Content does not publish lifecycle data for every edition/patch/variant/platform (e.g., LTSC vs. SAC, Datacenter vs. Standard).
-   Your normalized Software Model may be more specific or more generic than the lifecycle entry, causing mismatches.
-   The product might be custom/local or niche, not covered by Content lifecycle data.
-   The model may be mapped to a suite component, while lifecycle exists only at the suite (parent) level.

Bottom line: Lifecycle appears only when the software model mapped from the discovery model has matching, active lifecycle phase records with valid start dates in the Content—or you add them manually.

### Why Do Discovery Models with Other Normalization Statuses Also Lack Lifecycle? Why Do Some Show Blank Current Phase?

-   Normalization status (Not/Partial/Full) does not determine lifecycle presence. Lifecycle is computed solely from lifecycle phase records on the software model.

Reasons for empty Current Phase in reports:

-   Lifecycle records exist but no phase is “current” today (e.g., GA ended, EOS/EOL undefined, or date gaps/overlaps prevent identifying a current phase).
-   Phase records lack start dates or are inactive.
-   Multiple conflicting lifecycle records prevent resolving a single current phase.
-   The lifecycle job ran before lifecycle data was added or activated, or timezone/date-format issues resulted in no active phase today.

Key point: If the lifecycle join succeeds but no phase evaluates as “current,” the row shows with an empty Current Phase.

### Why Are Many Discovery Models Still Missing Lifecycle After Running the Generate Software Lifecycle Report Job?

-   This job does not create lifecycle data; it only recalculates the Current Phase for models that already have valid lifecycle records.

If models remain blank after running the job:

-   No lifecycle record exists for the mapped Software Model (no Content coverage or manual addition).
-   Lifecycle record exists but lacks valid start dates, is inactive, or has date gaps/overlaps.
-   Model/edition/version does not match the lifecycle key published by Content (granularity mismatch).
-   Lifecycle exists on a parent/suite model, but the installation is tied to a component model.

Recommended actions:

-   Open the Software Model mapped from the Discovery Model and check its lifecycle phases.
-   If missing, add manual lifecycle data or adjust the model to match a Content-covered variant; or request Content coverage from ServiceNow.
-   If present, ensure at least one phase has a valid start date, is active, and dates don’t overlap.
-   Re-run the _Generate Software Lifecycle Report_ job.

### What Does “In-Scope” Mean for the Lifecycle Report? What Are the Inclusion Criteria?

-   “In-scope” means the model meets the report’s selection criteria, so it’s included in the dataset—even if lifecycle data is missing.

Common inclusion criteria:

-   Software Models tracked by your organization for lifecycle (often those linked from Discovery or with installations).
-   Models that are normalized or mapped to allow lifecycle joins.
-   Filters such as publisher, product category, model type, and optional flags (e.g., managed by SAM, active models).
-   Optionally, models with current installations to reduce noise.

Because the report is designed to highlight gaps, it often includes models without lifecycle data, explaining rows with blank Current Phase.
