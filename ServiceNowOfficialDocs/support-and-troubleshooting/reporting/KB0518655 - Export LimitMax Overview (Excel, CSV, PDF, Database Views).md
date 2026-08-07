---
title: "Export Limit/Max Overview (Excel, CSV, PDF, Database Views)"
aliases:
  - KB0518655
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0518655
kb_number: KB0518655
last_modified: 2025-08-18
---

## Export Limit/Max Overview (Excel, CSV, PDF, Database Views)

  

### Issue

The following information details the platform's features for returning and exporting data, including properties to control record numbers.

### Release

### Resolution

### Database Views

The **_glide.db.max\_view\_records_** property is used for programs that are not using windowing. 

For example, if you have a business rule or script, the query will be limited by this property to prevent system overload.

```
var gr = new GlideRecord('incident_metric'); 
gr.query(); 
while (gr.next()) { 
 // do something 
} 
```

However, if the query is windowed to limit result set to only records between 0 and 50000, then the _**glide.db.max\_view\_records**_ property does not apply. 

### Exports

Exports are windowed by the property _**glide.ui.export.limit**_ which has a default value of 10000. To set these properties, navigate to **System Properties > Import Export**.

For more information, see [Export limits](https://www.servicenow.com/docs/csh?topicname=c_ExportLimits.html&version=latest "Export limits").

### Related Links

[Export limits](https://www.servicenow.com/docs/csh?topicname=c_ExportLimits.html&version=latest "Export limits")
