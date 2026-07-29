---
title: "Why doesn't getDisplayValue() obey Dictionary Overrides?"
aliases:
  - KB0714258
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714258
kb_number: KB0714258
last_modified: 2025-08-19
---

## Why doesn't getDisplayValue() obey Dictionary Overrides?

  

### Issue

# Symptoms

* * *

It does, but when you have **Dictionary Overrides for Display Value** in place on extended tables like the CMDB, **you expect using getDisplayValue() to give you the Display value specific to that record's Class** (sys\_class\_name).

e.g. You may have a custom CI Class in the CMDB, where instead of using "Name", you wish for that CI to displayed with the value of some other field, maybe Asset Tag. **But your scripts continue to return the CI 'Name' from this function**.

# Release

* * *

All.

# Cause

* * *

You may be using the wrong class when you declare the GlideRecord. The Display value is taken from the GlideRecord object, not the specific record within that.

# Resolution

* * *

Use the exact same class for the GlideRecord as of the record.

e.g. 53958ff0c0a801640171ec76aa0c8f86 is the sys\_id of a Linux Server (sys\_class\_name=cmdb\_ci\_linux\_server) in the Demo Data.

The cmdb.asset\_tag field has had a Dictionary Override added for that Linux Server class, with 'Override Display' ticked.

var dave = new GlideRecord('cmdb\_ci'); // This is the top level table for IT-based CIs.   
dave.get('53958ff0c0a801640171ec76aa0c8f86');   
gs.print(dave.getDisplayValue()); // This will use 'name' because that is still what cmdb\_ci defaults to.  
  
output   
\*\*\* Script: lnux100   
  
var dave = new GlideRecord('cmdb\_ci\_linux\_server'); // this is the actual class of this record  
dave.get('53958ff0c0a801640171ec76aa0c8f86');   
gs.print(dave.getDisplayValue());  // This will use asset\_tag, because it will now use the cmdb\_ci\_linux\_server specific override  
  
output   
\*\*\* Script: P1000165
