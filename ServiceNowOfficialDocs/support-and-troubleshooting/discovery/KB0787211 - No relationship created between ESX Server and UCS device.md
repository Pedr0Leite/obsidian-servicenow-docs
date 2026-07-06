---
title: "No relationship created between ESX Server and UCS device"
aliases:
  - KB0787211
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787211
kb_number: KB0787211
last_modified: 2024-04-08
---

## No relationship created between ESX Server and UCS device

  

### Issue

Some ESX Server does not have a Runs on:Runs relationship on UCS Blade / Chassis.

### Release

All current releases up to New York family version.

### Resolution

The relationship is created after running the UCS HD Pattern and Pre Post Processing script "Create relations between UCS Blade or Rack and OS".  We look up matching UCS Blade or Rack serial with the Server serial number and if there is a match we create the "Runs on::Runs"  relationship between the Server and the UCS Blade or Rack.  In some cases for ESX Servers, we do not get the serial number from the vCenter Discovery.  To get the ESX Server serial number we get the corresponding Service Tag from the vCenter and set this as the ESX Server serial number. If this is empty or has no value in the vCenter then the ESX Server serial number is not populated.
