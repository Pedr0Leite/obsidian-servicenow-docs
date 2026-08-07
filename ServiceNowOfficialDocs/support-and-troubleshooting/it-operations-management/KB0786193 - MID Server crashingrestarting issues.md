---
title: "MID Server crashing/restarting issues"
aliases:
  - KB0786193
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786193
kb_number: KB0786193
last_modified: 2024-04-07
---

## Issue

We are seeing some sporadic mid server issues where mid servers are randomly restarting and sometimes crashing. There seems to be no rhyme or reason to it, however there is one thing that is fairly obvious that will reveal what the issue may be. If you look at the wrapper.log, there are generally only a few entries in it, however we are seeing hundreds of entries in that file with this issue. You may not that the JVM Attempts to restart the service.

## Resolution

Comment out the variable wrapper.java.command in the file agent/conf/wrapper-override.conf and make sure that the one in agent/conf/wrapper.conf is pointing to a bundled JRE in the mid server agent folder, and then restart the service.
