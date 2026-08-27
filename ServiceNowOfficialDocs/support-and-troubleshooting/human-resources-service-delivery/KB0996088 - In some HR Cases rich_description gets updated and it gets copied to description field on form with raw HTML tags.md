---
title: "In some HR Cases rich_description gets updated and it gets copied to description field on form with raw HTML tags"
aliases:
  - KB0996088
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996088
kb_number: KB0996088
last_modified: 2025-09-03
---

## In some HR Cases rich\_description gets updated and it gets copied to description field on form with raw HTML tags

  

### Issue

HTML tags showing up in the description field on the case form due to  Sync Description and Description OOB business rules

### Cause

Starting NewYork release rich description which supports HTML was introduced to provide rich text formatting on description. This is the reason all the OOB HR forms shows rich description instead of description field.

### Resolution

Therefore customers should not use description field and rich\_description interchangeably. When user enters rich\_description, the data including html tags is copied to description field as well in order for the two fields be in sync.  
  
Additionally if customer wants to only use description field, then they should not have rich\_description added to their case forms and they should not modify any condition in "Synch description with rich\_description" BR.  
  
  
Customers should not use both description and rich \_description in the HR case form.  
This is not the correct setup.
