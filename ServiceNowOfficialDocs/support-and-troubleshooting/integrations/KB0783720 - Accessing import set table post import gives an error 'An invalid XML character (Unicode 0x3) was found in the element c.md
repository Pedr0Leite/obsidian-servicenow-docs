---
title: "Accessing import set table post import gives an error 'An invalid XML character (Unicode: 0x3) was found in the element content of the document."
aliases:
  - KB0783720
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783720
kb_number: KB0783720
last_modified: 2025-04-29
---

## Accessing import set table post import gives an error 'An invalid XML character (Unicode: 0x3) was found in the element content of the document.'

  

### Issue

After running the import when accessing the import set table gives an error '**An invalid XML character (Unicode: 0x3) was found in the element content of the document.**'

You might also see the error in another formatting like '**Character reference "&#3" is an invalid XML character.**'

### Release

All releases

### Cause

When the data imported from a file the additional columns are created based on the columns present in the file. If the data present in the file is with incorrect data then columns created contain invalid characters that make the whole table becomes unreadable.

1.  Go to the sys\_dictionary table and browse for the column name & label for the table.
2.  Notice the Column Label similar to PK�����!�{'È!z������\[Content\_Types\].xml ¢(" has been created.

### Resolution

To resolve, delete the invalid columns which will restore the table back to normal. Address the incorrect data in the file and import it again.
