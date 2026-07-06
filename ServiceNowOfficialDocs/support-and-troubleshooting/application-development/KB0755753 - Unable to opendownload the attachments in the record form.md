---
title: "Unable to open/download the attachments in the record form"
aliases:
  - KB0755753
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755753
kb_number: KB0755753
last_modified: 2026-04-22
---

## Unable to open/download the attachments in the record form

  

### Issue

The issue happens when a user is unable to open/ download the attachments in a form. The form gets refreshed, but the file does not get downloaded.

### Issue due to the browser's limitation

The issue happens due to the creation of a huge URL. When the URL has more characters than the browser limit, the browser truncates the URL, causing a broken URL to be sent to the server, and the attachment to not get downloaded.

#### Steps to Replicate

1.  Open any table list. ex. change\_request\_list.do
2.  Add a lot of filters to change\_request\_list.do
3.  Once enough filters are added, open any change request and try to download the attachment

### Release

Any

### Resolution

In order to fix this issue, enable "[Tiny URL support](https://docs.servicenow.com/csh?topicname=t_EnableTinyURLSupport.html&version=latest "Tiny URL support")".

If "**tiny URL support**" is enabled, then set below property values:

**Name**: glide.tiny\_url\_min\_length  
  
**Value:** 256
