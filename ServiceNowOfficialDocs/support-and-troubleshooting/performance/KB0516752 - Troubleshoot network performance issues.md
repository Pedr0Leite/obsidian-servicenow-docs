---
title: "Troubleshoot network performance issues"
aliases:
  - KB0516752
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0516752
kb_number: KB0516752
last_modified: 2026-04-29
---

## Issue

Troubleshoot network performance issues affecting your ServiceNow instance using this guide. It covers how to identify whether a problem originates in the ServiceNow network, the internet, or your own network, and how to gather data from both sides to isolate the cause.

## Resolution

Troubleshooting a network issue can be complex. Both you and ServiceNow must gather data from your respective networks at a level below the web browser. Until the gathered data is evaluated, there is no way to determine if the issue originated in:

-   The ServiceNow network — the issue may only exist in one data center
-   The internet
-   Your network
-   A combination of the three

**How do we know there is a network issue?**

When troubleshooting a possible network issue, you are attempting to find and isolate not only a complete reachability failure, but also other issues such as latency and packet loss that can affect the user experience.

The issue could be on the ServiceNow end, your end, or somewhere in the middle. Determining if and where the issue exists can be done using simple tools that work at a lower level than a web browser. Because traffic flows bidirectionally, data must be gathered from both your network and ServiceNow's vantage point.
