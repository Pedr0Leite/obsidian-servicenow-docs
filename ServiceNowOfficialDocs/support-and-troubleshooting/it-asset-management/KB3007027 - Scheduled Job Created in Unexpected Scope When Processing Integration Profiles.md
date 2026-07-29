---
title: "Scheduled Job Created in Unexpected Scope When Processing Integration Profiles"
aliases:
  - KB3007027
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3007027
kb_number: KB3007027
last_modified: 2026-05-07
---

## Scheduled Job Created in Unexpected Scope When Processing Integration Profiles

  

### Issue

When an Integration Profile is created, the background job "Process Integration Profiles and Stale Shipments" (from the Asset Management Common application) runs once and automatically creates a corresponding Scheduled Job record. In certain environments, the generated scheduled job appears under an unexpected application scope instead of the default Global scope.

### Release

Not release specific

### Cause

The job that creates the scheduled job record does not explicitly set an application scope. By default, scheduled jobs of this type are created in the Global scope. The scope is not inherited from the Integration Profile or from the job that triggers the creation. If a scheduled job is created under a scope other than Global, this is typically due to custom scripts or scoped processes that alter the creation context at the time the job runs.

### Resolution

This behavior is by design. By default, the scheduled job is created in the Global scope, which is the expected behavior.

If the scheduled job appears under a different scope in your environment, review any custom scripts or scoped processes that may be running at the time the Integration Profile is created, as these can alter the application context during record creation.
