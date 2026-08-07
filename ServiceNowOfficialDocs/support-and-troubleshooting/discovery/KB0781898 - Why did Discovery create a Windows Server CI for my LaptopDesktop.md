---
title: "Why did Discovery create a Windows Server CI for my Laptop/Desktop?"
aliases:
  - KB0781898
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781898
kb_number: KB0781898
last_modified: 2025-04-08
---

## Why did Discovery create a Windows Server CI for my Laptop/Desktop?

  

### Issue

Discovery may scan a Desktop/Laptop computer running a non-server edition of Windows - e.g. Windows 10 - and wrongly create a Windows Server CI for it.

Or an existing Computer CI for a desktop/laptop may get re-classified as a Windows Server.

### Release

Any, where Discovery is installed, and Credential-less Discovery is enabled.

### Cause

Discovery classifies Windows devices based on the Operating System version.

-   Windows Professional (NT, 2000, Vista, XP, 7, 8, 10) -> Computer \[cmdb\_ci\_computer\]
-   Windows Server (2003, 2008, 2012, 2016) -> Windows Server \[cmdb\_ci\_win\_server\]

This is regardless of the hardware, form-factor, or function. e.g. a Laptop running Windows Server is a Server. A VM running Windows 10 is a Computer.

For the above to work, Discovery must have a Credential that is able to log into the host to find out the OS version/edition.

However, **when there is no valid credential, Discovery may fall back to using Credential-less Discovery pattern**, and that makes guesses based on NMAP scan results.

**It may not have enough information to make an accurate guess, and in that situation defaults to Windows Server.**

### Resolution

Please configure the device to allow access by the Discovery Credentials entered in the instance, before scanning the device for the first time.
