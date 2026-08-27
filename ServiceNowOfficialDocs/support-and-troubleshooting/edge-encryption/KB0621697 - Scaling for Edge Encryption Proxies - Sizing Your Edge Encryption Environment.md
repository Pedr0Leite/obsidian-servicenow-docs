---
title: "Scaling for Edge Encryption Proxies - Sizing Your Edge Encryption Environment"
aliases:
  - KB0621697
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621697
kb_number: KB0621697
last_modified: 2024-04-07
---

## Scaling for Edge Encryption Proxies - Sizing Your Edge Encryption Environment

  

### Issue

Scaling for Edge Encryption Proxies – Sizing Your Edge Encryption Environment

  
  

Choosing the number of proxy servers for your environment is an important task. Because every environment is different, the advice in this article is stated as a guideline for choosing the configuration of your Edge Proxy environment.

# Redundancy

* * *

Redundancy is important in case of hardware failure. Proxy Servers should be located behind a Load Balancer to provide a functional path for all users should a Proxy Server be unreachable due to hardware issues. For this reason, at least two Proxy Servers should be available at all times.

# Sizing

* * *

Sizing refers to the number of Proxy Servers required to avoid additional latency that the encryption of data produces. As with any added component in a system, running through the Proxy Server itself will provide additional latency. The idea is to minimize the amount of latency. The environment in which the Proxy Servers run will affect your individual configuration. For example, if regular Mass Encryptions are run, adding additional Proxy Servers to handle that load might be a good idea, or run the Mass Encryptions when the user load is light. The hardware on which the Proxy Server runs will also influence the performance of the Proxy Server. Proxy Servers running on hardware with faster CPUs, more CPUs, and more RAM will have higher throughput than slower limited systems. The sizing information in this section assumes that the Proxy Server is running on at least the minimum set of hardware.

As a standard rule-of-thumb, try to have one Proxy Server for every two App Nodes on the instance. For redundancy's sake, there should be a minimum of two Proxy Servers behind a Load Balancer. Beyond that rule-of-thumb, you can make a more accurate calculation by using the following formula:

_Proxies = Max(Max Users / 500, 2)_

Breaking this down, once you approach 500 users / Proxy Server, latencies are likely to start increasing. It is best to determine ahead of time when you will approach a threshold of an additional 500 users and to place another Proxy Server in the Load Balancer pool.

# CPU Utilization

* * *

The CPU will spike while encrypting data, which is normal behavior. Data encryption and tokenization are CPU-intensive operations that will spike the CPU. When the CPU utilization is over 80% for several minutes at a time, it likely means that the Proxy Server has too much work to do (for example a Mass Encryption or some very complex work). When this happens, latency will increase for the period that the CPU utilization is high. If these persist, adding another proxy server might help decrease the latency.

# Memory Utilization

* * *

The Proxy Server must have a minimum of 4GB of free RAM available to use (6GB is recommended). For this reason, it's recommended to modify the <install dir>/conf/wrapper.conf configuration file.  For setting the memory size, refer to the documentation here:

[Set the proxy server initial memory limit and upper bound memory limit](https://docs.servicenow.com/csh?topicname=increase-memory.html&version=latest "Set the proxy server initial memory limit and upper bound memory limit")
