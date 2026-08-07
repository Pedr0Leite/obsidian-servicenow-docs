---
title: "Red Hat is listed as the Publisher for OpenJDK instead of Oracle"
aliases:
  - KB0864691
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864691
kb_number: KB0864691
last_modified: 2025-01-02
---

## Red Hat is listed as the Publisher for OpenJDK instead of Oracle

  

### Summary

**Description**:

You may find in some Software Models where OpenJDK's publisher is listed as "Red Hat" and not "Oracle" as expected, seemingly to be incorrect.

  

**Looking at the Software Product table \[samp\_sw\_product\]:**  
Here we can find that there are software product records where both"Red Hat" or "Oracle" are listed as the Publisher using the below query.

   
publisher.name=Red Hat^ORpublisher.name=Oracle^prod\_nameLIKEopenjdk

  

![](sys_attachment.do?sys_id=d2b87841db4878d0fec4fb243996195c)  
  

  

**Red Hat is also listed as a Publisher of OpenJDK for some these records because:**

Red Hat publishes their own OpenJDK alternative to OracleJDK. Thus the records have the correct Publisher listed.

[https://developers.redhat.com/oraclejdkalternative](https://developers.redhat.com/oraclejdkalternative)

![](sys_attachment.do?sys_id=5ab87841db4878d0fec4fb243996195d)
