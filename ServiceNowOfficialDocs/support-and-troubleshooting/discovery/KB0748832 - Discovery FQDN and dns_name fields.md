---
title: "Discovery FQDN and dns_name fields"
aliases:
  - KB0748832
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748832
kb_number: KB0748832
last_modified: 2025-08-26
---

## Discovery FQDN and dns\_name fields

  

### Issue

Discovery dns\_domain and FQDN are not the same.

### Release

All

### Cause

**How discovery sets the dns\_domain field:**  
  
The dns\_name and dns\_domain fields in a CI are usually collected in the Shazzam phase of discovery. The values returned are passed to the identification phase of the discovery. The identification phase populates/updates the field once the identification payload is processed. These are normally the dns values returned when doing an nslookup of the ip being discovered.

**How discovery sets the fqdn field:**  
  
The FQDN field will depend on the device type/probe&sensor/pattern.

As an example, for windows OS devices, the following WMI fields are used:

-   Win32\_ComputerSystem.Domain
-   Win32\_ComputerSystem.Name

There are properties under "Discovery Definition > Properties" which can change how the FQDN field is populated.

-   glide.discovery.hostname.dns\_nbt\_trusted
-   glide.discovery.hostname.ssh\_trusted
-   glide.discovery.hostname.wmi\_trusted
-   glide.discovery.hostname.snmp\_trusted

For more information on the properties mentioned above please review this document: [Discovery properties](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/discovery/reference/r_DiscoveryProperties.html "Discovery properties").

As seen above, the FQDN and DNS fields of a CI are determined differently.

### Resolution

It is not an issue in itself that the FQDN and DNS fields of a CI do not match. The DNS values are often populated based on the results returned by the DNS server the MID server can reach, while FQDN is usually populated based on the results of scripts/queries directly against the device.

If the FQDN and dns fields must match on the environment, the following can be done to accomplish it.

If using probes, use the following properties to control how the FQDN is populated for a CI and achieve the desired behavior, may need to update probes/sensors:

-   glide.discovery.hostname.dns\_nbt\_trusted
-   glide.discovery.hostname.ssh\_trusted
-   glide.discovery.hostname.wmi\_trusted
-   glide.discovery.hostname.snmp\_trusted

If using patterns, update the pattern so that the FQDN name is set to the same as that collected via DNS.
