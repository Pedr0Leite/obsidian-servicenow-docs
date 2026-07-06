---
title: "PDF export localization for thousand delimiter and decimal delimiter is not the same in the report UI and the PDF output"
aliases:
  - KB0782293
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782293
kb_number: KB0782293
last_modified: 2024-04-30
---

## PDF export localization for thousand delimiter and decimal delimiter is not the same in the report UI and the PDF output

  

### Issue

When running a report that has numbers like price fields and numbers larger than 1000, the behaviour when exporting as PDF is not the same in the exported PDF document and the PFD report produced

For example:

1 091 and 98,9 for France  
1,091 and 98.9 for US

### Release

Not release specific

### Cause

This is related to localization settings, global versus user specific that is not always set as required for report output consistency.

  

### Resolution

This is related to the localization settings

For the PDF export, to consistently use the same localization, the following pre-requisites exist

  

1) 'glide.system.locale'

The global localization variable 'glide.system.locale' should be set in table \[sys\_properties\]

glide.system.locale

This can be accessed from the menu as well, 'System localization'

  

2) sys\_user.country (country code)

The country code field should be used at the user level to ensure consistency, if the country field is not set, the PDF report will use the global variable set at the instance level: 'glide.system.locale'.

The country code is in the user table \[sys\_user\]

sys\_user.country (country code)
