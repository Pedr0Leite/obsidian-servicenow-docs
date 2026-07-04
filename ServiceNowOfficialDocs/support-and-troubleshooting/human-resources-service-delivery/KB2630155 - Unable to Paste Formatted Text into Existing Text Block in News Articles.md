---
title: "Unable to Paste Formatted Text into Existing Text Block in News Articles"
aliases:
  - KB2630155
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630155
kb_number: KB2630155
last_modified: 2026-01-01
---

## Unable to Paste Formatted Text into Existing Text Block in News Articles

  

### Issue

-   When pasting text into a Text Content block in News articles:
    -   The pasted text is inserted into a new text box at the bottom instead of the intended location.
-   Occurs when using:
    -   Ctrl+V or Right-click > Paste.
-   Does not occur when using Paste Plain Text.
-   Users cannot paste formatted text directly into existing text blocks, impacting workflows with templates or cloned articles.

### Release

Any Release

### Cause

-   Behavior is due to Rich Content Editor limitations introduced after a platform upgrade.
-   The editor cannot merge multiple stylings into a single text block.
-   Pasting formatted text from external sources creates new text components instead of replacing highlighted text.

### Resolution

To address the issue where formatted text cannot be pasted into an existing text block in News articles:

1.  Understand Current Behavior:
    -   This is expected behavior after a platform upgrade.
    -   The Rich Content Editor does not merge multiple stylings into a single text block.
    -   Pasting formatted text from external sources creates a new text component instead of replacing highlighted text.
2.  Workarounds:
    -   Use “Paste Plain Text”:
        -   Right-click in the text block and select Paste Plain Text to remove external formatting and paste in the same block.
    -   Use Browser Shortcut:
        -   Press Ctrl+Shift+V (or equivalent on your browser) to paste text matching the existing style.
    -   Apply Formatting Manually:
        -   Paste plain text first, then use the Rich Content Editor toolbar to apply styles.
