---
title: "HTML tags/attributes disappear from the message when added via gs.addInfoMessage or gs.addErrorMessage due to HTML sanitization"
aliases:
  - KB0621873
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621873
kb_number: KB0621873
last_modified: 2024-04-07
---

## Issue

HTML tags/attributes disappear from the message when added via gs.addInfoMessage or gs.addErrorMessage due to HTML sanitization

  
  

# Description

* * *

As part of the ongoing effort to maintain a secure platform, session info/error messages are now HTML sanitized by default. While this still allows for HTML tags/attributes that have been allow listed, any non-allow listed entities will be removed. The default allow list does not allow common security risks like script tags and attributes such as onclick and onerror.

The default allow list can be found here along with instructions for modifying the list: [HTML Sanitizer](https://docs.servicenow.com/csh?topicname=c_HTMLSanitizer.html&version=latest "HTML Sanitizer")

If the developer is certain a message contains no unsanitized user input and still needs access to an element or attribute that is not in the configured allow list, gs.addInfoMessageNoSanitization and gs.addErrorMessageNoSantization have been added to the API.
