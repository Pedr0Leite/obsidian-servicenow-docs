---
title: "Survey trigger condition - User field"
aliases:
  - KB0758184
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758184
kb_number: KB0758184
last_modified: 2024-04-07
---

## Survey trigger condition - User field

  

### Issue

The Trigger condition does not allow us to select the 'Contact' field as the value for 'User field.' It's visible, but grayed out.

### Cause

Attribute set on User Field

### Resolution

The behavior is seen due to the dictionary attribute 'reference\_types' set on the User field in the trigger condition. Please see this attribute in the dictionary entry in the "Attributes" field:

Dictionary Entry - User field  
<Instance name>/nav\_to.do?uri=sys\_dictionary.do?sys\_id=28333204db93230095a657935e9619b8%26sysparm\_view=advanced  
  
The current value set is:  
'reference\_types=sys\_user'  
  
This allows reference fields to be selected which point to the sys\_user table. As the Contact field is a reference to the Contact table, we will have to update this attribute:  
  
'reference\_types=sys\_user;customer\_contact'  
  
This will then allow the fields pointing to the Contact table to be clickable.  
  
  
  

### Related Links

Docs: [Dictionary attributes](https://docs.servicenow.com/csh?topicname=c_DictionaryAttributes.html&version=latest "Dictionary attributes")
