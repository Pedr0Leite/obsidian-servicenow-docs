---
title: "Instance URL is not accessible from MID Server host"
aliases:
  - KB0747617
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747617
kb_number: KB0747617
last_modified: 2024-04-07
---

## Issue

An instance URL (instancename.service-now.com) may not be accessible from the MID Server host, even though the specific instance IP is configured in the allow-list:

![](sys_attachment.do?sys_id=bfdae8e6db42b450e515c22305961956)

  

## Resolution

Generally, when allowing or denying in a list, the DNS name should be taken into consideration rather than the IP address.

Because when a specific node gets reassigned to a new node for an instance, the IP address will get changed eventually, but not the DNS name which will be unique, unless and until there is a DNS reconfiguration change.

At this stage when the new node gets assigned to the specific instance, the IP address will get reassigned in turn, which will cause access related issues. So the allow-list has to be configured against the DNS name along with the port 443 and not against the IP address.
