---
title: "Email client template fails to call up Email script"
aliases:
  - KB0791806
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791806
kb_number: KB0791806
last_modified: 2024-04-08
---

## Email client template fails to call up Email script

  

### Issue

The code: **email.setSubject** in an email script will not work when called in "Email Client Template" for example, with a  Major Incident Workbench use case.

### Cause

This functionality to call an Email script from an Email client template is not yet available out of the box.

### Resolution

We recommend that you create several Email client templates and then let the end user choose the most relevant template within the Email client interface, this will avoid having to call a script to dynamically populate an output in the Email body.
