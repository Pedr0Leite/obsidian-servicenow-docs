---
title: "Planned maintenance schedule triggerd twice when only expected to trigger once"
aliases:
  - KB0696141
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696141
kb_number: KB0696141
last_modified: 2024-04-07
---

## Planned maintenance schedule triggerd twice when only expected to trigger once

  

### Issue

# Symptoms

* * *

A maintenance schedule that is configured to run once a month ran twice, on the expected day and the following day.

# Release

* * *

Kingston Patch 6

# Cause

* * *

The Maintenance Schedule Due time was set after the the Planned Maintenance Nightly Run scheduled job.

# Resolution

* * *

The Maintenance Schedule Due time should be set before the the Planned Maintenance Nightly Run scheduled job.
