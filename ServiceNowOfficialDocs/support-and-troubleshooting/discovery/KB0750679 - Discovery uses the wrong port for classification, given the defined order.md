---
title: "Discovery uses the wrong port for classification, given the defined order"
aliases:
  - KB0750679
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750679
kb_number: KB0750679
last_modified: 2026-01-15
---

## Discovery uses the wrong port for classification, given the defined order

  

### Issue

Discovery apparently triggers classification probes in the wrong order, and not per the port probes' classification priority.

### Symptoms

For example, despite SSH being open and with valid Credentials, SNMP is instead used for classification, and getting it wrong, causing a Linux Server to be classified as an IP Router.

### Release

Since Rome, when IP Service Affinity was enabled by default.

### Cause

A system property called glide.discovery.ip\_service\_affinity allows Discovery to remember the last port of the IP address that was discovered. 

When set to true, glide.discovery.ip\_service\_affinity = true, an entry for the ip address and ip service will be created on table ip\_service\_affinity. The next time this ip address is discovered, **the ip service specified under ip\_service\_affinity will be attempted first regardless of classification priority.**

This is designed to speed up discovery, by preventing inevitable failed logins, and unnecessary timeouts.

However, if e.g. a Linux Server failed to log in with SSH, but did have SNMP running too, which discovery could read, it would record that, and continue doing that on the next scans, even after fixing the SSH credential issue.

### Resolution

1.  Make sure the expected port is open, and does have valid credentials
2.  Delete the ip\_service\_affinity record for the ip address having the issue.
3.  Discover again
4.  Discovery will automatically recreate the ip\_service\_affinity record, but this time with the expected one for future scans.
