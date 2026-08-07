---
title: "How to identify network latency indications leading to slow end-user performance experiences"
aliases:
  - KB0815240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815240
kb_number: KB0815240
last_modified: 2026-04-29
---

## How to identify network latency indications leading to slow end-user performance experiences

  

### Overview

This content can be referenced to identify trends indicating slow performance due to network overhead/latency

This content applies to all releases

### \[Subject\]

Slow performance is experienced by end-users, and you want to see if network overhead (or client side overhead) could be the cause.   This article will show you how to identify trends which may validate the impact of network or client side overhead leading to that slow performance experience.

### Example

You may have users from a specific location reporting slowness while users in other locations are not experiencing the same performance slowness.

### Additional Information

To identify what is slow:

\-- navigate to System Logs >>  Transactions (All user)

\-- Apply a filter to the list to show a time covering when performance slowness is known to have occurred

\-- Add all columns ending with "time" to your list of visible columns

\-- Sort (z-a) on "Client Response Time", as this is will show you the highest values for the end-user experience in terms of time taken for the transaction

    -- Compare the "Response Time" (time spent on ServiceNow's side of the platform to execute the transaction) with the "Client Response Time" (full time of the transaction from the end-user's experience.    

    -- When you see large differences between the "Client Response Time" and "Response Time", the difference is somewhere between the public interface to SercieNow and the end-user desktop (network, filrewall/proxy, desktop, browser, etc..), such as can be seen in this example:

![](sys_attachment.do?sys_id=8519f7a4476a8650c4e1a325126d430c)

You can also look for trends specifically for the network overhead by sorting on "Client Network Time" (z-a)![](sys_attachment.do?sys_id=8d19f7a4476a8650c4e1a325126d4307)

If you have output consistent with these trends it is very likely there is a network layer event impacting performance.   In this event please refer to the following article for network troubleshooting:

[KB0521688](/kb_view.do?sysparm_article=KB0521688) - Troubleshooting Network Performance\_Data Collection
