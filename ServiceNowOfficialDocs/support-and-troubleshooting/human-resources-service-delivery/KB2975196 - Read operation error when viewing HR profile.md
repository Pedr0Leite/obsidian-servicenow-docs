---
title: "Read operation error when viewing HR profile "
aliases:
  - KB2975196
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2975196
kb_number: KB2975196
last_modified: 2026-04-24
---

## Read operation error when viewing HR profile

  

### Issue

When using HR profile, a read operation error occurs with the message: 'Read operation on table 'sn\_hr\_core\_profile' from scope 'Global' was denied because the source could not be found. Please contact the application admin.' The system log shows a corresponding error: 'Source descriptor is empty while recording access for table sn\_hr\_core\_profile: no thrown error'.  
  

### Release

Before Zurich

### Cause

After reviewing the syslog, we can find the error was triggered by a transaction from the Scripted REST API 'AI Agent' (/api/now/ai\_agent/modified\_fields). The root cause was an issue with the RCA source identifier: the source of the read operation on the 'sn\_hr\_core\_profile' table could not be found, resulting in an access denial error. The 'modified\_fields' REST API resource (sys\_ws\_operation) was not a known source type.   
  

### Resolution

-   Upgrade the instance to the Zurich release, as the issue was resolved in this release by adding 'Scripted REST Resource (sys\_ws\_operation)' to the 'Source Type' field of the RCA records.
-   Alternatively, offload the API logic to a Script Include, as a script include is a known source type in RCA and will be properly traced when accessing the HR profile table. Refer to the KB article [KB0963922](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963922) for detailed instructions.

### Related Links

[KB0963922](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963922)
