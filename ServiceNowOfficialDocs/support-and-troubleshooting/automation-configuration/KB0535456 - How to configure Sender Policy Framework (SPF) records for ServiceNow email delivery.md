---
title: "How to configure Sender Policy Framework (SPF) records for ServiceNow email delivery"
aliases:
  - KB0535456
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535456
kb_number: KB0535456
last_modified: 2026-07-01
---

## How to configure Sender Policy Framework (SPF) records for ServiceNow email delivery

  

### Issue

Learn how to configure your email infrastructure to use ServiceNow Sender Policy Framework (SPF) records so that email delivery from your ServiceNow instance to your corporate email service is not interrupted

If your company blocks email from unknown IP addresses or uses spam filtering based on IP addresses, you can configure those services using ServiceNow SPF records. ServiceNow provides SPF records to assist with anti-spoofing and spam detection.

SPF is standardized under RFC 4408. For more information, see the following resources:

-   [OpenSPF](http://www.open-spf.org "OpenSPF")
-   [RFC 4408](http://www.ietf.org/rfc/rfc4408.txt "RFC 4408")

#### **ServiceNow email server IPs**

The ServiceNow email server IPs apply only when the instance uses the ServiceNow-provided SMTP account for outbound emails. If the instance uses a custom SMTP configuration, the node IPs listed under "Source address used for integrations into customer network with NO VPN" apply instead. For details, see [IP address information - Access and Integration.](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598826 "IP address information - Access and Integration")

#### **SPF record coverage across datacenters** 

ServiceNow email servers back each other up across datacenters. If there are capacity or connection issues in one datacenter, emails are routed through another. For example, an EMEA instance normally uses c.spf but may temporarily use b.spf or d.spf.

This failover occurs without notice and cannot be disabled for individual instances. Allow-list all three SPF records to avoid email delivery issues.

IPs may be added or removed frequently. To inspect the current list, run the following dig commands:

dig b.spf.service-now.com

dig c.spf.service-now.com

dig d.spf.service-now.com

**Note**: If you do not have access to the dig command (for example, on Windows), for output equivalent to dig <domain> TXT +short, use [MxToolbox SPF Lookup](http://mxtoolbox.com/spf.aspx).

### Release

All supported releases 

### Resolution

Configure your mail systems to use SPF records dynamically using your mail server's built-in feature for automatic retrieval. This is the preferred approach because if ServiceNow moves your instance to another datacenter, your mail servers continue to receive emails without manual updates.

If you encounter issues with SPF TXT record length, see [Configure long SPF TXT records (AWS)](https://repost.aws/knowledge-center/route-53-configure-long-spf-txt-records).

### Alternative solution: Manually query SPF records

If you cannot configure your mail servers to dynamically use SPF records, work with your email or system admin to gather SPF record data manually using dig commands to build your allow list.

**Skills required:**

-   Knowledge of SPF record format
-   Access to dig or a similar DNS tool

**Warning**: ServiceNow reserves the right to change SPF record structure and the hosts or IPs returned. This may affect the commands you run, and your allow list may become outdated over time, causing email issues.

While these types of updates are generally infrequent, they can occur. Implement a regular process, manual or automatic, to validate the SPF data you gather against your allow list. **Update your allow list regularly to avoid email issues.**

#### **Example: Querying SPF records with dig**

The following example issues an initial dig command and, based on the response structure, issues further queries to locate hosts and IPs.

**Warning**: This is only an example of commands and returned values. Work with your email admin to run the initial query and follow the SPF record data to gather current IP addresses.

#### **Step 1: Query the initial SPF record**

Run the following command to query the service-now.com domain for TXT records:

dig service-now.com TXT +short

This command returns data that includes three a: records, similar to the following:

"v=spf1 **a:b.spf.service-now.com a:c.spf.service-now.com a:d.spf.service-now.com**"

Each record points to a group of mail servers based on datacenter location:

-   b.spf.service-now.com — Canada datacenters
-   c.spf.service-now.com — US and Europe datacenters
-   d.spf.service-now.com — All other datacenters

#### **Step 2: Query the IP addresses for each group**

The IP addresses of mail servers for the service-now.com domain are available in the DNS A records on each of the listed domains. Run the following commands to retrieve the IP addresses for each datacenter group:

dig A b.spf.service-now.com +short # Canada DCs  
dig A c.spf.service-now.com +short # US/Europe DCs  
dig A d.spf.service-now.com +short # all other DCs  
  

**Important**: Include all IPs from all three records in your allow list regardless of where your instance is located. ServiceNow may reroute email traffic through any datacenter.

#### **SPF validation tool**

There are many tools for testing SPF records. To verify that a new SPF record is syntactically correct and does not require more than 10 DNS lookups before you publish it to DNS, one option is [Kitterman SPF Validator.](http://www.kitterman.com/spf/validate.html)

  

### Secondary alternative: Static IP allow list

If you cannot configure dynamic SPF records and do not have access to the tools needed to query the ServiceNow SPF records manually, run the following DNS queries and use the resulting IPs to statically define the ServiceNow mail server IP addresses in your allow list.

**Important**: ServiceNow may add or remove IP addresses from these records at any time.

To get the current IP address list, run the following commands:

dig A b.spf.service-now.com +short # Canada DCs  
dig A c.spf.service-now.com +short # US/Europe DCs  
dig A d.spf.service-now.com +short # all other DCs

Include all IPs from all three records in your allow list regardless of where your instance is located. ServiceNow may reroute email traffic through any datacenter to maintain availability.

### Special case: Hybrid Singapore instances

Instances in Hybrid Singapore must use the from domain @sg.service-now.com, not @service-now.com, for outbound SMTP accounts.

There is a separate SPF record for sg.service-now.com:

"v=spf1 a:spf.sg.service-now.com -all"

**Note**: This is different from the service-now.com SPF record.

To verify the current IPs, run: 

$ host spf.sg.service-now.com

spf.sg.service-now.com has address 149.96.220.3

spf.sg.service-now.com has address 149.96.221.3

If these IP addresses change, the change is reflected in the SPF record. A change in IPs is unlikely.

**Important**: If you are still using old SPF records after a change has been made on the datacenter, ServiceNow does not take responsibility for email delivery issues.

### Related Links

-   [IP address information - access and integration](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598826 "IP address information - Access and Integration")
-   [OpenSPF](http://www.open-spf.org "OpenSPF")
-   [RFC 4408](http://www.ietf.org/rfc/rfc4408.txt "RFC 4408")
-   [Configure long SPF TXT records (AWS)](https://repost.aws/knowledge-center/route-53-configure-long-spf-txt-records)

For GCC (servicenowservices.com) please see [https://hiwave.servicenowservices.com/kb\_view.do?sysparm\_article=KB20000578](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000578)
