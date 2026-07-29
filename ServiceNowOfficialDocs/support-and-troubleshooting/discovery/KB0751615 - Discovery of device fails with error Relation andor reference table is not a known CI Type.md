---
title: "Discovery of device fails with error \"Relation and/or reference table is not a known CI Type\"
aliases:
  - KB0751615
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751615
kb_number: KB0751615
last_modified: 2025-07-17
---

## Issue

Discovery of the device fails with the error:

"Relation and/or reference table <table\_name> is not a known CI Type"

## Resolution

1.  Review the "Create Relation/Reference" where the error is thrown and find the "Child" table. In this example we open the pattern step which caused the error and see the child table is cmdb\_ci\_ip\_switch  
    ![Pattern step showing Parent Table: $discovery\_net\_arp\_table](sys_attachment.do?sys_id=5da82e65933ea2d0c2513f986cba10b0)
2.  Determine the identifier being used for the table by navigating to "Configuration > CI Class Manager" and selecting the table. In the following example we see the "Hardware Rule" identifier being used for the IP Switch table  
    !["Hardware Rule" identifier ](sys_attachment.do?sys_id=95a82e65933ea2d0c2513f986cba10b3)
3.  Navigate to the identifiers table and open the identifier, "Configuration > Identification/Reconciliation > CI Identifiers".  
    1.  Add the "Parent" table to its "Related Entries", the one listed in the error message (discovery\_net\_arp\_table table in the example listed in the "Cause" section of this KB).  
        ![Related Entries tab on Identifier cmdb\_ci\_hardware screen](sys_attachment.do?sys_id=41a82e65933ea2d0c2513f986cba10ae)  
        In the image above the discovery\_net\_arp\_table is already present as the identifier is OOB
4.  Run discovery again and confirm the issue is resolved.

**Note:** To find the identifier used, search the cmdb\_identifier table for records where "Applies to" matches the "Child" table of the step. If none is found, search for the table which the "Child" table is extended from and so forth. Also, please check if any related records are customized or if any changes then revert to OOB as needed.

## Additional Information

If this error is seen with a table name starting with "cmdb" then this is likely due to [PRB1509992/KB0967245: GETCITypes discovery code assumes that the cmdb is the base table instead of previous cmdb\_ci - Relation and/or reference table <cmdb\_table\_example> is not a known CI Type](https://support.servicenow.com/kb_view.do?sysparm_article=KB0967245 "GETCITypes discovery code assumes that the cmdb is the base table instead of previous cmdb_ci - Relation and/or reference table <cmdb_table_example> is not a known CI Type").

[CMDB identification rules](https://docs.servicenow.com/csh?topicname=c_IdentificationRules.html&version=latest "CMDB identification rules")

[How to copy the Hardware Rule CMDB Identifier for specific Sub-Classes, to identify Unusual Hardware correctly, or where different devices are known to share name/serial](https://hi.service-now.com/kb_view.do?sysparm_article=KB0693296 "How to copy the Hardware Rule CMDB Identifier for specific Sub-Classes, to identify Unusual Hardware correctly, or where different devices are known to share name/serial")
