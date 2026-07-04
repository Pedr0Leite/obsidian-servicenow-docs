---
title: "Inactive choice of state in HR cases is still displayed with blue color"
aliases:
  - KB0994507
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994507
kb_number: KB0994507
last_modified: 2025-12-10
---

## Inactive choice of state in HR cases is still displayed with blue color

  

### Issue

Despite not being selectable from the drop-down list, the inactive choice of case state in HR cases is still shown in blue.

### Cause

Because the option that was chosen when the record was being created is no longer active or valid, the Records are left with a blue color option.  
  
To understand more about the feature, refer to ["Display invalid choice list values"](https://docs.servicenow.com/csh?topicname=t_ViewChoiceListDefinitions.html&version=latest) on the product document

Note the point **"By default, inactive or invalid choice list values appear in the blue text instead of black"**.

### Resolution

If there are any missing choice list entries that have records in the provided database and to remove them all, follow the below steps:

1.  Navigate to System Properties
2.  User Interface (UI) Properties
3.  Clear the check box for the Display missing choice list entries property

The blue records will disappear after making the above adjustments because the choice list entry is no longer valid or active.

Replace them with valid choices from the choice table by updating the empty values.
