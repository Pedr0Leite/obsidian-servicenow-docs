---
title: "Oracle Enterprise Manager (OEM) Trap using SNMPv3 Error"
aliases:
  - KB0745581
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745581
kb_number: KB0745581
last_modified: 2025-07-31
---

## Oracle Enterprise Manager (OEM) Trap using SNMPv3 Error

  

### Issue

When working with **Oracle Enterprise Manager \[OEM\]** SNMPv3 trap.

Start successfully and test parameters also show success, but no events are coming into the instance.

After running test parameter on the trap, in the MID logs we see an error like:

**WARNING \*\*\* WARNING \*\*\* (227)SNMPTrapListener - SNMPTrapListener: (OEM Traps): Listener minimum security level: 2 is higher then the trap security level: 1 aborting trap: CommandResponderEvent\[securityModel=1, securityLevel=1, maxSizeResponsePDU=65535, pduHandle=PduHandle\[0\]**

### Release

Any release where OEM trap SNMPv3 is configured. 

### Cause

This is due to the configuration of the user authentication on the SNMP trap and the listener's minimum security level on the listener (the listener is the record created on the ServiceNow instance for this trap collection).

The Minimum security field on the listener does not match the configuration setup on the OEM trap. They need to match. That is what is meant by the error message:

"Listener minimum security level: 2 is higher than the trap security level"

### Resolution

We have two options :   
1\. Change the trap to be _authPriv_ (in this case parameters of the trap should contain the user authentication key and the private key)   
2\. Change the SNMP listener security level to _authNoPriv_ 

Be sure to fill in all field for the SNMP credentials being used for this integration, including the appropriate "Privacy protocol" and "Privacy Key"

### Related Links

See the Oracle documentation about this security level (see section 3.5.2.2 related to security level):   
[https://docs.oracle.com/cd/E73210\_01/EMADM/GUID-B48F6A84-EE89-498D-94E0-5DE1E7A0CFBC.htm#EMADM14348](https://docs.oracle.com/cd/E73210_01/EMADM/GUID-B48F6A84-EE89-498D-94E0-5DE1E7A0CFBC.htm#EMADM14348)
