---
title: "Determine if there are client-side script errors"
aliases:
  - KB0547069
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547069
kb_number: KB0547069
last_modified: 2026-03-25
---

## Determine if there are client-side script errors

  

### Issue

Client-side script errors prevent forms from loading correctly, causing UI policies, UI actions, and client scripts to fail.

### Symptoms

-   Fields removed from or not visible on a form
-   Fields cannot be changed or are not mandatory as expected
-   Form sections not loading
-   UI policy not working
-   UI action not working
-   Client scripts not working

### Release

  All releases

### Cause

When a form loads, client scripts execute before UI policies are processed. An error in any client script halts all subsequent client-side processing, including UI policies, UI actions, and field visibility logic.

### Resolution

Use the browser's developer tools to identify which client script contains the error.

1.  Open the affected record in a browser.
2.  Open the browser's JavaScript console (typically via F12 or Developer Tools > Console).
3.  Clear the console to remove any pre-existing messages.
4.  Reload the form using Reload Form from the record header menu, or by right-clicking on a blank area of the record and selecting Reload Frame.
5.  Review the console for red error messages. An error caused by an undefined variable would appear similar to: `ReferenceError: test is not defined`
6.  Click the file link next to the error message ( `incident.do:1313`) to navigate to the failing line of JavaScript.
7.  In the script source, locate the surrounding function name. It will appear in a pattern similar to: **addRenderEventLogged(onLoad\_<hash>, 'onLoad Test Script');**
8.  Use the script name (e.g., Test Script) to locate the client script in ServiceNow and correct the error.

If the script name is not visible in the source view (for example, due to a minified or very long script), search for the offending variable or method directly in the Client Scripts list using the following filter:

**\[Script\] \[contains\] \[<offending text>\]**

 For Example:  
1\. Clear console logs.  
![Browser console log screen](/console_clear.pngx "Browser console log screen")

2\. Reload the form using Reload Form from the record header menu.  
After clearing the console and reloading the form, the following error appears: `ReferenceError: test is not defined`  
![red messages in the console. test is not defined](/console_error_sample.pngx "Example of console error message")

The failing line is highlighted in the source view, confirming the error originates inside an `onLoad` function.   
The function context reveals this belongs to a client script named Test Script.   
![incident onload function](/console_error_sample2.pngx "click into the error details")

### Related Links

[Client Script API - ServiceNow Fluent](https://www.servicenow.com/docs/r/application-development/servicenow-sdk/client-script-api-now-ts.html "Client Script API - ServiceNow Fluent")
