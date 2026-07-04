---
title: "Granting role sn_customerservice_manager is impacting viewing Active Supply Chain Contract"
aliases:
  - KB0869561
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869561
kb_number: KB0869561
last_modified: 2026-06-09
---

## Granting role sn\_customerservice\_manager is impacting viewing Active Supply Chain Contract

  

### Issue

Granting role sn\_customerservice\_manager is impacting viewing Active Supply Chain Contract

### Release

All

### Cause

Issue was caused by an out of the box business rule 'Contract query for agents'.  
  
Users with the role sn\_customerservice\_manager are passing the condition on 'Contract query for agents' business rule causing it not be skipped. Script inside business rule calls function 'addContractQueryforAgent' from script include 'CSQueryBRUtil'.  
  
The code mentioned below from the script include is what is causing this behavior:  
  
addContractQueryforAgent: function(current) {  
var query = this.getQBRConditionQueries(current,this.TABLE\_AST\_CONTRACT);  
return current;  
},

### Resolution

To fix this issue, you can modify the business rule condition, so it does not apply to users with the role 'sn\_customerservice\_manager'.  
/sys\_script.do?sys\_id=fb4c014fc300220071d07bfaa2d3aefb&sysparm\_view=&sysparm\_domain=null&sysparm\_domain\_scope=null  
  
An example of how you could change this behavior is by updating the condition on the business rule 'Contract query for agents':  
  
From:  
gs.hasRole('sn\_esm\_agent') && !gs.hasRole('admin')  
  
To:  
gs.hasRole('sn\_esm\_agent') && !gs.hasRole('admin, sn\_customerservice\_manager')  
  
This will prevent the script in business rule from running for users with sn\_customerservice\_manager role. This will allow all users with sn\_customerservice\_manager role to access the contract records.  
  
Please test this thoroughly prior to moving the fix to Prod.
