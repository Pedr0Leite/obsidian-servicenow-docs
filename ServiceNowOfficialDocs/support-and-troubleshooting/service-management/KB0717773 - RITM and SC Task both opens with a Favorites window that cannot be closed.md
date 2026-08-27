---
title: "RITM and SC Task both opens with a Favorites window that cannot be closed"
aliases:
  - KB0717773
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717773
kb_number: KB0717773
last_modified: 2024-04-07
---

## RITM and SC Task both opens with a Favorites window that cannot be closed

  

### Issue

Whenever a particular RITM is opened, there is a "Create favorite" pop-up that opens up

### Release

Kingston

### Cause

The code for the favorite window pasted in the "Comments" field.

### Resolution

 The HTML and CSS code for the "create favorite" window is posted as a comment to the RITM record.

Due to this reason, the "create favorite" pop-up opens up whenever the particular RITM with the issue is opened.

\*To remove the issue, user can delete the comment that has the code in the sys\_journal\_field table
