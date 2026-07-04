---
title: "Survey Preview not working and creates duplicate survey copies."
aliases:
  - KB0761214
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761214
kb_number: KB0761214
last_modified: 2024-04-08
---

## Survey Preview not working and creates duplicate survey copies.

  

### Issue

Survey Designer 'Preview' button in Survey designer gives an error and creates multiple copies of the survey.

### Cause

Custom business rule running on insert.

### Resolution

The behavior seen was due to custom business rule running on the Assessment Instance table. When previewing a survey, what the survey engine does is that it will create a temporary metric type copy and one survey instance with questions. This custom business rule runs on "insert" on "asmt\_assessment\_instance" table thus causing the duplicate.
