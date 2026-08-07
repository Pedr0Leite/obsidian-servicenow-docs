---
title: "CMDB identification error: Missing required attribute: 'attribute_name"
aliases:
  - KB0623724
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623724
kb_number: KB0623724
last_modified: 2024-04-07
---

## CMDB identification error: Missing required attribute: 'attribute\_name'

  

### Issue

CMDB identification error: Missing required attribute: 'attribute\_name'

# Issue

* * *

When Discovery is run against a target system, the following error message is seen in the discovery log:

CMDB identification error: Missing required attribute:'attribute\_name'

where 'attribute\_name' is the field name. 

# Solution

* * *

1.  In the Discovery log, look for the Source field identifier associated with the error message.
    
2.  Navigate to **Configuration > Identification/Reconciliation > CI Identifiers** and search for the identifier, for example, Hardware Rule.
    
3.  In the CI Identifier page, see which table the identifier applies to, for example, if it applies to, for example, Hardware (cmdb\_ci\_hardware).
    
4.  Navigate to **System Definition > Tables** and search for the table, for example, Hardware.
    
5.  In the Table columns, add the Mandatory field into the view and search for mandatory fields set to true. If the field matches the missing required attribute in step 1, then set the mandatory field to false.
    

# Additional Information

* * *

You may also need to check the parent tables for the CI class (for example, mandatory fields on cmdb\_ci that are not present on child tables
