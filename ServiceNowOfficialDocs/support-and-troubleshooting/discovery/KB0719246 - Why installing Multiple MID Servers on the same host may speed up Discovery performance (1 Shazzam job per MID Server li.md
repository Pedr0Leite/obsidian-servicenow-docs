---
title: "Why installing Multiple MID Servers on the same host may speed up Discovery performance (1 Shazzam job per MID Server limitation)"
aliases:
  - KB0719246
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719246
kb_number: KB0719246
last_modified: 2024-04-07
---

## Why installing Multiple MID Servers on the same host may speed up Discovery performance (1 Shazzam job per MID Server limitation)

  

### Issue

**A MID Server will only run one Shazzam job at a time**. Until Shazzam has returned its results from the port probes of the IPs, Discovery is held up and can't start the Classify, Identity and Exploration phases on those devices.

This can in theory lead to **Discovery Schedules taking longer than you expect, or even Timing Out and Cancelling without updating any CIs**.

### Release

Up to and including at least Orlando, and probably future as well.

### Cause

If you have very large IP ranges for a Discovery Schedule - e.g. a /16 subnet requires 65536 IPs to be port probed - and Shazzam is chunking the jobs up by the default 5000 IPs, then your MID Server will have 14 Shazzam Jobs to do.  
If you have multiple Discovery Schedules overlapping, then you may end up with more than that queued up for the single thread available in the MID Server to run them. Some may never get round to running before the Schedule times out.

If a Discovery Schedule Cancels due to Max Runtime while still running a Shazzam job, it will waste time pointlessly continuing that job until it ends, preventing any other Shazzam probes running in that MID Server, such as the following 'Run After' discovery schedule. So it's also important to make sure your Schedules are able to finish at least all the Shazzam probes in their allotted time.

### Resolution

In general for Discovery probes, [increasing the available worker Threads in the MID Server](https://docs.servicenow.com/search?fo=no&q=Set+MID+Server+thread+use "increasing the available worker Threads in the MID Server") would allow it to do more at the same time, but not in the case of Shazzam. In that case you are in effect reducing the proportion of the total available threads that Shazzam can be using at any one time.

So rather than increase the thread count of the MID Server from 25 to 50 or 100 ([with a corresponding increase in allocated memory](https://docs.servicenow.com/search?fo=no&q=Set+MID+Server+memory "with a corresponding increase in allocated memory")), you could [install additional MID Servers](https://docs.servicenow.com/search?fo=no&q=Multiple+MID+Server+deployments "install additional MID Servers") on the same host. The MID Server installer supports this. **You can then have one Shazzam Probe running for each of the MID Server installations on the host.**

The RAM/CPU requirement would only be a little higher due to the overhead of the MID Server itself, but now 2 Shazzam Probes can be run at the same time. This can speed up the throughput of discovery by more than a factor of 2 in some situations, as you are able to get stuck into the actual probing of individual computers quicker. some of the blocking is removed from some schedules.

If the MID Servers are grouped into a Load Balancing Cluster, then the setup of the discovery schedule is just as simple as before, as you select the Cluster via a Behaviour instead of the individual MID Server. This will also give you a little extra fault tolerance where an individual MID Server is Down.

Spreading the multiple MID Servers across different dedicated hardware would be even better, but if you are limited by the Hosts available to you, but have plenty of CPU and Memory on those hosts, then this would be worth considering. 

The 1 Shazzam probe running per MID Server limitation also mean **scheduling multiple Schedules at the same time is not a good idea**. If one schedule starts, the other schedule will be **blocked from starting until its Shazzam probes get a chance to run**. This can prolong runtimes, and lead to cancellations. It is better to sequence schedules for each MID Server or cluster, using the Run=After Discovery run type in the discovery schedule. Using that method does require sensible max runtimes to be set in schedules so that a stuck schedule doesn't hold up the rest of the day's sequence of schedules.

### Related Links

Search the [MID Server Documentation](https://docs.servicenow.com/search?q=mid+server "MID Server Documentation") for more information on actually doing this.

The multi-threaded Shazzam code added in Orlando still has a single concurrent Shazzam job per MID Server limitation, although it is able to run it a lot quicker.
