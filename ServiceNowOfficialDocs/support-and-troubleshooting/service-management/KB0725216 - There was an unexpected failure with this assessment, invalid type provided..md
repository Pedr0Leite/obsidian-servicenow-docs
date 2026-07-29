---
title: "There was an unexpected failure with this assessment, invalid type provided."
aliases:
  - KB0725216
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725216
kb_number: KB0725216
last_modified: 2024-12-17
---

## Issue

# Symptoms

* * *

When user tries to see survey results from UI page assessment\_take2 page they are getting the either of the following error messages:

There was an unexpected failure with this assessment, invalid type provided.  
  
You are not authorized to take this vendor risk assessment  

# Resolution

* * *

Check for the following:

1.  Make sure UI page assessment\_take2 is out-of-the-box
2.  Make sure User has either survey\_reader or survey\_admin role
3.  Make sure you are not hitting PRB623780 (Survey error if the properties glide.ui.escape\_text and glide.ui.escape\_all\_script are set to true)

## Resolution
