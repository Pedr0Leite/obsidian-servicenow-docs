---
title: "Email address in email client is improperly formatted"
aliases:
  - KB0787100
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787100
kb_number: KB0787100
last_modified: 2024-04-08
---

## Email address in email client is improperly formatted

  

### Issue

email address in email client from within an incident is improperly formatted.

For Example:  
 &lt;test.example@servicenow.com&gt;

### Cause

system property "glide.ui.escape\_text" value was false

### Resolution

Set the system property "glide.ui.escape\_text" as true in order to not to allow escaping of html characters.
