---
title: "Customer VIP Migration FAQ"
aliases:
  - KB0596772
tags:
  - servicenow
  - support-kb
  - ip-address
  - migration
  - data-center
  - faq
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596772
kb_number: KB0596772
last_modified: 2025-04-10
---

## Issue

## VIP Migration | Customer FAQ 

#### 1\. What is the Customer VIP Migration Project?

ServiceNow will be changing the IP addresses associated with all customers instances. The new IP address provided will be applicable to all of your instances on a per data center region. There is a unique IP address associated with each of the two paired data center regions. ServiceNow is changing these IP addresses to improve the overall availability, scalability and security posture. These are the addresses that are provided by DNS when you access your instance via its servicenow.com URL.

#### 2\. What do I need to do to prepare for this change prior to the planned start?

A vast majority of our customers trust DNS and do not apply any restrictions or filters on the IP address associated with their instance. However, we have experienced issues with some customers who do have restrictions. We simply need you to confirm that ServiceNow can proceed with this change without impact to access to your services. If you want to allow list the IP addresses associated with your instances, these can be provided to you ahead of the change. In addition to accessing your instances using the new IP address, please also validate any integrations you may have that access ServiceNow via that IP address. Note that any partners you have may also need to allow list the new IP address if they are accessing your instances.

#### 3\. Will we be able to stage the transition by first testing the migration on our sub-production instances?

No. The IP address is a single unique address across all of your instances. 

#### 4\. What happens if we don't update our firewalls or internal VPN with the new IP address before the change is executed?

When the DNS change is made, you will be unable to reach your instances on the new IP address assuming you are allow listing the addresses. The connectivity on the ServiceNow datacenter side is taken care of.

#### 5\. What are the new IP addresses? How will I be informed of the new IP addresses?

The new IP will be assigned dynamically. If needed, these can be provided to you ahead of the change.

#### 6\. What happens if we are unable to access an instance after changes have been done to our VIPs?

ServiceNow has sent an Incident notification (INT) regarding this change. Contact ServiceNow Customer Support using this INT for help and engagement with a network engineer.

#### 7\. I need to reschedule this change as I have conflicting operations at this time. How can I reschedule the change for our instance?

ServiceNow has sent an Incident notification (INT) regarding this change. Please respond using this INT and a representative from ServiceNow Customer Support will follow up on your request.

#### 8\. Will I be able to use a CNAME to direct traffic to the instance?

The host header must still be set, so you cannot use just a CNAME to direct traffic to an instance. Functionality will be no different from how it is now.

#### 9\. We restrict outbound communications from our networks to specific IPs. What services might be affected by the migration (MID Servers / user interfaces / webservices)?

Any service that relies on the IP address of your instance will be affected.

#### 10\. Will the Source IPs from my outbound integrations change?

No.

#### 11\. Will I experience downtime when switching from the old IP address to the new IP address?

Yes. There will be approximately 5 minutes of downtime while the DNS updates globally from the old IP to the new IP.

#### 12\. How do I get the new IP addresses?

These will be assigned to each customer ahead of time.

#### 13\. Our ServiceNow implementation has changed over time and we do not know what services or integrations are connecting to the instance. Can ServiceNow provide us with a list of impacted applications?

No. We are unable to see what integrations you may have or use.

  

## Resolution

## Related

- [[KB0623078 - Data Center Migration | Customer FAQ]] - related IP/data-center migration FAQ
