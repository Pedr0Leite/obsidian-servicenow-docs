---
title: "Unable to move flows through update sets from one instance to another instance."
aliases:
  - KB0783693
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783693
kb_number: KB0783693
last_modified: 2025-04-21
---

## Unable to move flows through update sets from one instance to another instance.

  

### Issue

We have built an update set with 1 sub-flow, and 5 actions.

Update set is then exported to XML and imported from one instance to another instance.

After committing the update set there are missing actions in the target instance.

### Resolution

The issue here is with the Field Classes.  
  
For 'Glide Var', glide object the attributes have been modified and due to this at some point it was missing its serializer.  
  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_glide\_object.do?sys\_id=c2a847d1c0a8016400e1397987c642ee  
  
'serializer=com.glide.vars.VariableValueXMLSerializer', needs to be present in the attributes section of this Glide object.

Add this attribute and then do a cache flush.

Once this is done, all the new flows will be captured in the update set and can be moved to target instance with out any issues.
