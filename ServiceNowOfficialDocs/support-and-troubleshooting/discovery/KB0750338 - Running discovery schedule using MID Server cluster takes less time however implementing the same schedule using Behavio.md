---
title: "Running discovery schedule using MID Server cluster takes less time however implementing the same schedule using Behaviors is taking more time there by affecting performance"
aliases:
  - KB0750338
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750338
kb_number: KB0750338
last_modified: 2024-04-07
---

## Issue

# Overview

Running a discovery schedule using MID Server cluster takes less time however implementing the same schedule using Behaviors is taking more time there by affecting performance.

# Context

1) If you observe the ECC queue records for Shazzam probe in the Cluster schedule, you will observe that the Shazzam is load balanced through multiple mid servers in that cluster.

2) However, If you observe the ECC queue records for Shazzam probe in the behavior schedule, you will observe that the Shazzam is picked up by only a single mid server. Rest of the ECC queue records are load balanced as expected.

3) Shazzam probe being limited to one mid server is causing the duration to increase when using behaviors compared to using clusters. 

4) The reason is that when using behaviors is because Shazzam batching does not work. This is as per design
