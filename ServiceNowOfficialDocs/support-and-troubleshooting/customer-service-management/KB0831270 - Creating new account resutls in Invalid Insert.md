---
title: "Creating new account resutls in Invalid Insert"
aliases:
  - KB0831270
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831270
kb_number: KB0831270
last_modified: 2025-02-27
---

## Creating new account resutls in Invalid Insert

  

### Issue

When creating a new customer\_account record, there is an "Invalid Insert" error and the record is not saved.

### Release

All Releases

### Cause

The customer\_account table has three fields that require unique values, one is the account code. This field is creating with a default value that is determined by the last used value. The 'last used' value is stored in the com.snc.cs\_base.last.generated.code.tree.path system property. If the property is reset to the original value, it will attempt to create new accounts with an account code that is already in use.

### Resolution

Identify the last used value for the account code field on the customer\_account table and update the com.snc.cs\_base.last.generated.code.tree.path system property with that value.

### Related Links

Update the com.snc.cs\_base.last.generated.code.tree.path sys\_property with the correct value  
You can get the value by sorting the record list in descending order based on account\_code and the first record will be the one with higher lexical order  
So, To get the latest code that is generated :  
Go to accounts  
Add Account Code field in the list view  
Sort the list in descending order based on "Account Code" Field  
The account code of the first record is the last generated code  
  
\* More Details :  
\* How new account code gets generated - account\_code is generated based on the pattern "!#$&()\*+,-.0123456789:;<?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\[\]\`}|{~" and sys\_property com.snc.cs\_base.last.generated.code.tree.path  
For e.g.: if value in sys\_property is !!!#, the next value for account code will be !!!$.
