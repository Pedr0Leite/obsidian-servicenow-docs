---
title: "Is \"Opt-In\" required to get software content from  Contents Data Services (CDS) Library? When do we start to get software content updates?"
aliases:
  - KB1650621
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1650621
kb_number: KB1650621
last_modified: 2026-05-17
---

## Is "Opt-In" required to get software content from Contents Data Services (CDS) Library? When do we start to get software content updates?

  

### Summary

**Is "Opt-In" required to download software content from the CDS Library?**

No, you do not need to opt-in to download software content from the CDS Library.  Software content download service is set up automatically after installing Software Asset Management Professional (com.snc.samp) plugin.

**When do we start to get software content updates?**

To balance the load on our CDS Servers, a download request initiated by your ServiceNow is randomized.  After the initial installation of Software Asset Management Professional plugin, it may take up to a week or more to get the full content.  After which contents downloads are initiated weekly.

The content download status can be checked from CDS Schedule Views(samp\_cds\_schedule\_view).  Note that the records in this table are updated by a weekly scheduled job so you may be getting content downloaded in your instance already by the time CDS Schedule Views records are created.
