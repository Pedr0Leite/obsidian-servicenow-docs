---
title: "When attempting to use the Manage Rota screen action Schedule Time Off, a red bar with no error text appears"
aliases:
  - KB0657112
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657112
kb_number: KB0657112
last_modified: 2024-04-07
---

## When attempting to use the Manage Rota screen action Schedule Time Off, a red bar with no error text appears

  

### Issue

In on-call scheduling, users might not be able to schedule time off for themselves or others. A red banner without text is displayed on the form.

### Release

All releases.

### Cause

An invalid Schedule record is referenced in the User record.

### Resolution

This behaviour might be due to an invalid reference to a Schedule record that does not exist in the instance.

From the sys\_user record, add the 'Schedule' field to the form, the field would display as blank. However, viewing the XML for the sys\_user record, the 'shedule' field might look like this:   
  
<schedule display\_value="">52f2b95c6fed4700188909c54b3ee4ce</schedule>   
  
A search for this record in the cmn\_schedule table would show that this record does not exist.

This explains the warning message. The record might have been deleted at some point or it was not moved across from another instance, while the user record is still referencing this record. I

Updating this field to point to an existing cmn\_schedule record would solve the issue.
