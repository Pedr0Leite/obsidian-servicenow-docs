---
title: "Alert can not be opened in Dashboard of Event Management"
aliases:
  - KB0724527
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724527
kb_number: KB0724527
last_modified: 2024-04-07
---

## Alert can not be opened in Dashboard of Event Management

  

### Issue

# Symptoms

* * *

Can't open alert in Dashboard of Event Management.

# Release

* * *

Kingston Patch 12, London.

# Cause

* * *

The system property "glide.tinyurl.minEncodedLength" controls when URLs in related lists will be shortened via the TinyURL engine. This was implemented basically because in the past, some users using legacy versions of Internet Explorer were having problems opening longer links. Modern browsers such as Chrome, Firefox, Safari and Microsoft Edge may not run into this issue, as the URL character limit for these browsers is 64k or above.

# Resolution

* * *

Workaround:

Create and set the system property "glide.tinyurl.minEncodedLength" of 'integer' type to a value of 64000.
