---
title: "Attachments in SNOW are always downloading as file"
aliases:
  - KB0759228
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759228
kb_number: KB0759228
last_modified: 2024-04-26
---

## Attachments in SNOW are always downloading as file

  

### Issue

User would like to know if there is a way to change settings in SNOW system, so attachments would be opening, not downloading after clicking it. Before we're able to view attachments. But now, attachments proceeds to download.

### Resolution

glide.ui.attachment.force\_download\_all\_mime\_types is set to true by default in Madrid.

### Related Links

https://docs.servicenow.com/csh?topicname=r\_AvailableSystemProperties.html&version=latest
