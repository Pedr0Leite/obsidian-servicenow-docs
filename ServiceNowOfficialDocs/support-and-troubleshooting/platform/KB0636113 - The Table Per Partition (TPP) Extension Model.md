---
title: "The Table Per Partition (TPP) Extension Model"
aliases:
  - KB0636113
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0636113
kb_number: KB0636113
last_modified: 2025-08-15
---

## Issue

### What are table hierarchies?

The ServiceNow platform stores data in tables within an underlying relational database (RDBMS). To allow the effective organization of this data, the platform uses the concept of hierarchies of related tables. Within these hierarchies, a child table can extend the functionality of a parent table thereby inheriting all of the fields available to the parent as well as adding its own additional fields. Hierarchies are known by the name of their base table which all other tables in the hierarchy extend – two common hierarchies are:

-   Task
-   Configuration Management Database (CMDB)

Using the CMDB hierarchy as an example, the base cmdb table contains fields that are common to all configuration items (CIs) such as:

-   asset\_tag
-   location
-   manufacturer
-   serial\_number
-   and so on

Child tables then extend cmdb to add their own fields to store details specific to a certain class of configuration item – for example, the cmdb\_ci table adds fields such as:

-   ip\_address
-   model\_number
-   operational\_status

Note that if a CI is added to a child table (for example cmdb\_ci) then a record for that CI will also be created in all parent/extended tables (i.e. cmdb). This means that, in some cases, adding a CI to a table which extends many other tables will cause multiple records to be created within the hierarchy. For example adding a new CI of type 'cmdb\_ci\_server' will add a record to:

-   cmdb
-   cmdb\_ci (extends cmdb)
-   cmdb\_ci\_hardware (extends cmdb\_ci)
-   cmdb\_ci\_computer (extends cmdb\_ci\_hardware)
-   cmdb\_ci\_server (extends cmdb\_ci\_computer)

### What are extension models?

Extension models define how physical data for a table hierarchy is stored in the underlying RDBMS. Prior to the Jakarta release, two extension models have been available:

-   Table per class (TPC)
-   Table per hierarchy (TPH)

The Jakarta release adds a new extension model:

-   Table per partition (TPP)

