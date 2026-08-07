---
title: "Discovery: Troubleshooting - DeviceL3Mapping"
aliases:
  - KB0598422
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598422
kb_number: KB0598422
last_modified: 2025-08-26
---

## Issue

Discovery | Troubleshooting DeviceL3Mapping 

  

<table class="tocTable" width="375"><tbody><tr><td>style="text-decoration: none;" name="toc"&gt;<span class="hd1">Content</span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#overview"><span style="color: #888888;">1. Overview</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#howitworks"><span style="color: #888888;">2. How it works</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#deepdive"><span style="color: #888888;">3. Deep dive</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#troubleshooting"><span style="color: #888888;">4. Troubleshooting</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#knownproblems"><span style="color: #888888;">5. Known problems</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#references"><span style="color: #888888;">6. References</span></a></span></td></tr></tbody></table>

style="text-decoration: none;" name="overview">Overview

* * *

<table class="noteTable" align="left"><tbody><tr><td style="text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Note</strong>: DeviceL3Mapping is different than Layer 2 Discovery. This article only discusses DeviceL3Mapping. See the product documentation for more information about <a title="dsfasd" href="https://docs.servicenow.com/csh?topicname=c_Layer2Discovery.html&amp;version=latest" target="_blank" rel="noopener noreferrer">Layer 2 Discovery</a>.</td></tr></tbody></table>

   
DeviceL3Mapping is a process that creates IP connection type relationships between a router and/or L3 switch to other types of network devices and servers based on its layer-3 routing information. This can be useful for visualizing the network topology and seeing what other devices may be affected by performing maintenance on a router or L3 switch.  

style="text-decoration: none;" name="howitworks">How it works

* * *

1.  Enable the [Discovery Plugin](https://docs.servicenow.com/csh?topicname=t_ActivateTheDiscoveryPlugin.html&version=latest "Discovery Plugin") on your instance.
2.  Navigate to **Discovery Definition > Properties**.
3.  Check that the **Map server and network devices to routers and layer-3 switches** (glide.discovery.L3\_mapping) property is set to **true**.
4.  Run a Discovery scan against at least one router or switch device that has associated valid and direct IP routes. (See the Troubleshooting section below for steps to determine if your router or switch is valid and returning the appropriate information).   
    You should see records created in the **Exit Interface Routing Rules** _(_dscy\_route\_interface_)_ table similar to the following:  
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=3e7c20aedb42b450e515c223059619c6)  
      
    
5.  Scan an IP of a server or other network device (not another switch or router) that falls within one of the ranges specified in the table.  
    The following occurs:
    -   When the discovery of the device is almost done, a business rule named Discovery - Device Complete is triggered
    -   The business rule then triggers an event named discovery.device.complete
    -   The event then calls a script action named Discovery - map device to netgears
    -   The script action also includes a call to a script include named DeviceL3Mapping  
        A breakdown of the key elements in this Discovery - map device to netgears script action and the DeviceL3Mapping script include can be found later in this article
    -   After the process is complete, IP Connection::IP Connection relationships are created between the server/network device (parent) and the router/switch (child) that look similar to the following screenshot:  
          
        ![](/sys_attachment.do?sys_id=ba7c20aedb42b450e515c223059619d2)

style="text-decoration: none;" name="deepdive">Deep dive

* * *

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Note</strong>: The following scripts are from the Istanbul release. Earlier (such as Geneva and Helsinki)&nbsp;and later versions may appear slightly different, which could affect the process as described below. &nbsp;</td></tr></tbody></table>

**  
Script Action: Discover - map device to netgears**

As mentioned in the How It Works section above, the Discover - map device to netgears script action record is called after the discovery.device.complete event is triggered. 

Following is a copy of the base system script for this script action, the key areas to look for, and what they do:

![](sys_attachment.do?sys_id=f27c20aedb42b450e515c223059619d8)

