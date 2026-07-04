---
aliases:
  - "save records in update sets that normaly wouldnt go there"
area: "Scripts"
source: custom
tags:
  - update-sets
  - glide-update-manager2
  - background-scripts
  - scripts
---

# save records in update sets that normaly wouldnt go there

Uses `GlideUpdateManager2().saveRecord(gr)` to force a record that wouldn't normally be tracked (data-only tables, or records that already existed) into the current update set — either a single record by sys_id, or every record matching a query looped in bulk.

```javascript
//save records in update sets that normaly wouldn't go there

var gr = new GlideRecord("incident"); // be sure to query the table the record exists on
gr.get("hd6s52gdhs8d7fhrbwghstw6e52"); // add the record sys_id here
var update = new GlideUpdateManager2();
update.saveRecord(gr);



//Multiple records at the same time from the same table
var query = 'group=82036eba1bd18c1082a5a64c2e4bcbb6';
var table = 'sys_group_has_role';
var gr = new GlideRecord(table), count = 0;
gr.addEncodedQuery(query);
gr.query();


var update = new GlideUpdateManager2();


while(gr.next()){
update.saveRecord(gr);
count++
}

gs.print(count);
```

## Related

- [[How to Backup All Development Work in 1 Click]]
- [[Update Set Mover]]
