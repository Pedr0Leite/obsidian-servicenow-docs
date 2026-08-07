---
title: "How to remove formatting from text in email notification message HTML fields"
aliases:
  - KB0686053
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686053
kb_number: KB0686053
last_modified: 2025-11-13
---

## How to remove formatting from text in email notification message HTML fields

  

### Issue

When you paste text into the message HTML field of an email notification, it may contain formatting that doesn't render correctly in HTML. This formatting can add Description Term <dt> and Description List <dl> elements to the HTML source code, causing unwanted line spacing. This article explains how to remove formatting so your text displays as expected.

### Release

All supported releases

### Resolution

To remove unwanted formatting from text:

1.  Copy and paste the text into a plain text editor such as Notepad (Windows) or TextEdit (Mac).
2.  In the text editor, organize the text as you want and remove any unwanted blank lines.
3.  Select all text and copy it from the text editor.
4.  Paste the unformatted text into the Message HTML field of the notification record.
5.  In the **Paste Formatting Options**, select **Keep Formatting**.

### Related Links

[How to fix HTML tags appearing in sent email notifications](https://support.servicenow.com/kb_view.do?sysparm_article=KB0727884 "How to fix HTML tags appearing in sent email notifications")

[How to fix unexpected HTML display in email preview tools](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743622 "How to fix unexpected HTML display in email preview tools")
