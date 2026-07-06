---
title: "How to resolve \"Duplicate entry for key 'PRIMARY'\" error when inserting a virtual Computer or Server CI in the CMDB"
aliases:
  - KB0748828
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748828
kb_number: KB0748828
last_modified: 2026-04-07
---

## How to resolve "Duplicate entry for key 'PRIMARY'" error when inserting a virtual Computer or Server CI in the CMDB

  

### Issue

Resolve a SQL-level "Duplicate entry for key 'PRIMARY'" error that occurs when inserting a Computer or Server CI in the CMDB, causing the insert to fail and related code to behave unexpectedly.

When inserting a Computer or Server CI in the CMDB — whether manually, through a discovery tool, or via an import — the following SQL error may appear, indicating the CI has already been inserted:

```
FAILED TRYING TO EXECUTE ON CONNECTION nn: INSERT INTO cmdb (`a_str_5`, `a_int_8`, `skip_sync`, `operational_status....
java.sql.BatchUpdateException: Duplicate entry '7caaf9c31b9dff846825a64fad4bcb6a' for key 'PRIMARY' 
: java.sql.SQLException: java.sql.BatchUpdateException: Duplicate entry '7caaf9c31b9dff846825a64fad4bcb6a' for key 'PRIMARY': com.glide.db.StatementBatcher.getSQLException(StatementBatcher.java:469)
```

### Release

Instances with Discovery or Service Mapping installed

### Cause

A custom business rule running on insert of a CI relationship record makes an `.update()` call to the parent CI before that CI exists in the database. This causes the platform to prematurely insert the parent CI, after which the actual insert transaction fails with a duplicate key error.

The following sequence explains how this occurs when the CI being inserted is a Computer CI `[cmdb_ci_computer]`, Server, or any class that extends Computer:

1.  The base system Virtual Computer Check business rule runs before the Computer CI is inserted, because the `IsVirtual` flag must be set before insert.
2.  If the rule finds a VM instance record, it identifies the CI as virtual and inserts an "instantiates" relationship record between the VM and the instance. A Relationship `[cmdb_rel_ci]` record is inserted.
3.  All insert business rules for the Relationship `[cmdb_rel_ci]` record run as part of this insert.
4.  If a custom business rule in step 3 calls `.update()` on the parent of the relationship, the platform inserts the parent Computer CI into the database prematurely — because calling `.update()` on a record that does not yet exist causes the platform to insert it.
5.  The remaining Relationship insert business rules complete.
6.  The remaining before-insert Computer CI business rules complete.
7.  The platform attempts to insert the Computer CI as part of the original transaction, but fails with a duplicate key error because the CI was already inserted in step 4.

### Resolution

The custom business rule must be redesigned to avoid calling `.update()` on a CI that has not yet been inserted. The following principles apply:

-   Do not assume that both parent and child CIs exist when a Relationship `[cmdb_rel_ci]` record is inserted. The base system Virtual Computer Check business rule is one example of code that can insert a relationship before the parent CI exists. Other platform processes may do the same.
-   Calling `.update()` on a record that does not exist causes the platform to insert it prematurely. Any subsequent code that expects to perform the original insert will fail with a duplicate key error.
-   Review the custom business rule logic and ensure it does not call `.update()` on the parent CI during a Relationship record insert. Consider using a deferred operation or checking whether the CI already exists before calling `.update()`.

### Related Links

The behavior described in this article is consistent with how `GlideRecord` works by design. When `.get()` is called for a record that does not exist, the platform initializes a new `GlideRecord` in memory. The same applies when dot-walking reference fields in scripts to retrieve a referenced record object. Any subsequent call to `.update()` on that in-memory record causes the platform to insert it.

This behavior is documented in the `GlideRecord` Server API reference under `.update()`:

> "Updates the GlideRecord with any changes that have been made. If the record does not exist, it is inserted."

For more information, see the [GlideRecord documentation](https://developer.servicenow.com/app.do#!/api_doc?v=newyork&id=r_ScopedGlideRecordUpdate_String "GlideRecord documentation") in the ServiceNow Developer documentation.
