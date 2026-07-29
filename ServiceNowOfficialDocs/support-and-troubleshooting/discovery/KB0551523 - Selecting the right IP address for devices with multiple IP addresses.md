---
title: "Selecting the right IP address for devices with multiple IP addresses"
aliases:
  - KB0551523
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551523
kb_number: KB0551523
last_modified: 2026-05-19
---

## Selecting the right IP address for devices with multiple IP addresses

  

### Issue

Many devices have multiple NICs and IP Addresses.

When Discovery first runs against a device, it will select the IP Address that it first encounters, and will associate that IP Address to the newly created CI Record.

In certain cases, a customer may not want to use this particular IP Address for the CI.

### Release

All

### Resolution

### How to define the IP you wish to use

As long as the IP Address is actually associated with the device, then it is as simple as manually setting the CI IP Address to the one that you require to use.

When Discovery next runs, it will see that the existing value for the IP Address is on the CI Record. If this value matches any of the IP Addresses that are being discovered on the device, it will leave the IP Address as defined on the CI.

### Example:

We have a device that has four IP Address:

10.10.1.1, 10.10.1.2, 10.10.1.3, 10.10.1.4

When the device was first Discovered, Discovery populated the CI with the IP Address of: 10.10.1.1

Unfortunately this IP Address is not "correct" for our use, and we need to Identify the device by IP Address 10.10.1.4.

1.  From the CMDB select the device you wish to modify
2.  Manually define the IP Address that should be used for the device - in this case replace: 10.10.1.1. with 10.10.1.4
3.  Save the record
4.  On subsequent Discoveries, we should see that the CI will remain defined to IP Address: 10.10.1.4
