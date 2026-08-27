---
title: "Numeric Scale/ Scale choices are not saved"
aliases:
  - KB0728360
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728360
kb_number: KB0728360
last_modified: 2024-04-07
---

## Numeric Scale/ Scale choices are not saved

  

### Issue

When updating the choices on Numeric Scale or Scale survey, they are not saved and the following error message is displayed: "The value must be an Integer"

### Release

All releases.

### Cause

The Script Include "AssessmentUtils" (sys\_id = ca4033c1d7110100fceaa6859e610326) might have been customized. 

### Resolution

Rever the Script Include "AssessmentUtils" (sys\_id = ca4033c1d7110100fceaa6859e610326) to its OOB version.
