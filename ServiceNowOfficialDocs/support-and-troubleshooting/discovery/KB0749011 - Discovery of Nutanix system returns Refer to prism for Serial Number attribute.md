---
title: "Discovery of Nutanix system returns \"Refer to prism\" for Serial Number attribute"
aliases:
  - KB0749011
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749011
kb_number: KB0749011
last_modified: 2025-06-26
---

## Discovery of Nutanix system returns "Refer to prism" for Serial Number attribute

  

### Issue

Discovery of Nutanix system returns "Refer to prism" for Serial Number attribute

While scanning Nutanix devices discovery returns "Refer to prism" for serial number thus keeps over riding same ESX server CI for each Nutanix device discovered.

![screenshot of discovery result showing "Refer to PRISM" in Serial Number field](sys_attachment.do?sys_id=d4d3463647166ad030fba325126d43a9)

### Release

All

### Cause

This is because the serial number specified on the ESX host does not reside on the location discovery checks for it according to standard practice.

### Resolution

As a work around NUTANIX has provided a script to run on the ESX server to copy the Serial Number at the correct location.

Note: This script needs a restart.

You can reach your NUTANIX support for that script.

### Related Links

[Community Article: Discovery of Nutanix returns "Refer to prism" for Serial Number attribute](https://www.servicenow.com/community/itom-forum/discovery-of-nutanix-system-returns-quot-refer-to-prism-quot-for/m-p/957074)
