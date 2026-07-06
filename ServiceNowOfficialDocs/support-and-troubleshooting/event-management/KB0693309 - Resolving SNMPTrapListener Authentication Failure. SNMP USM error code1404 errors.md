---
title: "Resolving \"SNMPTrapListener: Authentication Failure. SNMP USM error code:1404\" errors"
aliases:
  - KB0693309
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693309
kb_number: KB0693309
last_modified: 2024-04-07
---

## Resolving "SNMPTrapListener: Authentication Failure. SNMP USM error code:1404" errors

  

### Issue

  
  

# Description

* * *

The SNMP Trap Listener, starting in Kingston, supports SNMPv3 for mutual authentication. This requires additional configuration on the client's end in order for the SNMP credentials being sent by the MID server to authenticate properly.

Some networking devices (e.g: Cisco Prime Infrastructure) have a configuration section for northbound/outbound SNMP Traps to an SNMP Listener/Receiver. However they often also require that the user in the configuration exist as a local account on the networking device in order for SNMPv3 authentication to work properly.

If the authentication protocols and credentials have all been verified and confirmed as matching up and you are still seeing errors similar to this:

Trap.0 WARNING \*\*\* WARNING \*\*\* (4951)SNMPTrapListener - SNMPTrapListener: (\[NAME OF CREDENTIAL\]): Authentication failure. Message sent from: \[IP ADDRESS\]/25597. SNMP USM error code:1404 

Then it's likely that the SNMP credential "user" has not been configured as a local account on the device.

# Procedure

* * *

1.  Validate credentials are correct
2.  Verify "Minimum Security Level", "Authentication Protocol", and "Privacy Protocol" match on the SNMP Trap Collector Context and SNMP credentials with the networking device
3.  If all of these match and error code 1404 is still being observed in the MID logs, have the client check to see if the credential username exists as a local account on the device. The error code states that the username is not recognized, so it's likely at this point that the user wasn't configured on the device (just in the SNMP trap section)

# Applicable Versions

* * *

Kingston and above
