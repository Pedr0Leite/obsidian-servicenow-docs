---
title: "Assignment Rule is not working - incidents are created without an assignment group"
aliases:
  - KB0713093
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713093
kb_number: KB0713093
last_modified: 2026-06-03
---

## Assignment Rule is not working - incidents are created without an assignment group

  

### Issue

Incidents are being created without any value populated in the Assignment Group field (Assignment Rule is failing).

### Cause

The user has a custom Script in their Assignment Rule, and their Script is throwing a syntax error:

WARNING \*\*\* WARNING \*\*\* Javascript compiler exception: syntax error

### Resolution

It was recommended that the user review their custom code internally with their development team to resolve the syntax error(s).

ServiceNow Support handles OOB (Out of Box) break-fix behaviors. The behavior seen is not resulting from an OOB Assignment Rule - it is an Assignment Rule configured with a customized Script which is failing. ServiceNow Support is not trained to debug custom code or to provide assistance with implementation of custom code.

It is sufficient that Support has provided the location where the code is failing (line X or Y) and why (JavaScript syntax error).
