---
aliases:
  - "Loop a list of users over another table"
area: "Scripts"
source: custom
tags:
  - glide-record
  - background-scripts
  - sys-user-has-role
  - scripting
  - scripts
---

# Loop a list of users over another table

Background script pattern: query one table (`sys_user`, filtered by an encoded query) and for each matching record, query a second related table (`sys_user_has_role`) and insert a new record there carrying data pulled from the first loop. General "loop A, use it to seed B" template.

```javascript
//Loop a list of users over another table and create a new record on the second table with the information of the firs table

var usr = new GlideRecord('sys_user');
usr.addEncodedQuery('sourceISNOTEMPTY^sys_domain=');
usr.query();

var count = 0;

while(usr.next()) {

    var gr = new GlideRecord('sys_user_has_role');
    gr.addQuery('user', usr.sys_id);
    gr.addEncodedQuery('role!=^role!=^user.sys_domain=');
    gr.query();

      if(gr.next()){
        gr.initialize();
        gr.user = usr.sys_id;
        gr.setValue('role','');// snc_read_only
        gr.state = "active";
        gr.setWorkflow(false);
        gr.autoSysFields(false);
        gr.insert();
        count++;
        gs.print(usr.sys_id);
    }

}

// gs.log(gr.user);
// gs.log(usr.name);
gs.log(count);
```

## Related

- [[Random Scripts]]
