---
aliases:
  - "searchForUserInAllRecord"
area: "Scripts"
source: custom
tags:
  - sys-dictionary
  - reference-field
  - glide-record
  - user-search
  - scripts
---

# searchForUserInAllRecord

Finds every table/field that has a reference field pointing to `sys_user` by querying `sys_dictionary` (`internal_type=reference^reference=sys_user`), builds a `{table: [fields...]}` map, then searches all of those tables for a given sys_id across all its user-reference fields (`OR`-joined encoded query) — useful for finding every record a user is attached to (assigned_to, owned_by, managed_by, etc.) before deactivating or merging a user, e.g. `alm_asset` ownership fields.

```javascript
var obj = {
  alm_asset: [
    "supported_by",
    "managed_by",
    "reserved_for",
    "assigned_to",
    "owned_by",
  ],
  alm_entitlement: ["assigned_to"],
  alm_stockroom: ["manager"],
  alm_transfer_order_line: ["transferred_for"],
};


//All tables with User reference field
var sysId = '';
var tt = new GlideRecord("sys_dictionary");
tt.addEncodedQuery("internal_type=reference^reference=sys_user");
// tt.setLimit(10);
// tt.orderBy('name');
tt.query();

var obj = {};

while (tt.next()) {
  if (Object.keys(obj).indexOf(tt.name + "") == -1) {
    obj[tt.name] = [];
  }
  if (obj[tt.name + ""].indexOf(tt.element + "") == -1) {
    obj[tt.name + ""].push(tt.element + "");
  }
}

// gs.print(JSON.stringify(obj))


var recordsFound = [];

Object.keys(obj).forEach(function (key) {
  console.log("key :", key);
  var queryToSearch = "";
  obj[key].forEach(function (x, i) {
    if (i == obj[key].length - 1) {
      queryToSearch += x + "=" + sysId;
    } else {
      queryToSearch += x + "=" + sysId + "^OR";
    }
  });

  var recordSearch = new GlideRecord(key);
  recordSearch.addEncodedQuery(queryToSearch);
  recordSearch.query();

  while (recordSearch.next()) {
    if (recordSearch.number != "" && recordSearch.number != undefined) {
      recordsFound.push(recordSearch.number);
    } else if (recordSearch.number == "" && recordSearch.serial_number != "") {
      recordsFound.push(recordSearch.serial_number);
    } else {
      recordsFound.push(recordSearch.sys_id);
    }
  }
});

var uniqueArray = recordsFound.filter(function (item, pos) {
  return recordsFound.indexOf(item) == pos;
});

//   gs.print(recordsFound);
//   gs.print(uniqueArray);
```

## Related

- [[Impersonate a user via script]]
