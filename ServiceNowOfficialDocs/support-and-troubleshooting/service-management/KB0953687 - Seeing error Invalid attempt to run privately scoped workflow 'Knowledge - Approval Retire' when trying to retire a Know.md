---
title: "Seeing error \"Invalid attempt to run privately scoped workflow 'Knowledge - Approval Retire'\" when trying to retire a Knowledge Article"
aliases:
  - KB0953687
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953687
kb_number: KB0953687
last_modified: 2025-03-31
---

## Seeing error "Invalid attempt to run privately scoped workflow 'Knowledge - Approval Retire'" when trying to retire a Knowledge Article

  

### Issue

When the user was clicking the "Retire" UI Action on their Knowledge Article (KA) in an attempt to retire the KA, the error "Invalid attempt to run privately scoped workflow 'Knowledge - Approval Retire'" was thrown. The user wanted to know why this was, as they could not retire any of their KAs as a result.

### Cause

Within the XML of the wf\_workflow record for the "Knowledge - Approval Retire" record, the sys\_scope value was corrupted.

### Resolution

As shared above, it was found that the error being thrown was from back-end java, but it helped us to understand that the system could not properly understand/read the scope value of the workflow.

This lead to checking the XML of the wf\_workflow record for the "Knowledge - Approval Retire" workflow. In doing so, a discrepancy was noted in the "sys\_scope" field value in the user's instance in the XML vs. what is seen in the Out of Box (OOB) "sys\_scope" field.

In an OOB instance, the XML for the "sys\_scope" field of the "Knowledge - Approval Retire" workflow reads: <sys\_scope display\_value="Global">global</sys\_scope>

In the user's instance, it reads: <sys\_scope display\_value="Global">global </sys\_scope> (note the single space after the "global")

By exporting this to XML, correcting the space, and re-importing, the error was cleared and the issue stopped.
