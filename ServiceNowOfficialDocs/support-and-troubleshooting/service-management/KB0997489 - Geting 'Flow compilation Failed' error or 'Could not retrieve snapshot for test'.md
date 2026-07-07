---
title: "Geting  'Flow compilation Failed' error or 'Could not retrieve snapshot for test"
aliases:
  - KB0997489
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997489
kb_number: KB0997489
last_modified: 2024-08-28
---

## Geting 'Flow compilation Failed' error or 'Could not retrieve snapshot for test'

  

### Issue

When testing the flow by submitting a request, it was reporting 'Flow compilation Failed' error

And when testing the flow directly using the 'test' ui action the flow was reporting 'Could not retrieve snapshot for test'.

When trying to reactivate the flow once again resulted in 'flow compilation failed' error

### Cause

some of the catalog variables were deleted from the catalog item that were still being referenced in the flow

### Resolution

An error was reported in the logs when it was trying to compile the flow:

"invalid/deleted catalog variable found during flow publish"

  
Querying the customer update table showed that some of the variables had been deleted.

  
To resolve/fix the issue, it was suggested to revert these deleted catalog variables.
