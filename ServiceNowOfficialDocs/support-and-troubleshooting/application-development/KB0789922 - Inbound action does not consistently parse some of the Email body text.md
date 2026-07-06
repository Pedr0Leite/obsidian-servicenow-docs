---
title: "Inbound action does not consistently parse some of the Email body text"
aliases:
  - KB0789922
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789922
kb_number: KB0789922
last_modified: 2024-04-08
---

## Issue

Incoming email is getting processed and the inbound action is triggered. The inbound action creates/updates a record as expected but the update may be missing some parts of the text or the update may not be parsed as expected.

  

  

## Resolution

As a workaround ; 

-   `Change the script to retrieve BODY field instead of BODY_TEXT`
-   `Send the email with identical BODY and BODY_TEXT fields.`
