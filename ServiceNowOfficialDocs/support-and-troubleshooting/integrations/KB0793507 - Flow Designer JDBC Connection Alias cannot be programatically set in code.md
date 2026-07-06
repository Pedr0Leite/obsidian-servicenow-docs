---
title: "Flow Designer JDBC \"Connection Alias\" cannot be programatically set in code"
aliases:
  - KB0793507
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793507
kb_number: KB0793507
last_modified: 2024-04-08
---

## Flow Designer JDBC "Connection Alias" cannot be programatically set in code

  

### Issue

Use case: 

In flow designer, in a JDBC connection, you may want to code  to conditionally choose a connection, for example if the same code is used in production and test, you may have a connection for test and a connection for prod.

To code, you would typically set f(x) button  and use this kind of code trying to dynamically set the connection alias:

  
(function execute(inputs, outputs) {  
  
  var sysId = "";  
  if (condition...){  
    sysIdoftheconnection alias = "xxxxxxx";  
  }  
  
  outputs.connection = sysId;  
})(inputs, outputs);

However, this kind of code cannot be used and is not valid.

### Release

All

### Cause

This feature is not currently supported

### Resolution

  
  
A workaround consists in setting up a workflow (not flow designer) and then code within that workflow the connection alias that dynamically gets set in the code.
