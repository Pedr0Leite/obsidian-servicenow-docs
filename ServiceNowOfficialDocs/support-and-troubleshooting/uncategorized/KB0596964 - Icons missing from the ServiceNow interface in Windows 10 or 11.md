---
title: "Icons missing from the ServiceNow interface in Windows 10 or 11"
aliases:
  - KB0596964
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596964
kb_number: KB0596964
last_modified: 2024-11-28
---

## Icons missing from the ServiceNow interface in Windows 10 or 11

  

### Issue

Icons (Connect sidebar, Global text search, Help & Gear icons) are not appearing when using Windows 10 or 11.

### Release

UI 16 on Internet Explorer on Windows 10-11.

### Cause

If these icons are not appearing when using Windows 10, you might have [Untrusted Font Blocking](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/block-untrusted-fonts-in-enterprise "Untrusted Font Blocking") enabled.

![](/sys_attachment.do?sys_id=389ed8b61b2ff4509f20ece7624bcb42)

Untrusted Font Blocking is a new feature of Windows 10 that can be deployed throughout organizations using a group policy. A [TechNet article](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/block-untrusted-fonts-in-enterprise "The TechNet article") describes a scenario that can occur when visiting certain websites:

_Using Internet Explorer to look at websites that use embedded fonts. In this situation, the feature blocks the embedded font, causing the website to use a default font. However, not all fonts have all of the characters, so the website might render differently._

A simple way to test whether the Untrusted Font Blocking setting is causing your icon display issues is as follows:

-   Look for the **_@font-face encountered unknown error_** message in your browser console.
-   Try visiting the [Font Awesome Examples](http://fontawesome.io/examples/ "Font Awesome Examples") page and see if the icons appear on it.
-   Try visiting your ServiceNow instance using a different operating system, such as Windows 7 or MacOS. Although this group policy can be set on all Windows machines, its effects are seen only in Windows 10 or later releases. If the icons appear in Windows 7, for example, you probably have this setting enabled.

### Related Links

ServiceNow is not currently compatible with the Enabled setting of the Untrusted Font Blocking feature, ensure that this feature is set either to Disabled or to Not Configured. [PRB724940/KB0679934](https://support.servicenow.com/kb_view.do?sysparm_article=KB0679934 "PRB724940/KB0679934") has been raised to address the inability to install the web fonts locally. This is a known limitation in all current releases, and no plans are in place yet to introduce this product enhancement in a future release.
