---
title: "How to create an onSubmit Client Script to verify the mandatory variable is not empty"
aliases:
  - KB0622896
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622896
kb_number: KB0622896
last_modified: 2026-06-03
---

## How to create an onSubmit Client Script to verify the mandatory variable is not empty

  

### Issue

This article details the steps to implement checking if a mandatory field is populated before order submission.

This is also the recommended solution for [mandatory variables on Service Catalog RITM records intermittently created with empty values](https://support.servicenow.com/kb_view.do?sysparm_article=KB0622887 "mandatory variables on Service Catalog RITM records intermittently created with empty values").

### Release

All releases.

### Resolution

1.  Navigate to **Service Catalog > Catalog Policy > Catalog Client Scripts.** A list of current custom catalog client scripts appears.
2.  Click **New**.
3.  Fill in the fields:
    -   Active: Checked
    -   Applies on a Catalog Item view: Checked
    -   Type : onSubmit  
        After selecting onSubmit, the script section will be pre-populated with function, do not delete this. 
    -   Script:
        
        function onSubmit(){
        
           var mandatoryVar = g\_form.getValue('<mandatory variable name>');
        
           if (mandatoryVar ==""){
        
              alert("<variable name> is mandatory. Please populate the variable and resubmit the request.");
        
           return false; }
        
        }
        
4.  Fill in the remaining fields as needed: 
    -   Name : (any name)
    -   Applies to : (does the mandatory field belong to a variable set or catalog item?)
    -   Catalog item or Variable set: (select the catalog item or variable set that owns the mandatory field)
    -   UI Type : (will this apply to policy apply to Desktop, Mobile or Both?)
    -   Applies on Requested Items : (check if you want the policy to also apply on requested item view)
    -   Applies on Catalog Tasks :(check if you want the policy to also apply on catalog task view)
5.  Click **Submit**.

### Related Links

-   [Catalog Client Scripts](https://docs.servicenow.com/bundle/tokyo-application-development/page/script/client-scripts/concept/c_CatalogClientScriptCreation.html "Catalog Client Scripts")
-   [Client Scripts](https://docs.servicenow.com/bundle/tokyo-application-development/page/script/client-scripts/concept/client-scripts.html "Client Scripts")
