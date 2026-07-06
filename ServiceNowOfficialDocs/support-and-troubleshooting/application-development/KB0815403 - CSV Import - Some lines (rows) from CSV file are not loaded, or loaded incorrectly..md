---
title: "CSV Import - Some lines (rows) from CSV file are not loaded, or loaded incorrectly."
aliases:
  - KB0815403
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815403
kb_number: KB0815403
last_modified: 2024-04-08
---

## CSV Import - Some lines (rows) from CSV file are not loaded, or loaded incorrectly.

  

### Issue

When a CSV file is attached or configured to load from a remote location like FTP(S), HTTP(S), SFTP, etc. you may experience that not all records were loaded from the CSV correctly. (Number of lines in CSV and number of records in Import Set Table do not match)

### Release

All ServiceNow Platform releases.

### Cause

These issues are commonly caused by the formatting of the source CSV file.

CSV files are plain text files, and store the data without any type formatting. Because there are many applications like Microsoft Excel, Libre Office Sheets, Apple Numbers that can handle these files, they appear like they are natural file formats of these applications, and they allow users to display the data in a tabular form.

Here is an example CSV file displayed in Microsoft Excel:

![](/sys_attachment.do?sys_id=a033e08ddb8874d0b55f0b55ca9619f5)

But this file is actually a text file and when opened with Notepad, TextEdit or a similar basic text editor, it will reveal the actual data:

![](/sys_attachment.do?sys_id=2833e08ddb8874d0b55f0b55ca9619f6)

As you can see, native applications hide many of the underlying data structure, and makes troubleshooting difficult.

Because there is no strict standard on generation of CSV data, certain formatting or lack of signs like comma (,), quotes ('), double quotes (") might cause issues while trying to import this data on other systems, including ServiceNow platform.

### Resolution

Please validate your source CSV file before importing into ServiceNow platform.

-   Check your source data with a plain text editor against header columns count versus data columns count.

-   If it's a large file or contains large number of columns, you can use one of many online validation websites. You can upload your file, and it will provide feedback on its formatting. One example is:
    -   [https://csvlint.io/](https://csvlint.io/)
