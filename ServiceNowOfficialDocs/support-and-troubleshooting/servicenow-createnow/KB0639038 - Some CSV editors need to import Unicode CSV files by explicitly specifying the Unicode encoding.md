---
title: "Some CSV editors need to import Unicode CSV files by explicitly specifying the Unicode encoding "
aliases:
  - KB0639038
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639038
kb_number: KB0639038
last_modified: 2025-06-19
---

## Some CSV editors need to import Unicode CSV files by explicitly specifying the Unicode encoding

  

### Issue

Some CSV editors (for example, Excel), if not correctly used, display characters such as question marks "?" in place of other characters (for example, "") when opening Unicode CSV files.

When you export to CSV, for some users, some characters appear as "?" (question mark).

### Release

All

### Cause

CSV files are not inherently Unicode-safe. Some editors open CSV files using non-Unicode character sets by default. If the wrong character encoding is used, unsupported characters may be shown as question marks `"?"`. This issue may also occur if the system property `glide.export.csv.charset` is set to `UTF-8` but the editor does not interpret the file as UTF-8.

So it is not explicitly solving the issue if you set the system property in instance, but also make sure the platform where you are opening the file also supports/interprets UTF-8

### Resolution

If the operating system is Unicode safe, use the appropriate setting when opening the file to open Unicode files correctly. For example, in Excel, open the file by explicitly specifying the Unicode encoding on the "open dialog".

To ensure that Unicode characters display correctly when opening CSV files:

Set the `glide.export.csv.charset` system property to `UTF-8`.

Ensure the operating system supports the Unicode characters being used.

When opening the CSV file in an editor (e.g., Excel), explicitly select UTF-8 encoding during the file open process to avoid misinterpretation of characters.
