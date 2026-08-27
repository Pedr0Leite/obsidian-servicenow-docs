---
title: "IP address information - Access and Integrations"
aliases:
  - KB0598826
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598826
kb_number: KB0598826
last_modified: 2026-05-28
---

## IP address information - Access and Integrations

  

### Issue

This article is a landing page for IP address questions, from accessing your instance to IP address integrations. The article summarizes the high impact IP address knowledge base articles that are referenced frequently. These articles should provide meaningful information to help answer your integration-related IP address questions.

### Managing IP address issues

| **Issue** | **Reference** | **Details** |
| --- | --- | --- |
| How do I find my instance IP address? | [KB0538621: Finding the IP information for your instance](/kb_view.do?sysparm_article=KB0538621 "KB0538621: Finding the IP information for your instance") | Explains how to view your instance's IP address for each data center and the IP addresses that your network/security/firewall teams need to allow traffic into your network from your instance.  |
| How do I allow-list email servers? | [KB0535456: Enabling email delivery using SPF records to allow SN mail servers](/kb_view.do?sysparm_article=KB0535456 "KB0535456: Enabling email delivery using SPF records to allow SN mail servers") | Provides details about using SPF records. Also lists IP addresses for the mail servers.  |
| How do I find IP details for SMTP? | [KB0521756: Configuring the outbound SMTP mail server settings](/kb_view.do?sysparm_article=KB0521756 "KB0521756: Configuring the outbound SMTP mail server settings") | This document should only be used if you use your own SMTP server. |
| How do I restrict access by IP address? | [KB0550613: Identifying and enabling IP address restrictions](/kb_view.do?sysparm_article=KB0550613 "KB0550613: Identifying and enabling IP address restrictions") | Ensure that you understand the originating IP addresses before creating any IP address restrictions. This knowledge base article contains the details you should collect before enabling the restrictions, and also provides a step-by-step approach to enabling and confirming the IP address control restrictions. |
| 
ServiceNow Customer IP Block Space Allocation

 | 

[KB0656358: ServiceNow Customer IP Block Space Allocation](/kb_view.do?sysparm_article=KB0656358 "KB0656358: ServiceNow Customer IP Block Space Allocation")

 | This article contains information about ServiceNow public IP block address allocation for an instance IP and a detailed view of Service Now public IP address space by geographical distribution |

### Managing and troubleshooting network connection issues

-   If you cannot access an IP address, [KB0517267: Managing network connectivity issues](/kb_view.do?sysparm_article=KB0517267 "KB0517267: Managing network connectivity issues") contains tips and commands that can be used to help identify where the problem is occurring.
    
-   If LDAP Server connections fail and you receive a message containing the phrase "Verify server address and port are correct and accessible, the firewall may be blocking the connection from the ServiceNow instance to the LDAP URL. Follow the instructions in [KB0538621: Obtaining IP and datacenter information](/kb_view.do?sysparm_article=KB0538621 "KB0538621: Obtaining IP and datacenter information") to ensure that you have the correct details to allow the connection INTO your network. Both VPN and non-VPN IP address ranges are provided.
    
-   If you cannot resolve the issue and need to open an incident, review [KB0521688: Troubleshooting Network Performance Data Collection](/kb_view.do?sysparm_article=KB0521688 "KB0521688: Troubleshooting Network Performance Data Collection") to gather the information that ServiceNow Customer Support needs in order to help.
    

### Do IP addresses Change?

IP address will change if you request a datacenter move or ServiceNow initiates a datacenter change (extending capacity).  
These changes will be communicated way in advance  with the affected customers  and the new ip ranges will be communicated with you in the change and updates on the change are communicated on a regular basis

It is the customer responsibility to communicate this with their vendors as ServiceNow does not have any knowledge of firewall settings of the third parties our customers  work with.

### Release

N/A

### Resolution

n/a
