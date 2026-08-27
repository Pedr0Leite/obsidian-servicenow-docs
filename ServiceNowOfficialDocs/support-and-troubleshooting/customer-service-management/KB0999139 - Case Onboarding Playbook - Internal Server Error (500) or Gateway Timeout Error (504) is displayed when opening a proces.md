---
title: "Case Onboarding Playbook - Internal Server Error (500) or Gateway Timeout Error (504) is displayed when opening a process in Process Automation Designer."
aliases:
  - KB0999139
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999139
kb_number: KB0999139
last_modified: 2025-02-25
---

## Issue

Intermittent issue where Internal Server Error (500) or Gateway Timeout Error (504) is displayed when opening a process in Process Automation Designer.

## Resolution

Go to System Definition -> Transaction Quota Rules. Choose the REST Batch API request timeout rule and up the maximum duration.

  
This will allow the long running batch request to finish. The value to set here will depend on the time it takes the request to finish/depending on what the transaction logs show. Please keep in mind that this workaround is specific to the error seen: Internal Server Error (500) or Gateway Timeout Error (504). There will still be a delay in loading. We are looking at reducing the amount of information the PAD gathers at the start (reduce the amount of data asked for on load) in Tokyo via an existing story but until then, this property will need to be increased.
