---
title: "How to print in the filename and filepath using template.print"
aliases:
  - KB0791735
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791735
kb_number: KB0791735
last_modified: 2025-01-03
---

## How to print in the filename and filepath using template.print

  

### Summary

Using the following in the template.print, will remove the \\ from the printed value in the email that is generated.

template.print('path=\\\\server\\folder1\\folder2\\file.txt);

The above line will print - path=\\serverfolder1folder2file.txt

  

### Release

All Versions.

### Instructions

This is an expected behavior where the \\ in a file path needs to be escaped explicitly.

To get this print correct, escape every \\ with an other \\.

-   template.print('path=\\\\\\\\server\\\\folder1\\\\folder2\\\\file.txt);

OR

-   template.print('path=/\\/\\server/\\folder1/\\folder2/\\file.txt);
