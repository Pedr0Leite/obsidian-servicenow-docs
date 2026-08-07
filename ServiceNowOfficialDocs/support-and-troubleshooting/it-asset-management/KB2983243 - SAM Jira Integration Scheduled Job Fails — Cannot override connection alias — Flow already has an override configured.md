---
title: "SAM Jira Integration Scheduled Job Fails — Cannot override connection alias — Flow already has an override configured"
aliases:
  - KB2983243
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2983243
kb_number: KB2983243
last_modified: 2026-04-27
---

## SAM Jira Integration Scheduled Job Fails — Cannot override connection alias — Flow already has an override configured

  

### Issue

The SAM - Refresh Jira Atlassian Integration Subscriptions scheduled job fails with the following error:

Cannot override connection alias. Flow jira\_download\_subscriptions already has an override configured for alias:<alias\_sys\_id>

Or after partial remediation, the error appears on a nested subflow:

Cannot override connection alias. Flow <subflow\_internal\_name> already has an override configured for alias:<alias\_sys\_id>

Manually triggering the Jira Download Subscriptions subflow directly in Flow Designer works without error. Only the scheduled job fails.

### Release

Not release specific

### Cause

A connection was configured directly on the subflow via Configure Connections in Flow Designer. The scheduled job also applies its own connection override at runtime via the Integration Profile. The Flow engine does not allow two overrides for the same alias in the same execution context and throws the error. Manual triggering works because only the static override is present in that path.

### Resolution

Do not configure a connection override directly on the Jira Download Subscriptions subflow or any nested subflow within the integration chain via the Configure Connections dialog in Flow Designer. If a connection has already been configured there, remove it and set it back to Use Default Connection.

The connection alias should only be set on the Integration Profile. The scheduled job reads it from there and applies it to the entire execution chain automatically at runtime.
