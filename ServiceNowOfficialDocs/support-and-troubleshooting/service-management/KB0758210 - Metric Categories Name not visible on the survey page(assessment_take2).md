---
title: "Metric Categories Name not visible on the survey page(assessment_take2)"
aliases:
  - KB0758210
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758210
kb_number: KB0758210
last_modified: 2024-04-07
---

## Metric Categories Name not visible on the survey page(assessment\_take2)

  

### Issue

Question heading is not visible on the survey page when the name of "Assessment Metric Category" is same as "Survey Definition".

### Cause

As per OOB behavior, if values of "name" field of "Assessment Metric Category" and "name" field in "Survey Definition" is same then it doesn't display "Assessment Metric Category" name field over the questions in order to avoid duplication of its contents.

In case the field values are different but the translation is same then it will show different behavior owing to this feature i.e. in English it will show both the fields whereas in the translated language it will not show name field of "Assessment Metric Category".

### Resolution

Changing the value in English and make them the same will make the page appear similar or translation could be made different.
