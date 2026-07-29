---
title: "Requesting an IPSec VPN tunnel for LDAP integration "
aliases:
  - KB0541961
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0541961
kb_number: KB0541961
last_modified: 2024-11-04
---

## Issue

Requesting an IPSec VPN tunnel for LDAP integration 

Overview

* * *

The vast majority of VPN tunnel requests stem from integrating LDAP with ServiceNow. This article describes the two functions of LDAP integrations:  Authentication and user data imports, (the attributes). It provides the recommendation from ServiceNow to achieve this integration without the use of VPN tunnels. The driving factors for not using VPN tunnels as a solution for LDAP integration are cost, reliability, flexibility and security.  
  
  
LDAP functions

* * *

Authentication

ServiceNow recommends Single Sign-On (SSO) when possible for user authentication. SSO provides security and flexibility, and does not require the instance to make a connection to any server. With SSO configured, the instance redirects the user’s browser to the URL configured in the instance in order to validate the credentials, _or_ accept the token already obtained with a previous connection to the SSO provider. ServiceNow never makes this connection to the SSO provider but, rather, the user does. This method is not only more secure but also much more reliable and easier to maintain than VPN tunnels. SSO is the authentication method used by most of our customers and is our recommendation for authentication.

Since the Eureka release, we have included Okta for SSO as well as placing our LDAP listener on the MID server. Of course, you are free to use any SSO provider you choose, including ADFS. We fully support the SAML 2.0 protocol. 

  
User data imports

Since the release of Eureka, ServiceNow is now able to leverage user data imports dynamically with the use of the MID server. Because the MID server always initiates the connection to the instance and always over an encrypted session, not only is the data secure but also the connection. In contrast to using a VPN tunnel, the MID server method means that no server anywhere at ServiceNow, or anywhere else, needs to make a connection to a server in our customer’s network.

In Eureka, we implemented polling support on the MID server. This means that the MID server, which lives inside our customer’s private network, can poll the LDAP server directly and send updates securely to the Instance. MID server connections to the instance are always encrypted over a Secure Socket Layer (SSL) channel or uses Transport Layer Security (TLS), end-to-end at the application layer. The MID server makes this connection with the MID server user, which is like any other user, only with restricted roles that allow it to access only one table in the instance: the External Communications Channel (ECC) queue. Therefore, any modifications to the LDAP server are picked up by the MID server and sent securely to the instance.   

When SSO is not available, another option is to use LDAPS over the Internet. This method provides security at the application layer as opposed to VPN tunnels which only encrypt the traffic between the two VPN peer devices. The SSL certificate is uploaded to the instance over a secure encrypted channel, which allows the instance, and only the instance, to query the LDAP server.  That is, not even the server on which the Instance is installed would be able to query the LDAP server.  Only the Instance, which uses the SSL certificate supplied, will be able to encrypt and decrypt the LDAP traffic. The LDAP server could be locked down further to allow access only from the ServiceNow source IP addresses and ports used.  The default LDAPS port is 636 and is configurable in the Instance allowing our customers to use Port Address Translation (PAT) if desired. If using Microsoft Active Directory 2008 or later, a read-only domain controller that does not store any passwords could be used for this integration and is our recommendation when using LDAPS over the Internet.

  
Security

* * *

VPN tunnels have been used historically as a solution to encrypt traffic over the Internet, but this traffic is only encrypted between the two VPN devices. VPN tunnels still leave the traffic between the servers unencrypted inside each network at both ends of the tunnel, between the VPN device and the local machine. This leaves a gap in security as the traffic before entering  and after exiting VPN Device is not protected and could be potentially exposed to confidentiality and integrity risks. Customers are also advised to limit traffic to only required LDAP service on their end if using IPSEC VPN.

SSL, on the other hand, encrypts the traffic at the application layer using the same encryption and hash methods as VPN devices. SSO connections and MID server connections use SSL to encrypt all traffic end-to-end at the application layer, thereby providing a longer and more secure encryption path. This method of connectivity is highly secured and avoids all associated security risks with using IPSEC VPN.

  
  
Flexibility

* * *

The SSO configuration in the instance is fully maintained by the customer. Any changes to the configuration can be made without involving ServiceNow. There is no need to coordinate changes or open an incident in the event that you need to make a change to your SSO configuration. Similarly, if you add, change, or remove LDAP servers in your environment or make other modifications to your infrastructure, you can easily modify the MID server to accommodate these changes without coordinating with ServiceNow.

Using VPN tunnels, on the other hand, require coordination with ServiceNow engineers to make any changes to the tunnel configuration, including adding or removing a server or changing its IP address. In some cases, modifications to VPN tunnels require downtime to the tunnel, which would prevent users from logging in during the maintenance. Using SSO and the MID server solution means these simple changes can be done quickly and easily within any window without coordinating with anyone at ServiceNow. Of course, ServiceNow offers full 24/7 support in case any issues occur.  
  

Reliability

* * *

VPN tunnels work well once configured; however, and especially when different vendors are involved, there are times when an upgrade in code on one side or new settings are applied, for example, that a VPN tunnel ceases to function properly. In such an event, and if the tunnel is used for authentication, then this tunnel outage prevents any users from logging in to the instance. This effectively is an outage for them.

By contrast, SSO uses a URL that is typically a front end serving multiple servers. Authenticating using SSO provides better availability of services than a static connection between two VPN endpoints, which means the instance is available more often when authenticating using SSO, as opposed to relying on VPN tunnels for this functionality.  
  

Cost

* * *

The costs involved with VPN tunnels are mostly seen in maintenance, whether to the devices or modifications to the tunnel configurations. In the event of any issues where ServiceNow needs to troubleshoot the network, the introduction of a VPN tunnel adds complexity to that process and usually involve specialized engineers.

Using the Internet for the transport mechanism allows ServiceNow to focus on general infrastructure and common routing without troubleshooting the overhead traffic introduced when a VPN tunnel is involved. Because of the ease of complexity when using SSO for authentication and the MID server for user data imports, the cost of maintenance and troubleshooting are less than when using a VPN tunnel as a solution for functionality.  
  

Conclusion

* * *

ServiceNow recommends using SSO for authentication and the MID server for user data imports for all LDAP integrations. ServiceNow continues to support IPSec VPN tunnels if these options are not available and for other integrations where SSL certificates cannot be used to encrypt the traffic between the two endpoints.
