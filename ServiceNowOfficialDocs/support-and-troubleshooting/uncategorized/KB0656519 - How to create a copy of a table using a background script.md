---
title: "How to create a copy of a table using a background script"
aliases:
  - KB0656519
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656519
kb_number: KB0656519
last_modified: 2026-01-16
---

## How to create a copy of a table using a background script

  

### Issue

This article explains how to create a copy of an existing table so that you can access the copied table from the UI or from a background script. You may need to copy a table for a test case or to back up data from a rotated shard before it gets truncated. The new table is empty and does not contain data. You must copy date from the source table as a separate process. 

Although ServiceNow can create a backup of a table from the backend, you cannot access it from the instance such as from a form, list, or background script (/sys.scripts.do). The application does not recognize the new table because the application requires associated records in the metadata tables (sys\_db\_object, sys\_dictionary, sys\_documentation, and others). 

#### **Important considerations:**

The script in this article does not work for CMDB tables. 

This script uses a deprecated script include for Table Rotation to construct the new table. The resulting table may have differences, such as adding the edge\_encryption\_enabled attribute on the new table's sys\_dictionary records. **This is not an exact copy.** The edge encryption attribute only has impact if Edge Encryption is licensed, set up, and configured. Edge Encryption is deprecated and can no longer be purchased. For more details on Edge Encryption, see the [ServiceNow documentation](https://www.servicenow.com/docs/bundle/zurich-platform-security/page/administer/edge-encryption/reference/edge-encryption.html). 

### Release

All supported releases

### Resolution

### Before New York release

1\. Go to /sys.scripts.do.

2\. Copy the following code and customize it for your environment.

The script accepts three arguments:

-   **First argument**: The source table to be copied
-   **Second argument**: The new target table name
-   **Third argument**: Boolean value to control index creation. Set the value to false if you do not need to create indexes. (Creation time is fast either way because the table is empty.)

cpTable('sys\_upgrade\_history\_log', 'u\_testcase', true);  
   
function cpTable(strOldTable, strNewTable, bCopyIndexes) {  
    var tu = new TableUtils(strNewTable);  
    var bNewTableAlreadyExists = tu.tableExists();  
    if (bNewTableAlreadyExists) {  
        gs.print("WARNING: Target Table " + strNewTable + " already exists!  Please choose a new target table name");  
    } else {  
        var gr = new GlideRecord(strOldTable);  
        gr.initialize();  
        var td = GlideTableDescriptor.get(strOldTable);  
        var tdNewTable = new TableDescriptor(strNewTable, gr.getLabel());  
        var dbo = new GlideRecord("sys\_db\_object");  
        dbo.addEncodedQuery("super\_classISNOTEMPTY^name=" + strOldTable);  
        dbo.setLimit(1);  
        dbo.query();  
        if (dbo.next()) {  
            tdNewTable.setExtends(dbo.super\_class + '');  
        }  
        tdNewTable.setFields(gr);  
        tdNewTable.copyAttributes(td);  
        tdNewTable.setRoles(td);  
        tdNewTable.create();  
        if (bCopyIndexes) {  
            tdNewTable.copyIndexes(strOldTable, strNewTable);  
        }  
    }  
}  
  

3\. Select **Run Script**.

The script creates a new table called **u\_testcase**. You can access this table at /u\_testcase\_list.do or using GlideRecord('u\_testcase');. 

**Example output:**

