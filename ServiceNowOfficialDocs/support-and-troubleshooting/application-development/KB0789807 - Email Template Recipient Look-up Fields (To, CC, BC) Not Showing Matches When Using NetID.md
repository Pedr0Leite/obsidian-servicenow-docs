---
title: "Email Template Recipient Look-up Fields (To, CC, BC) Not Showing Matches When Using NetID"
aliases:
  - KB0789807
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789807
kb_number: KB0789807
last_modified: 2024-04-07
---

## Email Template Recipient Look-up Fields (To, CC, BC) Not Showing Matches When Using NetID

  

### Issue

When using an Email Template, the recipient's address is not showing relevant matches when using the NetID. Possible addresses will show when keying the first name but will not when using the NetID.

### Release

New York 

### Cause

Most Probable Cause: New York release has email recipient qualifier set as Name Out of Box.

### Resolution

  
To change the out of box behavior to desired configuration here is what you need to do.  
  
1) Navigation pane type email "email template configuration " > recipient qualifier  
2)click active users:  
  
Click Display Configuration Tab > Display name Field>switch the Choice to User ID
