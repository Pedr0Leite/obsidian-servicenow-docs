---
title: "How to bulk update attributes for all columns in a table"
aliases:
  - KB0656708
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656708
kb_number: KB0656708
last_modified: 2026-05-14
---

## Issue

Sometimes you need to modify an attribute for a sys\_dictionary field. This can be done easily by navigating to the appropriate sys\_dictionary record and modifying the attribute field.

Sometimes you need to modify an attribute for many sys\_dictionary fields. This can take some time to accomplish manually.

* * *

## Resolution

The following script enables you to do a mass update of a specific table and set an attribute for all of the fields in a table.

**Caution** you should always test scripts thoroughly in a subprod environment before running in prod. Make sure to run with vDryRun set to true (as given) first.

```
var vTableName = 'cmdb_ci_printer';
var vAttribute = 'no_text_index=true';
var vDryRun = true; // set this to false when you're ready to do the change

// Do Not Modify below this line

bulkUpdateTableAttributes(vTableName, vAttribute, vDryRun);

function bulkUpdateTableAttributes(pTableName, pAttribute, pDryRun) {
    var gr = new GlideRecord('sys_dictionary');
    gr.addEncodedQuery('name=' + pTableName + '^element!=NULL');
    gr.query();
    var bUpdate = false;
    while (gr.next()) {
        var vAttributes = gr.attributes;
        var nLength;
        if (vAttributes) {
            nLength = vAttributes.length;
        } else {
            nLength = 0;
        }
        if (0 == nLength) {
            // There are no other attributes, just set it
            gr.attributes = pAttribute;
            bUpdate = true;
        } else {
            // Attributes is not empty, check to see if we have it set already:
            var n = vAttributes.indexOf(pAttribute);
            if (-1 == n) {
                // The attribute is not set, so append it:
                gr.attributes = vAttributes + ',' + pAttribute;
                bUpdate = true;
            } else {
                // The attribute is set; do nothing
            }
        }
        gs.print('Updating record sys_dictionary.do?sys_id=' + gr.sys_id + ' to ' + gr.attributes);
        if (!pDryRun) {
            if (bUpdate) {
                gr.setWorkflow(false);
                gr.update();
            }
        }
        bUpdate = false;
    }
}
```

Example Output:

\[0:00:00.009\] Script completed in scope global: script

* * *

\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9a82cd3bdb3332007dbb76231f96196d to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1282cd3bdb3332007dbb76231f961974 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1282cd3bdb3332007dbb76231f961952 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9682cd3bdb3332007dbb76231f961969 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1e82cd3bdb3332007dbb76231f96195e to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9282cd3bdb3332007dbb76231f961976 to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9e82cd3bdb3332007dbb76231f961960 to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1682cd3bdb3332007dbb76231f961978 to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9682cd3bdb3332007dbb76231f961958 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1282cd3bdb3332007dbb76231f961963 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9682cd3bdb3332007dbb76231f96197a to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1e82cd3bdb3332007dbb76231f96196f to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9282cd3bdb3332007dbb76231f961965 to no\_audit=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9e82cd3bdb3332007dbb76231f961971 to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=8526413fdb7332007dbb76231f96199e to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1a82cd3bdb3332007dbb76231f96195a to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1a82cd3bdb3332007dbb76231f96196b to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1682cd3bdb3332007dbb76231f961956 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=0c46cd3fdb7332007dbb76231f961914 to no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9a82cd3bdb3332007dbb76231f96195c to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=1682cd3bdb3332007dbb76231f961967 to no\_audit=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9282cd3bdb3332007dbb76231f961954 to edge\_encryption\_enabled=true,no\_text\_index=true  
\*\*\* Script: Updating record sys\_dictionary.do?sys\_id=9682cd3bdb3332007dbb76231f96197c to no\_text\_index=true
