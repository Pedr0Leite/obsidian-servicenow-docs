---
title: "Understand GlideDateTime in flow action scripts and output variables"
aliases:
  - KB0812370
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812370
kb_number: KB0812370
last_modified: 2025-08-27
---

## Understand GlideDateTime in flow action scripts and output variables

  

### Issue

In a flow action, when a GlideDateTime object is stored in a local variable and passed as an output variable of String type or Date/Time, the flow execution details page displays the date/time in the user's time zone instead of in UTC format (Coordinated Universal Time). 

The following code in a flow action script section demonstrates the issue:

(function execute(inputs, outputs) {  
// ... code ...  
var current\_datetime = new GlideDateTime();  
outputs.current\_datetime = current\_datetime;   
outputs.current\_datetime\_in\_datetime = current\_datetime;   
gs.log("\*\*\* GlideDateTime object \*\*\* " + current\_datetime);  
})(inputs, outputs);

In this example, **current\_datetime** is an output variable of type **String** and **current\_datetime\_in\_datetime** is an output variable of type **Date/Time**

After the flow execution, the date/time appears differently.

In the system log: 

\*\*\* GlideDateTime object \*\*\* 2020-01-22 01:53:30 // in UTC 

On the flow execution details page:

current\_datetime 21-01-2020 17:53:30 // in User's timezone  
current\_datetime\_in\_datetime 21-01-2020 17:53:30 // in User's timezone

### Release

All supported releases

### Cause

The flow execution details page displays date/time using the GlideDateTime.getDisplayValue() method, which shows date/time in the user's time zone. 

### Resolution

To display date/time in UTC on the flow execution details page, use the GlideDateTime.getValue() method in your script.

Modify your script as follows:

(function execute(inputs, outputs) {  
// ... code ...  
var current\_datetime = new GlideDateTime();  
outputs.current\_datetime = current\_datetime.getValue();   
outputs.current\_datetime\_in\_datetime = current\_datetime.getValue();   
gs.log("\*\*\* GlideDateTime object \*\*\* " + current\_datetime);  
})(inputs, outputs);

After flow execution, the date/time appears consistently:

In the system log:

\*\*\* GlideDateTime object \*\*\* 2020-01-22 01:53:30 // in UTC 

On the flow execution details page:

current\_datetime 2020-01-22 01:53:30 // in UTC  
current\_datetime\_in\_datetime 2020-01-22 01:53:30 // in UTC

### Related Links

For more about GlideDateTime API and methods, see the product documentation, [GlideDateTime - Global](https://docs.servicenow.com/csh?topicname=c_GlideDateTimeAPI.html&version=latest "GlideDateTime - Global")