These extension models are explained in more detail in the following document: [Table flattening](https://docs.servicenow.com/csh?topicname=c_TaskTableFlattening.html&version=latest "Table flattening")

### The Table Per Partition (TPP) Extension Model:

The TPP extension model is known as a ‘flattened’ hierarchy. This means that:

-   At a logical layer (i.e. within the ServiceNow platform) the hierarchy contains a set of distinct tables
-   At a physical layer (i.e. within the underlying RDBMS), however, all data contained within the hierarchy is held in a single flat ‘storage layer’

### Differences Between TPH and TPP:

The TPP extension model is somewhat similar to the TPH extension model (used by Task). There are, however, a number of important differences:

-   The TPH hierarchy uses a single physical base table in which to store all data – this table cannot be grown in size
-   The TPP hierarchy initially uses a single physical base table to store all data - this table can be horizontally ‘grown’ using overflow/storage partitions
-   Each overflow/storage partition is an additional physical table within the underlying RDBMS
-   Overflow/storage partitions are created as/when required and have a common naming convention – using the CMDB hierarchy as an example:  
    -   The initial ‘base’ table is ‘cmdb’
    -   The first storage partition will be cmdb$par1
    -   The second storage partition will be cmdb$par2
    -   And so on

The TPP extension model introduces a number of new concepts when compared with TPC/TPH - these are discussed in more detail later in this document.

![](sys_attachment.do?sys_id=506f0bba479baa143b05ff48436d43f1)

### What do flattened hierarchies offer over TPC?

Table hierarchies consist of a number of tables within the ServiceNow platform with complex parent/child relationships. In the case of the TPC extension model (a non-flattened hierarchy) each of these tables corresponds to a physical table in the RDBMS. Whist this arrangement is easy to understand it is not optimized for performance:

-   Some table hierarchies can be extremely ‘deep’ (i.e. the out of the box CMDB hierarchy has child tables with 7 parent tables up to and including the base cmdb table)
-   Changes to entities within the hierarchy can therefore require multiple operations to be performed within the RDBMS - for example:  
    -   Add a new entity to a child table: Records must be inserted into this child table and all parent tables up to and including the hierarchies base table - this can cause multiple insert operations to be performed
    -   Delete an existing entity: Records must be removed from child and all parent tables up to and including the hierarchies base table - this can cause multiple delete operations to be performed
    -   Modify an existing entity: Modifications may affect multiple fields across the child and parent tables up to and including the hierarchies base table - this can cause multiple update operations to be performed
-   Certain queries against the hierarchy may need to retrieve data for entities which exist in multiple layers of the hierarchy  
    -   Such queries can only be satisfied by performing multiple joins against tables in the hierarchy
    -   Joins are computationally expensive and as a result such queries perform slowly which can, in some cases, cause poor performance of the platform or degradation of user experience

Flattened hierarchies overcome this performance bottleneck by storing all data for the hierarchy in a single physical table (TPH) or layer (TPP). This causes significant reduction in:

-   The number of operations required within the RDBMS when adding/updating/removing an entity:  
    -   TPH: A single insert/update/delete operation is required
    -   TPP: A small number of insert/update/delete operations are required (up to the number of existing storage partitions)
-   Significant reduction in the number of joins required when querying data:  
    -   TPH: Can, in theory, satisfy any query without joins as all data for the hierarchy is in a single physical table
    -   TPP: May require a small number of joins (as data is distributed across the base table and any storage partitions) however the total number of joins required is minimized

Due to the performance of TPH/TPP extension models should be considerably improved compared with the TPC extension model.

### What does TPP offer over TPH?

The MySQL database is relatively restrictive in terms of physical table structure – for example:

-   The width of a MySQL table cannot exceed 64Kb in size
-   The total size of a single row of data within a table cannot exceed 8Kb in size
-   A single table cannot exceed 1000 columns
-   A single table can only have a maximum of 64 indexes created against it

One or more of these limits can easily be exceeded when flattening a complex hierarchy (such as Task) into a single physical table (TPH extension model). Whilst solutions to avoid this do exist within the ServiceNow platform (for example use of the offrow storage plugin) this limits the scalability of TPH hierarchies.

In the Rome release the capability of the platform to support up to 128 indexes per table on MySQL/MariaDB was added, but this depends on the capabilities of the database software being used.  For On-Cloud instances 128 indexes are supported but for self-hosted installations this is only typically possible with the Enterprise versions of MySQL/MariaDB, with the Community releases still only supporting 64 indexes per table.  The platform does check the capabilities of the database it using to determining the number of indexes it can use without needing any specific configuration. 

This does mean that for Self-Hosted environments having a homogeneous version of MySQL/MariaDB is recommended as performing an on-premise clone from an instance on MySQL/MariaDB Enterprise instance to a instance using the MySQL/MariaDB Community release is liable to be fail because of the Community version not being able to support the number of indexes present on the Enterprise instance.

With RaptorDB based instances there is no functional limit to the number of indexes per table (its 2^32 = 2147483647).  There is no change in the maximum number of columns per table on RaptorDB, which remains at 1000.

The TPP extension model can overcome these restrictions by using multiple physical tables arranged in a horizontal layout. For example:

-   Initially, a single physical base table will be created within the RDBMS and have data inserted into it
-   The addition of fields to logical tables within the hierarchy may mean that physical columns are added to this base table
-   Indexes may need to be added to this base table to improve the performance of certain common queries
-   If the base table is in danger of exceeding any of the MySQL imposed restrictions a second storage partition can be added to the hierarchy to hold additional columns and/or indexes

As a result of the above, the TPP extension model adds significant scalability over the TPH extension model for large/complex table hierarchies.

### New concepts introduced with the TPP extension model:

TPP introduces a number of new concepts to the underlying ServiceNow platform. Whilst these are completely transparent to end-users they may be of interest to administrators wishing to understand how the TPP extension model functions.

**Synchronized Columns:**

-   The base table and each additional storage partition are distinct physical tables within the underlying RDBMS
-   Certain commonly used fields are ‘synchronized’ across these physical tables (i.e. they exist as columns in every physical table)  
    -   Columns which are ‘synchronized’ include:  
        -   All ‘sys\_\*’ columns
        -   Display values (which are not reference fields)
        -   Commonly queried fields
    -   A synchronized column is indicated by the existence of the ‘synchronizePartitions=true’ attribute against the fields dictionary entry (record in the sys\_dictionary table)
-   Synchronized columns are used for various reasons:  
    -   If the column is used in a large variety of queries then, by being synchronized, it will always be close to other columns used in these queries hence avoiding joins where possible
    -   Indexes cannot span physical tables so in some circumstances, it may be necessary to synchronize columns so that all columns in an index exist together on at least one physical table
-   When using TPP all entities recorded in the hierarchy will have a corresponding record in all physical tables/storage partitions:  
    -   All physical tables will therefore have an identical number of rows
    -   A single entities record in one physical table can be related to records for the same entity in other physical tables via a common sys\_id (which is synchronized across tables)
-   Inserts/updates/deletes of data in the TPP hierarchy is transactional meaning that the operation must complete across all physical tables or fail entirely

**Field Inheritance:**

-   All extension models share the concept of ‘application’ table extensibility, i.e.:  
    -   An existing table in the hierarchy can be extended by one or more child tables
    -   The child table should ‘inherit’ all fields which are available to the parent table
-   With the TPC and TPH extension models each distinct field in the hierarchy will have a single dictionary entry (record in the sys\_dictionary table):  
    -   This is related to the table which ‘owns’ the field (i.e. the table against which the field was created)
-   In the TPP extension model inherited fields are physically duplicated to child tables meaning that:  
    -   A single field can have multiple dictionary entries (i.e. multiple records in the sys\_dictionary table):  
        -   The single ‘base’ record (i.e. the sys\_dictionary record corresponding to the table against which the field was initially created)
        -   One additional cloned record corresponding to every child table which extends the fields ‘base’ table
    -   Only the base dictionary entry can be modified – if a cloned dictionary entry is opened in the user interface (UI) a message similar to the following will be shown:

This cloned descendant element is read-only, navigate to `/sys_dictionary.do?sysparm_query=name=cmdb%5eelement=asset_tag` to open the editable first element (cmdb.asset\_tag) in a new window.

-   Modifications to the base dictionary entry are automatically propagated to all cloned dictionary entries for that field
-   This means that, on conversion of a table hierarchy to TPP, there will be a significant increase in:  
    -   The total number of dictionary entries and attributes for the hierarchy
    -   The total number of dictionary attribute relationships (i.e. records in the sys\_schema\_attribute\_m2m table)

**Storage Aliases:**

-   The ServiceNow platform uses the concept of storage aliases (records in the sys\_storage\_alias table) to define the physical column in the underlying database where data for a certain field should be stored – this allows:  
    -   Use of logical field names which exceed underlying database limits (for example 64 characters when using MySQL)
    -   Sharing of physical database columns for data storage by multiple fields in a table hierarchy (also known as ‘glomming’)
-   With the TPC and TPH extension models each field in a table hierarchy will have a single corresponding storage alias:  
    -   This corresponds to the table against which the field was created
-   With the TPP hierarchy, however, inherited fields are physically duplicated to child tables (as explained above) meaning that there may be many storage aliases for a single field, i.e.:  
    -   A single record in the ‘sys\_storage\_alias’ table corresponding to the ‘base’ copy of the field (i.e. relating to the table against which the field was created)
    -   One additional record corresponding to every child table which extends the ‘base’ table and therefore has a clone of the field

**System Class Path:**

-   The TPP extension model provides every table in the table hierarchy with a sys\_class\_path value:  
    -   This is analogous to the sys\_domain\_path value seen in domain separated instances
    -   The root table has a sys\_class\_path value of ‘/’
    -   When a table within the hierarchy is extended the child table inherits the parents sys\_class\_path value then adds its own two-character stanza
-   To describe this further using the cmdb table hierarchy as an example:  
    -   The cmdb table has a sys\_class\_path of ‘/’
    -   The cmdb\_ci table (which extends cmdb) has a sys\_class\_path of ‘/!!’
    -   The cmdb\_ci\_appl table (which extends cmdb\_ci) has a sys\_class\_path of ‘/!!/!(’
-   Using a tables sys\_class\_path value it is possible to determine:  
    -   Which tables a child table extends
    -   Which tables are extended from a parent table

For example:

-   The cmdb\_ci\_infra\_service table has a sys\_class\_path of ‘/!!/!(/!3’:  
    
    mysql> select name, sys\_class\_path from sys\_db\_object where name = 'cmdb\_ci\_infra\_service';  
    +-----------------------+----------------+  
    | name                  | sys\_class\_path |  
    +-----------------------+----------------+  
    | cmdb\_ci\_infra\_service | /!!/!(/!3      |  
    +-----------------------+----------------+
    
-   Using this it is easy to determine that the cmdb\_ci\_infra\_service table extends the cmdb, cmdb\_ci, and cmdb\_ci\_appl tables:  
    
    mysql> select name, sys\_class\_path from sys\_db\_object where sys\_class\_path in ('/', '/!!', '/!!/!(', '/!!/!(/!3') order by sys\_class\_path;  
    +-----------------------+----------------+  
    | name                  | sys\_class\_path |  
    +-----------------------+----------------+  
    | cmdb                  | /              |  
    | cmdb\_ci               | /!!            |  
    | cmdb\_ci\_appl          | /!!/!(         |  
    | cmdb\_ci\_infra\_service | /!!/!(/!3      |  
    +-----------------------+----------------+
    
-   Likewise, it is possible to determine that 28 tables in the hierarchy extend the cmdb\_ci\_infra\_service table:
    
    mysql> select count(\*) from sys\_db\_object where sys\_class\_path like '/!!/!(/!3%';  
    +----------+  
    | count(\*) |  
    +----------+  
    |       28 |  
    +----------+ 
    

### Frequently Asked Questions (FAQs):

**Q: In the Jakarta release of ServiceNow do any table hierarchies actually use the TPP extension model?**

Yes – the CMDB table hierarchy will be converted to the TPP extension model during the upgrade to Jakarta. Additional table hierarchies may use the TPP extension model in future releases. Further information on the CMDB conversion process is available in the following document: [KB0683772: Migration of the CMDB table hierarchy to the Table Per Partition (TPP) Extension Model](https://support.servicenow.com/kb_view.do?sysparm_article=KB0683772 "KB0683772: Migration of the CMDB table hierarchy to the Table Per Partition (TPP) Extension Model")

**Q: The TPP is clearly more scalable than the TPH extension model (as used by ‘Task’). Are there any plans to migrate the ‘Task’ table hierarchy to the TPP extension model?**

At this time there are no plans to perform this. If customers are encountering storage limits in the task table hierarchy they should contact ServiceNow Technical Customer Support who can advise the best approach to mitigate issues.

**Q: This document references MySQL imposed row size/length limitations (64Kb and 8Kb respectively). How are these limitations dealt with by the TPP extension model?**

Unfortunately, there is no automation within the ServiceNow platform to solve these issues (yet). TPP does, however, provide the means to create additional storage partitions and migrate columns between these partitions as necessary to avoid these constraints. For example, if adding a column to an existing storage partition would cause rows in that partition to exceed 64Kb in length, an additional storage partition can instead be created to hold the column. Likewise, if rows being inserted into a storage partition are commonly over 8Kb in size (and therefore failing to insert) one or more columns holding a significant proportion of this data could be migrated to an alternate storage partition to avoid these issues.

As of the initial release of the TPP extension model interfaces to perform the above are not directly available to customers – any customers who feel they would benefit from these features should engage ServiceNow Technical Customer Support who will be pleased to advise further.

**Q: Using the TPP extension model is it possible to manually synchronize arbitrary columns across/move arbitrary columns between storage partitions?**

Yes, this is possible however as of the initial release of the TPP extension model interfaces to perform this is not directly available to customers – any customers who feel they would benefit from this feature should engage ServiceNow Technical Customer Support who will be pleased to advise further.

**Q: Will the TPP extension model automatically add new partitions to overcome limits on existing tables during normal runtime operation?**

Technically the platform does have the means to automatically add storage partitions to a hierarchy using the TPP extension mode in a range of scenarios. As of the initial release of the TPP extension model, however, this will only take place when the number of indexes on an existing partition is exhausted. For example:

-   The platform attempts to add a new index to an existing partition
-   This fails due to a ‘Too many indexes’ exception
-   The platform will then ensure that at least one partition exists which does have space available for this additional index and, if necessary, will create a new storage partition to adhere to this

Even in the above scenario, however, the required columns will not be automatically migrated/synchronized to the new storage partition to allow the creation of the index. This would have to be performed by ServiceNow Technical Customer support after which the index could be created on the new storage partition.

**Q: What happens when a new table is added to a table hierarchy using the TPP extension model?**

As with the TPH extension model if a new table is added to the hierarchy then no new physical table is created in the underlying RDBMS. Instead a new record with be created in the sys\_db\_object table with unique sys\_class\_name to describe the corresponding logical table. In addition to this:

-   The logical table will have dictionary entries (records in the sys\_dictionary table) created for every column on the table (including those inherited from parent tables)
-   Records will be created in the sys\_storage\_alias table to describe:
-   Physical columns in the RDBMS used by each column in the logical table (including those inherited from parent tables)
-   Which storage partition (i.e. cmdb, cmdb$par1, cmdb$par2, and so on) holds each physical column used by the table

As a result of the above, it is expected that there will be a large increase in the number of sys\_dictionary and sys\_storage\_alias records for TPP hierarchies when compared with TPP. For example, the following image shows distinct sys\_dictionary records for a single field on the base and extended tables:

![](TPP2.pngx)

**Q: What happens when a new column is added to a table in a TPP hierarchy?**

As described above TPP hierarchies can use a concept known as 'glomming' (where multiple columns in distinct logical tables share a single physical column in the underlying RDBMS). If the column being added can be glommed no changes take place to physical tables - instead metadata is added to describe the 'glommed' columns - in this scenario addition of the column will be extremely fast.

If, however, the newly added column cannot be 'glommed' a new physical column will be added to one or more of the physical tables in the RDBMS (i.e. the base table or one of the existing storage partitions). In this case:

-   A new physical table will be created which is structurally identical to the existing table/partition plus the new column
-   All data is copied from the existing table/partition to the new table
-   The existing/new table are swapped

The above happens online with the CMDB remaining available for use throughout. Triggers are used to ensure that any changes to data in the original table are also performed against the new table whilst data is copied. Note, however, that as data must be copied from a large base table/storage partition (containing many columns/rows from multiple logical tables) copying may take a long time. As a result this operation will certainly be slower than adding a physical column to a table in a TPC hierarchy (i.e. prior to flattening). This is expected/by design as:

-   Adding columns to a table in a table hierarchy is not expected to be a frequent operation
-   Performance of adding columns has been sacrificed in preference to general end-user performance

**Q: As there is no longer a one-to-one mapping between physical and logical tables how is it possible for the platform to determine how many rows exist in a logical table?**

This functionality is provided via the use of the 'sys\_class\_path' attribute of each logical table/record in the TPP hierarchy. For example, let's consider that:

-   The platform needs to determine the number of rows in the cmdb\_ci\_computer table
-   This table has a sys\_class\_path of '/!!/!2/!('

Any records in the TPP hierarchy which have a class corresponding to cmdb\_ci\_computer or any class extending this table will have a sys\_class\_path starting with '/!!/!2/!(' - as a result, the platform can perform a query such as the following to get row count in cmdb\_ci\_computer:

mysql> select count(\*) from cmdb where sys\_class\_path like ‘/!!/!2/!(/%’;

+------+----------+

| Port | count(\*) |

+------+----------+

| 3407 | 852      |

+------+----------+

**Q: With TPP a single entity can have records in multiple tables (i.e. the base table and one or more storage partitions) - how is consistency between these records guaranteed?**

If details of a new entity need to be added to the hierarchy a new record for the entity will be inserted into all tables (i.e. the base table and all storage partitions). Likewise, if details of an existing entity need to be removed from the hierarchy then a record for the entity will be deleted from all tables (i.e. the base table and all storage partitions). If details of an existing entity need to be modified then records in each table (i.e. base table and all storage partitions) referencing fields that have been modified will be updated (note that in this scenario one or more tables that do not hold fields that have changed may not be touched).

To confirm that updates/deletes/inserts are consistent across all tables these operations are batched together and either all complete or, in the case of issues, are rolled back together:

09:09:56.38: Time: 0:00:00.049 for: demonightlyjakarta\_1\[glide.13\] EXECUTE BATCH OF 2 STATEMENTS

09:09:56.40: Batch statement: 1 of 2 for: demonightlyjakarta\_1\[glide.13\] INSERT INTO cmdb (\`skip\_sync\`, \`sys\_updated\_on\`, \`sys\_class\_name\`, \`sys\_id\`, \`sys\_updated\_by\`, \`checked\_in\`, \`sys\_class\_path\`, \`sys\_created\_on\`, \`sys\_domain\`, \`install\_date\`, \`sys\_created\_by\`, \`warranty\_expiration\`, \`assigned\_to\`, \`sys\_mod\_count\`, \`checked\_out\`, \`sys\_domain\_path\`, \`cost\_cc\`, \`order\_date\`, \`delivery\_date\`, \`install\_status\`, \`due\`, \`unverified\`, \`assigned\`, \`purchase\_date\`) VALUES(0, '2017-09-15 16:09:55', 'cmdb\_catie\_test', '086b9f9cdb154700d300fd131d96197f', 'catie.carmody@snc', NULL, '/$7', '2017-09-15 16:09:55', 'global', NULL, 'catie.carmody@snc', NULL, '62826bf03710200044e0bfc8bcbe5df1', 0, NULL, '/', 'USD', NULL, NULL, 1, NULL, 0, NULL, NULL) /\*...\*/

## Resolution

Not applicable
