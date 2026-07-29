---
title: "Surveys do not trigger although the trigger condition is met."
aliases:
  - KB0726948
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726948
kb_number: KB0726948
last_modified: 2024-04-07
---

## Surveys do not trigger although the trigger condition is met.

  

### Issue

# Symptoms

* * *

Surveys are not triggering when an incident is closed. An error is noted in the logs from the 'Auto assessment business rule'. 

# Release

* * *

London Patch 4 

# Cause

* * *

On the trigger condition, a related field dictionary was modified to remove the 'types=reference' attribute. When passing in a non-reference field into the trigger condition, an error occurs and the survey is not created.

# Resolution

* * *

Reset the 'types=reference' attribute to the related field as this is a requirement.
