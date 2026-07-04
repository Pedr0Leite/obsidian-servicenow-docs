---
title: "Migration to U.S. Government Community Cloud (GCC) Customer FAQs"
aliases:
  - KB0745039
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745039
kb_number: KB0745039
last_modified: 2025-09-05
---

## Issue

**Migration to U.S. Government Community Cloud (GCC)**

**Customer FAQs**

![/var/folders/yf/th6p6wl97g306fv3hqx440lw0000gn/T/com.microsoft.Word/Content.MSO/FA5ACB41.tmp](/sys_attachment.do?sys_id=34d448b9933b2ad4d9743f986cba10ba)![/var/folders/yf/th6p6wl97g306fv3hqx440lw0000gn/T/com.microsoft.Word/Content.MSO/344CEFF7.tmp](/sys_attachment.do?sys_id=acd48c79933b2ad4d9743f986cba10f0)![/var/folders/yf/th6p6wl97g306fv3hqx440lw0000gn/T/com.microsoft.Word/Content.MSO/DC28941D.tmp](/sys_attachment.do?sys_id=28d48c79933b2ad4d9743f986cba10f5)![/var/folders/yf/th6p6wl97g306fv3hqx440lw0000gn/T/com.microsoft.Word/Content.MSO/ED759933.tmp](/sys_attachment.do?sys_id=f4d408b9933b2ad4d9743f986cba1024)![/var/folders/yf/th6p6wl97g306fv3hqx440lw0000gn/T/com.microsoft.Word/Content.MSO/1DF1DCB9.tmp](/sys_attachment.do?sys_id=24d4c0b9933b2ad4d9743f986cba106f)

                       ![](/sys_attachment.do?sys_id=90d48479933b2ad4d9743f986cba10af)         ![](/sys_attachment.do?sys_id=2cd48879933b2ad4d9743f986cba109e)

# **Table of Contents**

1.  What is ServiceNow's U.S. Government Community Cloud (GCC)? Which ServiceNow customers use the GCC environment?
    
2.  Are you required to move to the GCC data centers, or can you remain in ServiceNow's commercial data centers?
    
3.  What actions are required to prepare for a migration to the GCC data centers?
    
4.  What actions are required before moving my Now Support Portal (HI) users and data to Now Support Portal GCC (HIWAVE)?
    
5.  What changes need to be made to the MID server?
    
6.  When using SSO/SAML, what changes are needed for this migration?
    
7.  Why do all instances need to be upgraded to Orlando or to later versions?
    
8.  What is the Customer Responsibility Matrix (CRM) and where is it located?
    
9.  What is a NAT IP address and how is it used?
    
10.  How will the NAT IP address be changing, and how do you change it?
     
11.  Why does the NAT IP address need to be updated?
     
12.  What is the External Domain Name Space (DNS) address?
     
13.  Why does a new External DNS address need to be added?
     
14.  What is the difference between a NAT IP address and an External DNS IP address?
     
15.  How do these changes impact VPN customers?
     
16.  How does the ServiceNow team verify that the changes to the VPN are successful?
     
17.  Are there alternatives to using a VPN?
     
18.  How are these change requirements coordinated?
     
19.  What if there are already existing plans for a ServiceNow instance version upgrade?
     
20.  After you schedule the instance migration date/time, what happens if your not ready by that date?
     
21.  How long will the move take, and is there any downtime during the move?
     
22.  What happens if you have instances in the Commercial and GCC environments concurrently? Can you access instances in both environments concurrently?
     
23.  What happens if you are unable to access an instance after it has migrated into GCC?
     
24.  What is Multi-Factor Authentication?
     
25.  After the migration into GCC, what action do you take if unable to Clone-down Production instances to Sub-Production instances?
     
26.  What if you still have questions not answered in this FAQ?
     

# **Overview** ![/var/folders/yf/th6p6wl97g306fv3hqx440lw0000gn/T/com.microsoft.Word/Content.MSO/BDA31D31.tmp](/sys_attachment.do?sys_id=60d48879933b2ad4d9743f986cba10a1)

