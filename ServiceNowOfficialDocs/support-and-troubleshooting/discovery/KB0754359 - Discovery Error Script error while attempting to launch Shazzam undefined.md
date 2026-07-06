---
title: "Discovery Error \"Script error while attempting to launch Shazzam undefined\""
aliases:
  - KB0754359
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754359
kb_number: KB0754359
last_modified: 2025-07-17
---

## Discovery Error "Script error while attempting to launch Shazzam undefined"

  

### Issue

Discovery fails before launching the shazzam probe with the below error :

"Script error while attempting to launch Shazzam undefined"

### Release

Any

### Cause

1) Few Causes are mentioned in [KB0687593](https://support.servicenow.com/kb_view.do?sysparm_article=KB0687593):

-   "Because this is a 'Network' Discovery, Discovery will query the 'discovery\_function\_def' table for an entry named 'SNMP only' to get the right port probes to launch for Shazzam.
-   If the out of the box entry's name was changed from 'SNMP only' to something else, Discovery is prevented from pulling up the right record and NULL value was returned.
-   This caused exceptions further down the execution when Discovery attempts to launch Shazzam probe(s)."

and [KB0749861](https://support.servicenow.com/kb_view.do?sysparm_article=KB0749861):

-   "Check "discovery\_function\_def" for null files on the table, repair "com.snc.discovery.ip\_based" plugin if table is empty"

2) The other probable cause is that the discovery functionalities in discovery behaviors have invalid/non-existing mid servers specified on the mid servers field.

### Resolution

Make sure valid mid servers are assigned to the mid server field in the discovery functionalities.
