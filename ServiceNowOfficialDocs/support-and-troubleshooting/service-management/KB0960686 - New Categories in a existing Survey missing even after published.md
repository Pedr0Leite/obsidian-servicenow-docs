---
title: "New Categories in a existing Survey missing even after published"
aliases:
  - KB0960686
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960686
kb_number: KB0960686
last_modified: 2025-01-02
---

## New Categories in a existing Survey missing even after published

  

### Summary

There are categories defined in each survey to group the questions which will display all the questions in that category under one section.

Few questions defined in the category are also not visible as the category itself is not visible.

Steps to reproduce:

1\. Create a new survey definition.

2\. Create a new category.

3.Create a few set of questions in the category

4\. Assign the survey to the user.

5\. Impersonate the user to whom the survey is assigned.

6\. Open the survey assessment and click on take assessment ui action.

7\. Check for the category if it is visible or not.

### Release

All

### Instructions

The categories which need to be visible in the assessment\_Take2 page should be present in the asmt\_assessable\_record table.

As the category's records are not present in the asmt\_assessable\_record table, few categories are not visible on the UI page.

### Related Links

Categories that are not visible on the ui page needs to be added to the asmt\_assessable\_record table.

If there are any dependent questions in the category then dependent questions will be visible only when the conditions are met.
