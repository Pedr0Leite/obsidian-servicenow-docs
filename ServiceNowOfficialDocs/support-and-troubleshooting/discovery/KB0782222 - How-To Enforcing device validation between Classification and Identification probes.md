---
title: "How-To: Enforcing device validation between Classification and Identification probes"
aliases:
  - KB0782222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782222
kb_number: KB0782222
last_modified: 2024-05-21
---

## How-To: Enforcing device validation between Classification and Identification probes

  

### Issue

In certain edge cases (i.e: Short DHCP leases) it can occur that between the Classification and Identification phase for a specific IP that the underlying device has changed. This can cause issues in the CMDB as matched devices in Classification will be updated with incorrect information from Identification, which can then result in cascading CMDB issues as records will have mismatched data (e.g: hostname with wrong serial number).

### Release

Any version utilizing Probes

### Cause

With Probes we initiate separate PSSessions for Classification and Identification. If the underlying device an IP is assigned to changes between Classification and Identification (short DHCP leases and/or delayed MID server processing) then this issue will occur.

  

NOTE: This should not occur in Patterns as Classification and Identification are combined

### Resolution

The desired option here should be to upgrade to that supports Probes to Pattern migration and then utilize Patterns (New York+)

If this is not possible you can apply the attached update set. Elaboration on what the customization does and the drawbacks are as follows:

NOTE: This is not officially supported code; there is no guarantee of a break fix for this should the custom solution not function correctly in future releases.

The custom solution is as follows:  
\- New sub-probe part of "Windows - Identity" multi-probe  
\- Runs a WMI query from "Windows - Classify" probe and compares against ciData.host\_name value stored from Classification  
\- If there is a mismatch, append a "shouldAbort = true" param to ciData  
\- Customizations in DiscoveryJSONIDSensor to abort CI identification/exploration/update if "shouldAbort" is true  
\- Log abortion in Discovery Status  
  
Please note the following limitations of this solution:  
\- Only works for CIs that utilize the "Windows - Identity" probe (Defined in discovery\_classy record)  
\- Only works for Windows CIs that utilize the DiscoveryJSONIDSensor (Defined in discovery\_probe record's sensor)  
\- Only querying Win32\_ComputerSystem.Name. Typically we attempt multiple queries in Classification for the device host/name, in this customization we are only making a single query. If desired this can be modified to make multiple WMI queries in the Identification probe for several checks against ciData for more fault tolerance.  
\- As of Madrid Patch 5 there have been no modifications to DiscoveryJSONIDSensor. If this script is changed in future versions you will not receive the changes as we've customized the code. You will need to be diligent in checking for changes to this script on upgrade otherwise Discovery can break for any devices utilizing this script.

### Related Links

The customization code can be roughly adapted to other Identity probes and Discovery Sensors as desired.
