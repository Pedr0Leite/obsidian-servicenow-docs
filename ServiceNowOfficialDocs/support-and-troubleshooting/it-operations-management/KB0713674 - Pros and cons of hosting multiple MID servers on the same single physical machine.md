---
title: "Pros and cons of hosting multiple MID servers on the same single physical machine"
aliases:
  - KB0713674
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713674
kb_number: KB0713674
last_modified: 2025-10-01
---

## Pros and cons of hosting multiple MID servers on the same single physical machine

  

### Issue

When we have a single physical server to host multiple MID servers, we always wonder what are the pros and cons with this approach.

### Release

All

### Resolution

**Pros**

-   Convenience, since all mid servers are located on the same host machine (easy access/easy to manage).
-   Will not need to set up too many ACL rules.

**Cons**

-   You will need a powerful host machine (host machine will need to have sufficient resources for each MID server).
-   Only available on the specific subnet where it resides on.
-   When the host machine is down, it will cause all MID servers to be down at once.

### Related Links

-   [Install multiple MID Servers on a single system](https://www.servicenow.com/docs/csh?topicname=t_InstallMultplMIDSvrOnASingleSys.html&version=latest "Install multiple MID Servers on a single system")
-   [MID Server system requirements](https://docs.servicenow.com/csh?topicname=r_MIDServerSystemRequirements.html&version=latest "MID Server system requirements")
-   [Best practices for MID Server setup and tuning \[blog\]](https://community.servicenow.com/community?id=community_blog&sys_id=9d1deea5dbd0dbc01dcaf3231f961939 "Best practices for MID Server setup and tuning [blog]")
