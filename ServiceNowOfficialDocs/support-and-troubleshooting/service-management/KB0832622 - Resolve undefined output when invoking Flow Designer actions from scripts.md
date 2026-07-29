---
title: "Resolve undefined output when invoking Flow Designer actions from scripts"
aliases:
  - KB0832622
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832622
kb_number: KB0832622
last_modified: 2025-08-28
---

## Resolve undefined output when invoking Flow Designer actions from scripts

  

### Issue

Invoking Flow Designer actions from background scripts returns an undefined output but the same actions work correctly within Flow Designer.

To reproduce the issue:

1.  Go to Flow Designer.
2.  Enter the required inputs and select Test.
3.  Verify the flow returns the expected response.
4.  In Flow Designer, copy the script from More actions > Code snippet.
5.  Run the script in the background and observe the output displays as undefined.

### Release

New York

### Cause

 Adding error handling code (gs.print('exception: ' + ex);) reveals the underlying issue:

} catch (ex) {  
gs.print('exception: ' + ex);  
var message = ex.getMessage();  
gs.error(message);  
}

The error output shows:

\*\*\* Script: exception: JavaException: java.lang.IllegalArgumentException: objectToMap: invalid type class com.glide.vars2.GlideElementVariable for object property sapusers

  
This error occurs because FlowAPI validates input types and rejects the unexpected type "class com.glide.vars2.GlideElementVariable" when processing the variables. 

### Resolution

To resolve the issue, convert all inputs to strings by concatenating (add a +) with an empty string ("").

Incorrect usage:

inputs\['sapusers'\] = g1.variables.sap\_user\_role; // List

  
Correct usage

inputs\['sapusers'\] = '' + g1.variables.sap\_user\_role; // List

### Related Links

For more information, see the product documentation, [Create code snippets for flows, subflows, and action](https://www.servicenow.com/docs/bundle/zurich-build-workflows/page/administer/flow-designer/task/flow-design-code-snippet.html)
