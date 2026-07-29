---
title: "On one MID host, there are two MID servers with same mid server name, but connecting to different instances. If auto-upgrade started for both MID at same time, one is upgraded, and the other one is left stopped"
aliases:
  - KB0784389
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784389
kb_number: KB0784389
last_modified: 2024-04-07
---

## On one MID host, there are two MID servers with same mid server name, but connecting to different instances. If auto-upgrade started for both MID at same time, one is upgraded, and the other one is left stopped

  

### Issue

On one MID server host, there are two MID servers with same mid server name, but connecting to different instances.

If auto-upgrade started for both MID at same time, then one is upgraded, and the other one is left stopped & not upgraded.

### Cause

During MID server auto-upgrade, what normally happens is that after the upgrade files are downloaded, the MID server wrapper installs a different windows service called " ServiceNow Platform Distribution Upgrade (mid server name)".

Then the MID server wrapper stops itself, and the new service will install/upgrade the wrapper, then restart it.

The cause is, the auto-upgrade process always tries to install a windows service that partially uses MID server's name.

This means, when there are two MID servers having same name, and being upgraded at same time, the two MID servers are trying to install two new window services with same name.

Since windows only allows one service with that name, it will only accept the first request.

Thus the MID server sends the first request will be upgraded.

The other MID server will be have below warning in agent log, and it will be stopped and stay on old version:

11/02/19 19:07:59 (301) Gobbling stderr: cmd.exe /C bin\\glide-dist-upgrade.bat start Gobbled: ERROR | wrapperm | 2019/11/02 19:07:59 | The ServiceNow Platform Distribution Upgrade (midserver-lab) service is already started with status: START\_PENDING

### Resolution

In Orlando release the upgrade process has been redesigned, and we will no longer face the issue.

You may use either of below workaround options for pre-Orlando release:

-   \-Make sure MID servers installed on same host have different names (MID server names are configured in the value of the "name" tag in config.xml file)
-   \-Upgrade the MID servers on separate days. This can be done by scheduling instance upgrade for the different instances on separate days, or pin the MID server on a particular version then remove the version file laters.
