---
title: "The term 'executeRemote' is not recognized as the name of a cmdlet, function, script file, or operable program while running discovery."
aliases:
  - KB0752577
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752577
kb_number: KB0752577
last_modified: 2024-04-07
---

## Issue

# Cause

From Madrid, the PSScript.ps1 imports certain modules including ExecuteRemote module. If the PSScript.ps1is customized then on a Madrid upgrade the previous file retains. The previous file does not load the "executeRemote" module and hence you receive the error 

"The term 'executeRemote' is not recognized as the name of a cmdlet, function, script file, or operable program while running discovery."

# Resolution

Please revert the PSScript.ps1 file to OOB file for Madrid. This PSScript.ps1 file will load the ExecuteRemote module and discovery will run accordingly.
