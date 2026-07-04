---
aliases:
  - "Search the system with a sys_id"
area: "Scripts"
source: custom
tags:
  - sys-metadata
  - glide-record
  - background-scripts
  - troubleshooting
  - scripts
---

# Search the system with a sys_id

Queries `sys_metadata` (the base table every record extends) by a given sys_id to identify which table/class a mystery sys_id belongs to, logging the `sys_class_name`. Near-duplicate of [[searchBySysId]] — same technique, slightly different logging.

```javascript
// idea - Search for sysID
var sysId = "";   //Update your Sys ID

      var gr = new GlideRecord('sys_metadata');
      gr.addQuery('sys_id',sysId );
      gr.addActiveQuery();
      gr.query();
      gs.log("Number of Records matched: "+ gr.getRowCount());
      while(gr.next())
      {
              if(gr.sys_id == sysId )
              {

                      gs.log(" SYS ID: " + gr.sys_id + " Class Name: " + gr.sys_class_name);

              }

      }
```

## Related

- [[searchBySysId]]
