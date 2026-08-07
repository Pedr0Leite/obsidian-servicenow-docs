---
title: "PDf Generated on HR cases to do not respect the bold and  bullets positioning"
aliases:
  - KB0860238
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860238
kb_number: KB0860238
last_modified: 2024-04-08
---

## Issue

When generating a PDF document from the 'Preview document' functionality, bullet points are not indented correctly, manual indentations on paragraphs are not correct, and bold characters are not showing correctly in the PDF file.

The correct formats are presented while previewing (on Click of Preview Document button). 

## Resolution

Prior to Paris, this is a limitation with no workaround.  
There is a difference between preview and document. Preview directly shows the html content on the UI. But pdf document is created using itext5 API.  
There are a few unsupported functions with itext5.  
From Paris, we are supporting itext7. Bold and bullet points are supported by itext7.