This Customer FAQ relates to the migration of customer instances into ServiceNow's U.S. FedRAMP High and DoD Impact Level 4 authorized environment located in our two data centers in Ashburn, VA and Miami, FL. ServiceNow has named this environment "Government Community Cloud" (or "GCC") .

## **_1\. What is ServiceNow's U.S. Government Community Cloud (GCC)? Which ServiceNow customers use the GCC environment?_**

ServiceNow's Government Community Cloud (or "GCC") environment possesses both Federal Risk and Authorization Management Program (FedRAMP) High and Department of Defense (DoD) Impact Level 4 (IL4) authorizations which include over 400 security controls. This provides U.S. government agencies and eligible contractors the ability to leverage this environment for highly sensitive workloads, including Personal Identifiable Information (PII), sensitive patient records, financial data, law enforcement data, and other Controlled Unclassified Information (CUI).

ServiceNow has obtained both a FedRAMP High Provisional Authority to Operate (P-ATO) and DoD IL4 Provisional Authorization (PA). 

Within ServiceNow's GCC environment there are currently three (3) network segments, or "pods", that are intended for:

-   U.S. federal agencies operating at a High or Moderate level, and DoD IL2 customers may be located within GCC's Internet-connected pod.
-   U.S. DoD mission owners operating at an IL4-level and needing access from NIPRNet over ServiceNow's BCAP will be located in GCC's DISA CAP-connected pod.
-   U.S. DoD Medical Community of Interest (MedCOI) mission owners will be located within GCC's MedCOI CAP-connected pod.
-   Commercial entities supporting U.S. federal agencies and DoD mission owners will be located within GCC's Internet-connected pod.

## **2\. _Are you required to move to the GCC data centers, or can you remain in ServiceNow's commercial data centers_?**

The GCC environment has been built in adherence with all FedRAMP High & DoD IL4 compliance requirements. This includes controls to ensure your data is kept safe at a FedRAMP High and DoD Impact Level 4 impact level for ServiceNow's GCC environment.

However, customers can keep their instances in ServiceNow's Commercial environment, if they are unable to migrate to GCC and they comply with applicable laws and regulations. 

**NOTE**: Because of the more stringent compliance requirements in this environment, certain systems/systems/plugins will no longer be accessible post migration to this environment.  Please refer to KB0743854 for the list of services that are not be available in the GCC environment at this time.

## **3\. _What actions are required to prepare for a migration to the GCC data centers_?**

Before the migration to the GCC data centers, all instances must satisfy the following GCC pre-requisites. (More information about many of these requirements can be found within the answers in this article.)

