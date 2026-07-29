---
title: "Tracked Files Tab is not visible in Pattern Designer, after enabling system property glide.discovery.enable_file_tracking"
aliases:
  - KB0791864
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791864
kb_number: KB0791864
last_modified: 2024-04-08
---

## Tracked Files Tab is not visible in Pattern Designer, after enabling system property glide.discovery.enable\_file\_tracking

  

### Issue

**Tracked Files** Tab is hidden in Pattern Designer, after enabling system property glide.discovery.enable\_file\_tracking.

![](/sys_attachment.do?sys_id=2368d8c5dbc474d0b55f0b55ca961969)

### Cause

The "Tracked Files" Tab will only be displayed if the Pattern is already set to be triggered directly by a Classification.

For example:

-   "Windows OS - Servers" pattern displays it because it is triggered by the "Windows 2019 Server" Windows Classification.
-   "Apache on UNIX based OS" pattern displays it because it is triggered by the "Apache Server" Process Classification.
-   "F5 Load Balancer" pattern displays it because it is triggered by the "F5 BIG-IP Load Balancer" SNMP Classification, which is used due to the SNMP OID Classifications for F5.
-   "F5 BigIP GTM" pattern doesn't display it, because this isn't triggered as part of Horizontal Discovery. This is a Service Mapping pattern.

Only the discovery\_classifier\_probe records that reference the pattern are taken into account. If none exist, the tab is not shown.

### Resolution

You will need to save a new custom pattern, and configure a classification to trigger it, before you can re-load the pattern designer and see the tab.

If the Pattern is not designed for Horizontal Discovery, then you should not trigger it using a horizontal discovery Classification, and so you'll not expect to see the tab.
