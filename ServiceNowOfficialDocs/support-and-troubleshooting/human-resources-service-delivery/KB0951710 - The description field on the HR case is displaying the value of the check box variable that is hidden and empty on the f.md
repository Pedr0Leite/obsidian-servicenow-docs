---
title: "The description field on the HR case is displaying the value of the check box variable that is hidden and empty on the form and target record."
aliases:
  - KB0951710
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951710
kb_number: KB0951710
last_modified: 2023-12-29
---

## The description field on the HR case is displaying the value of the check box variable that is hidden and empty on the form and target record.

  

### Issue

Checkbox variables are displayed in description of case even if its not visible and emptied in variable editor while submission

### Cause

Product owner team suggested that the behavior is as expected.

### Resolution

Any new field will come in description irrespective of visibility in UI with default values or with the value entered.  
  
If this was a string field, the value would be empty and so the "original value" would empty as well and it wouldn't be written to the description.  
  
However, checkbox fields do not have an empty state, they are true or false.  
  
The API cannot know that a customer submitted the checkbox as false vs didn't use the field since it's hidden on the form.  
  
Any field that does not have an "empty" state would have this issue.
