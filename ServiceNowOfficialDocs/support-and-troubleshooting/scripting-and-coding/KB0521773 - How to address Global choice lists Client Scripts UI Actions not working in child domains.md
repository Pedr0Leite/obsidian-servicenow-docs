---
title: "How to address Global choice lists / Client Scripts / UI Actions not working in child domains"
aliases:
  - KB0521773
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521773
kb_number: KB0521773
last_modified: 2024-05-19
---

## How to address Global choice lists / Client Scripts / UI Actions not working in child domains

  

### Issue

Global choice lists / Client Scripts / UI Actions not working in child domains

  
  
Description

* * *

Overview of how choices work when using domains. 

  

Solution

* * *

**Partitioning** (using the sys\_domain field) and **Delegated Administration** (using the sys\_overrides field) work in different ways.  
  
**Partitioning**:

**Data** **records** are separated by a sys\_domain, which is hierarchical. For example, if you are in domain A, and domain A has a child domain B, which contains domain C, you can see any task record in domains A, B, or C.

  
**Delegated Administration**:

**Policy records** are _not_ separated by a sys\_domain. For example, sys\_choice, sys\_ui\_action, and sys\_client\_script all have both sys\_domain and sys\_overrides fields.  
For these **administration tables** (this is where the term, Delegated Administration, comes from) the sys\_domain field _does_ identify the domain that the policy record applies to.  
Sys\_overrides refers to another record in the same table, but _in a higher domain_, which this record replaces.  
  
This allows you to define a set of sys\_choice values that apply to the global domain, and then define a different set of choices that apply to a child domain.   
  
It is a common mistake to confuse Partitioning with Delegated Administration. If you create a new UI action and set the sys\_domain field to domain B, that means users in domain C will not see it. This is because policy tables are not partitioned like data. They use sys\_overrides and sys\_domain fields together to let child domains override policies in ancestral/parent domains.

  
**Example**:  
  
In a customized choice list field in the Change Request form, child domains do not inherit choices set to **global** in addition to any choices set to their **specific domain**.   
  
If the domains A, B, C are present in addition to the pseudo-domain **global**, the following will happen:   
  

-   Global has choices 1, 2, and 3 
-   A has no choices 
-   B has choices 4 and 5 
-   C has choices 6 and 7 

-   Users in domain C will see 6 and 7 
-   Users in domain B will see 4 and 5 
-   Users in domain A will see 1, 2, and 3 
-   Users in global will see 1, 2, and 3 

  
You may expect users in domain C to see 1, 2, 3, 6, and 7, or perhaps even 1, 2, 3, 4, 5, 6, and 7. That is not the case, because choices are not cumulative up the ancestor chain. The reason for this is that domain C may not actually want to see 1, 2, and 3.  
  
To address this, direct the first domain going up through the ancestry that has any choices to define _all_ choices. In other words, any domain that defines any choices, defines all of the choices for users in that domain or any descendant domain that doesn't define its own choices.
