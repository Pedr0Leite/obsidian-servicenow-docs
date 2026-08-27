---
title: "KB article downloaded automatically when user accessed the article link from knowledge home page"
aliases:
  - KB0824575
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824575
kb_number: KB0824575
last_modified: 2025-05-30
---

## KB article downloaded automatically when user accessed the article link from knowledge home page

  

### Issue

'Display attachments' and 'Attachment link' was set to true on a knowledge article. That resulted in downloading the knowledge article when the user clicked on the article link.

### Release

New York Patch 7a

### Cause

Attachment link check box for downloading an attached file automatically when a user accesses the article, instead of opening the article view.  
  
This was expected behavior because 'Display attachments' and 'Attachment link' were set to true.

### Resolution

Unchecking 'Display attachments' and 'Attachment link' on the knowledge article will open the article in the article view(kb\_view page) instead of downloading the article.

To clarify the purpose of the fields involved:

-   **Display attachments:** Controls whether attachments are shown directly within the article view (e.g., below the body in Service Portal or UI16). When disabled, attachments are still stored but not visually displayed in the article layout.
-   **Attachment link:** When enabled, the article becomes a direct download link for the attachment itself, bypassing the article body entirely. This is typically used for articles meant to deliver files such as templates or PDFs.

If both are checked, users may see only the file download behavior — not the article view — which can be confusing.

### Related Links

RELATED REFERENCES: [Create a knowledge article](https://docs.servicenow.com/csh?topicname=create-knowledge-article.html&version=latest)
