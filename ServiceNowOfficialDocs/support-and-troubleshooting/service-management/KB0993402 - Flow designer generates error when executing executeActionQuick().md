---
title: "Flow designer generates error when executing executeActionQuick()"
aliases:
  - KB0993402
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993402
kb_number: KB0993402
last_modified: 2025-11-07
---

## Flow designer generates error when executing executeActionQuick()

  

### Summary

Flow designer generates an error when wanting to execute "executeActionQuick()":

Flow Designer: Persisting an unterminated plan is not supported for plan 

This will be reported if the action to execute requires MID server.

Quick API does not support actions or flows that go to the MID. (Transferring execution to MID and back requires a sys\_flow\_context record and Quick API does not write a sys\_flow\_context record)

### Related Links

[Flow API methods - Scoped and Global](https://www.servicenow.com/docs/csh?topicname=ScriptableFlowAPI.html&version=latest)
