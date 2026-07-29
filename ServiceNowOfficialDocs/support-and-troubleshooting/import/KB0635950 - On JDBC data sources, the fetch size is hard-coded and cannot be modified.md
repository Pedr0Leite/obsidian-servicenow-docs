---
title: "On JDBC data sources, the fetch size is hard-coded and cannot be modified"
aliases:
  - KB0635950
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635950
kb_number: KB0635950
last_modified: 2024-04-07
---

## On JDBC data sources, the fetch size is hard-coded and cannot be modified

  

### Issue

On JDBC data sources, the fetch size is hard-coded and cannot be modified  

Problem

* * *

Attempts are sometimes made to optimize the JDBC data source fetch size to meet different conditions.  

Cause

* * *

On JDBC data sources, the fetch size is hard-coded on the JDBC probe and cannot be modified.

  
Resolution

* * *

Our version of this feature is the probe parameter **jdbcprobe\_result\_set\_rows,** which modifies the MID server payload instead.

Probes interact with the MID Server via the ECC Queue, and therefore the response of a JDBC probe returns as an XML payload in an "input" ECC Queue record. By default, each response payload will contain up to 200 returned rows. This value can be modified by setting the probe parameter **jdbcprobe\_result\_set\_rows** to the desired number.   
    
![jdbcprobe\_result\_set\_rows](sys_attachment.do?sys_id=35c96c62db42b450e515c223059619a0 "jdbcprobe_result_set_rows")

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: By default, each JDBC response payload will contain up to 200 returned rows.</td></tr></tbody></table>
