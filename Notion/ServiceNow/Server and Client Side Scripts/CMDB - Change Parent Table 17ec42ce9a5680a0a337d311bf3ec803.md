---
aliases:
  - "CMDB - Change Parent Table"
tags:
  - cmdb
  - script-include
  - table-parent-change
  - scripting
---

# CMDB - Change Parent Table

If you're a parent, have you ever wished you could hand your kid(s) off to someone else? Or...when you were a kid, did you ever wish you had a different set of (cooler) parents? The kid at right just found out he's getting some really cool parents, and is quite happy about that!

But I can't help you with those problems. I can, however, help you with a somewhat similar problem: a table in Service-now that has the wrong parent (i.e., extends the wrong table). There are lots of ways this can happen. For example, perhaps you created a table for your company's Internet-aware soda machines, and only after you built the table did you realize that it really should extend Configuration Item (cmdb_ci) — after all, a soda machine is just as much a part of your CMDB as that Oracle server. They probably contribute more to corporate productivity! Or perhaps you created a new table for those soda machines, and extended Configuration Item (cmdb_ci) — but later decided that you really should have extended Hardware (cmdb_ci_hardware). After all, those soda machines are just as much a piece of hardware as that Dell 4U server. In either case, how do you get yourself out of this pickle?

Why, with **TableParentChange**, of course!

Let's take one of the preceding examples. Suppose we have a table cmdb_ci_soda_machine which currently extends cmdb_ci. I'll write that as *cmdb_ci â†’ cmdb_ci_soda_machine*. Now we want to change it to extend cmdb_ci_hardware, so we'd end up with *cmdb_ci â†’ cmdb_ci_hardware â†’ cmdb_ci_soda_machine*. Here's the code that will do the trick:

```

// some setup...
var table = 'cmdb_ci_soda_machine';   // the table whose parent we want to change...
var old_parent = 'cmdb_ci';           // the current parent of cmdb_ci_soda_machine...
var new_parent = 'cmdb_ci_hardware';  // the parent we WANT cmdb_ci_soda_machine to have...

// now we actually do the work of changing parents...
var changer = new Packages.com.glide.db.table.TableParentChange(table);
changer.change(old_parent, new_parent);  // this actually does the work...
```

You can run this script from System Definition â†’ Scripts - Background (if you're an admin), or you can include it in a UI Action, Business Rule, etc. This does all the work of migrating existing entries in the table. On a table with a great many entries, this can take a while — but eventually it will be finished.

One word of caution: this operation does

*not*

take into account possible duplicate fields you might have. You need to resolve any such issues

*before*

you run TableParentChange. For example, suppose that cmdb_ci_hardware had a field named 'button_count', and cmdb_ci_soda_machine also had a 'button_count' field before you run TableParentChange. You'll need to move the data in cmdb_ci_soda_machine from 'button_count' to some new field with a different name, then delete the 'button_count' field from cmdb_ci_soda_machine

*before*

running TableParentChange.

======================================

You can also try

***var gr = new SNC.CMDBUtil.reParentTable('cmdb_ci_lb', 'cmdb_ci_server', 'cmdb_ci_netgear');***

***new SNC.CMDBUtil.reParentTable('<TABLE>', '<OLD PARENT>', '<NEW PARENT>')***

[https://developer.servicenow.com/dev.do#!/reference/api/quebec/server_legacy/c_CMDBUtilAPI#r_CMDBU-reParentTable_S_S_S](https://developer.servicenow.com/dev.do#!/reference/api/quebec/server_legacy/c_CMDBUtilAPI#r_CMDBU-reParentTable_S_S_S)

## Related

- [[Server and Client Side Scripts]]
- [[CMDB]]
- [[SCCM]]