---
title: "MID Server doesn't process python code"
aliases:
  - KB0784615
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784615
kb_number: KB0784615
last_modified: 2024-04-08
---

## MID Server doesn't process python code

  

### Issue

You might have a python file in the /usr/local/bin and the command works directly on the terminal in agent location but fails from ECC queue.

### Resolution

Our Mid server looks at files in two paths, /usr/bin and /usr/sbin.

Make sure the files are present in these locations.
