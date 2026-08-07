---
title: "Duplicate models are getting created by Discovery and SCCM"
aliases:
  - KB0727769
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727769
kb_number: KB0727769
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Duplicate models are getting created by discovery and SCCM constantly

# Release

* * *

All

# Cause

* * *

If Field Normalization (FS) plugin is setup to normalize core\_company table, and Normalization Data Services (NDS) plugin (which is hard-coded to normalize core\_company table) is also active. Weird behavior will happen if both plugins are setup to normalize core\_company. Before inserted a new model record, we first query to see if model already exists based on model name and company name, so causes duplicate models. The two plugins were not designed to both normalize the same table; You must pick one plugin or the other to normalize core\_company. 

# Resolution

* * *

Customer should pick only one plugin either Field Normalization (FS) or Normalization Data Services (NDS) plugin active at a time  to normalize core\_company
