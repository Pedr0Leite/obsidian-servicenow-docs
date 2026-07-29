---
title: "Lifecycle activity set is showing in the timeline unexpectedly"
aliases:
  - KB0953872
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953872
kb_number: KB0953872
last_modified: 2024-01-20
---

## Lifecycle activity set is showing in the timeline unexpectedly

  

### Issue

The user had created a Lifecycle Activity Set which had the "display to opened\_for" set to "false". Even so, the Activity Set was still showing in the Portal when impersonating the "opened\_for" user. They wanted to know why this was.

### Cause

There is a UI Policy Out of Box (OOB), "Display config options for display to subject person" which makes a second field "display to subject\_person" not visible.

### Resolution

It was found in the XML of the Activity Set (sn\_hr\_le\_activity\_set) that the "display\_to\_opened\_for" field value was indeed "false". However, there was another field which was later found to have been hidden by an OOB UI Policy (discussed above), "display\_to\_subject\_person". This second field had a value of "true".

The issue the user was facing was that the value in their opened\_for field on the HRC was also the subject\_person value on the same HRC - the same user was populated in both fields. Therefore, the Activity Set displayed as a result of meeting the second field (display to subject\_person = true).

Once both the display to opened\_for and display to subject\_person were set to "false", the expected result occurred - namely, that the Activity Set was completely hidden in both the Platform UI and the Portal. To access the second field's value, the OOB UI Policy can be set to active = false, or else the sn\_hr\_le\_activity\_set record can be exported to XML, the value changed in any text editor, and the record re-imported in any list-view.
