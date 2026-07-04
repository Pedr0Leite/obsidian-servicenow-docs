---
title: "Data Center Migration | Customer FAQ"
aliases:
  - KB0623078
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623078
kb_number: KB0623078
last_modified: 2026-06-18
---

## Issue

Data Center Migration | Customer FAQ 

* * *

Contents

[1.  What does the Data Center Migration maintenance entail?. 1](#_Toc93928691)

[2\. Why is this maintenance happening?. 1](#_Toc93928692)

[3\. How will ServiceNow communicate with me about this maintenance?. 1](#_Toc93928693)

[4\. How will I receive my new IP address(es)?. 1](#_Toc93928694)

[5\. What actions do I need to take before my instances are moved and IP addresses are updated?  1](#_Toc93928695)

[6\. What will happen if I do not make updates to my firewalls before my instances are moved?  2](#_Toc93928696)

[7\. What happens if we are unable to access an instance after changes have been done to our VIPs?. 2](#_Toc93928697)

[8\. Can I reschedule the change(s) scheduled for my instance(s)?. 2](#_Toc93928698)

[9\. Will I be able to use a CNAME to direct traffic to the instance?. 2](#_Toc93928699)

[10\. What services will be affected by the migration/IP change?. 3](#_Toc93928700)

[11\. Will the Source IPs from my outbound integrations change?. 3](#_Toc93928701)

[12\. Will I experience downtime when switching from the old IP address to the new IP address?  3](#_Toc93928702)

[13\. How do I get the new IP addresses?. 3](#_Toc93928703)

[14\. Can ServiceNow provide us with a list of impacted applications?. 3](#_Toc93928704)

* * *

1.  What does the Data Center Migration maintenance entail?

ServiceNow will be moving your instances to a new data center. With this move, there will also be an update to the associated IP addresses for your impacted instance(s).

2\. Why is this maintenance happening?

Adding additional data centers and updated IP addresses allow ServiceNow to provide you with improved performance and availability for your ServiceNow instance(s). 

3\. How will ServiceNow communicate with me about this maintenance?

You will be notified of this maintenance via a Communication record. After this Communication record is created, Change records will be created to schedule your instances moves. Change record information for your instances will be added to your Communication record. All the information regarding your new IP addresses can be found in the respective Change records.

4\. How will I receive my new IP address(es)?

Each instance will be scheduled to move through a Change record. The new IP address information for the related instance will be included in that Change record. We will utilize your Communication record to keep you updated on all your Changes throughout this maintenance. The new IP address provided will be applicable to all your instances on a per data center region. There is a unique IP address associated with each of the two paired data center regions.

5\. What actions do I need to take before my instances are moved and IP addresses are updated?

For most of our customers, there is no action required as they do not apply restrictions or filter IP addresses associated with their instance(s). If you are one of these customers, then no action is needed before your instance(s) are moved.

If you are not one of these customers and do have restrictions, all you need to do is the following:

-   Confirm that ServiceNow can proceed with this change without impact to access to your services.
-   Allow list the IP addresses associated with your instances (provided in the Change record)
-   Validate any integrations you may have that access ServiceNow via that IP address. Note: If you work with a Partner, be sure to let them know about this change as they will also need to allow list the new IP address if they are accessing your instances.
-   Configure your mail server to use SPF records dynamically. Please refer to the following KB article: [KB0535456](https://support.servicenow.com/kb_view.do?sysparm_article=KB0535456 "https://support.servicenow.com/kb_view.do?sysparm_article=KB0535456")
-   The ServiceNow source IP addresses for any integrations that do not use VPN tunnels will also be changing. Please be sure to allow inbound integrations traffic to your network from the new ranges which will be provided in the change. 

For customers with existing VPN tunnels:

-   Updating VPN tunnels requires coordination with the ServiceNow Network team. Once your move change is scheduled, the ServiceNow Network team will contact you through a separate change record to coordinate the creation of your VPN tunnels. The new tunnels must be in place to ensure your instances migrate successfully.
-   The ServiceNow source IP addresses for any integrations that do not use VPN tunnels will also be changing. As such, please be sure to allow inbound integrations traffic to your network from the new ranges which will be provided before the change. 

6\. What will happen if I do not make updates to my firewalls before my instances are moved?

If you have allowlisted the IP addresses for your instances and do not make the updates before your instances are moved, you will find that you are not able to reach your instance after the move and IP change have occurred. Please be sure to allowlist the new IP address(es) to ensure you are able to access your instances.

7\. What happens if we are unable to access an instance after changes have been done to our VIPs?

If you have any questions or concerns, please reply directly to your Communication record or visit the [Customer Support - Contact Us](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000420) page for contact information in your region.

8\. Can I reschedule the change(s) scheduled for my instance(s)?

You can request a reschedule for any of your moves via your Communication record.   

9\. Will I be able to use a CNAME to direct traffic to the instance?

After your instance is moved and IP address is changed, there will be not change to functionality. As with current functionality, use of a CNAME is not an option as the host header must be set.

10\. What services will be affected by the migration/IP change?

Any service that relies on the IP address of your instance will be affected by this maintenance. Please be sure to make necessary updates to IP information with these services to prevent interruption.

11\. Will the Source IPs from my outbound integrations change?

Yes, the source IP for outbound integrations for your instances will change. All IP information will be provided to you in the Change record when your move is scheduled.

12\. Will I experience downtime when switching from the old IP address to the new IP address?

Yes, you can expect some downtime within the maintenance window, but it will likely only be for a few minutes. During this time, the DNS updates globally from the old IP to the new IP.

13\. How do I get the new IP addresses?

Your new IP addresses will be provided to you when the Change record is created scheduling your instance(s) to move.

14\. Can ServiceNow provide us with a list of impacted applications?

No. We are unable to see what integrations you may have or use.

## Resolution
