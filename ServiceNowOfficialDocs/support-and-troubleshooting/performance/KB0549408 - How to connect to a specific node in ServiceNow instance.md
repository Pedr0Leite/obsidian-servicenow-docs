---
title: "How to connect to a specific node in ServiceNow instance"
aliases:
  - KB0549408
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549408
kb_number: KB0549408
last_modified: 2025-05-22
---

## Issue

This article provides information on how to connect to a specific node of a ServiceNow instance. 

## Resolution

There are times when you need to log in to a specific node to cancel a job running on that specific node. You may also need to cancel background jobs that are running longer than anticipated. These jobs can run on a node that you are not logged in to, and you are not in control of which node to connect to during the login process. Your request lands on a randomly selected application node if you have more than two nodes in your instance. The article provides steps for how to reach the target node.

#### **What is F5/load balancer?**

A load balancer is a device that acts as a reverse proxy and distributes network or application traffic across a number of servers/nodes. Load balancers are used to increase capacity (concurrent users) and reliability of applications. They improve the overall performance of applications by decreasing the burden on servers associated with managing and maintaining application and network sessions, as well as by performing application-specific tasks. It is through this load balancer that you are randomly logged into a node of your instance.

#### **Steps to connect to target node**

Follow the steps below to connect to the target node:

**Note: The steps below work only for instances that do not have customizations on their logouts.**

1.  Install the browser plugin **Edit this Cookie** for Chrome or Firefox.
2.  Find the instance node sys\_id from your System Diagnostics page.
3.  Log in to the instance like normal. You will be taken into the instance through any of the primary nodes by the F5.
4.  To manipulate this, edit the cookie icon that appears on the right-hand corner of your browser.
    1.  Edit the glide\_user\_route cookie to match the sys\_id of the node for desired login.
    2.  Delete the **BigIPServerPool** cookie.
5.  Log out of the node and log in again. You are now redirected by the F5 to the desired node.

**References:** For more information on Big – IP persistence cookie encoding, see: [https://support.f5.com/kb/en-us/solutions/public/6000/900/sol6917.html](https://support.f5.com/kb/en-us/solutions/public/6000/900/sol6917.html)
