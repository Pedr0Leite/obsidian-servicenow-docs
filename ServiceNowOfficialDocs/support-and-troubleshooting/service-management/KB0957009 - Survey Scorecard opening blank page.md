---
title: "Survey Scorecard opening blank page"
aliases:
  - KB0957009
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957009
kb_number: KB0957009
last_modified: 2026-06-24
---

## Survey Scorecard opening blank page

  

### Issue

After moving a Survey to a different instance the related Survey Scorecard does not work.   
When clicking on View Scorecards, the page is blank and does not display any content.

### Release

All

### Cause

This can happen when there are Multiple Duplicate Assessable Records for the Survey Metric Type  
This is incorrect behavior, a metric type using evaluation method 'survey' should only have one assessable record. 

### Resolution

  
The duplicate assessable records should be deleted to resolve this issue.

You can review the \[asmt\_assessable\_record\] Table to remove the duplicates for that Metric Type.

Feel free to take an export xml of the record as a backup before deleting.
