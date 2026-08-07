---
title: "Identification & Reconciliation Engine aborts creation or update of a record if payload is missing all the necessary attributes."
aliases:
  - KB0721442
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721442
kb_number: KB0721442
last_modified: 2025-04-07
---

## Identification & Reconciliation Engine aborts creation or update of a record if payload is missing all the necessary attributes.

  

### Issue

# Description

* * *

Identification & Reconciliation Engine stops creation or update of a record if payload is missing all the necessary attributes with a proper error message.

# Procedure

* * *

When passing the payload for insertion of a CI, IRE expects to have a certain type of relationships within the payload.

OOB Metadata Editor has Containment Rules, Hosting Rules, and Reference Rules. Hosting Rules define what classes of the configuration items are hosted on other classes of configuration items.

![](Metadata%20Editor.pngx) ![](sys_attachment.do?sys_id=d15968eedb02b450e515c22305961979)

As an Example, if you are trying to feed data for a Website(cmdb\_ci\_web\_site) table in which web server(cmdb\_ci\_web\_server) Hosted on a relationship is expected in the payload. If that is missing then IRE would throw a dependency error: INVALID\_INPUT\_DATA aborting the insertion. 

# Applicable Versions

* * *

All Versions

# Additional Information

* * *

The following documents provide good information in troubleshooting and understanding issues regarding the IRE:

-   [Identification and Reconciliation Components and Process](https://docs.servicenow.com/csh?topicname=c_CompsandProcessIDandReconcil.html&version=latest "Identification and Reconciliation Components and Process")
-   [Identification Engine Error Messages](https://docs.servicenow.com/csh?topicname=id-engine-error-messages.html&version=latest#d363848e812 "Identification Engine Error Messages")