\[0:00:01.621\] Script completed in scope global: script  
Creating table: u\_testcase  
TableCreate for: u\_testcase  
DBTable.create() for: u\_testcase  
Replication is not enabled on table: u\_testcase, not queueing replication table create special db event  
\*\*\* Script: Begin ResourceSupport.buildTableResources(u\_testcase, undefined)  
\*\*\* Script: End ResourceSupport.buildTableResources  
LicensingTableCreateListener: Initializing licensing attrs for table u\_testcase  
Time: 0:00:00.615 id: tundra\_1\[glide.2\] for: SELECT sys\_storage\_alias0.\`table\_name\`, sys\_storage\_alias0.\`element\_name\`, sys\_storage\_alias0.\`storage\_alias\` FROM sys\_storage\_alias sys\_storage\_alias0  WHERE sys\_storage\_alias0.\`storage\_alias\` != sys\_storage\_alias0.\`element\_name\` /\* tundra004, gs:329947A4DBAE4700671C51035E9619B8, tx:52c94328dbae4700671c51035e9619cb \*/   
Creating index(es): ALTER TABLE \`u\_testcase\`ADD INDEX (\`sys\_source\_table\`) ,ADD INDEX (\`update\_set\`) ,ADD INDEX (\`upgrade\_history\`)   
Duplicate index, skipping: u\_testcase(\[sys\_source\_table\]) NONUNIQUE  
Duplicate index, skipping: u\_testcase(\[update\_set\]) NONUNIQUE  
Redundant index check on u\_testcase found redundant index upgrade\_history (upgrade\_history) NONUNIQUE; caused by new index (upgrade\_history,file\_name,sys\_recorded\_at) NONUNIQUE  
Redundant index check on u\_testcase found 1 redundant indexes  
Creating index(es): ALTER TABLE \`u\_testcase\`ADD INDEX (\`upgrade\_history\`, \`file\_name\`, \`sys\_recorded\_at\`) ,ADD INDEX (\`upgrade\_history\`, \`order\`) ,ADD INDEX (\`upgrade\_history\`, \`disposition\`, \`resolution\_status\`, \`changed\`, \`order\`) ,ADD INDEX (\`upgrade\_history\`, \`resolution\_status\`, \`disposition\`, \`type\_priority\`) ,ADD INDEX (\`upgrade\_history\`, \`disposition\`, \`changed\`) ,ADD INDEX (\`order\`)   
Dropping index(es): ALTER TABLE \`u\_testcase\` DROP INDEX \`upgrade\_history\`

If you run the same script again with the same target table name, the following warning appears:

\[0:00:00.000\] Script completed in scope global: script  
\*\*\* Script: WARNING: Target Table u\_testcase already exists! Please choose a new target table name

### New York and subsequent releases

1\. Go to /sys.scripts.do.

2\. Copy the following code and customize it for your environment.

The script accepts three arguments:

-   **First argument**: The source table to be copied
-   **Second argument**: The new target table name
-   **Third argument**: Boolean value to control index creation. Set to false if you do not need to create indexes. (Creation time is fast either way because the table is empty.)

cpTable('sys\_upgrade\_history\_log', 'u\_testcase', true);  
   
function cpTable(strOldTable, strNewTable, bCopyIndexes) {  
    var tu = new TableUtils(strNewTable);  
    var bNewTableAlreadyExists = tu.tableExists();  
    if (bNewTableAlreadyExists) {  
        gs.print("WARNING: Target Table " + strNewTable + " already exists!  Please choose a new target table name");  
    } else {  
        var gr = new GlideRecord(strOldTable);  
        gr.initialize();  
        var td = GlideTableDescriptor.get(strOldTable);  
        var tdNewTable = new SNC.TableRotationBootstrap(strNewTable, gr.getLabel());  
        var dbo = new GlideRecord("sys\_db\_object");  
        dbo.addEncodedQuery("super\_classISNOTEMPTY^name=" + strOldTable);  
        dbo.setLimit(1);  
        dbo.query();  
        if (dbo.next()) {  
            tdNewTable.setExtends(dbo.super\_class.name + '');  
        }  
        tdNewTable.setFields(gr);  
        tdNewTable.copyAttributes(td);  
        tdNewTable.create();  
        if (bCopyIndexes) {  
            tdNewTable.copyIndexes(strOldTable, strNewTable);  
        }  
    }  
}  
  

3\. Select **Run Script**.

The script creates a new table called **u\_testcase**. You can access this table at /u\_testcase\_list.do or using GlideRecord('u\_testcase');. 

**Example output:**

Creating table: u\_testcase  
TableCreate for: u\_testcase  
DBTable.create() for: u\_testcase  
Replication is not enabled on table: u\_testcase, not queueing replication table create special db event  
\*\*\* Script: Begin ResourceSupport.buildTableResources(u\_testcase, undefined)  
\*\*\* Script: End ResourceSupport.buildTableResources  
LicensingTableCreateListener: Initializing licensing attrs for table u\_testcase  
Creating index(es): ALTER TABLE \`u\_testcase\`ADD INDEX (\`sys\_source\_table\`) ,ADD INDEX (\`upgrade\_history\`) ,ADD INDEX (\`update\_set\`)   
\[0:00:13.170\] DBTable.create of: u\_testcase  
\[0:00:14.839\] Table create for: u\_testcase  
Duplicate index, skipping: u\_testcase(\[sys\_source\_table\]) NONUNIQUE  
Duplicate index, skipping: u\_testcase(\[update\_set\]) NONUNIQUE  
Redundant index check on u\_testcase found redundant index upgrade\_history (upgrade\_history) NONUNIQUE; caused by new index (upgrade\_history,order) NONUNIQUE  
Redundant index check on u\_testcase found 1 redundant indexes  
Creating index(es): ALTER TABLE \`u\_testcase\`ADD INDEX (\`upgrade\_history\`, \`order\`) ,ADD INDEX (\`upgrade\_history\`, \`resolution\_status\`, \`disposition\`, \`type\_priority\`) ,ADD INDEX (\`upgrade\_history\`, \`file\_name\`, \`sys\_recorded\_at\`) ,ADD INDEX (\`upgrade\_history\`, \`disposition\`, \`changed\`) ,ADD INDEX (\`upgrade\_history\`, \`disposition\`, \`resolution\_status\`, \`changed\`, \`order\`) ,ADD INDEX (\`order\`)   
Dropping index(es): ALTER TABLE \`u\_testcase\` DROP INDEX \`upgrade\_history\`  
Altering storage table \[sh$sys\_cache\_flush\]: ALTER TABLE sh$sys\_cache\_flush ADD \`sh$context\`  VARCHAR(32) , ADD \`sh$operation\`  VARCHAR(40) , ADD \`sh$change\_count\`  INTEGER , ADD \`sh$first\_recorded\`  DATETIME , ADD \`sh$last\_recorded\`  DATETIME , ADD \`sh$sequence\`  VARCHAR(40) , ADD \`sh$first\_txn\_id\`  VARCHAR(32) , ADD INDEX \`mnixgjyj\_source\_primary\`(\`sys\_id\`)   
\*\*\* Script: Begin ResourceSupport.buildTableResources(sh$sys\_cache\_flush, undefined)  
\*\*\* Script: End ResourceSupport.buildTableResources
