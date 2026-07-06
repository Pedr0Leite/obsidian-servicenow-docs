---
title: "Service Mapping of Active Directory - Entry Point Type, Port and Protocol"
aliases:
  - KB0785205
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785205
kb_number: KB0785205
last_modified: 2024-05-21
---

## Issue

This article discusses the Endpoint type, the port, and protocol to use for Service Mapping on Active Directory.

There are NO connections coming through, traffic-based or otherwise and the application service MAP is just resulting to just the entry point DC. Using the Active Directory Forest Endpoint and the Active Directory Domain to Domain Controllers Endpoint, as well as multiple ports and protocols (445, 135, 389, LDAP, SMB, TCP, & UDP), with the same results.

## Resolution

Service mapping is mostly used to map out the applicative aspect.

The following information is used to create the proper Entry Point for Service Mapping of Active Directory.

1\. Go to Service Mapping > Application Services

2\. Click New

3\. Enter the Name, Owner of the Application Service

4\. Select "Discoverable by Service Mapping"

5\. Select "Other Application"

6\. Select the Entry Point Type as **TCP Endpoint**

a. Host: <IP Address of the Target AD>

b. Port: **389**

(Protocol: TCP)

## Additional Information

If looking for information on infrastructure, look at the table "cmdb\_ci\_ad\_controller". In the screenshot attached _"map.png"_ (name of the servers and other CIs were blanked out for security purposes), see the DC and a lot of the physical infrastructure that it resides on and uses.

To achieve this:

1\. Form the View Map of the Application Service, right-click the node  
2\. Click Open in Dependency Views.
