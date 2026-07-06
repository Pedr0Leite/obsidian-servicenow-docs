---
title: "Copy inbound email into the Work Notes or Additional Comments field of a target record"
aliases:
  - KB0727612
tags:
  - servicenow
  - support-kb
  - inbound-email-actions
  - scripting
  - work-notes
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727612
kb_number: KB0727612
last_modified: 2024-04-07
---

## Copy inbound email into the Work Notes or Additional Comments field of a target record

  

### Issue

# Description

* * *

Copy an inbound email into the Work Notes or Additional Comments field of a target record.

# Procedure

* * *

Use one of the existing inbound actions that does this as a model. For example, the Update Problem inbound email action does this in the script of the Action section:

if (current.getTableName() == "problem") {  
current.work\_notes = "reply from: " + email.origemail + "\\n\\n" + email.body\_text;  
...  
current.update();  
}

You can reuse this code, changing the target table name from problem to the intended target table.

The above code snippet copies the email into the Work Notes \[work\_notes\] field. To copy into the Additional Comments \[comments\] field, instead, replace current.work\_notes with current.comments in the script.

# Applicable Versions

* * *

All versions.

## Related

- [[KB0727619 - The Field actions menu for an inbound email action is not showing all fields]] - inbound email action configuration
- [[KB0743785 - Orphaned duplicate request is created via inbound email action using Cart() API]] - inbound email action scripting pitfalls
- [[processing-inbound-emails]] - official docs on inbound email processing
- [[use-inbound-email-action]] - official docs on configuring inbound email actions

