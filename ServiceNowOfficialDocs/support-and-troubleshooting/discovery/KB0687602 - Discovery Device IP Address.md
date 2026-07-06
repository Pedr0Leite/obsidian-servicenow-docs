---
title: "Discovery Device IP Address"
aliases:
  - KB0687602
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687602
kb_number: KB0687602
last_modified: 2025-07-25
---

## Discovery Device IP Address

  

### Issue

During discovery, a configuration item (CI) may have its IP address updated. This article focuses on the **ip\_address** field of a discovered CI, such as cmdb\_ci\_computer.ip\_address. When a CI is discovered, the **cmdb\_ci\_ip\_address** table is also populated with the IP addresses discovered for the CI.

The following steps show the discovery logic used to update such an IP address.

### Release

All releases

### Resolution

### Discovered CI IP Address

The IP address for a CI is set during the identification phase of discovery.

### Probes and sensors

At the identification phase, a payload called _cidata_ is passed to the Identification and Reconciliation Engine (IRE). The IRE uses the _cidata_ payload to create or update the CI. The IP address for the CI is updated if the **ip\_address** in the _cidata_ is not the same as the IP address currently set for the CI.

#### The IP address in the cidata is the same IP address being used to discover the CI.

In most cases, it is not desirable to have the IP address changing with each discovery. Therefore, before passing the payload to the IRE, discovery attempts to determine whether to remove the ip\_address from the payload. Removing the ip\_address from the payload ensures that the IP address for the CI is not updated.

The script include _DiscoveryJSONIDSensor_ uses the function processIPAddressField(ciRecord) to perform the following steps:

1.  Did the identification engine find a matching CI?  
    -   **No:** This is the first time the device is discovered. Uses the IP address from cidata
    -   **Yes:** Continue
2.  Does the existing CI have an IP address?  
    -   **No:** Uses the IP address from cidata to update CI
    -   **Yes:** Continue
3.  Does the CI current IP address match the cidata IP address?  
    -   **No:** Continue
    -   **Yes:** No need to remove the IP from the cidata. The CI maintains the IP address
4.  At this point, the IP address in the cidata does not match the CI current IP address. Leaving this IP address in the cidata would cause the CI IP address to be updated or flipped. The identification phase also collects the network adapters. Therefore, is the CI current IP address is one of the IP addresses discovered with the network cards?  
    -   **Yes:** This is still a valid IP address and it can be kept. Therefore, clear the cidata IP address so that the CI current IP address is not updated unnecessarily.
    -   **No:** The CI record has an IP address which is no longer valid. Keep the IP address in the cidata so that the CI record is updated

### Patterns

Patterns do not use the _DiscoveryJSONIDSensor_ script include. The ip\_address for a CI is set according to the logic in the pattern. Each pattern has a step where $<class\_name>\[\].ip\_address is set. Steps can be added to the pattern or removed to control what IP address should be used to update the **ip\_address** field.

#### Before Orlando Patch 5

CIs discovered via patterns have their ip\_address updated according to what is returned for the ip\_address field. The **ip\_address** field is updated each time a CI is discovered via different IP addresses. Extra logic was added to the Horizontal Discovery Sensor to prevent this flipping in PRB1343838.

#### Beginning with Orlando Patch 5

The preventFlappingAttributeOnParentClassReturnIreTime() function was added to the discovery sensor (PRB1343838). This function checks if the ip\_address field is already populated on the CI and if so does not update it. However, this keeps the IP address field from changing at all if it is already populated. The IP address field needs to be updated manually and the CI will keep the updated value (discovery will no longer update it). PRB1443223 fixes this in Rome.

#### Rome release

PRB1443223 added logic to check if the current IP address for the CI is still being discovered. If not, replace it with the new IP address discovered for the CI. This is similar to what was done with probes.

### Post-discovery

Once discovery completes for a CI, a _discovery.device.complete_ event is created. The script action that responds to this event calls the _IPAddressFixup_ script include. This script is controlled by the following properties:

1.  glide.discovery.enforce\_ip\_sync
2.  glide.discovery.exclude\_ip\_sync\_classes
3.  glide.discovery.enforce\_unique\_ips

**Note:** Post-discovery can update the ip\_address field for both probes and pattern- based discovery.

### Discovery Properties

#### glide.discovery.enforce\_ip\_sync

The glide.discovery.enforce\_ip\_sync property prevents the system from using a discovered IP address in the CI record if the address doesn't match that of a NIC on the device. If this property is true, discovery checks the IP address returned to determine if it is associated with a NIC on the device. If the address is not associated with a NIC, discovery uses the IP address from one of the NICs instead. The IP address used is the first found in the list of IP addresses belonging to the CI. The IP address is ordered by the ip\_address column. 

#### glide.discovery.exclude\_ip\_sync\_classes

The glide.discovery.exclude\_ip\_sync\_classes property defines CI classes whose IP addresses should not be substituted if the address returned by discovery does not match one of the devices' NICs. Use a comma-separated list to define multiple classes. By default, the system uses the management IP of a load balancer returned by discovery in the CI record, rather than substituting it for the IP address of one of the load balancer's NICs.

#### glide.discovery.enforce\_unique\_ips

The glide.discovery.enforce\_unique\_ips property ensures that each time a computer, printer, or network gear is discovered, and that device has a valid IP address, any other devices with the same IP address have their IP address field cleared.

### Common issues

#### CI IP address field updated after discovery completion by a system account

This is usually due to the glide.discovery.enforce\_ip\_sync system property set to true. This triggers code in the _IPAddressFixup_ script include that updates the IP address. Setting glide.discovery.enforce\_ip\_sync to false should stop this behavior. Alternatively, you can add the CI class to the glide.discovery.exclude\_ip\_sync\_classes system property.

#### IP Address updated each time discovery runs after migrating from probes to patterns

Prior to Orlando Patch 5, this is expected behavior. A custom script action triggered by the discovery.device.complete event could be put in place to add custom logic on how to update the IP address, or a sa\_pattern\_prepost\_script could perform this action.

#### IP Address not updated by discovery after migrating from probes to patterns

Beginning with Orlando Patch 5, the **ip\_address** field is no longer updated if it is not empty. You can clear the **ip\_address** field in a CI and then rediscover it so that discovery populates it. Alternatively, a custom script action or _sa\_pattern\_prepost\_script_ could perform this action. The  _glide.discovery.enforce\_ip\_sync_ system property can also ensure that the IP address is updated to a **valid/current** value. This property is explained previously in this document. This issue is fixed in Rome via PRB1443223.
