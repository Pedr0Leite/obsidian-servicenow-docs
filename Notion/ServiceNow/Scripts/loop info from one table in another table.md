---
aliases:
  - "loop info from one table in another table"
area: "Scripts"
source: custom
tags:
  - glide-record
  - attachments
  - knowledge-base
  - background-scripts
  - scripts
---

# loop info from one table in another table

Background script that loops `kb_knowledge` articles flagged as having attachments, then checks `sys_attachment` for each to confirm whether an attachment actually exists — counting real-attachment vs. flagged-but-missing articles. Useful audit for cleaning up stale "has attachment" flags on knowledge articles.

```javascript
var gr = new GlideRecord('kb_knowledge');
gr.addEncodedQuery('display_attachments=true');
gr.query();

var count,test = 0;

while(gr.next()){
var at = new GlideRecord('sys_attachment');
at.addQuery('table_sys_id', gr.sys_id);
at.query();
if(at.next()){
if(at.hasAttachments()){
count++
}else{
gs.print(at.sys_id);
test++
}
}

}

gs.print('amount of records with attach: ' + count);
gs.print('amount of records without attach: ' + test);
```

## Related

- [[Knowledge Base Articles]]
- [[Confidential Attachments]]
