---
title: "\"If\" statements in Flow Designer are evaluated as false when they appear to be true."
aliases:
  - KB0785106
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785106
kb_number: KB0785106
last_modified: 2025-08-20
---

## "If" statements in Flow Designer are evaluated as false when they appear to be true.

  

### Issue

When firing the user's Flow "General Procurement", the "If" statement "If user is located in Wakanda, assign to Wakanda Service Desk" is getting evaluating as false, even though this appears to be a true statement. The user wanted to know why this is.

### Release

### Resolution

The reason the user is seeing the Flow's "If" statement constantly evaluate to false is that a reference field cannot be compared to a string field.

As mentioned above, it was found that the "If" statement in question was comparing Trigger ➛ Hardware Record ➛ Location is "Wakanda". This will not ever be true because it is comparing a record reference (Location) to a string ("Wakanda").

After the Flow was changed to compare Trigger ➛ Hardware Record ➛ Location ➛ Name (a string) to "Wakanda" (also a string), it worked as expected.