1.  In this 'if' statement, the **_shouldBeDone_** function is called to check if the configuration item being scanned is qualified to run the DeviceL3Mapping against.
2.  Inside this **_shouldBeDone_** function, a check is performed to see if the glide.discovery.L3\_mapping property exists on the instance and what value is set for the property. If the property does not exist in the instance and/or it is set to false, the L3Mapping process will not run against any configuration items. If the property is set to true, the process continues.
3.  A back end Java function runs to obtain all the class types that may be associated to the configuration item being scanned. For example, if a Windows Server (cmdb\_ci\_win\_server) is scanned, this Windows Server class has a hierarchy where it also belongs to the Server (cmdb\_ci\_server), Computer (cmdb\_ci\_computer), Hardware (cmdb\_ci\_hardware), and Configuration Item (cmdb\_ci) tables. The list is populated into the tables variable that is used in the next steps.
4.  The classes and weedClasses variables are set up and contain the small list of classes that will be compared against the tables values retrieved in an earlier step. 
5.  A check is performed to determine if any of the tables gathered match any of the set up weedClasses values. If the device does associate to a table that is one of the weedClasses tables, then no L3Mapping relationships are created for the device. However, if no matches are made, the next for loop is run to see if any of the tables matches any of the classes values. If a match is made (for example, a Windows Server would make a match because one of its parent tables is cmdb\_ci\_server that matches in the classes array), then true is returned. The L3Mapping process continues by calling the [DeviceL3Mapping](#Mapping "DeviceL3Mapping") script include.  
      
    

**Script Include: DeviceL3Mapping**

This script include is called from the Discover - map device to netgears script action only if the shouldBeDone function returns as true.

Below is a breakdown of the DeviceL3Mapping script starting with the map function call and how it works to eventually create IP connection relationships.

![](sys_attachment.do?sys_id=477c60aedb42b450e515c223059619cf)

1.  The **_\_findAllDeviceIPs_** function (defined below) is called. It searches for any and all IPs that are associated with the device being scanned. This is done by first gathering the IP address assigned in the configuration item record itself. Then, the cmdb\_ci\_ip\_address table is queried to find any other IPs that may be associated to this device if, for example, this device has multiple NIC cards installed. If no IPs are associated with this device, the L3Mapping process ends.  
      
    ![](sys_attachment.do?sys_id=8f7c60aedb42b450e515c223059619de)
    
2.  The **_\_collectRouters_** function runs to find any routers/switches in CMDB that have associated IP routes containing any of the IPs found from the previous **_\_findAllDeviceIPs_** function. This is done by converting the IPs to a decimal value and checking if the value falls between the Hi IP and Lo IP decimal values converted from the Dest IP Network value in the dscy\_route\_interface records. For example, a range value of 192.0.0.0/24 converts to a Lo IP of 3221225472 and a Hi IP of 3221225727 (256 addresses in total). Any routers/switches that are found with IP routes including the IPs we are checking against are placed into an array. If no routers/switches are found with a range that includes the IPs of the scanned configuration item, the L3Mapping process ends.   
      
    ![](sys_attachment.do?sys_id=c37ca0aedb42b450e515c22305961909)
    
3.  If there is a list of IPs for the scanned configuration item and a list of routers/switches that can be associated to one or more of the IPs, the **_\_reconcileRelationships_** function is called to create/update the IP connection relationships. This function also removes any stale relationships not created/updated during this cycle that are linked to the configuration item being scanned. For the created relationship records, the parent is the configuration item currently being scanned and the child is the router/switch we are connecting this CI through.
    
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=5f7ca0aedb42b450e515c2230596192f)  
    

style="text-decoration: none;" name="troubleshooting">Troubleshooting

* * *

**Cannot see expected dscy\_route\_interface records being created for switch/router**

