---
title: "Troubleshooting Import - Missing data when importing from JDBC source via MID server"
aliases:
  - KB0538460
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538460
kb_number: KB0538460
last_modified: 2024-05-01
---

## Troubleshooting Import - Missing data when importing from JDBC source via MID server

  

### Issue

Troubleshooting Import – Missing data when importing from JDBC source via MID server

Problem

* * *

This issue is related to loading data from an external database (JDBC import) via the MID server. After the load, when you check the import set, the number of the records loaded is lower than what you expected.

Symptoms

* * *

-   Import does not complete
-   Import stopped in the middle
-   Import says complete, but not all data is present

Cause

* * *

Import set did not process all records from the ECC queue. Looking at the import log, you might be able to find the error that is causing the import process to stop processing data. One possiblity is that you failed to parse the data (XML format) message that causes the processor to stop processing data. The other possibility is that you run an import via a MID server that is part of a cluster.

Here are the possible cause possibilities:

1.  Data set is very large and sending the data in the payload versus the attachment causes a parsing failure.
2.  Netcool integration (if activated on the instance) might send events that our processor mistakenly identifies as part of the result set, then tries to parse and fails.
3.  MID server is part of a cluster, so some of the results are processed by different MID servers.

<table class="notetable" style="width: 800px;" align="left"><tbody><tr><td style="width: 12px;"><img title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td><strong>Note</strong>:&nbsp;Import process does not support import via a MID server that is part of a cluster.</td></tr></tbody></table>

Resolution 

* * *

To solve the issue with the large data set:

1.  If it is not already installed, install the Integration - JDBC plugin (ID: com.snc.integration.jdbc).
2.  Go to the data source that is currently failing and find the field, **Jdbcprobe result set rows**. (You may need to add the field to the form or list.)
3.  Set the value to 1000. (By default, the value is 200.)
4.  Start the import again.

To solve the issue with the Netcool integration:

1.  Shut down the Netcool integration or upgrade to CP5 and up, which includes the fix for this issue.

To solve the issue with the MID in cluster:

1.  Remove the MID server from the cluster or install another MID server that is dedicated for the import.
