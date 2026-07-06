---
title: "Mid server down in the instance hosted on a Azure VM"
aliases:
  - KB0723705
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723705
kb_number: KB0723705
last_modified: 2026-05-16
---

## Mid server down in the instance hosted on a Azure VM

  

### Issue

MID server service is up and running on the mid-server host, but the existing MID server shows as down in the instance. If it is a new installation, the mid-server record is not created in the ecc\_agent table.

From a command prompt, the following commands are successful but the Mid server is unable to communicate to the instance and hence it shows as down in the instance.

-   ping <instance\_name>.service-now.com
-   telnet <instance\_name>.service-now.com 443

08/27/18 16:09:14 (944) ECCSender.1 WARNING \*\*\* WARNING \*\*\* Socket error   
08/27/18 16:09:14 (944) ECCSender.1 WARNING \*\*\* WARNING \*\*\* RemoteGlideRecord failed to send data to https://<instance\_name>.service-now.com/ with (Socket error)   
08/27/18 16:09:14 (944) ECCSender.1 Attempt to send ecc\_queue.1657aa0ae3d0000001.2.xml failed: file remains enqueued for later sending   
08/27/18 16:09:15 (116) ECCSender.1 Sending ecc\_queue.1657aa0af080000001.2.xml

### Release

ALL

### Cause

Due to the Network security group settings in Azure not being configured correctly to allow communication between the mid-server host and the instance

### Resolution

Ensure the network security group in Azure is configured to allow traffic/communication between the mid-server host and the instance by allowing the desired Port/IP address.

The MID Server connects to a ServiceNow instance via the SOAP web service (TCP 443).