1.  Check the ecc\_queue from a recent Discovery scan of the device and determine if the "SNMP - Routing" probe is triggered against this device. If the probe is not triggered for the switch/router, it is likely due to the ['routing' capability](https://support.servicenow.com/kb_view.do?sys_kb_id=fcb956dcdb876e004816f3231f961946#routing "'routing' capability not being set from the \"SNMP - Classify\" probe results") not being set from the SNMP - Classify probe results.
2.  If the SNMP - Routing probe is not being run against this device, check the results in the payload to see if it contains some ipCidrRouteEntry or ipRouteEntry results similar to the following:  
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=9f7ca0aedb42b450e515c2230596199a)  
      
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=2b7ca0aedb42b450e515c223059619c6)

Following are the key elements required in this result to create a valid exit interface routing rule:

-   -   **ipCidrRouteIfIndex** or **ipRouteIfIndex:** Identifies the interface that should be used to route to the next hop IP. This value must be a number other than 0 for a routing rule record to be created for this range.
    -   **ipCidrRouteDest** or **ipRouteDest:** Starting IP of the range that will be specified in the **Dest IP Network** field. 
    -   **ipCidrRouteMask** or **ipRouteMask:** Subnet mask that determines how many IPs are included in this range. This represents the '/xx' value in the **Dest IP Network** field.
    -   **ipCidrRouteNextHop** or **ipRouteNextHop:** Destination IP of where the next hop would be if the route specified is an indirect route on this router/switch. However, when creating an exit interface routing rule, they are only created based on direct routes. This means that the value should either be 0.0.0.0 (as in the ipCidrRouteEntry) or a value within the range itself (as in the ipRouteEntry).
    -   **ipCidrRouteType** or **ipRouteType:** Determines if the route is direct (3) or indirect (4). By default, when creating an exit interface routing rule, records are only created for direct (3) routes.

If these entries are not being created inside SNMP - Routing input, there may be an issue where SNMP connections are timing out before retrieving all the data from the device. To resolve this issue, increase some of the SNMP Timeout parameters either at the [MID Server](https://docs.servicenow.com/ "MID Server") level and/or from the [Probe level](https://docs.servicenow.com/csh?topicname=r_SNMPProbeParameters.html&version=latest "Probe level").

**Cannot see any IP connection relationships being created for devices**

Check the following:

-   -   The system property glide.discovery.L3\_mapping is set to true
    -   The class of the configuration item (or one of the parent classes of the configuration item) matches to one of the _classes_ array values mentioned in the Discover - map devices to netgears script action
    -   There are records in your dscy\_route\_interface table with a Dest IP Network range value that includes any IPs associated to the scanned device

**IP connection relationships are created to routers/swtiches for which relationships should not be created**

-   -   Check the dscy\_route\_interface table to see if any routes have invalid values such as:
        -   0.0.0.0/0.0.0.0
        -   0.54.1.0/0.255.255.255
    -   Check the dscy\_route\_interface table to see if there are large range values that could be valid such as:
        -   10.0.0.0/8
        -   192.0.0.0/16Your network administrator can determine if these large range values are valid. If these values should not exist, check in the SNMP - Routing input when scanning the correlating router/switch to determine the results that are producing these large range records. 

style="text-decoration: none;" name="knownproblems">Known problems

* * *

-   [KB0563036: DeviceL3Mapping is only adding relationship to the first router that it finds](https://support.servicenow.com/kb_view.do?sysparm_article=KB0563036 "KB0563036: DeviceL3Mapping is only adding relationship to the first router that it finds")
-   Ignore default route in DeviceL3Mapping (PRB660627)

style="text-decoration: none;" name="references">References

* * *

-   [Data collected by Discovery on Relationships](https://docs.servicenow.com/csh?topicname=c_NetworkDevices.html&version=latest "Data collected by Discovery on Relationships")
-   [Data collected by Discovery on network routers and switches](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoNWRouteAndSwitch.html&version=latest "Data collected by Discovery on network routers and switches")
