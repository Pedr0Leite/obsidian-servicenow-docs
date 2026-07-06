---
title: "Event Management integration with Azure platform as data source does not work with no event records created"
aliases:
  - KB0779838
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779838
kb_number: KB0779838
last_modified: 2024-04-07
---

## Event Management integration with Azure platform as data source does not work with no event records created

  

### Issue

When integrating Azure alerts as data source for Event Management, no event records are created.  Instructions as to how to enable this is described in [Integrate Azure platform as a data source](https://docs.servicenow.com/ "Integrate Azure platform as a data source")

### Release

Kingston, London, Madrid, New York

### Cause

The Azure Events Transform Script was designed to process Azure Classic Alert Schema and does not process the newer [Common alert schema definitions](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-common-schema-definitions "Common alert schema definitions")

### Resolution

The same document [Integrate Azure platform as a data source](https://docs.servicenow.com/ "Integrate Azure platform as a data source") advises to use a different URL in configuring Azure webhook:

**Receive events from other Azure formats** Event Management can receive events from other Azure formats, such as Azure Activity Alert (also known as audit log), and Azure log Alert (also known as unified log). Use this generic JSON target URL to collect events from other Azure formats:`https:/<<INSTANCE>>/api/global/em/inbound_event?source=genericJson`. **This generic URL can be used as-is, and requires an event rule to be configured to populate the correct fields in the alert.**

This uses a different Scripted REST API than the one described in [Integrate Azure platform as a data source](https://docs.servicenow.com/ "Integrate Azure platform as a data source") and requires authentication.

To disable authentication please do the following:

1.  Navigate to **System Web Services > Scripted Web Services > Scripted Rest APIs**.
2.  Locate and click the Inbound Event script.
3.  In the Resources area, click Inbound Event Post.
4.  In Security tab untick "**Requires authentication**" and save the record.
