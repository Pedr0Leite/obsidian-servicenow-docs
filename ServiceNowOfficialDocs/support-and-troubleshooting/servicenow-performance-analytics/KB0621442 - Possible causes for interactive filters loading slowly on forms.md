---
title: "Possible causes for interactive filters loading slowly on forms"
aliases:
  - KB0621442
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621442
kb_number: KB0621442
last_modified: 2024-04-07
---

## Possible causes for interactive filters loading slowly on forms

  

### Issue

Possible causes for interactive filters loading slowly on forms

Problem Symptoms

* * *

Interactive filters load slowly or cause slowness when you select a value.  

Cause

* * *

The issue may be caused by **too many possible values**, or by **referencing too many tables**.  

  
Resolution

* * *

## Too many possible values

  
When you create the interactive filter, note the number of records that match the conditions. For example, in the following configuration there are greater than 20,000 possible values:  
  
![](sys_attachment.do?sys_id=526a6466db42b450e515c22305961939)

In this scenario, ensure that there are fewer than 10,000 possible values. Apply additional filter conditions to reduce the total number of matching values.  
  
If your conditions are particularly complex, consider creating a script include function that returns the correct set of records and create a condition that uses the result of that function.

  

## Too many references

  
When a user selects a value in an interactive filter, all widgets on the dashboard receive notifications about the change in the filter. The more references there are defined in the filter, the slower the response.  
  
When you create an interactive filter on a field used by extended tables such as **Assigned to** on Incident or Problem, create the filter on the parent table, such as Task. By creating the filter on the parent table, a single reference can be used in place of multiple references to the child tables.  
This behaviour has been fixed in the Istanbul release. Adding a filter condition on the extended table is equivalent to adding the filter condition on the parent table in Istanbul and later.
