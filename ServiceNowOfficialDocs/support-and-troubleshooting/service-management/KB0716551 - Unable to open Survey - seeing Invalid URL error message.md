---
title: "Unable to open Survey - seeing \"Invalid URL\" error message"
aliases:
  - KB0716551
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716551
kb_number: KB0716551
last_modified: 2024-04-07
---

## Unable to open Survey - seeing "Invalid URL" error message

  

### Issue

 

# Symptoms

* * *

-   Seeing "Invalid URL" error message when attempting to view a Survey

# Release

* * *

Kingston Patch 7, London, Madrid

# Resolution

* * *

The reason the user is seeing the "Invalid URL" error message is because the assessment they are trying to view is not assigned to them. The assessment the user is trying to access is not public.

There is some logic which happens when a user tries to view an assessment. The system runs a check which says, "Is the user who is trying to view this assessment the same as the person to whom it is assigned? If yes, display the assessment. If no, throw 'Invalid URL' error."

Therefore the behavior seen is expected, as the assessment the user is trying to view is not assigned to them.

Also, there are 2 scripts include called when opening a survey, ensure these scripts are not customized: SPSurveyAPI and AssessmentUtils
