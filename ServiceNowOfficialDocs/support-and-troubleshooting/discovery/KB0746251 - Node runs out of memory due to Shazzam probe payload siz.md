---
title: "Node runs out of memory due to Shazzam probe payload siz"
aliases:
  - KB0746251
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746251
kb_number: KB0746251
last_modified: 2026-07-02
---

## Node runs out of memory due to Shazzam probe payload siz

  

### Issue

A node runs low on memory while Shazzam processes sensor results during Discovery.

### Release

All currently supported releases.

### Cause

Shazzam is the first phase of Discovery. Shazzam will trigger port scan on x number of devices at a time as configured in on the Shazzam batch size value of the discovery schedule.

Only results from devices that reply to one of the scanners should be returned, however this is configurable. In some cases, all port scans may return closed due to environment configuration even though there is no alive device on such IP range. One example would be when discovering devices behind a firewall, depending on firewall configuration. This could cause a payload returned by Shazzam with a very large result, or as many configured in the Shazzam batch size. Memory issues may result when a very large payload is being processed, or multiple such payloads are being processed at the same time on the same node.

### Resolution

There are parameters which can help control the size of a Shazzam payload.

#### Encode Shazzam payload as JSON string

A system property, introduced in the Jakarta Patch 9 release, converts Shazzam payloads into JSON strings, which dramatically reduces their size. This setting prevents nodes from running out of memory when a single schedule discovers large numbers of IP ranges.

The **glide.discovery.shazzam\_ranges\_json** system property is set to true for new instances. This setting encodes the payload as a JSON string. The property is configurable by administrators and is available in the Discovery Definition > Properties module. The property label is "Use JSON for IP ranges in Shazzam" in the module. This property is set to false in upgraded instances and is not visible by default. Adding the property manually to your upgraded instance enables the feature, but does not add it to the Discovery Definition > Properties module. To enable JSON encoding and add it to the module, import the update set attached to [KB0687626](https://support.servicenow.com/kb_view.do?sysparm_article=KB0687626 "KB0687626").

#### Decrease the number of results returned by Shazzam probe

The payload size can be reduced by setting probe parameter **shazzam\_report\_inactive** when the Shazzam payload is large due to many ip addresses returned as inactive, devices which are alive however have no open ports detected. 

The following is an example as seen in Shazzam input:

<result alive="true" active="false" ip\_address="<ip\_address>">   
<scanner service="http" result="refused" protocol="tcp" portprobe="http" port="80" name="HTTP"/>   
<scanner service="https" result="refused" protocol="tcp" portprobe="http" port="443" name="HTTP"/>   
<scanner service="winrm" result="refused" protocol="tcp" portprobe="winrm" port="5985" name="HTTP"/>   
<scanner service="epmap" result="refused" protocol="tcp" portprobe="wmi" port="135" name="GenericTCP"/>   
<scanner service="wbem\_https" result="refused" protocol="tcp" portprobe="wbem" port="5989" name="GenericTCP"/>   
<scanner service="ssh" result="refused" protocol="tcp" portprobe="ssh" port="22" name="BannerTCP"/>   
<scanner service="vmapp\_https" result="refused" protocol="tcp" portprobe="vmapp" port="5480" name="BannerTCP"/>   
<scanner service="vmapp6\_https" result="refused" protocol="tcp" portprobe="vmapp" port="9443" name="BannerTCP"/>   
\-<scanner service="winrm\_ssl" result="io\_error" protocol="tcp" portprobe="winrm\_ssl" port="5986" name="HTTPS">   
<error\_msg>IOException - The remote computer refused the network connection. </error\_msg>   
</scanner>   
<scanner service="slp" result="timed\_out" protocol="udp" portprobe="slp" port="427" name="SLP"/>   
</result> 

To set the probe parameter:

1.  Navigate to "Discovery Definition > Probes".
2.  Open the Shazzam probe.
3.  Select the "Probe Parameters" related list and click "New".
4.  Set the name to "shazzam\_report\_inactive" and the value to "false".
5.  Click the "Submit" button.

#### Decrease how many ip addresses are scanned by Shazzam at a time

The discovery schedule field "Shazzam batch size" controls how many ip addresses to scan per Shazzam probe. Decrease this value from the default to a lower value if the Shazzam payload is large due alive and active results. The lowest valid value is 256. This will result in more Shazzam probes triggered, however each payload will be smaller. The same number of ip addresses will be discovered.

**Note**: Discovery will not "batch" Shazzam if the batch size is lower than 256. This means only a single Shazzam probe will be created. This could lead to a very large input. Thus, it is best to keep the batch size to a value greater than 256. Message "Shazzam will not batch since it is below minimum batch size of" can be seen in the discovery status log when the batch size is configured lower than 256 for a schedule. This will lead to a single Shazzam probe which could cause memory issues. If so, increase the Shazzam batch size to a value greater than 256.

#### Split large discovery into smaller discoveries

The last Shazzam sensor processed by a discovery does some extra processing which uses results from previous Shazzam probes. This can cause for a large result set held in memory. If the issue is caused by the last Shazzam sensor in a discovery, try splitting the discovery schedule into smaller discovery schedules.

### Related Links

-   [Enable JSON coding of Shazzam payloads for upgraded instances to prevent out of memory issues](https://support.servicenow.com/kb_view.do?sysparm_article=KB0687626 "KB0687626 - Enable JSON coding of Shazzam payloads for upgraded instances to prevent out of memory issues")
-   [Discovery/Shazzam Launch: Shazzam encoding for IPs is inefficient and leads to nodes running out of memory](https://support.servicenow.com/kb_view.do?sysparm_article=KB0693814 "Discovery/Shazzam Launch: Shazzam encoding for IPs is inefficient and leads to nodes running out of memory")
-   [Configure Shazzam probe parameters and payload size](https://docs.servicenow.com/csh?topicname=t_ConfigureTheShazzamProbe.html&version=latest#t_ConfigureTheShazzamProbe "Configure Shazzam probe parameters and payload size")
-   [Schedule a discovery (Shazzam Batch Size)](https://docs.servicenow.com/csh?topicname=t_CreateADiscoverySchedule.html&version=latest "Schedule a discovery (Shazzam Batch Size)")
-   [Discovery/Shazzam Launch: Shazzam encoding for IPs is inefficient and leads to nodes running out of memor](https://support.servicenow.com/kb_view.do?sys_kb_id=439c3be2dbe39b44d58ea345ca96195e&sysparm_rank=1&sysparm_tsqueryId=824411f8db3c3f841cd8a345ca961995 "Discovery/Shazzam Launch: Shazzam encoding for IPs is inefficient and leads to nodes running out of memory")
