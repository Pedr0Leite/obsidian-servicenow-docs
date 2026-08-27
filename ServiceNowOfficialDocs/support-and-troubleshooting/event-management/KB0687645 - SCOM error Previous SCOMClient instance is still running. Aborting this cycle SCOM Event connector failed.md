---
title: "SCOM error: \"Previous SCOMClient instance is still running. Aborting this cycle SCOM Event connector failed\"
aliases:
  - KB0687645
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687645
kb_number: KB0687645
last_modified: 2024-04-07
---

## Issue

Issue Summary  

* * *

This error occurs during the the SCOM connector execution:

"**Previous SCOMClient instance is still running. Aborting this cycle SCOM Event connector failed**"

Most Probable Cause  

* * *

It can happen in the following 3 scenarios:

1.  Two or more SCOM connectors have the same sys\_id and running on the same host
2.  When the MID is restarted, it might take several blocking requests from the ECC queue.
3.  There is a SCOMClient process running on this host (stuck)

  
Solution Proposed  

* * *

1.  There are two options for scenario 1:
    1.  Create connectors with different sys\_ids.
        1.  De-activate the original connector and check that it is not running (view the running field on the connector instance).
        2.  Insert and stay (give a different name), update parameters and assign MID server as the original one.
        3.  Activate the new one.
    2.  Run the non-prod connectors in a different host than the production ones. In case You want to keep the same sys\_id in both instances.
2.  In the second scenarios, please check that the MID server is up and running properly.
3.  For case  3, check in the Process Explorer for processes starting with "**SCOMClient**".
