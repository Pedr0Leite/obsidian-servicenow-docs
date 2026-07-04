---
title: "Flow Designer will not open a flow with the page stuck on 'Processing'"
aliases:
  - KB0821414
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821414
kb_number: KB0821414
last_modified: 2024-04-08
---

## Flow Designer will not open a flow with the page stuck on 'Processing'

  

### Issue

After moving a Flow from Test to Production via Update Set, the Flow cannot be opened in Production instance, the page just states 'Processing' and never loads anything

There are errors in Browser Console:

\---------------------  
uncaught at fetchActionsAndTriggerTypes SyntaxError: Unexpected token e in JSON at position 0  
at JSON.parse (<anonymous>)  
at getServiceCatalogVariablesInputLanguage (https://instance\_name/scripts/designer-bundle.min.js?sysparm\_substitute=false&version=1.4.31:63543:62)  
at natLangHtmlComponentInstance (https://instance\_name/scripts/designer-bundle.min.js?sysparm\_substitute=false&version=1.4.31:63575:48)  
  
..  
uncaught at fetchActionsAndTriggerTypes SyntaxError: Unexpected token e in JSON at position 0  
at JSON.parse (<anonymous>)  
at getServiceCatalogVariablesInputLanguage (https://instance\_name/scripts/designer-bundle.min.js?sysparm\_substitute=false&version=1.4.31:63575:48)  
at natLangHtmlComponentInstance (https://instance\_name/scripts/designer-bundle.min.js?sysparm\_substitute=false&version=1.4.31:63575:48)  
at https://instance\_name/scripts/designer-bundle.min.js?sysparm\_substitute=false&version=1.4.31:85575:92  
at Array.forEach (<anonymous>)  
  
..  
uncaught at loadFlowDetailsSaga SyntaxError: Unexpected token e in JSON at position 0  
at JSON.parse (<anonymous>)  
at getServiceCatalogVariablesInputLanguage (https://instance\_name/scripts/designer-bundle.min.js?  
..  
\--------------------------

### Cause

In the Flow > Action : Get Catalog Variables, the 'Template Catalog Item (Catalog Item)' field was referencing a catalog item that did not exist in Production. So it was unable to load. 

### Resolution

After importing the catalog item ( referenced in the Flow) into Production, the issue resolved and the Flow opened without errors
