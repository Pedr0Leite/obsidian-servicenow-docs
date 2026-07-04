---
title: "Smiley template images not showing on Survey"
aliases:
  - KB0782279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782279
kb_number: KB0782279
last_modified: 2026-02-26
---

## Issue

A survey template was configured to include some smiley images in to the "Assessment Template Definitions".

When viewing the survey through the "Survey Designer", the images are visible however they are not visible into the "Preview" or on the actual survey.

The images were manually added into the template and the 'Allow Image' field on the survey template form is checked.

## Resolution

Check each of the assessment definition records on the template and make sure that both "Selected Image" and "Unselected Image" is set for each of them.
