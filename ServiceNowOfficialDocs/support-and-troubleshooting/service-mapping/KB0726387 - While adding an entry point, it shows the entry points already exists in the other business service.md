---
title: "While adding an entry point, it shows the entry points already exists in the other business service"
aliases:
  - KB0726387
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726387
kb_number: KB0726387
last_modified: 2026-05-22
---

## While adding an entry point, it shows the entry points already exists in the other business service

  

### Issue

After deleting a business service, when trying to re-create it, you get an error: 

'The business service: contains the same entry point that was entered. Enter a different entry point or delete the entry point from: and try again'

The error does not show the business service name to delete the entry and there is no other business service that exists with the same URL that I am trying to use as the entry point. How do I get rid of this message so I can just re-create my business service?

# Release

* * *

Seen in London

# Resolution

* * *

Perform the below steps to resolve this issue

-   Search in the table https://<your instance>.service-now.com/sa\_m2m\_service\_entry\_point\_list.do for the URL of your entry point. There are two columns: Entry point and the business service column. 
-   Remove your entry point it will most likely have a business service column that is empty. Once this is done you will be able to recreate the business service using the previously used entry point

### Release

Has been seen up to Xanadu, and likely later

### Resolution

Perform the below steps to resolve this issue

-   Search in the table https://<your instance>.service-now.com/sa\_m2m\_service\_entry\_point\_list.do for the URL of your entry point. There are two columns: Entry point and the business service column. 
-   Remove your entry point it will most likely have a business service column that is empty. Once this is done you will be able to recreate the business service using the previously used entry point
