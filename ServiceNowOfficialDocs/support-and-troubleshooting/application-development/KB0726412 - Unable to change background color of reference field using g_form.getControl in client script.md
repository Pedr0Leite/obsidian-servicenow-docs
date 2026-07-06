---
title: "Unable to change background color of reference field using g_form.getControl in client script"
aliases:
  - KB0726412
tags:
  - servicenow
  - support-kb
  - client-scripts
  - g_form
  - reference-fields
  - ui-customization
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726412
kb_number: KB0726412
last_modified: 2024-04-07
---

## Unable to change background color of reference field using g\_form.getControl in client script

  

### Issue

# Symptoms

* * *

When trying to change the background color of a reference field, the following does not work:

g\_form.getControl('reference\_field').style.backgroundColor = 'red'

The above will work for other field types, except not for reference fields.

# Release

* * *

All

# Cause

* * *

The getControl() method is not appropriate for reference fields.

# Resolution

* * *

The right method for reference fields is getDisplayBox(), like so:

g\_form.getDisplayBox('reference\_field').style.backgroundColor = 'green'

## Related

- [[KB0725201 - Function URLSearchParams is not supported by IE]] - other client-script/browser API quirk
- [[KB0745114 - Catalog client script is not hiding the container and the variables within the container]] - g_form API usage pitfalls

