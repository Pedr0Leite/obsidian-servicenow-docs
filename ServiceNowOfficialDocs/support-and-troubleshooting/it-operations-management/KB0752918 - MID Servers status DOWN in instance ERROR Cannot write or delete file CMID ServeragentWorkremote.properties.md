---
title: "MID Servers status DOWN in instance :* ERROR * Cannot write or delete file C:\<MID Server>\agent\Work\remote.properties"
aliases:
  - KB0752918
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752918
kb_number: KB0752918
last_modified: 2024-04-07
---

## MID Servers status DOWN in instance :\* ERROR \* Cannot write or delete file C:\\\\agent\\Work\\remote.properties

  

### Issue

# Symptoms

MID Servers status is DOWN in instance - Agent log \* ERROR \* Cannot write or delete file C:\\<MID Server>\\agent\\Work\\remote.properties

![](sys_attachment.do?sys_id=fa2d6c62db82b450e515c223059619e5)

# Release

Any Release

# Cause

-   Upon reviewing MID Server agent folder, C:\\<MID Server>\\agent\\Work\\remote.properties, found file "remote.properties" is set to Read-only.
-   Hence, MID server status is showing DOWN in instance.

![](sys_attachment.do?sys_id=832d6c62db82b450e515c223059619ec)

# Resolution

-   Locate the remote.properties file under the work directory of the Mid Server agent folder. Uncheck Read-only Attribute and click Apply.
-   Restart MID Server service in Host Machine.

# Result

-   This change brings the MID Server Status to UP in instance successfully.

![](sys_attachment.do?sys_id=8b2dac62db82b450e515c2230596196d)