1.  Review the Customer Responsibility Matrix (CRM) ([KB0685212)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685212) and achieve a [Security Center Hardening score](https://www.servicenow.com/docs/csh?topicname=sc-hardening.html&version=latest) of 100%. ServiceNow will no longer mandate that instances be hardened prior to migration. This change means that ServiceNow will not validate the hardening status of your instance prior to migration. Hardening your instances is still a requirement to be compliant with FISMA/FedRAMP and DoD/DISA regulations, however, you may choose to implement these requirements post-migration into GCC.
2.  Your instances will be configured with both new URL addresses and IP addresses. Upon request, ServiceNow can provide an auto-redirect to the new URL for 30 days after migration. Please assess impact of a new URL address on your instance and make the necessary changes. Your instance URL addresses (domains) will change per the following examples:  
    -   Instancename@service-now.com will become: instancename@servicenowservices.com following the migration into the GCC's Internet-connected pod.
    -   Instancename@service-now.com will become instancename@servicenowservices.mil following the migration into the GCC's DISA CAP-connected pod.
    -   Instancename@service-now.com will become instancename@servicenowservices.health.mil. following the migration into the GCC's MedCOI CAP-connected pod.
3.  Emails to your old instance email address will be automatically forwarded.
4.  Permit the NAT IP address range from ServiceNow. (See Question 9).
5.  Update external DNS address; ensure all filters allow access to the new IP's (one for each data center) and that your instance name resolves to servicenowservices.com (or.mil or health.mil). Exact address to change will be provided closer to the migration date.
6.  Configuration of the SN Access Control plugin. For more information, including how to request the plugin, see [ServiceNow Access Control](https://docs.servicenow.com/bundle/quebec-platform-administration/page/administer/security/reference/snc-access-control-plugin.html). 
7.  ServiceNow strongly recommends against the use of a VPN for all instance traffic. This is due to the inherent instability of VPNs and the fact all traffic will be double encrypted. For more details, read [this](https://community.servicenow.com/community?id=community_blog&sys_id=4baca625dbd0dbc01dcaf3231f96193c) article. _**If you wish to use a VPN for all instance traffic, a call is required with the ServiceNow Network Engineering team**_. The use of a VPN for outbound integrations such as Active Directory is fully supported and can be requested [here](https://support.servicenow.com/com.glideapp.servicecatalog_cat_item_view.do?sysparm_id=89d00faf9c6b3400988397cb4ab545a9). 
8.  What updates are needed for Multi-Provider SSO when changing the instance name or domain? See [KB0814820](https://support.servicenow.com/kb_view.do?sysparm_article=KB0814820 "KB0814820").
9.  If you are a DoD DISA CAP or MedCOI CAP customer, there may be additional DoD/DISA or MedCOI-specific requirements for migrating into GCC. DoD customers should review [KB0823312](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0823312) and [KB0819715](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819715).
10.  Professional Services can be engaged for helping with this migration if needed. Please direct your questions regarding this engagement to [GovCommunityCloudPS@servicenow.com](mailto:GovCommunityCloudPS@servicenow.com).

## **4**_**. What actions are required before moving my Now Support Portal (HI) users and data to Now Support Portal GCC (HIWAVE)?**_

When all of your instances are completely migrated into GCC, ServiceNow will automatically schedule the migration of your Customer Data in HI our commercial Now Support Portal (support.servicenow.com or "HI") to GCC's Now Support Portal GCC (hiwave.servicenowservices.com or "HIWAVE"). As part of this migration, your user accounts within HI will be migrated to HIWAVE as both inactive and locked. The Customer's Administrator will need to update these users to make them active. Users who already have an account in HIWAVE will not be affected by the Data migration.

Review the [KB20000755](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000755 "KB20000755") regarding: _Users who are unable to log in after Customer Data Migration to HIWAVE complete, due to duplicate user records in HIWAVE._

## **5\. _What changes need to be made to the MID server_?**

When migrating to the GCC environment, all instance names change from the "service-now" domain to the "servicenowservices" domain. In the configuration files for the MID servers (\\agent\\config.xml) there is a URL parameter that tells the MID server which instance to target.

See more details at: [KB0821383](https://support.servicenow.com/kb_view.do?sysparm_article=KB0821383 "KB0821383").

## **6\. _When using SSO/SAML, what changes are needed for this migration_?**

When an instance is migrated into servicenowservices.com/mil/health.mil from service-now.com or when a custom URL is implemented for the first time, the Service Provider information for Single-Sign-On needs to be updated accordingly.

#### Cause

The Identity Provider record in Multi-Provider SSO defines not only the IDP information, but also the Service Provider (ServiceNow) information. If this information changes due to an instance move to a different domain (not datacenter) or implementation of a custom url, the updates have to be performed on both sides - ServiceNow and the IDP, or users will be unable to log in via SSO.

#### Resolution

In the Identity Provider record, the items to change are:

-   ServiceNow Home page
-   Entity ID / Issuer
-   Audience URI
-   and if e-Signature is used, also the URL containing consumer.do

The change will be to replace any occurrence of service-now.com with servicenowservices.com, or the old instance URL with the new custom URL.

After the record is saved, Test Connection, if prompted.

The IDP record does not have to be deactivated for the domain name change.

In the event something goes wrong, do the following:

With debugging turned on, if you go within the same browser tab that failed your login and go to "Node Log File Browser" in your module list and search for message=SAML (case sensitive) for the timeframe of the failed login, you will find the exact error message and can address the root cause.

See more details at: [KB0814820](https://support.servicenow.com/kb_view.do?sysparm_article=KB0814820 "KB0814820"). If you're using IE 11, also see details at: [KB0656513](https://support.servicenow.com/kb_view.do?sysparm_article=KB0656513 "KB0656513") and [KB0693310](https://support.servicenow.com/kb_view.do?sysparm_article=KB0693310 "KB0693310"). If you're using User Provisioning with Microsoft Azure AD: see their ServiceNow Tutorial. 

**NOTE**: Add the trailing slash ([https://instance.servicenowservices.com/](https://instance.servicenowservices.com/)) as required by Microsoft.

## **7\. _Why do all instances need to be upgraded to Orlando or to later versions?_**

The P-ATO is not valid for any instances prior to the Kingston release. The only approved releases as of March 2020 are the Orlando, Paris, Quebec and Rome (once General Availability is reached) releases. Future releases will be added to this list as and when they are approved.

## **8\. _What is the Customer Responsibility Matrix (CRM) and where is it located?_**

The GCC Customer Responsibility Matrix (CRM) includes a list of customer agency actions that should be part of an effective security program for a system based on a SaaS offering. As part of the pre-migration checklist, customers must confirm the completion of required actions as listed in the CRM before they can be migrated to the GovCommunityCloud (US) datacenters. Download this document for more information: [KB0685212](https://support.servicenow.com/kb_view.do?sysparm_article=KB0685212).

## **9\. _What is a NAT IP address and how is it used?_**

Network Address Translation (NAT) is the public/Internet, ServiceNow source IP address seen by your network for traffic initiated from your ServiceNow instance towards your network. ServiceNow specifies a range of IP addresses from which any single one could be used for a connection. If the customer wishes the inclusion list NAP IPs, it is mandatory the entire range is allowed. The Outbound NAT IP range is the same as the "Outbound Integration IP Range".

## **10\. _How will the NAT IP address be changing, and how do you change it?_**

The NAT IP address will be changing as follows:

<table style="width: 100%; border: solid;"><tbody><tr style="height: 20px;"><td style="height: 20px; width: 339.367px;"><span style="font-family: verdana, geneva;"><strong>Destination</strong></span></td><td style="height: 20px; width: 295.967px;"><span style="font-family: verdana, geneva;"><strong>NAT IP addresses</strong></span></td></tr><tr style="height: 20px;"><td style="height: 20px; width: 339.367px;"><span style="font-family: verdana, geneva;">GCC Internet-connected pod</span></td><td style="height: 20px; width: 295.967px;"><span style="font-family: verdana, geneva;">149.96.192.8/29 Asburn, VA</span><br><span style="font-family: verdana, geneva;">149.96.193.8/29 Miami, FL</span></td></tr><tr style="height: 20px;"><td style="height: 20px; width: 339.367px;"><span style="font-family: verdana, geneva;">GCC DISA CAP-connected pod</span></td><td style="height: 20px; width: 295.967px;"><span style="font-family: verdana, geneva;">Upon request</span></td></tr><tr style="height: 20px;"><td style="height: 20px; width: 339.367px;"><span style="font-family: verdana, geneva;">GCC MedCOI CAP-connected pod</span></td><td style="height: 20px; width: 295.967px;"><span style="font-family: verdana, geneva;">Upon request</span></td></tr></tbody></table>

It is the customer's responsibility to add the new NAT IP addresses ranges to their firewall in order to permit connections source from ServiceNow. Appropriate firewall configuration will prevent downtime post-migration. The Outbound NAT IP range is the same as the "Outbound Integration IP Range". 

## **11\. _Why does the NAT IP address need to be updated?_**

The GCC environment is built on an entirely new network architecture and is separate from ServiceNow's commercial networks. This mandates the use of new IP address blocks for NAT.

## **12\. _What is the External Domain Name Space (DNS) address?_**

The External DNS address is the IP address that is used when accessing or initiating connections into a ServiceNow instance. It is the IP associated with an instance ([https://<customer>.servicenowservices.com](https://%3Ccustomer%3E.servicenowservices.com/) or .mil or .health.mil). The IP is unique for each of the two redundant data centers. In the new network, the IP address will change to a unique address per customer (for example, from 149.96.3.100 to **149.96.192.100** in the HEF100 data center and from 149.96.4.100 to **149.96.193.100** in the MIA100 data center). The details about your specific IP address change will be provided as part of instance migration communications.

## **13\. _Why does a new External DNS address need to be added_?**

The DNS for instances within the new GCC requires a distinct name space from our existing commercial cloud. The domain will change from service-now.com to servicenowservices.com (or servicenowservices.mil or servicenowservices.health.mil) to meet this requirement.  The new external DNS address needs to be added to avoid downtime after the instance is moved into the GCC environment.

## **14\. _What is the difference between a NAT IP address and an External DNS IP address?_**

The External DNS address is the IP address that is used when accessing or initiating connections **into** a ServiceNow instance. The NAT IP address is used when an instance is making an **outbound** connection from ServiceNow. 

The following example illustrates the two different concepts: 

![](/sys_attachment.do?sys_id=bcd408b9933b2ad4d9743f986cba101d)

**NOTE**: In the preceding example, the specific IP addresses are for illustration purposes only. 

In the first example (in orange), a customer initiates a connection to a ServiceNow instance using the URL https://customer.service-now.com, which equates to an Internet IP address of x.x.x.x. This IP address is configured on a ServiceNow load-balancer, which then translates the x.x.x.x. IP address to an internal (RFC-1918) IP address of the instance: a.a.a.a. On the ServiceNow network, the instance replies back to the customer's connections using the ServiceNow load balancer that translates the IP address back to an Internet IP address of x.x.x.x. 

In the second example (in green), the ServiceNow instance initiates a connection to the customer for an integration or other service. In this case, the ServiceNow firewall translates from the private RFC-1918 IP address of a.a.a.a to an IP address from our Internet NAT IP range, shown as y.y.y.y. 

## **15\. _How do these changes impact VPN customers_?**

ServiceNow recommends against the use of VPNs as there are options that are far better and easier to manage. Refer to this Community blog on [alternatives to using a VPN](https://community.servicenow.com/community/blogs/blog/2014/11/25/you-dont-need-a-vpn).

If you want to continue using VPNs, please open a new VPN request [using this service catalog form](https://support.servicenow.com/com.glideapp.servicecatalog_cat_item_view.do?sysparm_id=89d00faf9c6b3400988397cb4ab545a9).  

## **16. _How does the ServiceNow team verify that the changes to the VPN are successful_?**

ServiceNow will be able to test each tunnel from the GCC environment to confirm that it has been configured correctly prior to signing off. This will be performed at the time of the scheduled change. You will be informed once all test passes have been completed successfully. 

## **17\. _Are there alternatives to using a VPN_?**

ServiceNow strongly recommends against the use of VPNs. As an alternative, ServiceNow also enables the use of private connectivity via the Equinix Cloud Exchange (ECX) or via DirectConnect of circuits to the ServiceNow network edge.

For more information, go to this Community blog on [alternatives to using a VPN](https://community.servicenow.com/community/blogs/blog/2014/11/25/you-dont-need-a-vpn). 

## **18\. _How are these change requirements coordinated_?**

Customer will receive a communication containing all of the pre-requisite requirements for GCC compliance.

Instance migration activities will be communicated via a customer Case record on the Now Support Portal or on the Now Support Portal GCC (HIWAVE), and in associated change records (CHG#) which will be visible on your service portal.

## **19\. _What if there are already existing plans for a ServiceNow instance version upgrade_?**

You can follow the normal upgrade process as long as the upgrade is going to complete ahead of the migration date. The change records for the instance migration activities will provide the date for the planned migration. If the upgrade timeline you are planning to follow is not going to be completed ahead of the GCC migration timeline, visit your portal page or contact the ServiceNow Global Technical Support team to request a rescheduling.

## **20\. _After you schedule the instance migration date/time, what happens if you're not ready by that date_?**

Your instance is eligible for a migration after prerequisites have been met (please refer to Qs.3).  If and when you realize that you are not ready for your instance migration, please contact customer support and request a rescheduling.

## **21\. _How long will the move take, and is there any downtime during the move_?**

**There is a migration downtime**: typically this will be 60 minutes, depending on the size of the database. This downtime is required to perform the final data sync between instances, shutdown the old instances and activating the new ones. 

There are background processes which occur prior to migration which require an estimated 6 to 96 hours to complete. There is expected to be a downtime during the cut-over window as the instance comes online in the GCC environment. The downtime window will be communicated on a per-instance basis as part of the overall migration and will be performed within the scheduled maintenance window.

## **22\. _What happens if you have instances in the Commercial and GCC environments concurrently? Can you access instances in both environments concurrently_?**

Yes. As long as the new external DNS IP address have been added for each environment, the instance URL will resolve appropriately to Commercial or GCC environment, depending on the location of the instance. 

A separate instance of Now Support Portal (HI) will be available inside GCC – this new instance, named Now Support Portal GCC, will be available at [https://hiwave.servicenowservices.com](https://hiwave.servicenowservices.com). You will have access to this additional instance of Now Support Portal once the migration process for your instances begins. Information for instances migrated to GCC can be accessed via Now Support Portal GCC. Once all of your instances have been migrated to GCC your access to NOW Support Portal  will be suspended, and all support portal access going forward will be exclusively via Now Support Portal inside our GCC environment.

## **23\. _What happens if you are unable to access an instance after it has migrated into GCC_?**

After the move is completed, part of the final test and sign-off will be confirming that you can access the instances. If issues occur, please contact the ServiceNow Global Technical Support team at [http://www.servicenow.com/support/contact-support.html](http://www.servicenow.com/support/contact-support.html) and reference the migration Case or Change record number; The normal escalation processes will be followed to remediate the problem. 

## **24\. _What is Multi-Factor Authentication_?**

Multi-factor authentication (MFA), also known as two-step verification, is a security requirement that requires a user to enter more than one set of credentials in order to authenticate or log in to a system. The goal of MFA is to create a layered defense and make it more difficult for an unauthorized person to access a target such as a physical location, computing device, network or database. If one factor is compromised or broken, the attacker still has at least one more barrier to breach before successfully breaking into the target.

Multi-factor authentication can be achieved through the use of a third-party SSO solution, such as SAML

Typical MFA scenarios include:

-   Swiping a card and entering a PIN.
-   Logging into a website and being requested to enter an additional one-time password (OTP) that the website's authentication server sends to the requester's phone or email address.
-   Swiping a card, scanning a fingerprint, and answering a security question. 
-   Attaching a USB hardware token to a desktop that generates a one-time passcode and using the one-time passcode to log in to a VPN client.

## **25\. _After the migration into GCC, what action do you take if unable to Clone-down Production instances to Sub-Production instances_?**

After instance migration into GCC, if you request a System Clone, the Target Clone instance records are still pointing to the old source environment URLs ([https://instancename.service-now.com](https://instancename.service-now.com)). As a result, Administrators are unable to clone-down from a Production instance to their Sub-Production instances. A request must be submitted is to rename the URL from [https://instancename.service-now.com](https://instancename.service-now.com) to [https://instancename.servicenowservices.com.](https://instancename.service-now.com) 

Or you can set up a new Clone Target from your Source instance (Production) for each of your Target instances in the GCC environment. See [KB20000875 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000875 "KB20000875 (HIWAVE)") for additional details. 

## **26\. _What if you still have questions not answered in this FAQ_?**

_If you have additional questions, please contact ServiceNow Global Technical Support team at_ _[http://www.servicenow.com/support/contact-support.html](http://www.servicenow.com/support/contact-support.html "http://www.servicenow.com/support/contact-support.html")_

# **Other Important KB Articles**

**Important instructions** related to preparation for the migration to the GCC environment are as below:

| KB Number | Description |
| --- | --- |
| [KB0685212](https://support.servicenow.com/kb_view.do?sysparm_article=KB0685212 "KB0685212") | Customer Responsibility Matrix |
| [Security Hardening Guide](https://www.servicenow.com/docs/csh?topicname=sc-hardening.html&version=latest) | Security hardening guidelines including hardening score comparison and settings |
| [KB0743854](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743854) | List of services unavailable in ServiceNow's Government Community Cloud (US) |
| [KB0814820](https://support.servicenow.com/kb_view.do?sysparm_article=KB0814820) | Updates needed for Multi-Provider SSO when changing the instance name or domain |
| [KB0821383](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821383) | Updates needed on the MID server when the instance FQDN (instance name or domain) change |
| [KB0782884](https://support.servicenow.com/kb_view.do?sysparm_article=KB0782884 "KB0782884") | Post-Migration, Google Maps setup FAQ |
| [KB0723599](https://support.servicenow.com/kb_view.do?sysparm_article=KB0723599 "KB0723599") | Google Maps - Geocoding Latitude and Longitude not working when using the Google API Map Key. |
| [KB0538598](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538598 "KB0538598") | Customer Instance Security Testing | Policy and Procedure (Penetration and Security Testing) |
| [KB20000755 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000755 "KB20000755 (HIWAVE)") | Users who are unable to log in after Customer Data Migration to HIWAVE complete, due to duplicate user records in HIWAVE |
| [KB20000578 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000578 "KB20000578 (HIWAVE)") | Enabling email delivery using SPF records to inclusion list ServiceNowServices mail servers |
| [KB20000813 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000813 "KB20000813 (HIWAVE)") | Upon Migration, which out-of-box scripts should be changed to point to "servicenowservices.com"? |
| [KB20000875 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000875 "KB20000875 (HIWAVE)") | Post-Migration, Unable to Clone-down Production instance to Sub-Production instances |
| [KB20000935 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000935 "KB20000935 (HIWAVE)") | Multi-Factor Authentication in HIWAVE |
| [KB20000818 (HIWAVE)](https://hiwave.servicenowservices.com/kb_view.do?sysparm_article=KB20000818 "KB20000818 (HIWAVE)") | Custom URL issue after GCC Migration |

# Acronyms and Terminology

| Term | Definition |
| --- | --- |
| ADC | Application Delivery Controller (Load Balancer) |
| ATO | Authorization to Operate |
| CAP | Cloud Access Point |
| DISA | Defense Information Systems Agency |
| DISA CAP | A Cloud Access Point connecting ServiceNow's GCC environment to NIPRNet |
| DNS | Domain Name System |
| DOD | Department of Defense |
| FedHigh | FedRAMP High and/or DoD IL4 |
| FedRAMP | Federal Risk and Authorization Management Program |
| HI | A legacy name for ServiceNow's Commercial Now Support portal (support.servicenow.com) |
| HI WAVE | ServiceNow's support portal in GCC (hiwave.servicenowservices.com) |
| IP | Internet Protocol |
| LDAP | Lightweight Directory Access Protocol |
| MedCOI | Medical Community of Interest (U.S. DoD) |
| MedCOI CAP | Cloud Access Point connecting ServiceNow's GCC environment to the MedCOI network |
| MFA | Multi-Factor Authentication |
| NAT | Network Address Translation |
| P-ATO | Provisional Authorization to Operate |
| VIP | Virtual IP address |
| VPN | Virtual Private Network |

## Resolution

N/A

## Text

undefined
