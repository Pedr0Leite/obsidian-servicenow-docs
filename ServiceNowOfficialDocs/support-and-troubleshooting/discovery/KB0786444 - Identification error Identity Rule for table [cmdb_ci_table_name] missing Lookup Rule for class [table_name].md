---
title: "Identification error \"Identity Rule for table [cmdb_ci_table_name] missing Lookup Rule for class [table_name]\"
aliases:
  - KB0786444
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786444
kb_number: KB0786444
last_modified: 2024-10-31
---

## Identification error "Identity Rule for table \[cmdb\_ci\_table\_name\] missing Lookup Rule for class \[table\_name\]"

  

### Issue

A payload passed to the identification engine returns error like:

-   "Identity Rule for table \[cmdb\_ci\_table\_name\] missing Lookup Rule for class \[table\_name\]".
-   "Identity Rule for table \[cmdb\_ci\_table\_name\] missing Related Rule for class \[table\_name\]".

Example error:

IDENTIFICATION\_RULE\_FOR\_LOOKUP\_MISSING Identity Rule for table \[cmdb\_ci\_hardware\] missing Lookup Rule for class \[cmdb\_serial\_number\]: no thrown error

This can happen from any data source or application sending data to the IRE to update the CMDB.

In the following example we see this error when running a windows server discovery:

Identity Rule for table \[cmdb\_ci\_win\_server\] missing Lookup Rule for class \[cmdb\_serial\_number\],Identity Rule for table \[cmdb\_ci\_win\_server\] missing Related Rule for class \[discovery\_net\_arp\_table\],Abandoned due to too many errors

![](sys_attachment.do?sys_id=2ca7f867dbc0c95080073ca8f49619f7)

### Cause

The Identification and Reconciliation Engine (IRE) will attempt to remove duplicate data from a payload before processing it. The IRE needs to understand what makes a record unique before removing it from the payload. Depending on the class this could be done via the identifiers, lookup rules, or related entries. However if rules cannot be found to determine uniqueness the error is returned. This issue is often seen when Out Of Box (OOB) identifiers are customized.

### Resolution

There are different options to resolve this error. First we need to find the identifier used.

#### Finding the Identifier:

1.  From the following error we see the identifier class is cmdb\_ci\_hardware, and missing rule for cmdb\_serial\_number
    
    IDENTIFICATION\_RULE\_FOR\_LOOKUP\_MISSING Identity Rule for table \[cmdb\_ci\_hardware\] missing Lookup Rule for class \[cmdb\_serial\_number\]: no thrown error
    
2.  Navigate to "Configuration > Identification/Reconciliation > CI Identifiers"
3.  Search for the identifier, in this case cmdb\_ci\_hardware would be used to search on field "Applies to"

#### Option A

Add a proper lookup identifier or related entry to the identifier:

1.  Is the error for a Lookup rule?  
    -   Yes: Add a lookup rule using the missing rule table  
        -   Would be cmdb\_serial\_number on this example, see following example
        -   ![](sys_attachment.do?sys_id=92ec3423db84c95080073ca8f49619d3)
2.  Is the error for Related entry?  
    -   Yes: Add related entry. In the following example we see a related entry for "cmdb\_key\_value"
    -   ![](sys_attachment.do?sys_id=776d3067db84c95080073ca8f496198b)

**Note:** If the OOB identifier already contained such rule or entry, revert to OOB.

#### Option B

If a rule for this class cannot be added for some reason the remove the problem records from the payload.

As an example, one would need to update the pattern steps which collect/build such data if this error were to happen on a pattern discovery. This would depend on the application calling the IRE.
