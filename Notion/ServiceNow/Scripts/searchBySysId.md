---
aliases:
  - "searchBySysId"
area: "Scripts"
source: custom
tags:
  - sys-metadata
  - glide-record
  - background-scripts
  - troubleshooting
  - scripts
---

# searchBySysId

Shorter version of [[Search the system with a sys_id]] — queries `sys_metadata` by sys_id and prints the record's `name` and `sys_class_name` to identify what table it belongs to.

```javascript
var searchSys_id = "";
var y = new GlideRecord('sys_metadata');
y.addQuery('sys_id', searchSys_id);
y.addActiveQuery();
y.query();
while (y.next()) {
  if (y.sys_id == searchSys_id) {
    gs.info(" ID: " + y.sys_id + " Name: " + y.name + " Class: " + y.sys_class_name);
    gs.info(y.getRowCount());
  }
}
```

## Related

- [[Search the system with a sys_id]]
