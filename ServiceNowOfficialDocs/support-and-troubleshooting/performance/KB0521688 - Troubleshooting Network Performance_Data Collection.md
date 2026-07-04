---
title: "Troubleshooting Network Performance_Data Collection"
aliases:
  - KB0521688
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521688
kb_number: KB0521688
last_modified: 2026-04-21
---

## Troubleshooting Network Performance\_Data Collection

  

### Issue

ServiceNow works to build and maintain an industry-leading network that allows for access to various services. Built on the pillars of availability, security, and performance, the network provides global connectivity to all of its available services, which is crucial for an optimal customer experience. The Internet is the primary means used to access ServiceNow and the product requires three parties to ensure its successful operation: ServiceNow, the user, and the Internet service providers (ISPs) used by both.

When troubleshooting network performance issues, it is important to quickly identify the issue and collect necessary data to mitigate the problem. This article documents the information the user must gather and provide to help resolve the performance issue as quickly as possible.

### Data Gathering

When a network issue is suspected and cannot be resolved internally, contact the ServiceNow Service Operations Center (SOC) to engage the right resources in a timely manner. In order to effectively troubleshoot the network issue, the following information is required:

### Required Information

-   A complete description of the problem.

Identify whether the issue originates from an _Inbound_ request to ServiceNow (for example, via a web browser) or an _Outbound_ request for other functionality, such as login or integrations.

**FOR ISSUES WITH INBOUND REQUESTS (i.e. inability to connect to the instance or slow performance connecting to the instance over the Internet):**

-   The source Internet IP address(es) from which the issue is occurring.

This is the most important information.

This **MUST** be the Public IP address the connection is coming from, **NOT** the private IP address of the workstation. (For info, the private IP ranges are 10.0.0.0 to 10.255.255.255, 172.16.0.0 to 172.31.255.255, 192.168.0.0 to 192.168.255.255).

If you have difficulties getting this information, the easiest way is to go to the following URL, which will tell you your public IP address: [http://www.whatismyipaddress.com/](http://www.whatismyipaddress.com/ "http://www.whatismyipaddress.com/")

-   nslookup to the instance's URL.

  Verify that the IP address of the URL is resolved successfully.

-   Telnet to the destination IP address or URL. Do you get a response or is this timing out? 

Telnet to the instance's URL (**_<instancename>_.service-now.com**) over port 443 (HTTPS).

Here's just an example of a successful connection:

$telnet xxx.service-now.com 443  
Trying 199.91.140.100...  
Connected to support.servicenow.com.  
Escape character is '^\]'.

-   Traceroute to the destination address.

The traceroute will display the transit hops the traffic is taking in order to reach ServiceNow, it will also display the various delays induced by these hops.

Please also ask the customer to verify whether they are using **DNSSEC** to communicate with the ServiceNow instance.

### FOR ISSUES WITH OUTBOUND REQUESTS (ie authentication issue using LDAP, VPN integration failures, etc.): 

-   The name of the ServiceNow instance.

-   Details on the integration that is having issues.

This includes IP address and port/protocol.

-   Has the integration ever worked before? (Yes/No)
-   Is a Virtual Private Network (VPN) being used for any part of the needed access? (Yes/No)

### Optional Information

### FOR ISSUES WITH INBOUND REQUESTS (i.e. inability to connect to the instance or slow performance connecting to the instance over the Internet):

-   Is this an intermittent issue? (Yes/No)

If so, please provide the dates and times of past occurrences.

-   Is the issue isolated to specific users or locations? (Yes/No)

If so, please provide sample IP addresses of affected users and their locations.

-   Are you going through a Proxy server in order to reach the Internet? (Yes/No)

If yes, can you try to bypass this proxy to reach Servicenow? Does that make any difference to the performance?

-   Include any additional information or data that can aid in the rapid mitigation of the issue.

### Troubleshooting

ServiceNow engineers use the information collected to troubleshoot the network issue. If it is determined that the cause lies outside of the ServiceNow network, ServiceNow engineers will enlist the help of support engineers. Depending on the issue, troubleshooting can also extend to the ISP(s) that are used by ServiceNow and the user. Issues that lie with the Internet are usually beyond the control of either the user or ServiceNow. However, all efforts are made to work in partnership with the user to restore service as quickly as possible.

 **Note:** For more information, see [Validate Network Connectivity](https://docs.servicenow.com/csh?topicname=t_ValidateNetworkConnectivity.html&version=latest "Managing Network Connectivity").

### Release

any

### Resolution

.
