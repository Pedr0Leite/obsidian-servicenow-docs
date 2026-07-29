---
title: "Mobile App - onload Client Scripts do not return the correct value for the g_form.getValue() API"
aliases:
  - KB0657642
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657642
kb_number: KB0657642
last_modified: 2024-04-07
---

## Mobile App - onload Client Scripts do not return the correct value for the g\_form.getValue() API

  

### Issue

Mobile App - onload Client Scripts do not return the correct value for the "g\_form.getValue()" API

  
  

# Overview

* * *

In the Helsinki release, the API **g\_form.getValue()** invoked from an on-load Client Script fails to return the expected correct value.

For example, on mobile devices, navigating to **Incident > Assigned to me** loads the list of incidents assigned to current logged-in user. On the list, when you click the "+" symbol, the system creates a new incident record with the **Assigned to** field populated as the currently logged-in user. During this time, the onload client script, doesn't return the correct value for the g\_form.getValue("assigned\_to") API. Instead, it returns the value as "javascript:gs.user\_id()". Therefore, if you are on the Helsinki release, you cannot build a customization based on the on-load and g\_form.getValue() API in new records on mobile devices.

# Solution

* * *

This issue is resolved beginning with the Istanbul release as part of other enhancements and improvements in the mobile platform. Therefore, if you upgrade to the latest release available, this issue will be automatically resolved.

If you are on Helsinki, apply the workaround.

# Workaround

* * *

You need to create a new Display business rule with the attributes listed below. In the affected on-load Client Script, use the **global scratchpad** variable in order to access form values, as, for example, the Assigned To user name. This enables the building of the required business logic with the expected values retrieved.

\================================  
  
Table: Incident   
  
Active: True   
  
Advanced: True   
  
When to run =>   
  
When: Display   
  
Query: True   
  
Advanced =>   
  
Script:   
  
(function executeRule(current, previous /\*null when async\*/) {   
  
   
  
g\_scratchpad.assignee\_sys\_Id = gs.user\_id();   
  
g\_scratchpad.assignee\_name = gs.getUserDisplayName();   
  
   
  
})(current, previous);   
  
\================================= 

\=================================  
  
function onLoad() {   
  
//Type appropriate comment here, and begin script below   
  
alert("Assigned to:"+g\_scratchpad.assignee\_name);   
  
}   
  
\==================================
